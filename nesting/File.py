import Polygon

# CONSTS
COLUMN_LINE_WIDTH_DATA = 3
INITIAL_LINE_POINTS_DATA = 5


def polygons_from_txt(file_name, board_limit_file):
    file = open(file_name, "r")
    line = file.readline()
    array_polygons = []
    amount_polygons = 0
    while line != "#":
        if line == "QUANTITY":
            amount_polygons = int(file.readline())
            line = amount_polygons
        elif line == "VERTICES (X,Y)":
            line = file.readline()
            array_points_tuple = []
            while line != "\n":
                points = line.split()
                array_points_tuple.append((int(points[0]), int(points[1])))
                line = file.readline()
            array_points_tuple = Polygon.set_points_to_positive(array_points_tuple)
            for i in range(amount_polygons):
                array_polygons.append(array_points_tuple)
        else:
            line = file.readline().strip()
    file.close()
    return array_polygons, return_limits_of_board_txt(board_limit_file)


def return_limits_of_board_txt(file_name):
    file = open(file_name, "r")
    file.readline()
    x = file.readline()
    x = x.split("\n")
    x = x[0].split("#")
    x = x[1].split(" ")
    y = file.readline()
    y = y.split("\n")
    y = y[0].split("#")
    y = y[1].split(" ")
    file.close()
    return int(x[1]), int(y[1])
