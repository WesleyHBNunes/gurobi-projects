import model
import parser


def main():
    parser.read_file('Instances/instance1.txt')
    objective_function, m = model.solve()
    model.print_used_vars(m)
    print("Objective Function: " + str(objective_function))


if __name__ == "__main__":
    main()
