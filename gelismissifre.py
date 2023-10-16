import random
import string

# Şifre oluşturucu fonksiyon
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
4
#(kullanıcı adı ve şifre)
passwords = {}

while True:
    print("\n1. Şifre Oluştur")
    print("2. Şifre Depola")
    print("3. Şifre Göster")
    print("4. Çıkış")

    choice = input("Seçiminizi yapın: ")

    if choice == "1":
        username = input("Kullanıcı adı: ")
        password = generate_password()
        passwords[username] = password
        print(f"Oluşturulan şifre: {password}")

    elif choice == "2":
        username = input("Kullanıcı adı: ")
        password = input("Şifre: ")
        passwords[username] = password
        print("Şifre depolandı.")

    elif choice == "3":
        username = input("Kullanıcı adı: ")
        if username in passwords:
            print(f"Kullanıcı adı: {username}, Şifre: {passwords[username]}")
        else:
            print("Kullanıcı adı bulunamadı.")

    elif choice == "4":
        print("Çıkış yapılıyor.")
        break

    else:
        print("Geçersiz seçenek. Lütfen tekrar deneyin.")
