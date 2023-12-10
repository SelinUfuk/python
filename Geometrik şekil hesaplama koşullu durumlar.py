print("Geometrik şekil hesaplama işlemi yapalım;")
print("""*****
1 = seçilen şekil üçgendir.
2 = seçilen şekil dörtgendir.
*****""")

skl = input("Seçilen şekil üçgen mi, dörtgen mi:")
if skl == "1":
    a = float(input("Üçgenin 1. kenarını giriniz:"))
    b = float(input("Üçgenin 2. kenarını giriniz:"))
    c = float(input("Üçgenin 3. kenarını giriniz:"))
    if a==a and b==b and c==c:
        if abs(a-b) < c < a+b:
            if a != b and a != c and b != c:
                print("Üçgeniniz çeşitkenar üçgendir.")
            elif a != b and a == c and b != c:
                print("Üçgeniniz ikizkenar üçgendir.")
            elif a != b and a != c and b == c:
                print("Üçgeniniz ikizkenar üçgendir.")
            elif a == b and a != c and b!= c:
                print("Üçgeniniz ikizkenar üçgendir.")
            else:
                print("Üçgeniniz eşkenar üçgendir.")
        else:
            print("Girilen kenarlar üçgen oluşturmaz.")
elif skl == "2":
    a = float(input("Dörtgenin 1. kenatrını giriniz:"))
    b = float(input("Dörtgenin 2. kenatrını giriniz:"))
    c = float(input("Dörtgenin 3. kenatrını giriniz:"))
    d = float(input("Dörtgenin 4. kenatrını giriniz:"))
    if a == a and b == b and c == c and d == d:
        if a == b == c == d:
            print("Dörtgeniniz karedir.")
        elif a == b and c == d and a != c:
            print("Dörtgeniniz dikdörtgendir.")
        elif a == c and b == d and a != b:
            print("Dörtgeniniz dikdörtgendir.")
        elif a == d and c == b and a != c:
            print("Dörtgeniniz dikdörtgendir.")
        else:
            print("Dörtgeniniz sıradan bir dörtgendir.")
