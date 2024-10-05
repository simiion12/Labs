import numpy as np


with open('matrix.txt', 'r') as file:
    matrix = [line.strip().split() for line in file]

names = [name.strip(" '[],") for name in matrix[0][1:] if len(name) > 3]
numbers = np.array([list(map(lambda x: float(x.replace(',', '').replace('[','').replace(']','')), row[1:])) for row in matrix[1:]])


# Compute eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(numbers)

# Find the index of the dominant eigenvalue
dominant_index = np.argmax(np.abs(eigenvalues))

# Retrieve the dominant eigenvalue and its corresponding eigenvector
dominant_eigenvalue = eigenvalues[dominant_index]
dominant_eigenvector = eigenvectors[:, dominant_index]

# Print the dominant eigenvalue and its corresponding eigenvector
print(f" The most dominant person is {names[dominant_index]}, with the Eigenvalue = {dominant_eigenvalue}")
print(" and corresponding Eigenvector:", dominant_eigenvector)
print()
for i in range(len(eigenvalues)):
    print("-------------------------------------------------------------------")
    print("Eigenvalue λ{}:".format(i+1))
    print(eigenvalues[i])
    print("Eigenvector v{}:".format(i+1))
    print(eigenvectors[:, i])
    print()

# Sort eigenvalues and eigenvectors in descending order based on eigenvalues

sort_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sort_indices]
eigenvectors = eigenvectors[:, sort_indices]

# Print the eigenvalues
print("-------------------------------------------------------------------")
print("Eigenvalues sorted:")
for eigenvalue in eigenvalues:
    print(eigenvalue)
print()
# Print the eigenvectors
print("Eigenvectors sorted:")
for eigenvector in eigenvectors.T:
    print(eigenvector)






