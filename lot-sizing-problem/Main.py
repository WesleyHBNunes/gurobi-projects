import model
import parser


def main():
    n, p, h, f, d = parser.read_file('Instances/instance1.txt')
    objective_function, m = model.solve(n, p, h, f, d)
    print("Objective Function: " + str(objective_function))


if __name__ == "__main__":
    main()
