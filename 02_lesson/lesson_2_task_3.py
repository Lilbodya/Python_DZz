import math


def square(side):
    area = side * side
    return math.ceil(area)


s = 4
result = square(s)

print("Сторона квадрата:", s)
print("Площадбь квадрата:", result)
