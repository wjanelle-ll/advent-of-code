input = open('input.txt').read()

split_count = 0

current_line: list[str] = list(input.splitlines()[0])
for next_line in input.splitlines()[1:]:
    next_line = list(next_line)
    for i in range(len(next_line)):
        # initial condition
        if current_line[i] == "S":
            next_line[i] = "1"

        # bring down counter
        if current_line[i].isnumeric() and (next_line[i] == "." or next_line[i].isnumeric()):
            add_to_below = int(current_line[i])
            if next_line[i].isnumeric():
                add_to_below += int(next_line[i])
            next_line[i] = str(add_to_below)
        
        # add to counter
        if current_line[i].isnumeric() and next_line[i] == "^":
            split_count += 1

            add_to_left = int(current_line[i])
            if next_line[i-1].isnumeric():
                add_to_left += int(next_line[i-1])
            next_line[i-1] = str(add_to_left)

            add_to_right = int(current_line[i])
            if next_line[i+1].isnumeric():
                add_to_right += int(next_line[i+1])
            next_line[i+1] = str(add_to_right)

    current_line = next_line
    sum = 0
    for c in current_line:
        if c.isnumeric():
            sum += int(c)
    print(f"{current_line} {sum}")
