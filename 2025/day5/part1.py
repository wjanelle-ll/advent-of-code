input = open('input.txt').read()

ranges = [
    range(
        int(r.split('-')[0]),
        int(r.split('-')[1])+1,
    )
    for r in input.split("\n\n")[0].splitlines()
]
ids = input.split("\n\n")[1].splitlines()

fresh_ids = 0

for id in ids:
    for r in ranges:
        if int(id) in r:
            fresh_ids += 1
            break

print(fresh_ids)
