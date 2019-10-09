from gurobi import *
M = 99999


def solve(n, p, h, f, d):
    env = Env()
    env.setParam('TimeLimit', 3600)
    model = Model('Lot sizing model', env)
    x, s, y = add_vars(model, n)
    set_objective_function(model, n, p, h, f, x, s, y)
    add_constraints(model, n, x, s, y, d)
    model.update()
    write_model(model)
    model.optimize()
    print_used_vars(x, s, y)
    return model.getObjective().getValue(), model


def add_vars(model, n):
    x = [model.addVar(vtype=GRB.CONTINUOUS, name="Amount produced of item in period " + str(t)) for t in range(n)]
    s = [model.addVar(vtype=GRB.CONTINUOUS, name="Stock on period " + str(t)) for t in range(n)]
    y = [model.addVar(vtype=GRB.BINARY, name="Produced on period " + str(t)) for t in range(n)]
    model.update()
    return x, s, y


def set_objective_function(model, n, p, h, f, x, s, y):
    model.setObjective(quicksum(p[t] * x[t] for t in range(n)) +
                       quicksum(h[t] * s[t] for t in range(n)) +
                       quicksum(f[t] * y[t] for t in range(n)), GRB.MINIMIZE)


def add_constraints(model, n, x, s, y, d):
    for t in range(n):
        if t == 0:
            model.addConstr(0 + x[t] == d[t] + s[t], name="Production on period " + str(t))
        else:
            model.addConstr(s[t - 1] + x[t] == d[t] + s[t], name="Production and stock on period " + str(t))

    [model.addConstr(x[t] <= M * y[t], name="Activation of production on period " + str(t)) for t in range(n)]


def write_model(model):
    model.write('model.lp')


def print_used_vars(x, s, y):
    print()
    for var in x:
        if var.x != 0:
            print(var.varName + ": " + str(var.x))
    print()
    for var in s:
        if var.x != 0:
            print(var.varName + ": " + str(var.x))
    print()
    for var in y:
        if var.x != 0:
            print(var.varName)
    print()
