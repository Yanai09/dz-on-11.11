#100 // 10 = 10 
for byki in range(11):
    #100 // 5 = 20
    for korovy in range(21):
        for telyata in range(0, 101, 2):
            if byki + korovy + telyata == 100:
                if (byki * 10 + korovy * 5 + telyata * 0.5) == 100:
                    print(f"Быков: {byki}, Коров: {korovy}, Телят: {telyata}")
