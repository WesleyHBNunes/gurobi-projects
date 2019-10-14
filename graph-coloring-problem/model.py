from gurobi import *


def solve(graph):
    env = Env()
    env.setParam('TimeLimit', 3600)
    model = Model('Graph Coloring model', env)
    add_vars(model, graph)
    set_objective_function(model)
    add_constraints(model, graph)
    write_model(model)
    model.optimize()
    return model.getObjective().getValue(), model


def add_vars(model, graph):
    pass
    return


def set_objective_function(model):
    pass


def add_constraints(model, graph):
    pass


def write_model(model):
    model.write('model.lp')


def print_used_vars(model):
    print()
    variables = model.getVars()
    for var in variables:
        if var.x >= 0:
            print(var.varName + ": " + str(var.x))
    print()
