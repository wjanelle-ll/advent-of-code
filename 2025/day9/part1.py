input = open("input.txt").read()

coords = [
    (
        int(line.split(',')[0]),
        int(line.split(',')[1]),
    )
    for line in input.splitlines()
]

max_area = 0
max_area_pair = None
for i in range(len(coords)):
    for j in range(i+1, len(coords)):
        width = (max(coords[i][0], coords[j][0]) - min(coords[i][0], coords[j][0]) + 1)
        height = (max(coords[i][1], coords[j][1]) - min(coords[i][1], coords[j][1]) + 1)
        area = width * height
        if area > max_area:
            max_area = area
            max_area_pair = (coords[i], coords[j])

print(max_area)
print(max_area_pair)
