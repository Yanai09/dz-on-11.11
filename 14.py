stip = float(input("Стипендия: "))
rashod = float(input("Расходы: "))
nuzhno = 0 
for mesyac in range(10):
    doplata = rashod - stip
    nuzhno = nuzhno + doplata
    rashod = rashod * 1.03
print("У родителей нужно попросить:", nuzhno)