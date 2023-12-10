print("""********************
Kullanıcı Girişi:
********************""")
sys_kullanici_adi = "mmurat"
sys_parola = "12345"

kullanici_adi = input("Kullanıcı Adı:")
parola = input("Prola:")

if (kullanici_adi == sys_kullanici_adi and sys_parola != parola):
    print("Parola hatalı.")
elif (kullanici_adi != sys_kullanici_adi and sys_parola == parola):
    print("Kullanıcı adı hatalı.")
elif (kullanici_adi != sys_kullanici_adi and sys_parola != parola):
    print("Kullanıcı adi ve parola hatalı.")
else:
    print("Sisteme başarıyla giriş yapıldı....")
