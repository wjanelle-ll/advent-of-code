input = open("input.txt").read()

sum = 0

def max_digit(s) -> int:
    for i in range(9,0, -1):
        if str(i) in s:
            return i

for line in input.splitlines():
    num_str = ''
    for i in range(12,0,-1):
        if i == 1:
            digit = max_digit(line)
        else:
            digit = max_digit(line[:-i+1])
        if i != 1:
            line = line.split(str(digit), 1)[1]
        num_str += str(digit)
    sum += int(num_str)

print(sum)
