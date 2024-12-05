with open('./input.txt', 'r') as file:
    lines = file.readlines()

def is_ascendant_or_descendant(numbers):
    ascendant = all(numbers[i] < numbers[i+1] for i in range(len(numbers) - 1))
    descendant = all(numbers[i] > numbers[i+1] for i in range(len(numbers) - 1))
    return ascendant or descendant

def is_in_range(numbers): 
    return all(1 <= abs(numbers[i+1] - numbers[i]) <= 3 for i in range(len(numbers) - 1))
     
counter = 0
for line in lines:
    numbers = list(map(int, line.split()))
    if is_ascendant_or_descendant(numbers):
        counter += 1
print(counter)