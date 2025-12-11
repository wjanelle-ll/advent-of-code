import itertools
import re

input = open('input.txt').read()

sum = 0
for machine in input.splitlines():
    lights = machine.split(']')[0][1:]
    vec = [
        1 if light == "#" else 0
        for light in lights
    ]
    buttons = [
        [
            int(index)
            for index in button.split(",")
        ]
        for button in re.findall("\(([0-9,]+)\)", machine)
    ]

    min_combo_found = False
    for combination_size in range(len(buttons) + 1):
        for subset in itertools.combinations(buttons, combination_size):
            test_vec = [0] * len(vec)
            for button_press in subset:
                for toggle_index in button_press:
                    test_vec[toggle_index] = (test_vec[toggle_index] + 1) % 2
            
            if test_vec == vec:
                sum += combination_size
                min_combo_found = True
                break
        if min_combo_found:
            break

print(sum)
