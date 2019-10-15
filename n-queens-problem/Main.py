import parser
import model


def main():
    n = parser.read_file("Instances/instance1.txt")
    objective_function, m = model.solve(n)
    print("Objective Function: " + str(objective_function))


if __name__ == "__main__":
    main()
