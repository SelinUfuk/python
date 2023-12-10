
'''
print("""
**************************
Mükemmel sayıları bulalım;
**************************

""")
toplam = 0
sayi = int(input("Bir sayı giriniz:"))
for i in range (1,sayi):
    if sayi % i == 0:
        toplam += i

if sayi == toplam:
    print(sayi, "mükemmel sayıdır.")
else:
    print(sayi, "mükemmel sayı değildir")
'''


ensondeger = int(input("bir sayı giriniz:"))

for uretilensayi in range (1,ensondeger):

    toplam = 0
    for bolen in range (1,uretilensayi):
        if uretilensayi % bolen == 0:
            toplam += bolen


    if uretilensayi == toplam:
        print(uretilensayi, "mükemmel sayıdır.")










