def read_file(file):
    file = open(file, "r")
    lines = file.readlines()
    n = int(lines[1].strip('\n'))
    line = 3
    p = []
    while lines[line][0] != '#':
        p.append(float(lines[line].strip('\n')))
        line += 1
    line += 1
    h = []
    while lines[line][0] != '#':
        h.append(float(lines[line].strip('\n')))
        line += 1
    line += 1
    f = []
    while lines[line][0] != '#':
        f.append(float(lines[line].strip('\n')))
        line += 1
    line += 1
    d = [float(l.strip('\n')) for l in lines[line:]]
    return n, p, h, f, d
