
print("merhaba dünya")
a = 2
b = 3
c = 4
d = 5
l = 9
f = 8
l, f = f, l
print(l)
print(a + c)
print(d / a)
print(d // a)
print(d % a)
print(b ** 2)
print(8 ** (1 / 3))
# type fonksiyonu verinin türünü/snıfını söyler
print(type(a))
print("yazıyı bölcem ve\n alta geçircem")
print('burada operatör değili göstercem = Ahmet\'in kodu')
# yazdiğımız her harf veya satir bir indextir,indeks alma göstercem.
x = "ankara"
print(x[0])
print(x[4])
print(x[1:4])
print(x[0:5:2])
print(x[::-1])  # listeyi tersten yazar
print(len(x))
print(x * 3)  # verilen sayı kadar tekrar eder
k = 'mustafa'
k = k + ' murat coşkun'
print(k)
print("yaziyı yazarken\n alt satıra geçer")
print("yazıyı yazarken\tarasına 1 tab\tboşluk bırakır")
# veriler arasına işaretker koyar ve değiştirebilir
print(35, 43, 54, 65, sep="7")
print(35, 43, 54, 65, sep="/")
print(35, 43, 54, 65, sep="değişik")
print(*"koyup yazarsak harfler arası boşluk koyar")
# sep eklersek her karakter arasına bişi ekleyebiliriz
print(*"koyup yazarsak harfler arası boşluk koyar", sep=".")
# formatlama yapcaz
print("{} + {}'nin toplamı {}'dır".format(a, b, a + b))
# ondalıklı sayılarda format özelliği
print("{}  {}  {}".format(7.34, 37.2356, 9))
print("{:.2f} {:.3f} {:.2f}".format(7.3854, 37.2356, 9))
liste = ["elma", 35, "merhaba,3.14,5"]
print(type(liste))
liste2 = []
print(liste2)
liste3 = list()
print(liste3)
liste4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(liste4))
liste5 = list("merhaba")
print(liste5)
print(liste5[2])
print(liste4[5])
print(liste5[-1])
print(liste4[-1])
print(len(liste5) - 1)  # listedeki eleman sayısında 1 çikardı
# kalan eleman sayısını söyledi
print(liste4[:5])
print(liste4[6:])
print(liste4[::3])
print(liste4[::-1])
liste6 = [1, 2, 3]
liste7 = [4, 5, 6]
liste8 = liste6 + liste7
print(liste8)
print(liste6 * 3)
print(liste6)
liste6 = 3 * liste6
print(liste6)
print(liste7)
liste7[1] = 10
print(liste7)
liste9 = [1, 2, 3, 4, 5, 6]
print(liste9[:2])
liste9[:2] = [10, 11]
print(liste9)
liste9.append("yazı ekledim")
print(liste9)
liste9.append(12)
print(liste9)
liste9.pop()
print(liste9)
liste9.pop(0)
print(liste9)
liste0 = [34, 2, 1, 5, 6, 32, 100]
liste0.sort()
print(liste0)
liste0.sort(reverse=True)
print(liste0)
liste11 = ['python', 'php', 'java', 'C']
liste11.sort(reverse=True)
# alfabetik sıralar
print(liste11)
liste = [[1, 2], [3, 4], [5, 6]]
print(liste[1])
print(liste[1][1])
demet = (1, 2, 3, 4, 5, 6, 7)
print(type(demet))
# demette listelerdeki uygulamalar geçerli
demet2 = (1, 1, 1, 1, 1, 2, 2, 4, 5)
print(demet2.count(1))
# kaç kez tekrar ettiğini yazar
print(demet2.count(2))
# olayanı yazaesan 0 der
print(demet2.count(10))
demet3 = ['python', 'C++', 'php', 'java', 'C']
print(demet3.index("java"))
# demetlerin elemanlarını başka bişiyle değiştiremeyiz
# SÖZLÜKLER
sözlük1 = {'sıfır': 0, 'bir': 1, 'iki': 2, 'üç': 3}
print(sözlük1)
print(type(sözlük1))
sözlük2 = {}
print(sözlük2)
sözlük2 = dict()
print(sözlük2)
print(sözlük1['iki'])
sözlük1["beş"] = 5
print(sözlük1)
a = {"bir": [1, 2, 3, 4], "iki": [[1, 2], [3, 4], [5, 6]], "üç": 15}
print(a)
print(a["iki"][2][1])
sözlük1["üç"] = 7
print(sözlük1)
sözlük1["beş"] += 4
print(sözlük1)
# iç içe sözlükler
b = {"sayılar": {"bir": 1, "iki": 2, "üç": 3, "dört": 4},
     "meyveler": {"kiraz": "yaz", "portakal": "kış", "erik": "bahar"}}
print(b["sayılar"])
print(b["sayılar"]["iki"])
print(b["meyveler"]["kiraz"])
sözlük3 = {'sıfır': 0, 'bir': 1, 'iki': 22, 'üç': 333}
print(sözlük3.keys())
print(sözlük3.values())
print(sözlük3.items())
# input=veri alma

x = input("sayı giriniz:")
print("kullanıcının girdiği değer:", x)
print(x * 3)
print(type(x))
# x str algılandığı için aritmetiik işlem uygulanmıyor.
# aritmrtik işlrm için ineger olmalı.
x = int(input("sayı giriniz:"))
print(x * 3)

a = int(input("birincci sayı:"))
b = int(input("ikinci sayı:"))
c = int(input("üçüncü sayıyı giriniz:"))
print("toplamları",a+b+c)
#kullanıcı sayı dışında girdi verirse alınan hatayı düzeltir.
try:
    a = a=int(input("a:"))
    print(a)
except ValueError:
    print("lütfen inputu doğru formatta girin.")

isim = input("isim: ")
print("isminiz: ",isim)
