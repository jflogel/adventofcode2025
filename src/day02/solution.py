starting_position = 50

def solution_1(lines):
    ranges_strs = lines[0].split(",")
    ranges = []
    for range_str in ranges_strs:
        split = range_str.split("-")
        ranges.append(range(int(split[0]), int(split[1]) + 1))

    sum = 0

    for given_range in ranges:
        for num in given_range:
            num_str = f"{num}"
            length = len(num_str)
            if length % 2 == 1:
                continue
            split_index = int(length / 2)
            first = num_str[0:split_index]
            second = num_str[split_index:]
            if first == second:
                sum = sum + num

    return sum


def divisors(num, possible, arr):
    if possible == 0:
        return arr
    if num % possible == 0:
        return divisors(num, possible - 1, [possible, *arr])
    return divisors(num, possible - 1, arr)


def divisors_of_num(num):
    return divisors(num, int(num / 2), [])

def solution_2(lines):
    ranges_strs = lines[0].split(",")
    ranges = []
    for range_str in ranges_strs:
        split = range_str.split("-")
        ranges.append(range(int(split[0]), int(split[1]) + 1))

    total = 0

    for given_range in ranges:
        for num in given_range:
            num_str = f"{num}"
            length = len(num_str)
            if length == 1:
                continue

            divisors = divisors_of_num(length)
            for divisor in divisors:
                parts = [num_str[length_to_split:length_to_split + divisor]
                         for length_to_split
                         in range(0, length, divisor)]
                first = parts[0]
                if all(x == first for x in parts):
                    total = total + num
                    break
    return total
