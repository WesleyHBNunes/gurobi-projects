from gurobi import *


def solve(graph):
    env = Env()
    env.setParam('TimeLimit', 3600)
    model = Model('Graph Coloring model', env)
    x, w = add_vars(model, graph)
    set_objective_function(model, w)
    add_constraints(model, graph, x, w)
    write_model(model)
    model.optimize()
    return model.getObjective().getValue(), model


def add_vars(model, graph):
    x = [[model.addVar(vtype=GRB.BINARY, name="Vertex " + str(i) + " colored with color " + str(j))
          for j in range(len(graph))]
         for i in range(len(graph))]

    w = [model.addVar(vtype=GRB.BINARY, name="Color " + str(j) + " used") for j in range(len(graph))]
    model.update()
    return x, w


def set_objective_function(model, w):
    model.setObjective(quicksum(w[j] for j in range(len(w))))


def add_constraints(model, graph, x, w):
    for i in range(len(x)):
        model.addConstr(quicksum(x[i][j] for j in range(len(w))) == 1, name="One color in vertex " + str(i))

    for i in range(len(x)):
        for k in range(len(x)):
            if graph[i][k] == 1 or graph[k][i] == 1:
                for j in range(len(w)):
                    model.addConstr(x[i][j] + x[k][j] <= w[j],
                                    name="Sum of colors of vertex " + str(i) + " and " + str(k)
                                         + " less or equal color " + str(j))

    model.update()
    return


def write_model(model):
    model.write('model.lp')


def print_used_vars(model):
    print()
    variables = model.getVars()
    for var in variables:
        if var.x == 1:
            print(var.varName)
    print()
