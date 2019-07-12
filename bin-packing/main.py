import parser
import model
import sys


def main():
    items, total_weight = parser.read_file("instances/" + sys.argv[1])
    objective_function, m = model.solve(items, total_weight)
    model.print_used_vars(m)
    print("Objective Function: " + str(objective_function))


if __name__ == "__main__":
    main()
