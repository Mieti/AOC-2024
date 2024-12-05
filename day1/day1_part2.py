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

def similarity_score(column1, column2):
    progressive_sum = 0
    for value1 in column1:
        counter = 0
        for value2 in column2:
            if value1 == value2:
                counter += 1
        progressive_sum += counter*int(value1)
    return progressive_sum

file_path = './input.txt'
lines = read_file(file_path)
column1, column2 = separate_columns(lines)

print(f"Similarity score: {similarity_score(column1, column2)}")

