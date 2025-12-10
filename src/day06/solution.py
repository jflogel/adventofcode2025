import re


def _parse_line(line):
    return [int(x) for x in re.split(r"\s+", line)]

def _parse_operations(line):
    return [x for x in re.split(r"\s+", line)]

def solution_1(lines):
    list_of_numbers = [_parse_line(x) for x in lines[:len(lines) - 1]]
    operations = _parse_operations(lines[len(lines) - 1])
    total = 0

    for index, operation in enumerate(operations):
        total_for_operation = 1 if operation == '*' else 0
        for numbers in list_of_numbers:
            if operation == '*':
                total_for_operation = total_for_operation * numbers[index]
            else:
                total_for_operation = total_for_operation + numbers[index]
        total = total + total_for_operation

    return total

def solution_2(lines):
    lines_without_line_breaks = [x.replace("\n", "") for x in lines]

    last_line = lines[len(lines) - 1]
    # all_numbers = "\n".join(lines[:len(lines) - 1])
    # operations = _parse_operations(lines[len(lines) - 1])
    columns = []
    # for char in lines_without_line_breaks[0]:
    #     print(char)


    print("\n\n")
    print(lines_without_line_breaks)
    print(columns)
    # print(all_numbers)
    # print(operations)
    print(re.findall(r"[\*\+]\s*", last_line))

    total = 0

    # for index, operation in enumerate(operations):
    #     total_for_operation = 1 if operation == '*' else 0
    #     for numbers in list_of_numbers:
    #         if operation == '*':
    #             total_for_operation = total_for_operation * numbers[index]
    #         else:
    #             total_for_operation = total_for_operation + numbers[index]
    #     total = total + total_for_operation

    return total
