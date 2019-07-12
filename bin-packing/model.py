from gurobipy import *

PROFIT = 0
WEIGHT = 1


def solve(items, total_weight):
    env = Env()
    env.setParam('TimeLimit', 3600)
    model = Model('Bin Packing Model', env)
    add_vars(model, items)
    set_objective_function(model, items)
    add_constraints(model, items, total_weight)
    model.update()
    write_model(model)
    model.optimize()
    return model.getObjective().getValue(), model


def add_constraints(model, items, total_weight):
    variables = model.getVars()
    sum_weight = 0
    for i, items in enumerate(items):
        sum_weight += variables[i] * items[WEIGHT]
    model.addConstr(sum_weight <= total_weight, name="Capacity_constraint")


def set_objective_function(model, items):
    variables = model.getVars()
    sum_profit = 0
    for i, item in enumerate(items):
        sum_profit += variables[i] * item[PROFIT]
    model.setObjective(sum_profit, GRB.MAXIMIZE)


def add_vars(model, items):
    for i, item in enumerate(items):
        model.addVar(vtype=GRB.BINARY, name="item_" + str(i))
    model.update()


def write_model(model):
    model.write("model.lp")


def print_used_vars(model):
    variables = model.getVars()
    for var in variables:
        if var.x == 1:
            print(var.varName)
    print()
