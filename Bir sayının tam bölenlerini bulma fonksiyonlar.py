def tambolenleribulma(sayi):
    tam_bolenler = []

    for i in range(2, sayi):
        if sayi % i == 0:
            tam_bolenler.append(i)
    return tam_bolenler


while True:
    say = input("sayı:")

    if say == 'q':
        print("Program sonlandırılıyor...")
        break
    else:
        sayi = int(say)
        print("Tam bölenler:", tambolenleribulma(say))
