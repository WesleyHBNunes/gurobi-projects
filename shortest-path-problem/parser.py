def read_file(file):
    file = open(file, "r")
    lines = file.readlines()
    n = int(lines[1].strip('\n'))
    begin_end = lines[3].strip('\n').split()
    line = 5
    graph = [[-1 for _ in range(n)] for _ in range(n)]
    while lines[line][0] != '#':
        i, j, coast = lines[line].strip('\n').split(' ')
        graph[int(i)][int(j)] = float(coast)
        line += 1
    return graph, int(begin_end[0]), int(begin_end[1])


