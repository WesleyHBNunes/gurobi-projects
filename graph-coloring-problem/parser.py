def read_file(file):
    file = open(file, "r")
    lines = file.readlines()
    n = int(lines[1].strip('\n'))
    line = 3
    graph = [[0 for _ in range(n)] for _ in range(n)]
    while lines[line][0] != '#':
        i, j = lines[line].strip('\n').split(' ')
        graph[int(i)][int(j)] = 1
        graph[int(j)][int(i)] = 1
        line += 1
    return graph


