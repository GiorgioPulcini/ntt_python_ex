from hello import hello
from math_function import EquilateralTriangle, IsoscelesTriangle, ScaleneTriangle

if __name__ == "__main__":
    friend = input("Hi, what's your name?\n")
    hello(friend)
    while True:
        triangle_type = input("Choose a type of triangle between equilateral, isosceles and scalene\n").lower()
        if triangle_type == "equilateral":
            side = float(input("Insert side length\n"))
            et = EquilateralTriangle(side)
            print("Perimeter:", et.perimeter())
            print("Area:", et.area())
            break
        elif triangle_type == "isosceles":
            base = float(input("Insert base side\n"))
            lateral = float(input("Insert lateral side\n"))
            it = IsoscelesTriangle(base, lateral)
            print("Perimeter:", it.perimeter())
            print("Area:", it.area())
            break
        elif triangle_type == "scalene":
            sides = [float(input("Insert side lenght\n")) for _ in range(3)]
            st = ScaleneTriangle(*sides)
            print("Perimeter:", st.perimeter())
            print("Area:", st.area())
            break
        else:
            print("Sorry, I don't understand")
