from gurobi import *


def solve(graph):
    env = Env()
    env.setParam('TimeLimit', 3600)
    model = Model('Graph Coloring model', env)
    x = add_vars(model, graph)
    k = set_objective_function(model)
    add_constraints(model, graph, x, k)
    write_model(model)
    model.optimize()
    return model.getObjective().getValue(), model


def add_vars(model, graph):
    x = [model.addVar(vtype=GRB.BINARY, name="Color of vertex " + str(i)) for i in range(len(graph))]
    model.update()
    return x


def set_objective_function(model):
    k = model.addVar(vtype=GRB.INTEGER, name="Amount of colors")
    model.setObjective(k, GRB.MINIMIZE)
    model.update()
    return k


def add_constraints(model, graph, x, k):
    for i in range(len(x)):
        model.addConstr(x[i] <= k, "K les or equal of the number of colors of vertex " + str(i))

    constraints = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 1 or graph[j][i] == 1:
                c = model.addConstr(x[i] != x[j],
                                    name="Difference of color between vertex " + str(i) + " and " + str(j))
                constraints.append(c)
    model.update()
    return constraints


def write_model(model):
    model.write('model.lp')


def print_used_vars(model):
    print()
    variables = model.getVars()
    for var in variables:
        if var.x >= 1:
            print(var.varName + ": " + str(var.x))
    print()
