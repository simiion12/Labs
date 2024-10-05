import numpy as np

def inverse_distance_weighting(data, power, coordinates):
    """
    Perform Inverse Distance Weighting (IDW) interpolation to estimate missing values.

    Args:
        data (ndarray): Array containing the known data points with missing values.
        power (float): Power parameter for the inverse distance calculation.
        coordinates (tuple): Coordinates of the missing value to be estimated.

    Returns:
        float: Estimated value using IDW interpolation.
    """
    weighted_sum = 0.0
    weight_sum = 0.0

    for point in data:
        if np.isnan(point[2]):
            continue

        distance = np.sqrt((point[0] - coordinates[0]) ** 2 + (point[1] - coordinates[1]) ** 2)

        if distance == 0:
            return point[2]

        weight = 1 / distance ** power
        weighted_sum += weight * point[2]
        weight_sum += weight

    return weighted_sum / weight_sum


# Read data from file
data = []
with open("map.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        if line.startswith("Coordinate")or line.startswith("---"):  # skip the header line
            continue
        parts = line.strip().split()
        x = int(parts[0][1:-1])
        y = int(parts[1][:-1])
        elevation = parts[2]
        if elevation == 'NaN':
            elevation = inverse_distance_weighting(data, 2, (x, y))
        else:
            elevation = int(elevation)
        data.append([x, y, elevation])

data = np.array(data)

# Interpolate missing values using IDW
for i, point in enumerate(data):
    if np.isnan(point[2]):
        interpolated_value = inverse_distance_weighting(data, 2, (point[0], point[1]))
        data[i][2] = interpolated_value

# Calculate elevation changes between adjacent points
elevation_changes = np.diff(data[:, 2])

# Find the indices of the path with minimal elevation changes
safest_path_indices = np.argmin(np.abs(elevation_changes))

# Extract the safest path coordinates
safest_path_coordinates = data[safest_path_indices:safest_path_indices + 2, :2]

# Sort the data by elevation in ascending order
sorted_data = data[data[:, 2].argsort()]

elevation_1 = "{:.2f}".format(elevation)
# Print all points in ascending order of elevation
print("Sorted data by elevation:")
print("")
for point in sorted_data:
    coordinate = point[:2]
    elevation = point[2]
    elevation_1 = "{:.2f}".format(elevation)
    print(f"Coordinate: ({coordinate[0]}, {coordinate[1]}) \t Elevation: {elevation_1}")
print("")
print("--------------------------------------------------------------")
print("")
print("All data how it appears in file:")
print("")

for point in data:
    print(f"Coordinate: ({point[0]}, {point[1]}), Elevation: {point[2]}")

