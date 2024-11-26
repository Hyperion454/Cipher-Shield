import module
import os

while True:
    print("\nParolanızın güvenliğini kontrol etmek için                   1")
    print("Parolanızın veri ihlallerinde açığa çıktığını sorulamak için 2")
    print("Güçlü parola önerisi için                                    3")
    print("Parola Kasanıza erişmek için                                 4")
    user_input = input("Uygulamadan çıkış yapmak için                                5\ntuşlayınız\n>>> ")
    
    # Parola Güvenlik kontrolü
    if user_input == "1":

        parola = input("Parolanızı giriniz >>> ")
        uzunluk, kucuk_harf, buyuk_harf, sayi, karakter = module.password_control(parola)
        parola_uzunlugu = len(parola)
        deger = 0

        if uzunluk:
            deger += 2
        if kucuk_harf:
            deger += 1
        if buyuk_harf:
            deger += 2
        if sayi:
            deger += 2
        if karakter:
            deger += 3

        print(f"Parolanızın güvenlik düzeyi: {deger}/10")

        if deger == 0:
            print("[_ _ _ _ _ _ _ _ _ _]")
        elif deger == 1:
            print("[# _ _ _ _ _ _ _ _ _]")
        elif deger == 2:
            print("[# # _ _ _ _ _ _ _ _]")
        elif deger == 3:
            print("[# # # _ _ _ _ _ _ _]")
        elif deger == 4:
            print("[# # # # _ _ _ _ _ _]")
        elif deger == 5:
            print("[# # # # # _ _ _ _ _]")
        elif deger == 6:
            print("[# # # # # # _ _ _ _]")
        elif deger == 7:
            print("[# # # # # # # _ _ _]")
        elif deger == 8:
            print("[# # # # # # # # _ _]")
        elif deger == 9:
            print("[# # # # # # # # # _]")
        elif deger == 10:
            print("[# # # # # # # # # #]")

        if deger > 9:
            print("\nYaşasın! Parolanız oldukça güvenli.")
        elif deger > 4 and deger < 10:
            print("\nParolanız kısmen güvenli. Lütfen aşağıdaki önerilere dikkat ederek farklı bir parola belirleyiniz!")
        elif deger <= 4:
            print("\nParolanız çok zayıf. Lütfen aşağıdaki önerilere dikkat ederek farklı bir parola belirleyiniz!")
        
        if not uzunluk:
            print(f"\n  ---Parolanız en az 12 karakter uzunluğunda olmalıdır! Sizin parolanız ise {parola_uzunlugu} uzunluğunda.")
        if not kucuk_harf:
            print("\n   ---Parolanız küçük harf içermelidir!")
        if not buyuk_harf:
            print("\n   ---Parolanız büyük harf içermelidir!")
        if not sayi:
            print("\n   ---Parolanız sayı içermelidir!")
        if not karakter:
            print("\n   ---Parolanız özel karakter içermelidir!")

    # Parola pwned kontrolü
    elif user_input == "2":
        parola = input("Parolanızı giriniz >>> ")
        is_pwn = module.check(parola,"pwned.txt")

        if not is_pwn:
            print("\nParolanız şu ana kadarki hiçbir veri ihlalinde açığa çıkmamış. Parolanız güvende.")
        else:
            print("\nEyvah! Görünüşe göre parolanız bir veri ihlalinde ortaya çıkarılmış. Bu parolayı değiştirmeniz şiddetle tavsiye edilir!")

    # Parola önerisi
    elif user_input == "3":
        oneri = module.generate_password()
        print(f"\nGüçlü parola: {oneri}")

    # Cipher Vault'a erişim
    elif user_input == "4":
        print("Tekrar görüşmek dileğiyle...")
        isVault_password = os.path.exists("VaultPass.txt")
        if isVault_password:
            Vault_password_input = input("Kasa parolanızı giriniz >>> ")
            isReal = module.check_vault_password(Vault_password_input)
            if isReal:
                key = module.create_or_load_key()
                save_or_load_input = input("Parolalarınızı görüntülemek içi 1\nParola kaydetmek için 2 tuşlayınız >>> ")
                if save_or_load_input == "1":
                    passwords = module.load_passwords(key)
                    print(passwords)
                elif save_or_load_input == "2":
                    new_user_name = input("Kaydetmek istediğiniz kullanıcı adını giriniz >>> ")
                    new_password= = input(f"{new_user_name} adına kaydetmek istediğiniz parolayı giriniz >>> ")
                    module.save_password(new_user_name,new_password)  
                    print("Parolanız başarıyla kaydedildi!")    
                else: 
                    print("Lütfen geçerli bir sayı giriniz!!!")
            else:
                print("Girdiğiniz kasa parolası hatalı.")
        
    # Çıkış   
    elif user_input == "5":
        print("Tekrar görüşmek dileğiyle...")
        break

    # Hatalı sayı girişi 
    else:
        print("\nLütfen geçerli bir sayı giriniz!!!")

