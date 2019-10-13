from gurobi import *


def solve():
    env = Env()
    env.setParam('TimeLimit', 3600)
    model = Model('Shortest Path Problem model', env)
    add_vars(model)
    set_objective_function(model)
    add_constraints(model)
    model.update()
    write_model(model)
    model.optimize()
    return model.getObjective().getValue(), model


def add_vars(model):
    pass


def set_objective_function(model):
    pass


def add_constraints(model):
    pass


def write_model(model):
    model.write('model.lp')


def print_used_vars(model):
    print()
    variables = model.getVars()
    for var in variables:
        if var.x == 1:
            print(var.varName)
    print()
