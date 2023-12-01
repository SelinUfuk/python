print("kilometreye göre yakıt fiyatını hesaplayalım:)")
d = int(input("Aracın depo kapasitesini litre cinsinden yazınız:"))
t = int(input("Arcın deposu tam dolu iken aldığı yolu km cinsinden yazınız: "))
kbasiy = d/t
gy = int(input("Kaç km yol gittiniz yazınız:"))
hy = kbasiy*gy
yf = int(input("Bir litre yakıt kaç TL yazınız"))
ot = hy*yf
print("Ödemeniz gereken fiyat:{:.2f}".format(ot))
