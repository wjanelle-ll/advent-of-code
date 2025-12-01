from math import floor


input = open("input.txt").read()

dial = 50
password = 0

for line in input.splitlines():
    direction = 1 if line[0] == "R" else -1
    distance = int(line[1:])
    delta = direction * distance
    password += floor(distance / 100)

    if dial != 0:
        if direction > 0:
            if dial + (distance % 100) >= 100:
                password += 1
        else:
            if dial - (distance % 100) <= 0:
                password += 1

    dial += delta
    dial %= 100

print(password)
