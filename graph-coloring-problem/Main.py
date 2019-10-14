import model
import parser


def main():
    graph = parser.read_file('Instances/instance1.txt')
    objective_function, m = model.solve(graph)
    model.print_used_vars(m)
    print("Objective Function: " + str(objective_function + 1))


if __name__ == "__main__":
    main()
