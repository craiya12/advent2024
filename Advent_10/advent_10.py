# Define a function to read the matrix from a text file
def read_matrix_from_file(file_path):
    with open(file_path, "r") as file:
        # Read all lines and strip whitespace
        lines = [line.strip() for line in file.readlines()]

        # Convert each line into a list of characters
        matrix = [list(line) for line in lines]

    return matrix


# Specify the file path
file_path = "advent_10_test.txt"  # Replace with your file name or path

# Read the matrix from the file
M = read_matrix_from_file(file_path)

# Output the matrix

for item in M:
    print(item)

trailhead = []

for i in range(len(M)):
    for j in range(len(M[0])):
        if M[i][j] == "0":
            trailhead.append((i, j))
print(trailhead)


def find_next(M, i, j, index):
    if index == "9":
        return True
    if int(index) > 9:
        return False

    direction = {"up": [-1, 0], "down": [1, 0], "right": [0, 1], "left": [0, -1]}

    for dir in direction:
        if (
            i + direction[dir][o] < len(M)
            and i + direction[dir][o] >= 0
            and j + direction[dir][1] < len(M[0])
            and j + direction[dir][1] >= 0
        ):
            if M[i + direction[dir][o]][j + direction[dir][1]]:
                wow = 2


"""
find position of 0
find position of 9

for position of 0
    for position of 9



"""
