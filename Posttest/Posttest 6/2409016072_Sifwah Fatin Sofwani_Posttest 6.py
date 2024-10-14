
import os

os.system('cls || clear')

listherometa = {"Jungle" : ["Fanny: Assasin, Mekanik tinggi", "Ling: Assasin, Mekanik tinggi", "Nolan: Aassasin, Mekanik tinggi", "Julian: Assasin, Mage, Mekanik sedang", "Hayabusa: Assasin, Mekanik tinggi"], 
                "Roam" :["Gatot kaca: Tank, Fighter, Mekanik mudah", "Edith: Tank, Mekanik Sedang", "Chip: Support, Tank, Mekanik sedang", "Angela: Support, Mekanik Rendah", "Mathilda: Support, Mekanik rendah", "Grock: Support, Mekanik sedang"],
                "Mid" :["Valentina: Mage, Mekanik sedang", "Yve: Mage, Mekanik Sedang", "Faramis: Mage, Mekanik sedang", "Aurora: Mage, Mekanik rendah", "Zhuxin: Mage, Mekanik sedang"], 
                "Gold" : ["Harith: Mage, Mekanik tinggi", "Moskov: Marskman, Mekanik tinggi", "Claude: Marskman, Mekanik tinggi", "Nathan: Marksman, Mekanik tinggi", "Roger: Fighter, Marskman, Mekanik tinggi", "Lunox: Mage, Mekanik Tinggi", "Miya: Marskman, Mekanik tinggi"], 
                "Exp" : ["Ruby: Fighter, Mekanik sedang", "Edith: Tank, Fighter, Mekanik sedang", "Terizla: Fighter, Mekanik sedang", "Arlott: Fighter, Mekanik sedang", "Phoveus: Fighter, Mekanik sedang", "Gatotkaca: Tank, Fighter, Mekanik sedang", "Hylos: Tank, Mekanik rendah",
                "Benedetta: Assasin, Fighter, Mekanik tinggi"]
}

listakun = {"admin": {"password": "123", "role": "admin"}, 
            "user": {"password": "123", "role": "user"}
            }


masuk = 0
login = False
loginuser1 = False
loginadmin = False

while masuk == 0:
    print("Selamat datang di list data hero meta")
    print("[1] Login akun yang sudah ada")
    print("[2] Buat akun baru")
    print("[3] Keluar dari program")
    loginatautidak = input("Masukkan pilihan yang anda inginkan: ")
    if loginatautidak == "1":
        login = True
        while login == True:
            os.system('cls || clear')
            username = input("Masukkan username anda: ")
            password = input("Masukkan password anda: ")
            for cek_login in listakun:
                if username in listakun and listakun[username]["password"] == password:
                    if listakun[username]["role"] == "user":
                        os.system('cls || clear')
                        while login == True:
                            print(f"login berhasil user, selamat datang, {username}")
                            print("anda telah berhasil masuk sebagai user")
                            print("[1] Melihat list hero meta")
                            print("[2] Logout dari akun")
                            menu = input("Masukkan pilhan anda: ")
                            os.system('cls || clear')
                            if menu == "1":
                                loginuser1 = True
                                while loginuser1:
                                    print("[1] Melihat semua hero meta")
                                    print("[2] Melihat Hero Jungle yang meta")
                                    print("[3] Melihat Hero Roam yang meta")
                                    print("[4] Melihat Hero Mid yang meta")
                                    print("[5] Melihat Hero Gold yang meta")
                                    print("[6] Melihat Hero EXP yang meta")
                                    print("[7] Kembali ke menu sebelumnya")
                                    menuuser1 = input("Masukkan pilihan anda: ")
                                    os.system('cls || clear')
                                    os.system('cls || clear')
                                    if menuuser1 == "1":
                                        os.system('cls || clear')
                                        os.system('cls || clear')
                                        print(f"Berikut adalah list hero meta\n")
                                        for role, semuahero in listherometa.items():
                                            print(f"{role} Role: ")
                                            for hero in semuahero:
                                                print(f"{hero}")
                                                print()
                                    elif menuuser1 == "2":
                                        os.system('cls || clear')
                                        os.system('cls || clear')
                                        print(f"Berikut adalah list hero Jungle meta\n")
                                        for hero in listherometa["Jungle"]:
                                            print(f"{hero}")
                                            print()
                                    elif menuuser1 == "3":
                                        os.system('cls || clear')
                                        os.system('cls || clear')
                                        print(f"Berikut adalah list hero Roam meta\n")
                                        for hero in listherometa["Roam"]:
                                            print(f"{hero}")
                                            print()
                                    elif menuuser1 == "4":
                                        os.system('cls || clear')
                                        os.system('cls || clear')
                                        print(f"Berikut adalah list hero Mid meta\n")
                                        for hero in listherometa["Mid"]:
                                            print(f"{hero}")
                                            print()
                                    elif menuuser1 == "5":
                                        os.system('cls || clear')
                                        os.system('cls || clear')
                                        print(f"Berikut adalah list hero Gold meta\n")
                                        for hero in listherometa["Gold"]:
                                            print(f"{hero}")
                                            print()
                                    elif menuuser1 == "6":
                                        os.system('cls || clear')
                                        os.system('cls || clear')
                                        print(f"Berikut adalah list hero Exp meta\n")
                                        for hero in listherometa["Exp"]:
                                            print(f"{hero}")
                                            print()
                                    elif menuuser1 == "7":
                                        break
                                    else:
                                        os.system('cls || clear')
                                        print("Anda memasukkan nomor yang salah")
                            
                            elif menu == "2":
                                os.system('cls || clear')
                                login = False  
                                break
                                
                          
                            else:
                            
                                print("Anda memasukkan nomor yang salah")
                            
            
                      
                
                  
                    elif listakun[username]["role"] == "admin":
                        os.system('cls || clear')
                        while login == True:
                            print(f"login berhasil sebagai admin, selamat datang, {username}")
                            print("[1] Melihat list hero meta")
                            print("[2] Menambahkan hero meta dari list")
                            print("[3] Mengedit hero meta dari list")
                            print("[4] Menghapus hero meta dari list")
                            print("[5] Logout dari akun")
                            adminmenu = input("Masukkan pilihan anda: ")
                            os.system('cls || clear')
                            loginadmin1 = True
                            if adminmenu == "1":
                                while loginadmin1:
                                    print("[1] Melihat semua hero meta")
                                    print("[2] Melihat Hero Jungle yang meta")
                                    print("[3] Melihat Hero Roam yang meta")
                                    print("[4] Melihat Hero Mid yang meta")
                                    print("[5] Melihat Hero Gold yang meta")
                                    print("[6] Melihat Hero EXP yang meta")
                                    print("[7] Kembali ke menu sebelumnya")
                                    adminmenu1 = input("Masukkan pilihan anda: ")
                                    os.system('cls || clear')
                                    if adminmenu1 == "1":
                                        os.system('cls || clear')
                                        for role, semuahero in listherometa.items():
                                            print(f"{role} Role: ")
                                            for hero in semuahero:
                                                print(f"{hero}")
                                                print()
                                    elif adminmenu1 == "2":
                                        os.system('cls || clear')
                                        print(f"Berikut adalah list hero Jungle meta\n")
                                        for hero in listherometa["Jungle"]:
                                            print(f"{hero}")
                                            print()
                                    elif adminmenu1 == "3":
                                        os.system('cls || clear')
                                        print(f"Berikut adalah list hero Roam meta\n")
                                        for hero in listherometa["Roam"]:
                                            print(f"{hero}")
                                            print()
                                    elif adminmenu1 == "4":
                                        os.system('cls || clear')
                                        print(f"Berikut adalah list hero Mid meta\n")
                                        for hero in listherometa["Mid"]:
                                            print(f"{hero}")
                                            print()
                                    elif adminmenu1 == "5":
                                        os.system('cls || clear')
                                        print(f"Berikut adalah list hero Gold meta\n")
                                        for hero in listherometa["Gold"]:
                                            print(f"{hero}")
                                            print()
                                    elif adminmenu1 == "6":
                                        os.system('cls || clear')
                                        print(f"Berikut adalah list hero Exp meta\n")
                                        for hero in listherometa["Exp"]:
                                            print(f"{hero}")
                                            print()
                                    elif adminmenu1== "7":
                                        break
                                    else:
                                        os.system('cls || clear')
                                        print("Anda memasukkan nomor yang salah")
                            elif adminmenu == "2":
                                while loginadmin1:
                                    print("[1] Menambah hero Jungle di list meta")
                                    print("[2] Menambah hero Roam di list meta")
                                    print("[3] Menambah Mid di list meta")
                                    print("[4] Menambah hero Gold di list meta")
                                    print("[5] Menambah hero EXP di list meta")
                                    print("[6] Kembali ke menu sebelumnya")
                                    adminmenu1 = input("Masukkan pilihan yang anda inginkan: ")
                                    os.system('cls || clear')
                                    if adminmenu1 == "1":
                                        inputhero = input("Masukkan nama hero Jungle yang anda inginkan di list meta: ")
                                        inputrole = input("Masukkan role hero: ")
                                        inputmekanik = input("Masukkan mekanik hero: ")
                                        listherometa["Jungle"].append(inputhero + ": " + inputrole + ", " + "Mekanik " + inputmekanik)
                                        os.system('cls || clear')
                                        print(f"Berikut adalah list hero Jungle meta\n")
                                        for hero in listherometa["Jungle"]:
                                            print(f"{hero}")
                                            print()
                                    elif adminmenu1 == "2":
                                        inputhero = input("Masukkan nama hero Roam yang anda inginkan di list meta: ")
                                        inputrole = input("Masukkan role hero: ")
                                        inputmekanik = input("Masukkan mekanik hero: ")
                                        listherometa["Roam"].append(inputhero + ": " + inputrole + ", " + "Mekanik " + inputmekanik)
                                        os.system('cls || clear')
                                        print(f"Berikut adalah list hero Roam meta\n")
                                        for hero in listherometa["Roam"]:
                                            print(f"{hero}")
                                            print()
                                    elif adminmenu1 == "3":
                                        inputhero = input("Masukkan nama hero Mid yang anda inginkan di list meta: ")
                                        inputrole = input("Masukkan role hero: ")
                                        inputmekanik = input("Masukkan mekanik hero: ")
                                        listherometa["Mid"].append(inputhero + ": " + inputrole + ", " + "Mekanik "  + inputmekanik)
                                        os.system('cls || clear')
                                        print(f"Berikut adalah list hero Mid meta\n")
                                        for hero in listherometa["Mid"]:
                                            print(f"{hero}")
                                            print()
                                    elif adminmenu1 == "4":
                                        inputhero = input("Masukkan nama hero EXP yang anda inginkan di list meta: ")
                                        inputrole = input("Masukkan role hero: ")
                                        inputmekanik = input("Masukkan mekanik hero: ")
                                        listherometa["Gold"].append(inputhero + ": " + inputrole + ", " + "Mekanik " + inputmekanik)
                                        os.system('cls || clear')
                                        print(f"Berikut adalah list hero Gold meta\n")
                                        for hero in listherometa["Gold"]:
                                            print(f"{hero}")
                                            print()
                                    elif adminmenu1 == "5":
                                        inputhero = input("Masukkan nama hero Gold yang anda inginkan di list meta: ")
                                        inputrole = input("Masukkan role hero: ")
                                        inputmekanik = input("Masukkan mekanik hero: ")
                                        listherometa["Exp"].append(inputhero + ": " + inputrole + ", " + "Mekanik " + inputmekanik)
                                        os.system('cls || clear')
                                        print(f"Berikut adalah list hero Exp meta\n")
                                        for hero in listherometa["Exp"]:
                                            print(f"{hero}")
                                            print()
                                    elif adminmenu1 == "6":
                                        break                    
                                    else:
                                        os.system('cls || clear')
                                        print("Anda memasukkan nomor yang salah")
                            elif adminmenu == "3":
                                while loginadmin1:
                                    print("[1] Mengedit hero Jungle di list meta")
                                    print("[2] Mengedit hero Roam di list meta")
                                    print("[3] Mengedit Mid di list meta")
                                    print("[4] Mengedit hero Gold di list meta")
                                    print("[5] Mengedit hero EXP di list meta")
                                    print("[6] Kembali ke menu sebelumnya")
                                    adminmenu1 = input("Masukkan pilihan yang anda inginkan: ")
                                    os.system('cls || clear')
                                    if adminmenu1 == "1":
                                        print(f"Berikut adalah list hero Jungle meta\n")
                                        for hero in listherometa["Jungle"]:
                                            print(f"{hero}")
                                            print()
                                        nomoredithero = int(input("Contoh: Fanny maka ketik 0 untuk mengubah data Fanny, 1 untuk Ling\nMasukkan urutan hero yang ingin anda ganti: "))
                                        if nomoredithero < (len(listherometa['Jungle'])) and (nomoredithero > -1) :
                                            namahero = input("Masukkan perubahan yang anda inginkan: ")
                                            namarole = input("Masukkan role hero yang diinginkan: ")
                                            jenismekanik = input("Masukkan mekanik hero: ")
                                            os.system('cls || clear')
                                            listherometa["Jungle"][nomoredithero] = (namahero + ": " + namarole + ", " + "Mekanik " + jenismekanik)
                                            os.system('cls || clear')
                                            print(f"Berikut adalah list hero Jungle meta\n")
                                            for hero in listherometa["Jungle"]:
                                                print(f"{hero}")
                                                print()
                                        else:
                                            os.system('cls || clear')
                                            print("Anda memasukkan nomor yang salah")
                                            break
                                                
                                    elif adminmenu1 == "2":
                                        print(f"Berikut adalah list hero Roam meta\n")
                                        for hero in listherometa["Roam"]:
                                            print(f"{hero}")
                                            print()
                                        nomoredithero = int(input("Contoh: Gatot maka ketik 0 untuk mengubah data Gatot, 1 untuk Edith\nMasukkan urutan hero yang ingin anda ganti: "))
                                        if nomoredithero < (len(listherometa['Roam'])) and (nomoredithero > -1) :
                                            namahero = input("Masukkan perubahan yang anda inginkan: ")
                                            namarole = input("Masukkan role hero yang diinginkan: ")
                                            jenismekanik = input("Masukkan mekanik hero: ")
                                            os.system('cls || clear')
                                            listherometa["Roam"][nomoredithero] = (namahero + ": " + namarole + ", " + "Mekanik "+ jenismekanik)
                                            os.system('cls || clear')
                                            print(f"Berikut adalah list hero Roam meta\n")
                                            for hero in listherometa["Roam"]:
                                                print(f"{hero}")
                                                print()
                                        else:
                                            os.system('cls || clear')
                                            print("Anda memasukkan nomor yang salah")
                                            break
                                    elif adminmenu1 == "3":
                                        print(f"Berikut adalah list hero Mid meta\n")
                                        for hero in listherometa["Mid"]:
                                            print(f"{hero}")
                                            print()
                                        nomoredithero = int(input("Contoh: Valen maka ketik 0 untuk mengubah data Valen, 1 untuk Yve\nMasukkan urutan hero yang ingin anda ganti: "))
                                        if nomoredithero < (len(listherometa['Mid'])) and (nomoredithero > -1) :
                                            namahero = input("Masukkan perubahan yang anda inginkan: ")
                                            namarole = input("Masukkan role hero yang diinginkan: ")
                                            jenismekanik = input("Masukkan mekanik hero: ")
                                            os.system('cls || clear')
                                            listherometa["Mid"][nomoredithero] = (namahero + ": " + namarole + ", " + "Mekanik " + jenismekanik)
                                            os.system('cls || clear')
                                            print(f"Berikut adalah list hero Mid meta\n")
                                            for hero in listherometa["Mid"]:
                                                print(f"{hero}")
                                                print()
                                        else:
                                            os.system('cls || clear')
                                            print("Anda memasukkan nomor yang salah")
                                            break
                                    elif adminmenu1 == "4":
                                        print(f"Berikut adalah list hero Gold meta\n")
                                        for hero in listherometa["Gold"]:
                                            print(f"{hero}")
                                            print()
                                        nomoredithero = int(input("Contoh: Harith maka ketik 0 untuk mengubah data Harith, 1 untuk Moskov\nMasukkan urutan hero yang ingin anda ganti: "))
                                        if nomoredithero < (len(listherometa['Gold'])) and (nomoredithero > -1) :
                                            namahero = input("Masukkan perubahan yang anda inginkan: ")
                                            namarole = input("Masukkan role hero yang diinginkan: ")
                                            jenismekanik = input("Masukkan mekanik hero: ")
                                            os.system('cls || clear')
                                            listherometa["Gold"][nomoredithero] = (namahero + ": " + namarole + ", " + "Mekanik " + jenismekanik)
                                            os.system('cls || clear')
                                            print(f"Berikut adalah list hero Gold meta\n")
                                            for hero in listherometa["Gold"]:
                                                print(f"{hero}")
                                                print()
                                        else:
                                            os.system('cls || clear')
                                            print("Anda memasukkan nomor yang salah")
                                            break 
                                    elif adminmenu1 == "5":
                                        print(f"Berikut adalah list hero Exp meta\n")
                                        for hero in listherometa["Exp"]:
                                            print(f"{hero}")
                                            print()
                                        nomoredithero = int(input("Contoh: Ruby maka ketik 0 untuk mengubah data Ruby, 1 untuk Edith\nMasukkan urutan hero yang ingin anda ganti: "))
                                        if nomoredithero < (len(listherometa['Exp'])) and (nomoredithero > -1) :
                                            namahero = input("Masukkan perubahan yang anda inginkan: ")
                                            namarole = input("Masukkan role hero yang diinginkan: ")
                                            jenismekanik = input("Masukkan mekanik hero: ")
                                            os.system('cls || clear')
                                            listherometa["Exp"][nomoredithero] = (namahero + ": " + namarole + ", " + "Mekanik " + jenismekanik)
                                            print(f"Berikut adalah list hero Exp meta\n")
                                            for hero in listherometa["Exp"]:
                                                print(f"{hero}")
                                                print()
                                        else:
                                            os.system('cls || clear')
                                            print("Anda memasukkan nomor yang salah")
                                            break
                                    elif adminmenu1 == "6":
                                        break
                                    else:
                                        ("Anda memasukkan nomor yang salah")
                                        
                            elif adminmenu == "4":
                                while loginadmin1:
                                    print("[1] Menghapus hero Jungle di list meta")
                                    print("[2] Menghapus hero Roam di list meta")
                                    print("[3] Menghapus Mid di list meta")
                                    print("[4] Menghapus hero Gold di list meta")
                                    print("[5] Menghapus hero EXP di list meta")
                                    print("[6] Kembali ke menu sebelumnya")
                                    adminmenu1 = input("Masukkan pilihan anda: ")
                                    os.system('cls || clear')
                                    if adminmenu1 == "1":
                                        print(f"Berikut adalah list hero Jungle meta\n")
                                        for hero in listherometa["Jungle"]:
                                            print(f"{hero}")
                                            print()
                                        nomoredithero = int(input("Contoh: Fanny maka ketik 0 untuk mengubah data Fanny, 1 untuk Ling\nMasukkan urutan hero yang ingin anda hapus: "))
                                        if nomoredithero < (len(listherometa["Jungle"]))and nomoredithero > -1:
                                            os.system('cls || clear')
                                            del listherometa["Jungle"][nomoredithero]
                                            os.system('cls || clear')
                                            print(f"Berikut adalah list hero Exp meta\n")
                                            for hero in listherometa["Jungle"]:
                                                print(f"{hero}")
                                                print()
                                        else:
                                            os.system('cls || clear')
                                            print("Anda memasukkan nomor yang salah")
                                            break
                                    elif adminmenu1 == "2":
                                        print(f"Berikut adalah list hero Roam meta\n")
                                        for hero in listherometa["Roam"]:
                                            print(f"{hero}")
                                            print()
                                        nomoredithero = int(input("Contoh: Gatot maka ketik 0 untuk mengubah data Gatot, 1 untuk Edith\nMasukkan urutan hero yang ingin anda hapus: "))
                                        if nomoredithero < (len(listherometa["Roam"])) and (nomoredithero > -1) :
                                            os.system('cls || clear')
                                            del listherometa["Roam"][nomoredithero]
                                            os.system('cls || clear')
                                            print(f"Berikut adalah list hero Roam meta\n")
                                            for hero in listherometa["Roam"]:
                                                print(f"{hero}")
                                                print()
                                        else:
                                            os.system('cls || clear')
                                            print("Anda memasukkan nomor yang salah")
                                            break
                                    elif adminmenu1 == "3":
                                        print(f"Berikut adalah list hero Mid meta\n")
                                        for hero in listherometa["Mid"]:
                                            print(f"{hero}")
                                            print()
                                        nomoredithero = int(input("Contoh: Valen maka ketik 0 untuk mengubah data Valen, 1 untuk Yve\nMasukkan urutan hero yang ingin anda hapus: "))
                                        if nomoredithero < (len(listherometa["Mid"])) and (nomoredithero > -1) :
                                            os.system('cls || clear')
                                            del listherometa[2][nomoredithero]
                                            os.system('cls || clear')
                                            print(f"Berikut adalah list hero Mid meta\n")
                                            for hero in listherometa["Mid"]:
                                                print(f"{hero}")
                                                print()
                                        else:
                                            os.system('cls || clear')
                                            print("Anda memasukkan nomor yang salah")
                                            break
                                    elif adminmenu1 == "4":
                                        print(f"Berikut adalah list hero Gold meta\n")
                                        for hero in listherometa["Gold"]:
                                            print(f"{hero}")
                                            print()
                                        nomoredithero = int(input("Contoh: Harith maka ketik 0 untuk mengubah data Harith, 1 untuk Moskov\nMasukkan urutan hero yang ingin anda hapus: "))
                                        if nomoredithero < (len(listherometa["Gold"])) and (nomoredithero > -1):
                                            os.system('cls || clear')
                                            del listherometa[3][nomoredithero]
                                            os.system('cls || clear')
                                            print(f"Berikut adalah list hero Gold meta\n")
                                            for hero in listherometa["Gold"]:
                                                print(f"{hero}")
                                                print()
                                        else:
                                            os.system('cls || clear')
                                            print("Anda memasukkan nomor yang salah")
                                            break
                                    elif adminmenu1 == "5":
                                        print(f"Berikut adalah list hero Exp meta\n")
                                        for hero in listherometa["Exp"]:
                                            print(f"{hero}")
                                            print()
                                        nomoredithero = int(input("Contoh: Ruby maka ketik 0 untuk mengubah data Ruby, 1 untuk Edith\nMasukkan urutan hero yang ingin anda hapus: "))
                                        if nomoredithero < (len(listherometa["Exp"])) and (nomoredithero > -1):
                                            os.system('cls || clear')
                                            del listherometa[4][nomoredithero]
                                            os.system('cls || clear')
                                            print(f"Berikut adalah list hero Exp meta\n")
                                            for hero in listherometa["Exp"]:
                                                print(f"{hero}")
                                                print()
                                        else:
                                            os.system('cls || clear')
                                            print("Anda memasukkan nomor yang salah")
                                            break
                                    elif adminmenu1 == "6":
                                        break
                                    else:
                                        print("Nomor yang anda masukkan salah")
                            elif adminmenu == "5":
                                login = False 
                                os.system('cls || clear')
                                break
                            else:
                                print("Anda memasukkan nomor yang salah")  
                else:    
                    os.system('cls || clear')           
                    print("password atau akun anda salah")
                                    
            break            
                        
                    
                    
                
               
                    
                
            
    elif loginatautidak == "2":
        while True:
            username = input("masukkan username : ")
            usnpwsudahterpakai = False
            if username in listakun:
                usnpwsudahterpakai = True
                os.system('cls || clear')
                print("Username telah dipakai")    
                continue
            else:
                password = input("masukkan password : ")
                role = input("pilih salah satu\n1 untuk admin, 2 untuk user : ")
                if role == "1":
                    role = "admin"
                elif role == "2":
                    role = "user"
                else:
                    os.system('cls || clear')
                    print("invalid")
                    continue
                listakun[username] = {"password" : password, "role" : role }
                os.system('cls || clear')
                print("register berhasil")
                break
    elif loginatautidak == "3":
            break
    else:
        print("anda memasukkan nomor yang salah")
        os.system('cls || clear')


print("program selesai")