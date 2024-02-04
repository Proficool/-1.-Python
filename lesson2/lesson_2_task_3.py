side_input = input("Введите длину стороны квадрата:")
side_length = float(side_input)

import math

def square(side_length):

    if isinstance(side_length, int):
        area = side_length * side_length
    else:
        area = math.ceil(side_length * side_length)

    return area

result = square(side_length)

print("Площадь квадрата со стороной " + str(side_length) + ": " + str(result))
