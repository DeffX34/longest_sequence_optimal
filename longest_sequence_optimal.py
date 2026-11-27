import os, time as t
import random as rd
os.system("cls" if os.name == "nt" else "clear")

def longest_sequence(sequence: list[int]) -> int:
    if not sequence: return 0

    num_set, max_sequence, already_passed = set(sequence), 1, set()

    for current_element in num_set:
        if current_element in already_passed: continue

        current_sequence = 1

        potential_prev, potential_next = current_element - 1, current_element + 1

        while True:
            if potential_prev not in num_set and potential_next not in num_set:
                break

            if potential_next in num_set:
                already_passed.add(potential_next)
                potential_next += 1
                current_sequence += 1

            if potential_prev in num_set:
                already_passed.add(potential_prev)
                potential_prev -= 1
                current_sequence += 1

        max_sequence = max(current_sequence, max_sequence)

    return max_sequence

sequence = [i for i in range(1_000_000)]
rd.shuffle(sequence)

start_time = t.perf_counter()

result = longest_sequence(sequence)

elapsed = t.perf_counter() - start_time

print(f"Результат функции: {result}; Время выполнения функции: {elapsed}")