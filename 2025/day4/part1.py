input = open("input.txt").read()

height = len(input.splitlines())
width = len(input.splitlines()[0])

def lookup(x: int, y: int) -> str:
    if 0 <= y and y < len(grid) and 0 <= x and x < len(grid[y]):
            return grid[y][x]
    return '.'

grid: list[list[str]] = []
for y in range(0, height):
    grid.append([])
    for x in range(0, width):
        grid[y].append(input.splitlines()[y][x])

removable = 0

for y in range(0, height):
    for x in range(0, width):
        if lookup(x,y) == "@":
            surrounding = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    if lookup(x+i, y+j) == "@":
                        surrounding += 1
            if surrounding - 1 < 4:
                removable += 1

print(removable)
