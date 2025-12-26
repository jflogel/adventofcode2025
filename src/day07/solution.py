def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def solution_1(lines):
    total = 0
    new_lines = [lines[0], lines[0].replace("S", "|")]

    for index, original_line in enumerate(lines[2:]):
        previous_line = new_lines[index + 1]
        all_beam_indexes = find(previous_line, "|")
        all_splitter_indexes = find(original_line, "^")
        beam_indexes_to_split = [b for b in all_beam_indexes if b in all_splitter_indexes]
        total = total + len(beam_indexes_to_split)

        new_line = ""
        for index, char in enumerate(original_line):
            prev_line_char = previous_line[index]
            prev_line_prev_char = previous_line[index - 1] if index > 0 else None
            prev_line_next_char = previous_line[index + 1] if index + 1 < len(original_line) else None
            curr_line_prev_char = original_line[index - 1] if index > 0 else None
            curr_line_next_char = original_line[index + 1] if index + 1 < len(original_line) else None

            if prev_line_char == "^":
                new_line = new_line + "."
                continue
            if char == "^":
                new_line = new_line + "^"
                continue
            if (prev_line_prev_char == "|" and curr_line_prev_char == "^") or (prev_line_next_char == "|" and curr_line_next_char == "^"):
                new_line = new_line + "|"
                continue
            if prev_line_char == "|":
                new_line = new_line + "|"
                continue
            else:
                new_line = new_line + "."

        new_lines.append(new_line)

    return total

def solution_2(lines):
    total = 0

    return total
