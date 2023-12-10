print("Harf notunuzu hesaplayalım;")

v1 = float(input("Birinci vize notunuzu giriniz:"))
v2 = float(input("İkinci vize notunuzu giriniz."))
fnl = float(input("Final notunuzu giriniz:"))

an = (v1 * 0.3) + (v2 * 0.3) + (fnl * 0.4)

print("Notunuz:", an)

if an >= 90:
    print("AA")
elif an >= 85:
    print("BA")
elif an >= 80:
    print("BB")
elif an >= 75:
    print("CB")
elif an >= 70:
    print("CC")
elif an >= 65:
    print("CD")
elif an >= 60:
    print("DD")
elif an >= 55:
    print("FD")
elif an < 55:
    print("FF")
