print("Girdiğiniz üç sayının en büyüğünü seçelim:")

a = float(input("Birinci sayınızı giriniz:"))
b = float(input("İkinci sayınızı giriniz:"))
c = float(input("Üçüncü sayınızı giriniz:"))

if a > b and a > c:
    print("Girdiğiniz en büyük sayı:", a)
elif b > a and b > c:
    print("Girdiğiniz en büyük sayı:", b)
else:
    print("Girdiğiniz en büyük sayı:", c)
