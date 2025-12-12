# Incomplete. Algorithm passes test case, but is not
# efficient enough for full input.

import itertools
import re

input = open('input.txt').read()

def apply_buttons(vec: list[int], buttons: list[list[int]]):
    for button in buttons:
        for index in button:
            if index < len(vec):
                vec[index] += 1
    
    return vec

total = 0
for machine in input.splitlines():
    joltage = machine.split('{')[1][:-1]
    vec: list[int] = [
        int(j)
        for j in joltage.split(',')
    ]
    buttons: set[tuple] = set(
        tuple(
            int(index)
            for index in button.split(",")
        )
        for button in re.findall(r"\(([0-9,]+)\)", machine)
    )

    starter_sets = [tuple()]

    sorted_indicies = sorted(range(len(vec)), key=lambda k: vec[k])
    sorted_indicies.reverse()

    potential_solutions = []

    for i in sorted_indicies:
        min_combo_found = False

        buttons_with_index: set[tuple] = set()
        for j in buttons:
            if i in j:
                buttons_with_index.add(j)
        
        next_starter_sets = []
        
        for starter in starter_sets:
            combination_size = vec[i] - apply_buttons([0] * len(vec), starter)[i]
            for subset in itertools.combinations_with_replacement(buttons_with_index, combination_size):
                subset = list(subset)
                subset.extend(starter)
                test_vec = apply_buttons([0] * len(vec), subset)
                dont_append = False
                for j in range(len(vec)):
                    if test_vec[j] > vec[j]:
                        dont_append = True
                        break
                if not dont_append:
                    next_starter_sets.append(tuple(subset))

                print(len(next_starter_sets))
                if test_vec == vec:
                    potential_solutions.append(subset)
                    break

        buttons -= buttons_with_index
        starter_sets = next_starter_sets
    total += len(min(potential_solutions, key=lambda k: len(k)))

print(total)
