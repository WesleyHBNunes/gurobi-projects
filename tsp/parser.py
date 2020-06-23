def read_file(file):

    file = open(file, "r")
    lines = file.readlines()
    number_of_vertex = int(lines[0].strip('\n'))
    graph = [[99999 for _ in range(number_of_vertex)] for _ in range(number_of_vertex)]
    for line in lines[1:]:
        i, j, coast = line.strip('\n').split(' ')
        graph[int(i)][int(j)] = float(coast)
    return graph, number_of_vertex
