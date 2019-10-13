from gurobi import *


def solve(graph, begin, end):
    env = Env()
    env.setParam('TimeLimit', 3600)
    model = Model('Shortest Path Problem model', env)
    x = add_vars(model, graph)
    set_objective_function(model, graph, x)
    add_constraints(model, x, begin, end)
    model.update()
    write_model(model)
    model.optimize()
    return model.getObjective().getValue(), model


def add_vars(model, graph):
    x = []
    for i in range(len(graph)):
        x.append([])
        for j in range(len(graph)):
            if graph[i][j] != -1:
                x[i].append(model.addVar(vtype=GRB.BINARY,
                                         name=str(i) + " to " + str(j) + " with distance: " + str(graph[i][j])))
            else:
                x[i].append(0)
    model.update()
    return x


def set_objective_function(model, graph, x):
    model.setObjective(quicksum(x[i][j] * graph[i][j]
                                for j in range(len(graph))
                                for i in range(len(graph))
                                if graph[i][j] != -1), GRB.MINIMIZE)


def add_constraints(model, x, begin, end):
    for i in range(len(x)):
        if i == begin:
            model.addConstr(quicksum(x[i][j] for j in range(len(x)))
                            - quicksum(x[j][i] for j in range(len(x))) == 1,
                            name="Consesvation restriction of vertex " + str(i))
        elif i == end:
            model.addConstr(quicksum(x[i][j] for j in range(len(x)))
                            - quicksum(x[j][i] for j in range(len(x))) == -1,
                            name="Consesvation restriction of vertex " + str(i))
        else:
            model.addConstr(quicksum(x[i][j] for j in range(len(x)))
                            - quicksum(x[j][i] for j in range(len(x))) == 0,
                            name="Consesvation restriction of vertex " + str(i))

    for i in range(len(x)):
        model.addConstr(quicksum(x[i][j] for j in range(len(x))) <= 1, name="One arc going out vertex " + str(i))


def write_model(model):
    model.write('model.lp')


def print_used_vars(model):
    print()
    variables = model.getVars()
    for var in variables:
        if var.x == 1:
            print(var.varName)
    print()
