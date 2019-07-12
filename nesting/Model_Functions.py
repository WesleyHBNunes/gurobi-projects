from gurobipy import *

import Polygon
from Visualizer import Visualizer


def add_var(m, polygons, limit_x, limit_y):
    inner_fit_polygon = []
    # Created a IFP set for all polygons based on limits and NFP
    for t in range(len(polygons)):
        inner_fit_polygon.append(return_inner_fit(polygons[t], limit_x, limit_y, (polygons[t][0])))

    # Objective Function
    z = m.addVar(vtype=GRB.INTEGER, name="z")
    m.setObjective(z, GRB.MINIMIZE)

    # Defined all d point for all polygon in IFP
    delta = []
    for t in range(len(polygons)):
        delta.append([])
        for x in range(limit_x + 1):
            delta[t].append([])
            for y in range(limit_y + 1):
                delta[t][x].append(m.addVar(vtype=GRB.BINARY, name=str(t) + " " + str(x) + " " + str(y)))
                if not (x, y) in inner_fit_polygon[t]:
                    m.addConstr(delta[t][x][y] == 0,
                                name="IFP = Point(" + str(x) + "," + str(y) + ") in polygon: " + str(t))
    return m, delta, z, inner_fit_polygon


def add_constraints(m, polygons, limit_x, limit_y, inner_fit_polygon, delta, z):
    # Constraint of Z
    for t in range(len(polygons)):
        for x in range(limit_x + 1):
            for y in range(limit_y + 1):
                if (x, y) in inner_fit_polygon[t]:
                    list_x, list_y = list(zip(*polygons[t]))
                    x_m_d = max(list_x) - polygons[t][0][0]
                    m.addConstr((x * 1 + x_m_d) * delta[t][x][y] <= z)

    # Constraint of the number of polygon
    total_sum = []
    for t in range(len(polygons)):
        total_sum.append(0)
        for x in range(limit_x + 1):
            for y in range(limit_y + 1):
                total_sum[t] += delta[t][x][y]
        m.addConstr(total_sum[t] == 1, name="Qtde polygons " + str(t))

    # No overlapping constraint
    for t in range(len(polygons)):
        for u in range(len(polygons)):
            if u != t:
                for x in range(limit_x + 1):
                    for y in range(limit_y + 1):
                        if (x, y) in inner_fit_polygon[t]:
                            for e_x in range(limit_x + 1):
                                for e_y in range(limit_y + 1):
                                    aux_poly_t = Polygon.add_number_axis_x_y(polygons[t],
                                                                             x - polygons[t][0][0],
                                                                             y - polygons[t][0][1])
                                    aux_poly_u = Polygon.add_number_axis_x_y(polygons[u],
                                                                             e_x - polygons[u][0][0],
                                                                             e_y - polygons[u][0][1])
                                    if Polygon.is_overlapping(aux_poly_t, aux_poly_u):
                                        m.addConstr(delta[t][x][y] + delta[u][e_x][e_y] <= 1)
    return m


def return_inner_fit(polygon, limit_x, limit_y, reference_point):
    points = []
    min_x, max_x, min_y, max_y = Polygon.min_max_points_polygon(polygon)
    for x in range(limit_x):
        for y in range(limit_y):
            if x + max_x <= limit_x and y + max_y <= limit_y and x >= reference_point[0] and y >= reference_point[1]:
                points.append((x, y))
    return points


def plot_polygon(m, polygons, limit_x, limit_y, title):
    for v in m.getVars():
        if v.x == 1:
            name = v.varName
            name = name.split(" ")
            i = int(name[0])
            point = [int(name[1]), int(name[2])]
            point[0] = point[0] - polygons[i][0][0]
            point[1] = point[1] - polygons[i][0][1]
            polygons[i] = Polygon.add_number_axis_x_y(polygons[i], point[0], point[1])
    polygons = Polygon.create_polygons_to_plot(polygons)
    visualiser = Visualizer(polygons, limit_x, limit_y, title)
    visualiser.plot_polygons()
