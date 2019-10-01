from gurobi import *


def solve():
    env = Env()
    env.setParam('TimeLimit', 3600)
    model = Model('Drudge Model', env)
    add_vars(model)
    set_objective_function(model)
    add_constraints(model)
    model.update()
    write_model(model)
    model.optimize()
    return model.getObjective().getValue(), model


def add_vars(model):
    model.addVar(vtype=GRB.INTEGER, name="x1 - Drudge")
    model.addVar(vtype=GRB.INTEGER, name="x2 - Donkey")
    model.update()


def set_objective_function(model):
    variables = model.getVars()
    model.setObjective(30 * variables[0] + 20 * variables[1], GRB.MINIMIZE)


def write_model(model):
    model.write('model.lp')


def add_constraints(model):
    variables = model.getVars()
    model.addConstr(100 * variables[0] + 50 * variables[1] == 1000, name="Load")
    model.addConstr(3 * variables[0] + 2 * variables[1] <= 35, name="Food")
    model.addConstr(100 * variables[0] + 30 * variables[1] <= 900, name="Water")
    model.addConstr(variables[0] >= 0, name="Not negativity Drudge")
    model.addConstr(variables[1] >= 0, name="Not negativity Donkey")
    model.update()


def print_vars(model):
    variables = model.getVars()
    print()
    print("x1 - Drudge: " + str(variables[0].x))
    print("x2 - Donkey: " + str(variables[1].x))
