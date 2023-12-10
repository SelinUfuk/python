print("""********************
Hesap Makinesi Programı

İşlemler:  

1.Toplama İşlemi

2.Çıkarma İşlemi

3.Çarpma İşlemi

4.Bölme İşlemi
********************
""")
a = int(input("Birinci sayı:"))
b = int(input("İkinci sayı:"))

işlem = input("İşlem giriniz:")

if işlem =="1":
    print("{} ile {} in toplamı {} dır.".format(a, b, (a+b)))
elif işlem == "2":
    print("{} ile {} in çıkarması {} dır.".format(a, b, (a - b)))
elif işlem == "3":
    print("{} ile {} in çarpması {} dır.".format(a, b, (a * b)))
elif işlem =="4":
    print("{} ile {} in bölmesi {} dır.".format(a, b, (a / b)))
else:
    print("Geçerli bir işlem giriniz")
