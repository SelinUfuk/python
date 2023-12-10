print("""
********************************
Kullanıcı adı giriş programı
********************************
""")

sys_kullanici_adi = "mmurat"
sys_parola = "12345"
giriş_hakki = 3

while True:
    kullanici_adi = input("Kullanıcı Adı:")
    parola = input("Parola:")
    if (kullanici_adi == sys_kullanici_adi and sys_parola != parola):
        print("Parola hatalı.")
        giriş_hakki -= 1
    elif (kullanici_adi != sys_kullanici_adi and sys_parola == parola):
        print("Kullanıcı adı hatalı.")
        giriş_hakki -= 1
    elif (kullanici_adi != sys_kullanici_adi and sys_parola != parola):
        print("Kullanıcı adi ve parola hatalı.")
        giriş_hakki -= 1
    else:
        print("Sisteme başarıyla giriş yapıldı....")
        break
    if (giriş_hakki == 0):
        print("Giriş hakkınız bitti...")
        break


