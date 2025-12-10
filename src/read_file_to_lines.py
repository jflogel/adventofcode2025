def read_file_to_lines(filename, with_strip = True):
    with open(filename) as f:
        lines = []
        for x in f:
            lines.append(x.strip() if with_strip else x)
        return lines