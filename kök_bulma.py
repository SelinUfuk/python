print("kök bulma")


a = int(input("x değişkeninin katsayısını giriniz:"))
b = float(input("y değişkeninin katsayısını giriniz:"))
c = int(input("c değişkenini giriniz:"))
delta = b**2 - (4 * a * c)

x1 = (-b - delta ** 0.5)/(2 * a)
x2 = (-b + delta ** 0.5)/(2 * a)

print("1. kök:  {} \n2.kök: {}".format(x1,x2) )
