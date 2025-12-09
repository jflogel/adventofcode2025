def read_file_to_lines(filename):
    with open(filename) as f:
        lines = []
        for x in f:
            lines.append(x.strip())
        return lines