def read_file(file):
    file = open(file, "r")
    lines = file.readlines()
    return int(lines[1].strip('\n'))
