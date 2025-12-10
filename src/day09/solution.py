def _parse_line(line):
    arr = line.split(",")
    return int(arr[0]), int(arr[1])

def area_of_points(point1, point2):
    return (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)

def solution_1(lines):
    points = [_parse_line(x) for x in lines]

    largest_box_coordinates = [points[0], points[1]]
    largest_area = area_of_points(largest_box_coordinates[0], largest_box_coordinates[1])

    for index, point in enumerate(points):
        for next_point in points[index:]:
            area = area_of_points(point, next_point)
            if area > largest_area:
                largest_area = area
                largest_box_coordinates = [point, next_point]

    return largest_area

def solution_2(lines):
    return 0
