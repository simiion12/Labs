from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.x509 import (
    NameOID, CertificateBuilder, BasicConstraints, Name, random_serial_number,
    NameAttribute, load_pem_x509_certificate
)
from datetime import datetime, timedelta, timezone
import os


class PKIManager:
    def __init__(self):
        self.BASE_DIR = "pki"
        self.CA_DIR = os.path.join(self.BASE_DIR, "ca")
        self.USERS_DIR = os.path.join(self.BASE_DIR, "users")
        os.makedirs(self.CA_DIR, exist_ok=True)
        os.makedirs(self.USERS_DIR, exist_ok=True)

    def generate_ca(self):
        ca_key_path = os.path.join(self.CA_DIR, "rootCA.key")
        ca_cert_path = os.path.join(self.CA_DIR, "rootCA.pem")

        print("Generating CA private key...")
        ca_private_key = rsa.generate_private_key(
            public_exponent=65537, key_size=4096
        )
        with open(ca_key_path, "wb") as f:
            f.write(
                ca_private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )

        print("Generating CA self-signed certificate...")
        subject = issuer = Name([
            NameAttribute(NameOID.COUNTRY_NAME, "Moldova"),
            NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Chisinau"),
            NameAttribute(NameOID.LOCALITY_NAME, "Chisinau"),
            NameAttribute(NameOID.ORGANIZATION_NAME, "FAF"),
            NameAttribute(NameOID.COMMON_NAME, "FAF"),
        ])

        ca_cert = (
            CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(ca_private_key.public_key())
            .serial_number(random_serial_number())
            .not_valid_before(datetime.now(timezone.utc))
            .not_valid_after(datetime.now(timezone.utc) + timedelta(days=3650))
            .add_extension(BasicConstraints(ca=True, path_length=None), critical=True)
            .sign(private_key=ca_private_key, algorithm=hashes.SHA256())
        )
        with open(ca_cert_path, "wb") as f:
            f.write(ca_cert.public_bytes(serialization.Encoding.PEM))

        print(f"CA setup complete: {ca_key_path}, {ca_cert_path}")

    def generate_user_certificate(self, username):
        user_key_path = os.path.join(self.USERS_DIR, f"{username}.key")
        user_cert_path = os.path.join(self.USERS_DIR, f"{username}.crt")

        with open(os.path.join(self.CA_DIR, "rootCA.key"), "rb") as f:
            ca_private_key = serialization.load_pem_private_key(f.read(), password=None)
        with open(os.path.join(self.CA_DIR, "rootCA.pem"), "rb") as f:
            ca_cert = load_pem_x509_certificate(f.read())

        print(f"Generating private key for user: {username}...")
        user_private_key = rsa.generate_private_key(
            public_exponent=65537, key_size=2048
        )
        with open(user_key_path, "wb") as f:
            f.write(
                user_private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )

        print(f"Generating certificate for user: {username}...")
        subject = Name([
            NameAttribute(NameOID.COUNTRY_NAME, "US"),
            NameAttribute(NameOID.ORGANIZATION_NAME, username),
            NameAttribute(NameOID.COMMON_NAME, f"{username} Certificate"),
        ])
        user_cert = (
            CertificateBuilder()
            .subject_name(subject)
            .issuer_name(ca_cert.subject)
            .public_key(user_private_key.public_key())
            .serial_number(random_serial_number())
            .not_valid_before(datetime.now(timezone.utc))
            .not_valid_after(datetime.now(timezone.utc) + timedelta(days=365))
            .add_extension(BasicConstraints(ca=False, path_length=None), critical=True)
            .sign(private_key=ca_private_key, algorithm=hashes.SHA256())
        )
        with open(user_cert_path, "wb") as f:
            f.write(user_cert.public_bytes(serialization.Encoding.PEM))

        print(f"User certificate generated: {user_key_path}, {user_cert_path}")

    def sign_file(self, username, file_path):
        signature_path = f"{file_path}.sig"
        with open(os.path.join(self.USERS_DIR, f"{username}.key"), "rb") as f:
            user_private_key = serialization.load_pem_private_key(f.read(), password=None)

        with open(file_path, "rb") as f:
            data = f.read()

        print(f"Signing file: {file_path}...")
        signature = user_private_key.sign(
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH,
            ),
            hashes.SHA256(),
        )
        with open(signature_path, "wb") as f:
            f.write(signature)

        print(f"File signed: {signature_path}")
        return signature_path

    def verify_signature(self, username, file_path, signature_path):
        with open(os.path.join(self.USERS_DIR, f"{username}.crt"), "rb") as f:
            user_cert = load_pem_x509_certificate(f.read())

        user_public_key = user_cert.public_key()

        with open(file_path, "rb") as f:
            data = f.read()
        with open(signature_path, "rb") as f:
            signature = f.read()

        print(f"Verifying signature for: {file_path}...")
        try:
            user_public_key.verify(
                signature,
                data,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256(),
            )
            print("Signature verified successfully.")
            return True
        except Exception as e:
            print("Verification failed:", e)
            return False