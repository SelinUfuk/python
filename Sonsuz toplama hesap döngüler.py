print("""
sürekli toplanacak sayı alıyor
ve q ya basınca girilen sayıları toplayıp ekrana bastırıyor.


""")
toplam = 0
while True:
    sayi = input("Sayı:")
    if (sayi == "q"):
        print("Program sonlandırılıyor...")

        break
    else:
        sayi = int(sayi)
        toplam += sayi

print(toplam)
