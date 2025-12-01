input = open("input.txt").read()

dial = 50
password = 0

for line in input.splitlines():
    direction = 1 if line[0] == "R" else -1
    distance = int(line[1:])
    delta = direction * distance
    dial += delta
    dial %= 100
    if dial == 0:
        password += 1

print(password)
