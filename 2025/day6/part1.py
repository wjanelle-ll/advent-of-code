from functools import reduce

input = open("input.txt").read()
lines = input.splitlines()

matrix: list[list[int]] = []

for line in lines[:-1]:
    operands = line.split()
    for i in range(len(operands)):
        if i == len(matrix):
            matrix.append([])
        matrix[i].append(int(operands[i]))

i = 0
sum = 0
for operator in lines[len(lines)-1].split():
    operands = matrix[i]

    if operator == '*':
       transform = lambda a, b: a*b
    if operator == '+':
       transform = lambda a, b: a+b
    sum += reduce(transform, operands)

    i += 1

print(sum)
