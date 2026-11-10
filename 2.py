S = int(input("Введите количество дней (S): "))
dis = 10
plus = 0
for day in range (S):
    plus += dis
    dis = dis * 1.1
print(f"За {S} дней спортсмен суммарно пробежит: {round(plus, 2)} км")