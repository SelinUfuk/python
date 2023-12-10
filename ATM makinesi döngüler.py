print("""
*****************************************
Atm Makinesine Hoşgeldiniz.

İşlemler:

1.Bakiye Sorgulama

2.Para Yatırma

3.Para Çekme

Programdan çıkmak için 'q' ya basın.
*******************************************
""")

bakiye = 1000

while True:
    işlem = input("İşlem seçiniz:")

    if (işlem == "q"):
        print("yine bekleriz.")
        break
    elif (işlem == "1"):
        print("Bakiyeniz {} tl dir.".format(bakiye))

    elif (işlem == "2"):
        miktar = int(input("Yatırılacak miktarı giriniz:"))
        bakiye += miktar
        print("Güncel bakiyeniz {} tl dir.".format(bakiye))

    elif (işlem == "3"):
        miktar = int(input("Çekilecek miktarı giriniz:"))

        if (bakiye - miktar < 0):
            print("Yetersiz bakiye.")
            continue
        bakiye -= miktar
        print("Güncel bakiyeniz {} tl dir.".format(bakiye))

    else:
        print("Geçersiz işlem....")