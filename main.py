print("Wszystkie wartości podaj w jednostkach ukladu SI")
inductance = float(input("Podaj indukcyjnosc: "))
capacity = float(input("Podaj pojemnosc: "))
voltage = float(input("Podaj napiecie: "))
resistance = float(input("Podaj rezystancje: "))
mass = float(input("Podaj mase pocisku: "))
print()

CurrentChanging = voltage/inductance
TimeConstant = capacity * resistance
MaxCurrent = voltage/resistance
Capacity = MaxCurrent/(CurrentChanging * 5 * resistance)

if CurrentChanging*5*TimeConstant >= MaxCurrent:
    Current = MaxCurrent
else:
    Current = CurrentChanging*5*TimeConstant

print("Prad zmieniajacy sie w cewce: ", CurrentChanging, "A/s")
print("Stala czasowa: ", TimeConstant)
print("Maksymalny prad: ", MaxCurrent, "A")
print("Prad ktory osiagnie obwod (ogranicza pojemnosc kondensatora):", Current, "A")
print("Minimalna pojemnosc kondensatora, ktora musi byc aby wystapil maksymalny prad: ", Capacity, "F")
print("Maksymalna sila: ", MaxCurrent * inductance, "N")
print("Osiagnieta sila: ", Current * inductance, "N")
print("Maksymalne przyspieszenie pocisku: ", MaxCurrent*inductance/mass, "m/s")
print("Przyspieszenie pocisku: ", Current*inductance/mass, "m/s")




