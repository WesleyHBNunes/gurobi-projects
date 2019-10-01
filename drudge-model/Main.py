import model


def main():
    objective_function, m = model.solve()
    model.print_vars(m)
    print("Objective Function: " + str(objective_function))


if __name__ == "__main__":
    main()
