from gurobi import *


def solve(coast, n):
    env = Env()
    env.setParam('TimeLimit', 3600)
    model = Model('TSP model', env)
    x, u = add_vars(model, n)
    set_objective_function(model, x, coast, n)
    add_constraints(model, x, u, n)
    model.update()
    write_model(model)
    model.optimize()
    return model.getObjective().getValue(), model


def add_vars(model, n):
    x = [[model.addVar(vtype=GRB.BINARY, name='X ' + str(i) + '-' + str(j)) for j in range(n)] for i in range(n)]
    model.update()
    u = [model.addVar(vtype=GRB.INTEGER, name='U' + str(i)) for i in range(n)]
    return x, u


def set_objective_function(model, x, coast, n):
    model.setObjective(quicksum(quicksum(x[i][j] * coast[i][j] for j in range(n)) for i in range(n)))


def add_constraints(model, x, u, n):
    for i in range(n):
        model.addConstr(quicksum(x[i][j] for j in range(n)) == 1)
    for j in range(n):
        model.addConstr(quicksum(x[i][j] for i in range(n)) == 1)

    model.addConstr(u[0] == 1)
    for i in range(1, n):
        model.addConstr(2 <= u[i])
        model.addConstr(u[i] <= n)

    for i in range(1, n):
        for j in range(1, n):
            model.addConstr(u[i] - u[j] + 1 <= (n - 1) * (1 - x[i][j]))

    model.update()


def write_model(model):
    model.write('model.lp')


def print_used_vars(model):
    print()
    variables = model.getVars()
    for var in variables:
        if var.x == 1:
            print(var.varName)
    print()
