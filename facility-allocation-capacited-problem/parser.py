def read_file(file):
    file = open(file, "r")
    lines = file.readlines()
    m = int(lines[1].strip('\n'))
    n = int(lines[3].strip('\n'))
    line = 5
    c = [[[] for _ in range(n)] for _ in range(m)]
    while lines[line][0] != '#':
        coast, j, i = lines[line].strip('\n').split(' ')
        c[int(i)][int(j)] = float(coast)
        line += 1
    line += 1
    a = []
    while lines[line][0] != '#':
        a.append(float(lines[line].strip('\n')))
        line += 1
    line += 1
    b = []
    while lines[line][0] != '#':
        b.append(float(lines[line].strip('\n')))
        line += 1
    line += 1
    f = [float(l.strip('\n')) for l in lines[line:]]

    return n, m, c, a, b, f
