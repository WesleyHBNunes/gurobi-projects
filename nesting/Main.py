from gurobipy import *

import File
import Model_Functions


def main():
    polygons, limits = File.polygons_from_txt("Test/shirts_4/instance.txt", "Test/shirts_4/general_data.txt")
    limit_x = limits[0]
    limit_y = limits[1]
    m = Model('nesting')
    m, delta, z, inner_fit_polygon = Model_Functions.add_var(m, polygons, limit_x, limit_y)
    m = Model_Functions.add_constraints(m, polygons, limit_x, limit_y, inner_fit_polygon, delta, z)
    m.write("model.lp")
    m.update()
    m.optimize()

    for v in m.getVars():
        if v.x == 1:
            print(v.varName)

    obj = m.getObjective()
    print("Objective Function: " + str(obj.getValue()))
    Model_Functions.plot_polygon(m, polygons, limit_x, limit_y, "shirts_4")


if __name__ == "__main__":
    main()
