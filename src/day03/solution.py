def solution_1(lines):
    total = 0

    for line in lines:
        numbers = [int(x) for x in line]
        all_but_last = numbers[:-1]
        first = max(all_but_last)
        index_of_first = all_but_last.index(first)
        after_first = numbers[index_of_first + 1:]
        second = max(after_first)

        total = total + int(f"{first}{second}")

    return total


def solution_2(lines):
    total = 0

    return total
