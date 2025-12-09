starting_position = 50

def solution_1(lines):
    zero_count = 0
    current_position = 50
    for line in lines:
        direction = line[:1]
        count = int(line[1:])
        if direction == "L":
            current_position = current_position - count
        else:
            current_position = current_position + count
        if current_position % 100 == 0:
            zero_count = zero_count + 1
    return zero_count

def solution_2(lines):
    zero_count = 0
    current_position = 50
    for line in lines:
        direction = line[:1]
        count = int(line[1:])
        hundreds = int(count / 100)
        zero_count = zero_count + hundreds
        remainder = count % 100

        if direction == "L":
            next_position = current_position - remainder
        else:
            next_position = current_position + remainder
        if ((int(next_position / 100) != int(current_position / 100) and current_position % 100 != 0) or
                (next_position >= 0 > current_position) or
                (next_position <= 0 < current_position)):
            zero_count = zero_count + 1
        current_position = next_position
    return zero_count

# L68 - 82 (-18) +1
# L30 - 52 (-48)
# R48 - 0 (0) +1
# L5 - 95 (-5)
# R60 - 55 (55) +1
# L55 - 0 (0) +1
# L1 - 99 (-1)
# L99 - 0 (-100) +1
# R14 - 14 (-86) ~ something wrong here
# L82 - 68 (-168) +1