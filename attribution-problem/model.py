from gurobi import *


def solve(coast, n):
    env = Env()
    env.setParam('TimeLimit', 3600)
    model = Model('Attribution Problem model', env)
    x = add_vars(model, n)
    set_objective_function(model, x, coast, n)
    add_constraints(model, x, n)
    model.update()
    write_model(model)
    model.optimize()
    return model.getObjective().getValue(), model


def add_vars(model, n):
    x = [[model.addVar(vtype=GRB.BINARY, name='Edge ' + str(i) + '-' + str(j)) for j in range(n)] for i in range(n)]
    model.update()
    return x


def set_objective_function(model, x, coast, n):
    model.setObjective(quicksum(quicksum(x[i][j] * coast[i][j] for j in range(n)) for i in range(n)))


def add_constraints(model, x, n):
    for i in range(n):
        model.addConstr(quicksum(x[i][j] for j in range(n)) == 1,
                        name='Number of task executed by people ' + str(i))
    for j in range(n):
        model.addConstr(quicksum(x[i][j] for i in range(n)) == 1, name='Number of people executing task ' + str(j))

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
