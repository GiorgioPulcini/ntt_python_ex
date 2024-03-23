def is_triangle(side1: float, side2: float, side3: float) -> bool:
    if side1 <= 0.0 or side1 <= 0.0 or side1 <= 0.0:
        return False
    else:
        first_cond = ((side1 + side2) > side3)
        second_cond = ((side1 + side3) > side2)
        third_cond = ((side2 + side3) > side1)
        return first_cond and second_cond and third_cond
