import time

from gurobipy import *

import File
import Model_Functions


def main():
    begin = time.time()
    polygons, limits = File.polygons_from_txt("Test/" + sys.argv[1] + "/instance.txt",
                                              "Test/" + sys.argv[1] + "/general_data.txt")
    limit_x = limits[0]
    limit_y = limits[1]
    m = Model('nesting')
    m, delta, z, inner_fit_polygon = Model_Functions.add_var(m, polygons, limit_x, limit_y)
    m = Model_Functions.add_constraints(m, polygons, limit_x, limit_y, inner_fit_polygon, delta, z)
    m.write("model.lp")
    m.update()
    m.optimize()
    obj = m.getObjective()
    print("Objective Function: " + str(obj.getValue()))
    print("Time: " + str(time.time() - begin))
    Model_Functions.plot_polygon(m, polygons, limit_x, limit_y, sys.argv[1])


if __name__ == "__main__":
    main()
