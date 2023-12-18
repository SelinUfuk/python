# Asalsayılar 1 ve kendisinden baska sayıya bölünmeyen sayılardır.

def asal_mi(sayif):

    if sayif == 1:
        return False
    elif sayif == 2:
        return True
    else:
        for i in range(2, sayif):
            if sayif % i == 0:
                return False
            return True


while True:
    sayi = input("Sayı:")
    if sayi == 'q':
        break
    else:
        sayi = int(sayi)

        if asal_mi(sayi):
            print(sayi, "asal bir sayıdır.")
        else:
            print(sayi, "Asal bir sayı değildir.")
