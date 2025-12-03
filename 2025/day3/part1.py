input = open("input.txt").read()

sum = 0

def max_digit(s) -> int:
    for i in range(9,0, -1):
        if str(i) in s:
            return i

for line in input.splitlines():
    first_digit = max_digit(line[:-1])
    line = line.split(str(first_digit), 1)[1]
    second_digit = max_digit(line)
    sum += 10 * first_digit + second_digit

print(sum)
