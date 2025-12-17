def _is_roll(char):
    return char == '@'

def solution_1(lines):
    total = 0

    for line_index, line in enumerate(lines):
        line_before = None
        line_after = None
        if line_index > 0:
            line_before = lines[line_index - 1]
        if line_index + 1 < len(lines):
            line_after = lines[line_index + 1]

        for char_index, char in enumerate(line):
            if not _is_roll(char):
                continue

            adjacent_rolls = 0
            if char_index > 0:
                char_before = line[char_index - 1]
                line_before_char_before = line_before[char_index - 1] if line_before is not None else None
                line_after_char_before = line_after[char_index - 1] if line_after is not None else None

                adjacent_rolls = adjacent_rolls + (1 if _is_roll(char_before) else 0)
                adjacent_rolls = adjacent_rolls + (1 if _is_roll(line_before_char_before) else 0)
                adjacent_rolls = adjacent_rolls + (1 if _is_roll(line_after_char_before) else 0)

            if char_index + 1 < len(line):
                char_after = line[char_index + 1]
                line_before_char_after = line_before[char_index + 1] if line_before is not None else None
                line_after_char_after = line_after[char_index + 1] if line_after is not None else None

                adjacent_rolls = adjacent_rolls + (1 if _is_roll(char_after) else 0)
                adjacent_rolls = adjacent_rolls + (1 if _is_roll(line_before_char_after) else 0)
                adjacent_rolls = adjacent_rolls + (1 if _is_roll(line_after_char_after) else 0)

            adjacent_rolls = adjacent_rolls + (1 if line_before is not None and _is_roll(line_before[char_index]) else 0)
            adjacent_rolls = adjacent_rolls + (1 if line_after is not None and _is_roll(line_after[char_index]) else 0)

            if adjacent_rolls < 4:
                total = total + 1

    return total

def solution_2(lines):
    total = 0
    return total