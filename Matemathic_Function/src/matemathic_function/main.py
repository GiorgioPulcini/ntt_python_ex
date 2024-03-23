from Matemathic_Function.src.matemathic_function.hello import hello
from Matemathic_Function.src.matemathic_function.math_function import EquilateralTriangle, IsoscelesTriangle, ScaleneTriangle


def main():
    friend = input("Hi, what's your name?\n")
    print(hello(friend))
    triangle_type = input("Choose a type of triangle between equilateral, isosceles and scalene\n").lower()
    try:
        if triangle_type == "equilateral":
            side = float(input("Insert side length\n"))
            if side < 0.0:
                print("Sorry, the side length must be positive")
            else:
                et = EquilateralTriangle(side)
                print("Perimeter:", et.perimeter())
                print("Area:", et.area())
        elif triangle_type == "isosceles":
            base = float(input("Insert base side\n"))
            lateral = float(input("Insert lateral side\n"))
            if base < 0.0 or lateral < 0.0:
                print("Sorry, side lengths must be positive")
            else:
                it = IsoscelesTriangle(base, lateral)
                print("Perimeter:", it.perimeter())
                print("Area:", it.area())
        elif triangle_type == "scalene":
            sides = [float(input("Insert side length\n")) for _ in range(3)]
            if any(side < 0.0 for side in sides):
                print("Sorry, side lengths must be positive")
            else:
                st = ScaleneTriangle(*sides)
                print("Perimeter:", st.perimeter())
                print("Area:", st.area())
        else:
            print("Sorry, I don't understand")
    except ValueError:
        print("Sorry, that was not a valid number. Please enter numeric values.")


if __name__ == "__main__":
    main()
