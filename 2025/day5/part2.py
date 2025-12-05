input = open('input.txt').read()

ranges = sorted(
    [
        range(
            int(r.split('-')[0]),
            int(r.split('-')[1])+1,
        )
        for r in input.split("\n\n")[0].splitlines()
    ],
    key=lambda a: a.start
)

total = 0
covered_range = 0

for i in ranges:
    if i.stop < covered_range:
        continue
    if i.start < covered_range:
        i = range(covered_range, i.stop)
    total += i.stop - i.start
    if covered_range < i.stop:
        covered_range = i.stop

print(total)
