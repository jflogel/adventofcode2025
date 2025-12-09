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
    combination = range(100)
    for line in lines:
        direction = line[:1]
        count = int(line[1:])
        hundreds = int(count / 100)
        zero_count = zero_count + hundreds
        remainder = count % 100

        if direction == "L":
            temp = current_position - remainder
            next_position = combination[temp]
            if remainder >= current_position != 0:
                zero_count = zero_count + 1
        else:
            temp = current_position + remainder
            if temp >= 100:
                next_position = temp - 100
                zero_count = zero_count + 1
            else:
                next_position = temp
        current_position = next_position
    return zero_count
