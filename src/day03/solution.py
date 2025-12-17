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

def get_largest_12_digit(numbers: list[int], digit: int, largest: str):
    if len(largest) == 12:
        return int(largest)

    end = len(numbers) - digit + 1
    subset = numbers[:end]
    first = max(subset)
    index_of_first = subset.index(first)
    after_first = numbers[index_of_first + 1:]
    return get_largest_12_digit(after_first, digit - 1, f"{largest}{first}")


def solution_2(lines):
    total = 0
    for line in lines:
        numbers = [int(x) for x in line]
        total = total + get_largest_12_digit(numbers, 12, '')
    return total
