from gurobi import *

# N Facilities
# M Client


def solve(n, m, c, a, b, f):
    env = Env()
    env.setParam('TimeLimit', 3600)
    model = Model('Facility allocation model', env)
    x, y = add_vars(model, n, m)
    set_objective_function(model, x, y, n, m, f, c)
    add_constraints(model, x, y, n, m, a, b)
    model.update()
    write_model(model)
    model.optimize()
    return model.getObjective().getValue(), model


def add_vars(model, n, m):
    x = [[model.addVar(vtype=GRB.CONTINUOUS, name="Client " + str(i) + " attend by facility " + str(j))
          for j in range(n)] for i in range(m)]
    y = [model.addVar(vtype=GRB.BINARY, name="Facility " + str(j) + " activated") for j in range(n)]
    model.update()
    return x, y


def set_objective_function(model, x, y, n, m, f, c):
    model.setObjective(quicksum(quicksum(c[i][j] * x[i][j] for j in range(n)) for i in range(m))
                       + quicksum(f[j] * y[j] for j in range(n)))


def add_constraints(model, x, y, n, m, a, b):
    for i in range(m):
        model.addConstr(quicksum(x[i][j] for j in range(n)) == a[i],
                        name="Attendance of client " + str(i))

    for j in range(n):
        model.addConstr(quicksum(x[i][j] for i in range(m)) <= b[j] * y[j],
                        name="Capacity of facility " + str(j))
    model.update()


def write_model(model):
    model.write('model.lp')


def print_used_vars(model):
    print()
    variables = model.getVars()
    for var in variables:
        if var.x != 0:
            print(var.varName)
    print()
