def fmuksayi(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    if toplam == sayi:
        return sayi
    else:
        return


for i in range(1, 1001):
    muk = fmuksayi(i)
    if muk is not None:
        print(muk)
