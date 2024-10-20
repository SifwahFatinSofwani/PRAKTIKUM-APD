import os
os.system('cls() || clear')

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

def cls():
    os.system('cls() || clear')
        
    


def menuadminindeks():
    if adminmenu1 == "1":
        nomoredithero = int(input("Contoh: Fanny maka ketik 0 untuk mengubah data Fanny, 1 untuk Ling\nMasukkan urutan hero yang anda inginkan: "))
        if nomoredithero < (len(listherometa["Jungle"]))and nomoredithero > -1:
            return int(nomoredithero)
        else:
            print("Anda memasukkan nomor yang salah")
            return menuadminindeks()
    elif adminmenu1 == "2":
        nomoredithero = int(input("Contoh: Gatot maka ketik 0 untuk mengubah data Gatot, 1 untuk Edith\nMasukkan urutan hero yang ingin anda anda inginkan: "))
        if nomoredithero < (len(listherometa["Roam"]))and nomoredithero > -1:
            return int(nomoredithero)
        else:
            print("Anda memasukkan nomor yang salah")
            return menuadminindeks()
    elif adminmenu1 == "3":
        nomoredithero = int(input("Contoh: Valen maka ketik 0 untuk mengubah data Valen, 1 untuk Yve\nMasukkan urutan hero yang ingin anda anda inginkan: "))
        if nomoredithero < (len(listherometa["Mid"]))and nomoredithero > -1:
            return int(nomoredithero)
        else:
            print("Anda memasukkan nomor yang salah")
            return menuadminindeks()
    elif adminmenu1 == "4":
        nomoredithero = int(input("Contoh: Harith maka ketik 0 untuk mengubah data Harith, 1 untuk Moskov\nMasukkan urutan hero yang ingin anda anda inginkan: "))
        if nomoredithero < (len(listherometa["Gold"]))and nomoredithero > -1:
            return int(nomoredithero)
        else:
            print("Anda memasukkan nomor yang salah")
            return menuadminindeks()
    elif adminmenu1 == "5":
        nomoredithero = int(input("Contoh: Ruby maka ketik 0 untuk mengubah data Ruby, 1 untuk Edith\nMasukkan urutan hero yang ingin anda anda inginkan: "))
        if nomoredithero < (len(listherometa["Exp"]))and nomoredithero > -1:
            return int(nomoredithero)
        else:
            print("Anda memasukkan nomor yang salah")
            return menuadminindeks()
        
def inputhero():
    inputhero1 = input("Masukkan nama hero yang anda inginkan: ")
    inputrole = input("Masukkan role hero yang diinginkan: ")
    inputmekanik = input("Masukkan mekanik hero: ")
    inputnamahero = inputhero1 + ": " + inputrole + ", " + "Mekanik " + inputmekanik
    return inputnamahero

def listjungle():
    print("berikut adalah list hero jungle meta: ")
    print()
    for hero in listherometa["Jungle"]:
        print(f"{hero}")
        print()

def listroam():
    print("berikut adalah list hero Roam meta: ")
    print()
    for hero in listherometa["Roam"]:
        print(f"{hero}")
        print()

def listmid():
    print("berikut adalah list hero Mid meta: ")
    print()
    for hero in listherometa["Mid"]:
        print(f"{hero}")
        print()

def listgold():
    print("berikut adalah list hero Gold meta: ")
    print()
    for hero in listherometa["Gold"]:
        print(f"{hero}")
        print()

def listexp():
    print("berikut adalah list hero Exp meta: ")
    print()
    for hero in listherometa["Exp"]:
        print(f"{hero}")
        print()

def garis(panjanggaris):
    print("="*panjanggaris)

def lihatlisthero():
    login1 = True
    while login1:
        garis(38)
        print("[1] Melihat semua hero meta")
        print("[2] Melihat Hero Jungle yang meta")
        print("[3] Melihat Hero Roam yang meta")
        print("[4] Melihat Hero Mid yang meta")
        print("[5] Melihat Hero Gold yang meta")
        print("[6] Melihat Hero EXP yang meta")
        print("[7] Kembali ke menu sebelumnya")
        garis(38)
        menuuser1 = input("Masukkan pilihan anda: ")
        cls()
        if menuuser1 == "1":
            cls()
            print(f"Berikut adalah list hero meta\n")
            for role, semuahero in listherometa.items():
                print(f"{role} Role: ")
                for hero in semuahero:
                    print(f"{hero}")
                    print()
        elif menuuser1 == "2":
            cls()
            listjungle()
        elif menuuser1 == "3":
            cls()
            listroam()
        elif menuuser1 == "4":
            cls()
            listmid()
        elif menuuser1 == "5":
            cls()
            listgold()
        elif menuuser1 == "6":
            cls()
            listexp()
        elif menuuser1 == "7":
            cls()
            break
        else:
            cls()
            print("Anda memasukkan nomor yang salah")
    

def tambahhero(role):
    herobaru = inputhero()
    listherometa[role].append(herobaru)
    return herobaru


masuk = 0
login = False
login1 = False


while masuk == 0:
    garis(38)
    print("Selamat datang di list data hero meta")
    print("[1] Login akun yang sudah ada")
    print("[2] Buat akun baru")
    print("[3] Keluar dari program")
    garis(38)
    loginatautidak = input("Masukkan pilihan yang anda inginkan: ")
    
    if loginatautidak == "1":
        login = True
        while login == True:
            cls()

            username = input("Masukkan username anda: ")
            password = input("Masukkan password anda: ")
            
            for cek_login in listakun:
                if username in listakun and listakun[username]["password"] == password:
                    if listakun[username]["role"] == "user":
                        cls()
                        
                        while login == True:
                            print(f"login berhasil user, selamat datang, {username}")
                            print("anda telah berhasil masuk sebagai user")
                            garis(38)
                            print("[1] Melihat list hero meta")
                            print("[2] Logout dari akun")
                            garis(38)
                            menu = input("Masukkan pilhan anda: ")
                            cls()
                            if menu == "1":
                                lihatlisthero()
    
                            elif menu == "2":
                                cls()
                                login = False  
                                break
                                
                            else:
                            
                                print("Anda memasukkan nomor yang salah")

                    elif listakun[username]["role"] == "admin":
                        cls()
                        while login == True:
                            print(f"login berhasil sebagai admin, selamat datang, {username}")
                            garis(38)
                            print("[1] Melihat list hero meta")
                            print("[2] Menambahkan hero meta dari list")
                            print("[3] Mengedit hero meta dari list")
                            print("[4] Menghapus hero meta dari list")
                            print("[5] Logout dari akun")
                            garis(38)
                            adminmenu = input("Masukkan pilihan anda: ")
                            cls()
                            loginadmin1 = True
                            if adminmenu == "1":
                                lihatlisthero()
                            elif adminmenu == "2":
                                while loginadmin1:
                                    garis(38)
                                    print("[1] Menambah hero Jungle di list meta")
                                    print("[2] Menambah hero Roam di list meta")
                                    print("[3] Menambah Mid di list meta")
                                    print("[4] Menambah hero Gold di list meta")
                                    print("[5] Menambah hero EXP di list meta")
                                    print("[6] Kembali ke menu sebelumnya")
                                    garis(38)
                                    adminmenu1 = input("Masukkan pilihan yang anda inginkan: ")
                                    cls()
                                    if adminmenu1 == "1":
                                        herobaru = tambahhero("Jungle")
                                        cls()
                                        listjungle()
                                    elif adminmenu1 == "2":

                                        herobaru = tambahhero("Roam")
                                        cls()
                                        listroam()
                                    elif adminmenu1 == "3":
                                        
                                        herobaru = tambahhero("Mid")
                                        cls()
                                        listmid()

                                    elif adminmenu1 == "4":

                                        herobaru = tambahhero("Gold")
                                        cls()
                                        listgold()

                                    elif adminmenu1 == "5":

                                        herobaru = tambahhero("Exp")
                                        cls()
                                        listexp()

                                    elif adminmenu1 == "6":
                                        break                    
                                    else:
                                        cls()
                                        print("Anda memasukkan nomor yang salah")
                            elif adminmenu == "3":
                                while loginadmin1:
                                    garis(38)
                                    print("[1] Mengedit hero Jungle di list meta")
                                    print("[2] Mengedit hero Roam di list meta")
                                    print("[3] Mengedit Mid di list meta")
                                    print("[4] Mengedit hero Gold di list meta")
                                    print("[5] Mengedit hero EXP di list meta")
                                    print("[6] Kembali ke menu sebelumnya")
                                    garis(38)
                                    adminmenu1 = input("Masukkan pilihan yang anda inginkan: ")
                                    cls()
                                    if adminmenu1 == "1":
                                        cls()
                                        listjungle()
                                        nomoredithero = menuadminindeks()
                                        inputherobaru = inputhero()
                                        cls()
                                        listherometa["Jungle"][nomoredithero] = (inputherobaru)
                                        cls()
                                        listjungle()
                                                
                                    elif adminmenu1 == "2":
                                        cls()
                                        listroam()
                                        nomoredithero = menuadminindeks()
                                        inputherobaru = inputhero()
                                        cls()
                                        listherometa["Roam"][nomoredithero] = (inputherobaru)
                                        cls()
                                        listroam()
                                       
                                    elif adminmenu1 == "3":
                                        cls()
                                        listmid()
                                        nomoredithero = menuadminindeks()
                                        inputherobaru = inputhero()
                                        cls()
                                        listherometa["Mid"][nomoredithero] = (inputherobaru)
                                        cls()
                                        listmid()

                                    elif adminmenu1 == "4":
                                        cls()
                                        listgold()
                                        nomoredithero = menuadminindeks()
                                        inputherobaru = inputhero()
                                        cls()
                                        listherometa["Gold"][nomoredithero] = (inputherobaru)
                                        cls()
                                        listgold()
                                      
                                    elif adminmenu1 == "5":
                                        cls()
                                        listexp()
                                        nomoredithero = menuadminindeks()
                                        inputherobaru = inputhero()
                                        cls()
                                        listherometa["Exp"][nomoredithero] = (inputherobaru)
                                        listexp()

                                    elif adminmenu1 == "6":
                                        break
                                    else:
                                        ("Anda memasukkan nomor yang salah")
                                        
                            elif adminmenu == "4":
                                while loginadmin1:
                                    garis(38)
                                    print("[1] Menghapus hero Jungle di list meta")
                                    print("[2] Menghapus hero Roam di list meta")
                                    print("[3] Menghapus Mid di list meta")
                                    print("[4] Menghapus hero Gold di list meta")
                                    print("[5] Menghapus hero EXP di list meta")
                                    print("[6] Kembali ke menu sebelumnya")
                                    garis(38)
                                    adminmenu1 = input("Masukkan pilihan anda: ")
                                    cls()
                                    if adminmenu1 == "1":
                                        cls()
                                        listjungle()
                                        cls()
                                        nomoredithero = menuadminindeks()
                                        del listherometa["Jungle"][nomoredithero]
                                        cls()   
                                        listjungle()
                                        
                                    elif adminmenu1 == "2":
                                        cls()
                                        listroam()
                                        nomoredithero = menuadminindeks()
                                        del listherometa["Roam"][nomoredithero]
                                        listroam()
                                    
                                    elif adminmenu1 == "3":
                                        cls()
                                        listmid() 
                                        nomoredithero = menuadminindeks()
                                        cls()
                                        del listherometa["Mid"][nomoredithero]
                                        cls()
                                        listmid()
                                        
                                           
                                    elif adminmenu1 == "4":
                                        cls()
                                        listgold()
                                        cls()
                                        nomoredithero = menuadminindeks()
                                        del listherometa["Gold"][nomoredithero]
                                        cls()
                                        listgold()
                                      
                                    elif adminmenu1 == "5":
                                        cls()
                                        listexp()
                                        cls()
                                        nomoredithero = menuadminindeks()
                                        del listherometa["Exp"][nomoredithero]
                                        cls()
                                            
                                        listexp()
                       
                                    elif adminmenu1 == "6":
                                        break
                                    else:
                                        print("Nomor yang anda masukkan salah")
                            elif adminmenu == "5":
                                login = False 
                                cls()
                                break
                            else:
                                print("Anda memasukkan nomor yang salah")  
                else:    
                    cls()           
                    print("password atau akun anda salah")
                                    
            break            
                        
                    
                    
                
               
                    
                
            
    elif loginatautidak == "2":
        while True:
            username = input("masukkan username : ")
            usnpwsudahterpakai = False
            if username in listakun:
                usnpwsudahterpakai = True
                cls()
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
                    cls()
                    print("invalid")
                    continue
                listakun[username] = {"password" : password, "role" : role }
                cls()
                print("register berhasil")
                break
    elif loginatautidak == "3":
            masuk = 1
    else:
        print("anda memasukkan nomor yang salah")
        cls()

cls()
print("program selesai")