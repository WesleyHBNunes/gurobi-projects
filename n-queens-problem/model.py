from gurobipy import *


def solve(n):
    env = Env()
    env.setParam('TimeLimit', 3600)
    model = Model('Bin Packing Model', env)
    x = add_vars(model, n)
    set_objective_function(model, x)
    write_model(model)
    add_constraints(model, x)
    model.update()
    model.optimize()
    print_used_vars(x)
    return model.getObjective().getValue(), model


def add_vars(model, n):
    x = [[model.addVar(vtype=GRB.BINARY, name="One queen in position " + str(i) + ", " + str(j))
          for j in range(n)]
         for i in range(n)]
    model.update()
    return x


def set_objective_function(model, x):
    model.setObjective(quicksum(x[i][j] for j in range(len(x)) for i in range(len(x))), GRB.MAXIMIZE)


def add_constraints(model, x):
    for i in range(len(x)):
        model.addConstr(quicksum(x[i][j] for j in range(len(x))) <= 1, name="One queen on line " + str(i))

    for j in range(len(x)):
        model.addConstr(quicksum(x[i][j] for i in range(len(x))) <= 1, name="One queen on column " + str(j))

    for j in range(len(x)):
        model.addConstr(quicksum(x[i][i + j] for i in range(len(x) - j))
                        <= 1, name="Sum diagonal right upper " + str(j))
        model.addConstr(quicksum(x[i + j][i] for i in range(len(x) - j))
                        <= 1, name="Sum diagonal right lower" + str(j))

    for j in range(len(x)):
        model.addConstr(quicksum(x[j - i][i] for i in range(j + 1))
                        <= 1, name='Sum diagonal left upper ' + str(j))

    for i in range(len(x)):
        sum_of_diagonal_lower = 0
        aux = i
        for j in range(len(x) - 1, i - 1, -1):
            sum_of_diagonal_lower += x[aux][j]
            aux += 1
        model.addConstr(sum_of_diagonal_lower <= 1, name='Sum diagonal left upper ' + str(i))
    model.update()


def write_model(model):
    model.write("model.lp")


def print_used_vars(x):
    m = [[0 for _ in range(len(x))] for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x)):
            if x[i][j].x == 1:
                m[i][j] = 1
                print(x[i][j].varName)
            else:
                m[i][j] = 0
    print()
    for i in range(len(m)):
        print(m[i])
    print()
