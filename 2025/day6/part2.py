from functools import reduce

input = open("input.txt").read()
lines = input.splitlines()

grid: list[list[str]] = []
for x in range(0, len(lines[0])):
    grid.append([])
    for y in range(0, len(lines)):
        grid[x].append(lines[y][x])

sum = 0
operator = ''
operands = []
for i in range(len(grid)):
    digits = ''.join(grid[i][:-1]).strip()
    if digits != '':
        operands.append(
            int(digits)
        )

    if grid[i][len(grid[i])-1] != ' ':
        operator = grid[i][len(grid[i])-1]

    if digits == '' or i == len(grid) - 1:
        if operator == '*':
            transform = lambda a, b: a*b
        if operator == '+':
            transform = lambda a, b: a+b
        sum += reduce(transform, operands)
        operands = []

print(sum)
