print("Vücut kitke indeksinizi hesaplayalım:)")

kg = float(input("Kilonuzu kg cinsinden giriniz:"))
m = float(input("Boyunuzu metre cinsinden giriniz:"))

vki = kg / (m**2)
print("Vücut kitle indeksiniz: {:.2f}".format(vki))
if vki < 18.5:
    print("Zayıf.")
elif 18.5 <= vki < 25:
    print("Normal")
elif 25 <= vki < 30:
    print("Fazla kilolu.")
else:
    print("Obez.")
    