import model
import parser


def main():
    n, m, c, f = parser.read_file('Instances/instance1.txt')
    objective_function, model_created = model.solve(n, m, c, f)
    model.print_used_vars(model_created)
    print("Objective Function: " + str(objective_function))


if __name__ == "__main__":
    main()
