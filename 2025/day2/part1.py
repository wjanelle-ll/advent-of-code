input = open("input.txt").read()
ranges = input.split(",")

invalid_id_sum = 0

for r in ranges:
    start = r.split("-")[0]
    end = r.split("-")[1]
    for i in range(int(start), int(end) + 1):
        as_str = str(i)
        if len(as_str) % 2 != 0:
            continue
        if as_str[int(len(as_str)/2):] == as_str[:int(len(as_str)/2)]:
            invalid_id_sum += i

print(invalid_id_sum)
