import math
k = float(input("Длина палки: "))
h = float(input("Шаг: "))
steps = int((3 - 2) / h) + 1
for i in range(steps):
    y = 2 + i * h
    gradus = math.degrees(math.acos(y / k))
    print("При y =", round(y, 2), "угол =", round(gradus, 1))