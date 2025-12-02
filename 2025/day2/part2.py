input = open("input.txt").read()
ranges = input.split(",")

invalid_id_sum = 0

for r in ranges:
    start = r.split("-")[0]
    end = r.split("-")[1]
    for i in range(int(start), int(end) + 1):
        as_str = str(i)
        for j in range(2, len(as_str) + 1):
            if len(as_str) % j != 0:
                continue
            if as_str == as_str[:int(len(as_str)/j)] * j:
                invalid_id_sum += i
                break

print(invalid_id_sum)
