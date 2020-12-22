
def my_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    max_lines = len(lines)
    for i in range(max_lines):
        lines[i] = lines[i].strip()

    return lines
