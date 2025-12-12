# Incomplete. Algorithm does not pass test case.

input = open("test.txt").read()

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

        right_wall = max(coords[i][0], coords[j][0])
        left_wall = min(coords[i][0], coords[j][0])
        top_wall = max(coords[i][1], coords[j][1])
        bottom_wall = min(coords[i][1], coords[j][1])
        width = (right_wall - left_wall + 1)
        height = (top_wall - bottom_wall + 1)
        area = width * height

        print(f"Examining {coords[i]}->{coords[j]}")
        crossed = False
        for k in range(len(coords)):
            coord_a = coords[k]
            coord_b = coords[(k+1) % len(coords)]
            crossed_h = False
            crossed_v = False
            if not (
                ( # both coords to right of rect
                    coord_a[0] >= right_wall
                    and coord_b[0] >= right_wall
                ) or
                ( # both coords to left of rect
                    coord_a[0] <= left_wall
                    and coord_b[0] <= left_wall
                )
            ):
                crossed_h = True
                print(f"Crossed h {coord_a}->{coord_b}")
            if not (
                ( # both coords to right of rect
                    coord_a[1] >= top_wall
                    and coord_b[1] >= top_wall
                ) or
                ( # both coords to left of rect
                    coord_a[1] <= bottom_wall
                    and coord_b[1] <= bottom_wall
                )
            ):
                crossed_v = True
                print(f"Crossed v {coord_a}->{coord_b}")
            if crossed_h and crossed_v:
                print(f"Crossed both! {coord_a}->{coord_b}")
                crossed = True
                break

        if not crossed and area > max_area:
            max_area = area
            max_area_pair = (coords[i], coords[j])

print(max_area)
print(max_area_pair)
