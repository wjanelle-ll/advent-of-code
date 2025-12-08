input = open('input.txt').read()

def str_replace_at_index(s: str, c: str, i: int):
    return s[:i] + c + s[i+1:]

split_count = 0

current_line = input.splitlines()[0]
for next_line in input.splitlines()[1:]:
    for i in range(len(next_line)):
        if current_line[i] in ["S", "|"] and next_line[i] == ".":
            next_line = str_replace_at_index(next_line, "|", i)
        if current_line[i] == "|" and next_line[i] == "^":
            split_count += 1
            next_line = str_replace_at_index(next_line, "|", i-1)
            next_line = str_replace_at_index(next_line, "|", i+1)
    current_line = next_line
    print(current_line)

print(split_count)
