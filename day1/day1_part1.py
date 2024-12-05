def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def separate_columns(lines):
    column1 = []
    column2 = []
    for line in lines:
        col1, col2 = line.strip().split()
        column1.append(col1)
        column2.append(col2)
    return column1, column2

def calculate_progressive_sum(column1, column2):
    progressive_sum = 0
    for col1, col2 in zip(column1, column2):
        difference = abs(int(col1) - int(col2))
        progressive_sum += difference
    return progressive_sum

# Example usage
file_path = './input.txt'
lines = read_file(file_path)
column1, column2 = separate_columns(lines)

# Sort columns
column1.sort()
column2.sort()

# Calculate progressive sum of differences
progressive_sum = calculate_progressive_sum(column1, column2)
print(f"Progressive sum of differences: {progressive_sum}")


