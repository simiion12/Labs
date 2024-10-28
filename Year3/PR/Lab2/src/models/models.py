import uuid
from sqlalchemy import  Column
from sqlalchemy import MetaData, String, Table
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()

car = Table(
    'car', metadata,
    Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('capacit_motor', String),
    Column('tip_combustibil', String),
    Column('anul_fabricatiei', String),
    Column('cutia_de_viteze', String),
    Column('marca', String),
    Column('modelul', String),
    Column('tip_tractiune', String),
    Column('distanta_parcursa', String),
    Column('tip_caroserie', String),
    Column('price', String),
    Column('link', String)
)
