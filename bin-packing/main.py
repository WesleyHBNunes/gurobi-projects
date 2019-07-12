import parser
import model


def main():
    items, total_weight = parser.read_file("instances/knapPI_3_10000_1000_1")
    objective_function, m = model.solve(items, total_weight)
    model.print_used_vars(m)
    print("Objective Function: " + str(objective_function))


if __name__ == "__main__":
    main()
