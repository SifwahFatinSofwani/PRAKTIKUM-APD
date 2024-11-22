import os
import json 
import datetime
import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)       

# default database
default_data = {
    "users": [
    {
    "id": 1,
    "username": "admin",
    "password": "admin",
    "role": "admin",
    "balance": None
    },
    {
    "id": 2,
    "username": "user",
    "password": "user",
    "role": "user",
    "balance": 0
    }
],
"teaters": [],
"films": [],
"ticketTransactions": [],
"fnb": [],
"fnbTransactions": [],
"comments": []
}

# mengakses database untuk pertama kali
try:
    with open('database.json') as f:
        database = json.load(f)
        # Membuat dictionary untuk menyimpan database film
        film_dict = {film["id"]: film["name"] for film in database["films"]}
        film_rating = {film["id"]: film["filmRating"] for film in database["films"]}
        user_dict = {user["id"]: user["username"] for user in database["users"]}
        teater_dict = {teater["id"]: teater["name"] for teater in database["teaters"]}
        fnb_dict = {fnb["id"]: fnb["name"] for fnb in database["fnb"]}
        fnb_price = {fnb["id"]: fnb["price"] for fnb in database["fnb"]}
except FileNotFoundError:
    print("File database.json tidak ditemukan. Membuat file baru dengan database default.")
    input("\nTekan enter untuk lanjut")
    database = default_data
    with open('database.json', 'w') as f:
        json.dump(database, f, indent=2)

    film_dict = {}
    film_rating = {}
    user_dict = {}
    teater_dict = {}
    fnb_dict = {}
    fnb_price = {}

# --------------------------------------------------> FUNGSI-FUNGSI < --------------------------------------------------
# --------------------------------------------------> FUNGSI UMUM
# fungsi clear screen
def cls():  
    os.system('cls')

# fungsi mengakses database
def buka():
    try:
        with open('database.json') as f:
            return json.load(f)
    except FileNotFoundError:
        print("File database.json tidak ditemukan")
        return

# fungsi kamus
def kamus():
    global film_dict, film_rating, user_dict, teater_dict, fnb_dict, fnb_price
    film_dict = {film["id"]: film["name"] for film in database["films"]}
    film_rating = {film["id"]: film["filmRating"] for film in database["films"]}
    user_dict = {user["id"]: user["username"] for user in database["users"]}
    teater_dict = {teater["id"]: teater["name"] for teater in database["teaters"]}
    fnb_dict = {fnb["id"]: fnb["name"] for fnb in database["fnb"]}
    fnb_price = {fnb["id"]: fnb["price"] for fnb in database["fnb"]}

# fungsi menyimpan database
def save(database):
    with open('database.json', 'w') as f:
        json.dump(database, f, indent=2)

# fungsi mengambil id terbesar
def get_next_id(data_list):
    id_terbesar = 0
    for item in data_list:
        if item["id"] > id_terbesar:
            id_terbesar = item["id"]
    return id_terbesar + 1

# fungsi menu awal
def menuawal():
    while True:
        print(Fore.CYAN + Style.BRIGHT + "=" * 60)
        print(Fore.CYAN + Style.BRIGHT + "||" + " Selamat datang di Program Bioskop Online ".center(56) + "||")
        print(Fore.CYAN + Style.BRIGHT + "=" * 60)
        print(Fore.MAGENTA + Style.BRIGHT + "MENU UTAMA".center(60))
        print(Fore.CYAN + "1. " + Fore.GREEN + Style.BRIGHT + "Login ")
        print(Fore.CYAN + "2. " + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Register")
        print(Fore.CYAN + "3. " + Fore.RED + Style.BRIGHT + "Keluar")
        pilihan = input(Fore.BLUE + Style.BRIGHT + ">> Masukkan pilihan anda: ").strip()
        cls()

        match pilihan:
            case "1":
                try:
                    level, masuk, username = menulogin()
                    return level, masuk, username
                except:
                    continue
            case "2":
                menuregis()
            case "3":
                print("Terima kasih! Program selesai.")
                quit()
            case "":
                continue
            case _:
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Pilihan tidak tersedia.\n")

# fungsi menu login
def menulogin():
    while True:
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        print(Fore.CYAN + Style.BRIGHT + "||" +"Silahkan login terlebih dahulu".center(56)+"||")
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        username = input(Fore.BLUE + Style.BRIGHT + ">> Masukkan username anda: ")
        password = input(Fore.BLUE + Style.BRIGHT + ">> Masukkan password anda: ")
        cls()
        # mengecek username dan password
        for user in database['users']:
            if user['username'] == username and user['password'] == password:
                if user['role'] == "user":
                    masuk = 2
                    level = "user"
                    username = user['username']
                    return level, masuk, username
                elif user['role'] == "admin":
                    masuk = 2
                    level = "admin"
                    username = user['username']
                    return level, masuk, username
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Username atau password yang anda masukkan salah.\n")
        break 

# fungsi menu register
def menuregis():
    while True:
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        print(Fore.CYAN + Style.BRIGHT + "||" +"Silahkan register terlebih dahulu".center(56)+"||" )
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        username = input(Fore.BLUE + Style.BRIGHT + ">> Masukkan username : ").strip()
        
        usnterpakai = False
        # mengecek apakah username sudah terpakai
        for user in database['users']:
            if user['username'] == username:
                usnterpakai = True
                break
        
        if usnterpakai:
            cls()
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Username telah dipakai.\n")
            break
        
        password = input(Fore.BLUE + Style.BRIGHT + ">> Masukkan password : ").strip()

        # mengecek apakah username dan password kosong
        if username == "" or password == "":
            cls()
            print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Username dan password tidak boleh kosong!\n")
            break
        
        # menentukan role
        role = "user"

        # membuat user baru
        regis = {
            "id": get_next_id(database['users']),
            "username": username,
            "password": password,
            "role": role,
            "balance": 0
        }
        
        # menambahkan user baru ke database
        database['users'].append(regis)
        
        # menyimpan database baru ke file
        save(database)
        
        cls()
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + "Register berhasil!\n")
        break

# ---------------------------------------------------> FUNGSI USER
# fungsi menu user
def menuuser():
    while True:
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        print(Fore.CYAN + Style.BRIGHT + "||" +"Behasil masuk: Selamat datang User".center(56)+"||")
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        print(Fore.BLUE + Style.BRIGHT + "Silahkan pilih menu di bawah ini\n".center(60))
        print(Fore.BLUE + "1. "+ Fore.GREEN + Style.BRIGHT + "Beli tiket")
        print(Fore.BLUE + "2. " + Fore.GREEN + Style.BRIGHT + "Beli Makanan")
        print(Fore.BLUE + "3. " + Fore.GREEN + Style.BRIGHT + "Topup Saldo")
        print(Fore.BLUE + "4. " + Fore.GREEN + Style.BRIGHT + "Cek Saldo")
        print(Fore.BLUE + "5. " + Fore.GREEN + Style.BRIGHT + "Histori Pembelian Makanan")
        print(Fore.BLUE + "6. " + Fore.GREEN + Style.BRIGHT + "Histori Pembelian Tiket")
        print(Fore.BLUE + "7. " + Fore.GREEN + Style.BRIGHT + "Beri Komentar")
        print(Fore.BLUE + "8. " + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Logout")
        print(Fore.BLUE + "9. " + Fore.LIGHTRED_EX + Style.BRIGHT + "Keluar Program")
        inputmenu = input( Fore.LIGHTBLUE_EX + Style.BRIGHT +">> Masukkan pilihan yang anda inginkan: ")
        cls()
        return inputmenu
    
# fungsi menu tiket
def menutiket(username, masuk):
    try:
        while masuk == 3:
            # menampilkan daftar teater dan film
            print(Fore.CYAN + Style.BRIGHT + "="*60)
            print(Fore.CYAN + Style.BRIGHT + "||"+"Daftar Teater dan Film:".center(50)+"||")
            print(Fore.CYAN + Style.BRIGHT + "="*60)

            print(Fore.WHITE + "-" * 50)
            for data in database['teaters']:
                film_name = film_dict.get(data["film_id"])
                rating = film_rating.get(data["film_id"])
                if data['film_id'] is not None:
                    print(Fore.GREEN + Style.BRIGHT + f"  {data['name']}")
                    print(Fore.LIGHTWHITE_EX + f"  Nama Film    : {film_name}")
                    print(Fore.LIGHTWHITE_EX + f"  Rating       : {rating}")
                    print(Fore.LIGHTWHITE_EX + f"  Harga        : Rp.{data['price']}")
                    print(Fore.LIGHTWHITE_EX + f"  Jumlah Kursi : {data['available']}/{data['capacity']}")
                    print(Fore.LIGHTWHITE_EX + f"  Tipe Teater  : {data['type'].capitalize()}")
                    print(Fore.WHITE + "-" * 50)

            beli = int(input(Fore.BLUE + Style.BRIGHT +">> Masukkan urutan teater yang anda inginkan (0 untuk kembali ke halaman utama): "))
            if beli == 0:
                cls()
                return masuk == 2
            teaterada= False
            for cekteater in database['teaters']:
                if cekteater['film_id'] is None:
                    continue
                elif cekteater['id'] == beli:
                    teaterada = True
                    if cekteater['available'] <= 0:
                        cls()
                        print(Fore.LIGHTRED_EX + Style.BRIGHT + "Kursi telah habis")
                        return menutiket(masuk)
                    break

            if teaterada == False:
                cls()
                print(Fore.LIGHTRED_EX + Style.BRIGHT + "Nomor teater tidak valid")
                menutiket(masuk)

            belikursi = int(input(Fore.BLUE + Style.BRIGHT +">> Masukkan jumlah kursi yang ingin anda beli: "))

            if belikursi == 0:
                cls()
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Anda tidak membeli kursi.\n")
                break
        
            for cekursi in database['teaters']:
                if beli == cekursi['id']:
                    cekkursi = cekursi['available']

            if belikursi > cekkursi:
                cls()
                print(Fore.LIGHTRED_EX + Style.BRIGHT +"Anda memesan kursi lebih dari yang tersedia\n")
                continue
            
            elif cekkursi > 0 and belikursi <= cekkursi:
                for ceksaldo in database['users']: 
                    if ceksaldo['username'] == username:
                        iduser = ceksaldo['id']
                        saldopengguna = ceksaldo['balance']
                        for belitiket in database['teaters'] :
                            if saldopengguna >= belikursi*belitiket['price']:
                            
                                if belitiket['id'] == beli:
                                    namateater = belitiket['name']
                                    idteater = belitiket['id']
                                    belitiket['available'] -= belikursi
                                    ceksaldo['balance'] -= belikursi*belitiket['price']
                                    for idfilm in database['films']:
                                        if beli == idfilm['id']:
                                            idnamafilm = idfilm['id']
                                            namafilm = idfilm['name']

                                            riwayat = {
                                                "id": get_next_id(database['ticketTransactions']),
                                                "film_id": idnamafilm,
                                                "teater_id": idteater,
                                                "user_id": iduser,
                                                "price": belitiket['price'],
                                                "totalTicket": belikursi,
                                                "totalPrice": belikursi*belitiket['price'],
                                                "purchaseTime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                            }
                                            database['ticketTransactions'].append(riwayat)

                                    save(database)

                                cls()
                                print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"Anda telah membeli sebanyak {belikursi} kursi untuk {namateater} dengan film {namafilm}\nHarga satuan tiket adalah Rp {belitiket['price']} dan total harganya adalah Rp {belikursi*belitiket['price']} \n")
                                return masuk == 2
                            else: 
                                cls()
                                print(Fore.LIGHTRED_EX + Style.BRIGHT + "Saldo anda tidak cukup\n")   
                                menutiket(username, masuk) 
                            

    except ValueError:
        cls()
        print(Fore.LIGHTRED_EX + Style.BRIGHT +"Input yang anda masukkan harus berupa angka\n")
        menutiket(username, masuk)
    except TypeError:
        cls()
        print(Fore.LIGHTRED_EX + Style.BRIGHT +"Anda memasukkan input yang salah\n")
        menutiket(username, masuk)

# fungsi menu top up
def menutopup():
    try: 
        while True:
            print(Fore.BLUE + Style.BRIGHT +"="*60)
            print(Fore.BLUE + Style.BRIGHT +"||"+"Top up".center(56)+"||")
            print(Fore.BLUE + Style.BRIGHT +"="*60)

            topup = int(input(Fore.LIGHTGREEN_EX + Style.BRIGHT +">> Masukkan nominal top up anda (0 untuk kembali ke halaman utama): Rp."))
            if topup > 0:
                for topups in database['users']:
                    if topups['username'] == username:
                        topups['balance'] += topup
                save(database)
                cls()
                print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"Anda telah top up sebanyak Rp.{topup}\n")
                return
            elif topup == 0:
                cls()
                return
            else:
                cls()
                print(Fore.LIGHTYELLOW_EX + Style.BRIGHT +"Nominal top up harus lebih besar dari 0.\n")
    except ValueError:
        cls()
        print(Fore.LIGHTRED_EX + Style.BRIGHT +"Input yang anda masukkan harus berupa angka.\n")
        menutopup()
    except TypeError:
        cls()
        print(Fore.LIGHTRED_EX + Style.BRIGHT +"Anda memasukkan input yang salah.\n")
        menutopup()

# fungsi menu makanan
def menumakanan():
    try:
        while True:
            # Menampilkan daftar makanan
            print(Fore.BLUE + Style.BRIGHT +"="*60)
            print(Fore.BLUE + Style.BRIGHT +"||"+"Daftar makanan dan minuman:".center(56)+"||")
            print(Fore.BLUE + Style.BRIGHT +"="*60)

            print(Fore.WHITE + "-" * 50)
            for data in database['fnb']:
                print(Fore.GREEN + Style.BRIGHT + f"  {data['id']}. {data['name']}")
                print(Fore.LIGHTWHITE_EX + f"  Stok   : {data['stock']}")
                print(Fore.LIGHTWHITE_EX + f"  Harga  : Rp.{data['price']}")
                print(Fore.WHITE + "-" * 50)

            beli = int(input(Fore.BLUE + Style.BRIGHT +">> Masukkan nomor makanan yang ingin anda beli (0 untuk kembali ke halaman utama): "))

            if beli == 0:
                cls()
                return
            
            for data in database['fnb']:
                if data['id']  == beli:
                    idmakanan = data['id']
                    if data['stock'] <= 0:
                        cls()
                        print(Fore.LIGHTRED_EX + Style.BRIGHT +"Stok habis\n")
                        continue

                    totalfnb = int(input(Fore.BLUE + Style.BRIGHT +">> Masukkan jumlah yang ingin anda beli: "))

                    if totalfnb == 0:
                        cls()
                        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Anda tidak membeli FnB Apapun.\n")
                        break

                    if totalfnb > data['stock']:
                        cls()
                        print(Fore.LIGHTRED_EX + Style.BRIGHT +"Anda membeli melebihi stok yang tersedia\n")
                        continue

                    elif totalfnb <= data['stock']:
                        for ceksaldo in database['users']:
                            if ceksaldo['username'] == username:
                                iduser = ceksaldo['id']
                                if ceksaldo['balance'] >= totalfnb*data['price']:
                                    ceksaldo['balance'] -= totalfnb*data['price']
                                    data['stock'] -= totalfnb

                                    transaksi_baru = {
                                        "id": get_next_id(database['fnbTransactions']),
                                        "user_id": iduser,
                                        "fnb_id": idmakanan,
                                        "quantity": totalfnb,
                                        "total": totalfnb*database['price'],
                                        "purchaseTime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    }

                                    database['fnbTransactions'].append(transaksi_baru)

                                    save(database)

                                    cls()
                                    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"Anda telah membeli {database['name']} sebanyak {totalfnb} buah\nHarga satuannya adalah Rp {database['price']} dan totalnya adalah Rp {totalfnb*database['price']}")
                                    return masuk == 2
                                else:
                                    cls()
                                    print(Fore.LIGHTRED_EX + Style.BRIGHT +"Saldo anda tidak cukup")

    except ValueError:
        cls()
        print(Fore.LIGHTRED_EX + Style.BRIGHT +"Input yang anda masukkan harus berupa angka\n")
        menumakanan()
    except TypeError:
        cls()
        print(Fore.LIGHTRED_EX + Style.BRIGHT +"Anda memasukkan input yang salah\n")
        menumakanan()

# fungsi menu riwayat makanan
def menuhistorymakanan():
    user_found = 0
    for user in database['users']:
        if user['username'] == username:
            user_id = user['id']
            user_found = 1
            break

    if user_found == 0:
        print(Fore.LIGHTRED_EX + Style.BRIGHT +"Pengguna tidak ditemukan\n")
        return
    
    print(Fore.CYAN + Style.BRIGHT +"="*60)
    print(Fore.CYAN + Style.BRIGHT + "||"+f"Riwayat Pembelian FnB untuk {username}".center(56) +"||")
    print(Fore.CYAN + Style.BRIGHT +"="*60)
    print(Fore.WHITE + "-" * 50)
    
    transaksi_ditemukan = 0
    for transaksi in database['fnbTransactions']:
        if transaksi['user_id'] == user_id:
            transaksi_ditemukan = 1
            for fnb_item in database['fnb']:
                if fnb_item['id'] == transaksi['fnb_id']:
                    nama_makanan = fnb_item['name']
                    total_pembelian = transaksi['total']
                    harga_per_item = fnb_item['price']
                    jumlah_dibeli = transaksi['quantity']
                    waktu_pembelian = transaksi['purchaseTime']
                    
                    print(Fore.LIGHTWHITE_EX + f"FnB              : {nama_makanan}")
                    print(Fore.LIGHTWHITE_EX + f"Harga            : Rp.{harga_per_item}")
                    print(Fore.LIGHTWHITE_EX + f"Jumlah           : {jumlah_dibeli}")
                    print(Fore.LIGHTWHITE_EX + f"Total Harga      : Rp.{total_pembelian}")
                    print(Fore.LIGHTWHITE_EX + f"Waktu Pembelian  : {waktu_pembelian}")
                    print(Fore.WHITE +"-" * 50)
                    

    if transaksi_ditemukan == 0:
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT +"Tidak ada riwayat pembelian FnB untuk pengguna ini.\n")
        input(Fore.LIGHTBLUE_EX + Style.BRIGHT +">> Klik enter untuk kembali ke halaman utama\n")
        cls()

# fungsi menu riwayat tiket
def menuhistorytiket():
    user_found = 0
    for user in database['users']:
        if user['username'] == username:
            user_id = user['id']
            user_found = 1
            break

    if user_found == 0:
        print("Pengguna tidak ditemukan\n")
        return
    
    print(Fore.CYAN + Style.BRIGHT + "="*60)
    print(Fore.CYAN + Style.BRIGHT + "||"+f"Riwayat Pembelian Tiket untuk {username}".center(56) +"||")
    print(Fore.CYAN + Style.BRIGHT + "="*60)
    print(Fore.WHITE + "-" * 50)
    
    tiket_ditemukan = 0
    for transaksi in database['ticketTransactions']:
        if transaksi['user_id'] == user_id:
            tiket_ditemukan = 1
            for film in database['films']:
                if film['id'] == transaksi['film_id']:
                    nama_film =  film['name']
                    for teater in database['teaters']:
                        if teater['id'] == transaksi['teater_id']:
                            nama_teater = teater['name']

                            print(Fore.LIGHTWHITE_EX + f"Film            : {nama_film}")
                            print(Fore.LIGHTWHITE_EX + f"Teater          : {nama_teater}")
                            print(Fore.LIGHTWHITE_EX + f"Harga Tiket     : Rp.{transaksi['price']}")
                            print(Fore.LIGHTWHITE_EX + f"Jumlah          : {transaksi['totalTicket']}")
                            print(Fore.LIGHTWHITE_EX + f"Total           : Rp.{transaksi['totalPrice']}")
                            print(Fore.LIGHTWHITE_EX + f"Waktu Pembelian : {transaksi['purchaseTime']}")
                            print(Fore.WHITE +"-" * 50)
                            

    if tiket_ditemukan == 0:
        print(Fore.LIGHTYELLOW_EX + Style.BRIGHT +"Tidak ada riwayat pembelian\n")
        input(Fore.LIGHTBLUE_EX + Style.BRIGHT +">> Klik enter untuk kembali ke halaman utama\n")
        cls()

# fungsi menu komentar
def menukomentar(username):
    while True:
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        print(Fore.CYAN + Style.BRIGHT + "||" +"Forum Komentar".center(56)+"||")
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        print(Fore.BLUE + Style.BRIGHT + "Silahkan pilih menu di bawah ini\n".center(60))
        print(Fore.BLUE + "1. "+ Fore.GREEN + Style.BRIGHT + "Lihat semua komentar")
        print(Fore.BLUE + "2. "+ Fore.GREEN + Style.BRIGHT + "Tambah komentar baru")
        print(Fore.BLUE + "3. "+ Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Keluar")

        pilihan = input(Fore.LIGHTBLUE_EX + Style.BRIGHT +">> Pilih opsi (1-3): ")
        cls()

        if pilihan == '1':
            # Tampilkan semua komentar
            if not database['comments']:
                print(Fore.LIGHTYELLOW_EX + "\nBelum ada komentar.")
            else:
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.CYAN + Style.BRIGHT + "||" +"Daftar Komentar".center(56)+"||")
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.WHITE + "-" * 50)
                for comment in database['comments']:
                    # Cari nama pengguna berdasarkan user_id
                    username = next(
                        (user['username'] for user in database['users'] if user['id'] == comment['user_id']), "Unknown User"
                    )
                    print(Fore.LIGHTWHITE_EX + f"\nUsername: {username}")
                    print(Fore.LIGHTWHITE_EX + f"Komentar: {comment['comment']}")
                    print(Fore.WHITE + "-" * 50)

                input(Fore.LIGHTBLUE_EX + Style.BRIGHT +">> Klik enter untuk kembali\n")
                cls()

        elif pilihan == '2':
            # Tambah komentar baru
            for user in database['users']:
                if user['username'] == username:
                    user_id = user['id']
                    komentar_baru = input(Fore.BLUE + Style.BRIGHT +">> Masukkan komentar Anda: ").strip()
                    if komentar_baru == "":
                        cls()
                        print(Fore.LIGHTYELLOW_EX + "Komentar tidak boleh kosong!\n")
                        break
                    komentar = {
                        "user_id": user_id,
                        "comment": komentar_baru
                    }
                    database['comments'].append(komentar)
                    save(database)
                    cls()
                    print(Fore.LIGHTGREEN_EX + "Komentar berhasil ditambahkan!\n")

        elif pilihan == '3':
            cls()
            print(Fore.LIGHTYELLOW_EX + "Keluar dari forum diskusi.\n")
            break

        else:
            cls()
            print(Fore.LIGHTYELLOW_EX + "Pilihan tidak valid. Silakan coba lagi.")


# ---------------------------------------------------> FUNGSI ADMIN
# fungsi menu admin
def menuadmin():
    while True:
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        print(Fore.CYAN + Style.BRIGHT + "||" +"Behasil masuk: Selamat datang Admin".center(56)+"||")
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        print(Fore.BLUE + Style.BRIGHT + "Silahkan pilih menu di bawah ini\n".center(60))
        print(Fore.BLUE + "1. "+ Fore.GREEN + Style.BRIGHT + "Lihat Daftar")
        print(Fore.BLUE + "2. "+ Fore.GREEN + Style.BRIGHT + "Tambah Data ")
        print(Fore.BLUE + "3. "+ Fore.GREEN + Style.BRIGHT + "Edit Data")
        print(Fore.BLUE + "4. "+ Fore.GREEN + Style.BRIGHT + "Hapus Data")
        print(Fore.BLUE + "5. " + Fore.LIGHTYELLOW_EX + Style.BRIGHT + "Logout")
        print(Fore.BLUE + "6. " + Fore.LIGHTRED_EX + Style.BRIGHT + "Keluar Program")
        inputmenu = input(Fore.LIGHTBLUE_EX + Style.BRIGHT +">> Masukkan pilihan Anda: ")
        cls()
        return inputmenu

# fungsi lihat daftar
def lihatadmin():
    while True:
        # mengecek apakah database ada
        if not database:
            print(Fore.LIGHTYELLOW_EX + "Data tidak tersedia")
            input(Fore.LIGHTYELLOW_EX + "\n>> Tekan enter untuk kembali")
            return

        # menampilkan daftar database
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        print(Fore.CYAN + Style.BRIGHT + "||"+"Daftar Data".center(56)+"||")
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        print(Fore.BLUE + "1. "+ Fore.GREEN + Style.BRIGHT +"Teater")
        print(Fore.BLUE + "2. "+ Fore.GREEN + Style.BRIGHT +"Film")
        print(Fore.BLUE + "3. "+ Fore.GREEN + Style.BRIGHT +"FnB")
        print(Fore.BLUE + "4. "+ Fore.GREEN + Style.BRIGHT +"Pengguna")
        print(Fore.BLUE + "5. "+ Fore.GREEN + Style.BRIGHT +"Komentar")
        print(Fore.BLUE + "6. "+ Fore.GREEN + Style.BRIGHT +"Riwayat Pembelian Tiket")
        print(Fore.BLUE + "7. "+ Fore.GREEN + Style.BRIGHT +"Riwayat Pembelian FnB")
        pilihlihat = input(Fore.LIGHTBLUE_EX + Style.BRIGHT +"\n>> Masukkan angka yang sesuai (0 untuk kembali): ").strip()
        cls()

        match pilihlihat:
            case "0":
                return
            case "1":
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.CYAN + Style.BRIGHT + "||"+"Daftar Teater".center(56)+"||")
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.WHITE + "-" * 50)
                if not database['teaters']:
                    print(Fore.LIGHTYELLOW_EX + "Tidak ada database teater\n")
                else:
                    for data in database['teaters']:
                        film_name = film_dict.get(data["film_id"])
                        print(Fore.LIGHTWHITE_EX + f"  ID           : {data['id']}")
                        print(Fore.LIGHTWHITE_EX + f"  Nama Teater  : {data['name']}")
                        print(Fore.LIGHTWHITE_EX + f"  Nama Film    : {film_name}")
                        print(Fore.LIGHTWHITE_EX + f"  Harga        : {'None' if data['price'] is None else 'Rp.' + str(data['price'])}")
                        print(Fore.LIGHTWHITE_EX + f"  Jumlah Kursi : {data['available']}/{data['capacity']}")
                        print(Fore.LIGHTWHITE_EX + f"  Tipe Teater  : {data['type'].capitalize()}")
                        print(Fore.WHITE + "-" * 50)
                input(Fore.LIGHTBLUE_EX + "\n>> Tekan enter untuk kembali\n")
                cls()
            case "2":
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.CYAN + Style.BRIGHT + "||"+"Daftar Film".center(56)+"||")
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.WHITE + "-" * 50)
                if not database['films']:
                    print(Fore.LIGHTYELLOW_EX + "Tidak ada database film\n")
                else:
                    for data in database['films']:
                        print(Fore.LIGHTWHITE_EX + f"  ID     : {data['id']}")
                        print(Fore.LIGHTWHITE_EX + f"  Nama   : {data['name']}")
                        print(Fore.LIGHTWHITE_EX + f"  Genre  : {', '.join(data['genre'])}")
                        print(Fore.LIGHTWHITE_EX + f"  Rating : {data['filmRating']}")
                        print(Fore.WHITE + "-" * 50)
                input(Fore.LIGHTBLUE_EX + "\n>> Tekan enter untuk kembali\n")
                cls()
            case "3":
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.CYAN + Style.BRIGHT + "||"+"Daftar FnB".center(56)+"||")
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.WHITE + "-" * 50)
                if not database['fnb']:
                    print(Fore.LIGHTYELLOW_EX + "Tidak ada database FnB\n")
                else:
                    for data in database['fnb']:
                        print(Fore.LIGHTWHITE_EX + f"  ID     : {data['id']}")
                        print(Fore.LIGHTWHITE_EX + f"  Nama   : {data['name']}")
                        print(Fore.LIGHTWHITE_EX + f"  Stok   : {data['stock']}")
                        print(Fore.LIGHTWHITE_EX + f"  Harga  : Rp.{data['price']}")
                        print(Fore.WHITE + "-" * 50)
                input(Fore.LIGHTBLUE_EX + "\n>> Tekan enter untuk kembali\n")
                cls()
            case "4":
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.CYAN + Style.BRIGHT + "||"+"Daftar Pengguna".center(56)+"||")
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.WHITE + "-" * 50)
                if not database['users']:
                    print(Fore.LIGHTYELLOW_EX + "Tidak ada database pengguna\n")
                else:
                    for data in database['users']:
                        print(Fore.LIGHTWHITE_EX + f"  ID        : {data['id']}")
                        print(Fore.LIGHTWHITE_EX + f"  Username  : {data['username']}")
                        print(Fore.LIGHTWHITE_EX + f"  Role      : {data['role'].capitalize()}")
                        print(Fore.WHITE + "-" * 50)
                input(Fore.LIGHTBLUE_EX + "\n>> Tekan enter untuk kembali\n")
                cls()
            case "5":
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.CYAN + Style.BRIGHT + "||"+"Daftar Komentar".center(56)+"||")
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.WHITE + "-" * 50)
                if not database['comments']:
                    print(Fore.LIGHTYELLOW_EX + "Tidak ada database komentar\n")
                else:
                    for data in database['comments']:
                        user_name = user_dict.get(data["user_id"])
                        print(Fore.LIGHTWHITE_EX + f"  ID        : {data['user_id']}")
                        print(Fore.LIGHTWHITE_EX + f"  Nama      : {user_name}")
                        print(Fore.LIGHTWHITE_EX + f"  Komentar  : {data['comment']}")
                        print(Fore.WHITE + "-" * 50)
                input(Fore.LIGHTBLUE_EX + "\n>> Tekan enter untuk kembali\n")
                cls()
            case "6":
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.CYAN + Style.BRIGHT + "||"+"Daftar Riwayat Pembelian Tiket".center(56)+"||")
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.WHITE + "-" * 50)
                if not database['ticketTransactions']:
                    print(Fore.LIGHTYELLOW_EX + "Tidak ada database riwayat pembelian tiket\n")
                else:
                    for data in database['ticketTransactions']:
                        user_name = user_dict.get(data["user_id"])
                        teater_name = teater_dict.get(data["teater_id"])
                        film_name = film_dict.get(data["film_id"])
                        print(Fore.LIGHTWHITE_EX + f"ID              : {data['id']}")
                        print(Fore.LIGHTWHITE_EX + f"Nama            : {user_name}")
                        print(Fore.LIGHTWHITE_EX + f"Teater          : {teater_name}")
                        print(Fore.LIGHTWHITE_EX + f"Film            : {film_name}")
                        print(Fore.LIGHTWHITE_EX + f"Harga           : Rp.{data['price']}")
                        print(Fore.LIGHTWHITE_EX + f"Jumlah Tiket    : {data['totalTicket']}")
                        print(Fore.LIGHTWHITE_EX + f"Waktu Pembelian : {data['purchaseTime']}")
                        print(Fore.WHITE +"-" * 50)
                input("\nTekan enter untuk kembali\n")
                cls()
            case "7":
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.CYAN + Style.BRIGHT + "||"+"Daftar Riwayat Pembelian Tiket".center(56)+"||")
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.WHITE + "-" * 50)
                if not database['fnbTransactions']:
                    print(Fore.LIGHTYELLOW_EX + "Tidak ada database riwayat pembelian FnB\n")
                else:
                    for data in database['fnbTransactions']:
                        user_name = user_dict.get(data["user_id"])
                        fnb_name = fnb_dict.get(data["fnb_id"])
                        harga = fnb_price.get(data["fnb_id"])
                        waktu_pembelian = data['purchaseTime']
                        print(Fore.LIGHTWHITE_EX + f"ID               : {data['id']}")
                        print(Fore.LIGHTWHITE_EX + f"Nama User        : {user_name}")
                        print(Fore.LIGHTWHITE_EX + f"FnB              : {fnb_name}")
                        print(Fore.LIGHTWHITE_EX + f"Harga            : Rp.{harga}")
                        print(Fore.LIGHTWHITE_EX + f"Jumlah           : {data['quantity']}")
                        print(Fore.LIGHTWHITE_EX + f"Total Harga      : Rp.{data['total']}")
                        print(Fore.LIGHTWHITE_EX + f"Waktu Pembelian  : {waktu_pembelian}")
                        print(Fore.WHITE +"-" * 50)
                input(Fore.LIGHTBLUE_EX + "\n>> Tekan enter untuk kembali\n")
                cls()
            case "":
                continue
            case _:
                print("Pilihan tidak tersedia.\n")

# fungsi tambah database teater dan fnb
def tambahadmin(username):
    while True:
        # mengecek apakah database ada
        if not database:
            print(Fore.LIGHTYELLOW_EX + "Data tidak tersedia")
            input(Fore.LIGHTYELLOW_EX + "\n>> Tekan enter untuk kembali")
            return
        
        # menampilkan menu tambah database
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        print(Fore.CYAN + Style.BRIGHT + "||"+"Tambah Data".center(56)+"||")
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        print(Fore.BLUE + "1. "+ Fore.GREEN + Style.BRIGHT + "Teater")
        print(Fore.BLUE + "2. "+ Fore.GREEN + Style.BRIGHT + "Film")
        print(Fore.BLUE + "3. "+ Fore.GREEN + Style.BRIGHT + "FnB")
        print(Fore.BLUE + "4. "+ Fore.GREEN + Style.BRIGHT + "User")
        print(Fore.BLUE + "5. "+ Fore.GREEN + Style.BRIGHT + "Komentar")
        pilihtambah = input(Fore.LIGHTBLUE_EX + "\n>> Masukkan angka yang sesuai (0 untuk kembali): ").strip()
        cls()

        match pilihtambah:
            case "0":
                return
            case "1":
                try:
                    # menampilkan daftar film
                    print(Fore.CYAN + Style.BRIGHT + "="*60)
                    print(Fore.CYAN + Style.BRIGHT + "||" +"Daftar Film".center(56)+"||")
                    print(Fore.CYAN + Style.BRIGHT + "="*60)
                    print(Fore.WHITE + "-" * 50)
                    for data in database['films']:
                        print(Fore.LIGHTWHITE_EX + f"  ID     : {data['id']}")
                        print(Fore.LIGHTWHITE_EX + f"  Nama   : {data['name']}")
                        print("-" * 50)

                    print(Fore.CYAN + Style.BRIGHT + "="*60)
                    print(Fore.CYAN + Style.BRIGHT + "||" +"Tambah Teater".center(56)+"||")
                    print(Fore.CYAN + Style.BRIGHT + "="*60)
                    name = input(Fore.LIGHTBLUE_EX + ">> Nama Teater: ").capitalize().strip()
                    # cek apakah nama teater kosong
                    if name == "":
                        cls()
                        print(Fore.LIGHTYELLOW_EX + "Nama teater tidak boleh kosong\n")
                        continue
                    # cek apakah nama sudah ada
                    for teater in database["teaters"]:
                        if teater["name"].lower() == name.lower():
                            cls()
                            print(Fore.LIGHTYELLOW_EX + "Teater dengan nama tersebut sudah ada\n")
                            break

                    film_id = int(input(Fore.LIGHTBLUE_EX + ">> ID Film (0 untuk None): ").strip())
                    if film_id == 0:
                        film_id = None
                    else:
                        # Cek apakah id film ada
                        film_found = False  # Inisialisasi flag untuk ID film
                        for film in database["films"]:
                            if film["id"] == film_id:
                                film_found = True
                                break  # Keluar dari loop jika film ditemukan
                        
                        if not film_found:
                            print(Fore.LIGHTYELLOW_EX + "Film dengan ID tersebut tidak ditemukan\n")
                            break

                    type = input(Fore.LIGHTBLUE_EX + ">> Tipe Teater (R untuk Regular, P untuk Premiere): ").capitalize().strip()
                    match type:
                        case "R":
                            type = "Regular"
                        case "P":
                            type = "Premiere"
                        case "Regular":
                            type = "Regular"
                        case "Premiere":
                            type = "Premiere"
                        case _:
                            cls()
                            print(Fore.LIGHTYELLOW_EX + "Input yang anda masukkan salah\n")
                            continue

                    capacity = int(input(Fore.LIGHTBLUE_EX + ">> Kapasitas Teater: ").strip())
                    if capacity <= 0:
                        cls()
                        print(Fore.LIGHTYELLOW_EX + "Kapasitas harus lebih dari 0\n")
                        continue

                    if film_id is not None:
                        price = int(input(Fore.LIGHTBLUE_EX + ">> Harga Tiket: ").strip())
                        if price <= 0:
                            cls()
                            print(Fore.LIGHTYELLOW_EX + "Harga harus lebih dari 0\n")
                            continue
                    else:
                        price = None

                    teater_baru = {
                        "id": get_next_id(database["teaters"]),
                        "name": name,
                        "film_id": film_id,
                        "type": type,
                        "capacity": capacity,
                        "available": capacity,
                        "price": price
                    }
                    database["teaters"].append(teater_baru)
                    save(database)
                    cls()
                    print(Fore.LIGHTGREEN_EX + "Teater baru berhasil ditambahkan!\n")
                except ValueError:
                    cls()
                    print(Fore.LIGHTYELLOW_EX + "Input yang anda masukkan harus berupa angka\n")
                except TypeError:
                    cls()
                    print(Fore.LIGHTYELLOW_EX + "Anda memasukkan input yang salah\n")
            case "2":
                try:
                    while True:
                        print(Fore.CYAN + Style.BRIGHT + "="*60)
                        print(Fore.CYAN + Style.BRIGHT + "||" +"Tambah Film".center(56)+"||")
                        print(Fore.CYAN + Style.BRIGHT + "="*60)

                        nama = input(Fore.LIGHTBLUE_EX + ">> Nama Film: ").strip().capitalize()
                        # cek apakah nama kosong
                        if nama == "":
                            cls()
                            print(Fore.LIGHTYELLOW_EX + "Nama tidak boleh kosong\n")
                            continue
                        # cek apakah nama sudah ada
                        if nama in [data['name'] for data in database['films']]:
                            cls()
                            print(Fore.LIGHTYELLOW_EX + "Film dengan nama tersebut sudah ada di daftar\n")
                            break

                        genre_input = input(Fore.LIGHTBLUE_EX + ">> Genre film (pisahkan dengan koma jika lebih dari satu): ").strip()
                        # Memisahkan input berdasarkan koma, menghilangkan spasi di sekitar, dan mengabaikan entri kosong
                        genre = [g.strip().capitalize() for g in genre_input.split(",") if g.strip()]
                        
                        # cek apakah genre kosong
                        if not genre:
                            cls()
                            print(Fore.LIGHTYELLOW_EX + "Genre tidak boleh kosong\n")
                            tambahadmin()

                        filmRating = input(Fore.LIGHTBLUE_EX + ">> Rating Film: ").strip()
                        # cek apakah rating kosong
                        if filmRating == "":
                            cls()
                            print(Fore.LIGHTYELLOW_EX + "Rating tidak boleh kosong\n")
                            continue

                        film_baru = {
                            "id": get_next_id(database["films"]),
                            "name": nama,
                            "genre": genre,
                            "filmRating": filmRating
                        }
                        database["films"].append(film_baru)
                        save(database)
                        cls()
                        print(Fore.LIGHTGREEN_EX + "Film baru berhasil ditambahkan!\n")
                        break
                except ValueError:
                    cls()
                    print(Fore.LIGHTYELLOW_EX + "Input yang anda masukkan harus berupa angka\n")
                except TypeError:
                    cls()
                    print(Fore.LIGHTYELLOW_EX + "Anda memasukkan input yang salah\n")
            case "3":
                try:
                    while True:
                        print(Fore.CYAN + Style.BRIGHT + "="*60)
                        print(Fore.CYAN + Style.BRIGHT + "||" +"Tambah FnB".center(56)+"||")
                        print(Fore.CYAN + Style.BRIGHT + "="*60)

                        nama = input(Fore.LIGHTBLUE_EX + ">> Nama: ").strip().capitalize()
                        # cek apakah nama kosong
                        if nama == "":
                            cls()
                            print(Fore.LIGHTYELLOW_EX + "Nama tidak boleh kosong\n")
                            continue
                        # cek apakah nama sudah ada
                        if nama in [data['name'] for data in database['fnb']]:
                            cls()
                            print(Fore.LIGHTYELLOW_EX + "FnB dengan nama tersebut sudah ada di daftar\n")
                            break

                        harga = int(input(Fore.LIGHTBLUE_EX + ">> Harga: ").strip())
                        # cek apakah harga kurang dari atau sama dengan 0
                        if harga <= 0:
                            cls()
                            print(Fore.LIGHTYELLOW_EX + "Harga tidak boleh kurang dari atau sama dengan 0\n")
                            break

                        stock = int(input(Fore.LIGHTBLUE_EX + ">> Stok awal: ").strip())
                        # cek apakah stok kurang dari 0
                        if stock < 0:
                            cls()
                            print(Fore.LIGHTYELLOW_EX + "Stok tidak boleh kurang dari 0\n")
                            break

                        fnb_baru = {
                            "id": get_next_id(database["fnb"]),
                            "name": nama,
                            "price": harga,
                            "stock": stock
                        }
                        database["fnb"].append(fnb_baru)
                        save(database)
                        cls()
                        print(Fore.LIGHTGREEN_EX + "FnB baru berhasil ditambahkan!\n")
                        break
                except ValueError:
                    cls()
                    print(Fore.LIGHTYELLOW_EX + "Input yang anda masukkan harus berupa angka\n")
                except TypeError:
                    cls()
                    print(Fore.LIGHTYELLOW_EX + "Anda memasukkan input yang salah\n")
            case "4":
                try:
                    while True:
                        print(Fore.CYAN + Style.BRIGHT + "="*60)
                        print(Fore.CYAN + Style.BRIGHT + "||" +"Tambah Pengguna".center(56)+"||")
                        print(Fore.CYAN + Style.BRIGHT + "="*60)

                        username = input(Fore.LIGHTBLUE_EX + ">> Username: ").strip()
                        # cek apakah username kosong
                        if username == "":
                            cls()
                            print(Fore.LIGHTYELLOW_EX + "Username tidak boleh kosong\n")
                            break
                        # cek apakah username sudah ada
                        if username in [data['username'] for data in database['users']]:
                            cls()
                            print(Fore.LIGHTYELLOW_EX + "Pengguna dengan username tersebut sudah ada\n")
                            continue

                        password = input(Fore.LIGHTBLUE_EX + ">> Password: ").strip()
                        # cek apakah password kosong
                        if password == "":
                            cls()
                            print(Fore.LIGHTYELLOW_EX + "Password tidak boleh kosong\n")
                            break

                        role = input(Fore.LIGHTBLUE_EX + ">> Role (U untuk User, A untuk Admin): ").strip().capitalize()
                        # cek apakah role kosong
                        match role:
                            case "U":
                                role = "user"
                                balance = 0
                            case "A":
                                role = "admin"
                                balance = None
                            case "User":
                                role = "user"
                                balance = 0
                            case "Admin":
                                role = "admin"
                                balance = None
                            case _:
                                cls()
                                print(Fore.LIGHTYELLOW_EX + "Role tidak valid\n")
                                continue

                        # membuat user baru
                        regis = {
                            "id": get_next_id(database["users"]),
                            "username": username,
                            "password": password,
                            "role": role,
                            "balance": balance
                        }

                        # menambahkan user baru ke database
                        database['users'].append(regis)
                        
                        # menyimpan database baru ke file
                        save(database)
                        
                        cls()
                        print(Fore.LIGHTGREEN_EX + "Register berhasil!\n")
                        break
                except TypeError:
                    cls()
                    print(Fore.LIGHTYELLOW_EX + "Anda memasukkan input yang salah\n")

            case "5":
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                print(Fore.CYAN + Style.BRIGHT + "||" +"Tambah Komentar".center(56)+"||")
                print(Fore.CYAN + Style.BRIGHT + "="*60)
                for user in database['users']:
                    if user['username'] == username:
                        user_id = user['id']
                        komentar_baru = input(Fore.BLUE + Style.BRIGHT +">> Masukkan komentar Anda: ").strip()
                        if komentar_baru == "":
                            cls()
                            print(Fore.LIGHTYELLOW_EX + "Komentar tidak boleh kosong!\n")
                            break
                        komentar = {
                            "user_id": user_id,
                            "comment": komentar_baru
                        }
                        database['comments'].append(komentar)
                        save(database)
                        cls()
                        print(Fore.LIGHTGREEN_EX + "Komentar berhasil ditambahkan!\n")
            
            case "":
                continue
            case _:
                print(Fore.LIGHTYELLOW_EX + "Pilihan tidak tersedia.\n")

def edit():
    while True:
        print(Fore.CYAN + Style.BRIGHT+"="*60)
        print(Fore.CYAN + Style.BRIGHT+"||"+"Edit Teater, Fnb, dan Film".center(56)+"||")
        print(Fore.CYAN + Style.BRIGHT+"="*60)
        print()
        print(Fore.BLUE + "1. "+ Fore.GREEN + Style.BRIGHT +"Teater")
        print(Fore.BLUE + "2. "+ Fore.GREEN + Style.BRIGHT +"Fnb")
        print(Fore.BLUE + "3. "+ Fore.GREEN + Style.BRIGHT +"Film")
        print()
        edit_pilih = input(Fore.LIGHTBLUE_EX+">> Masukkan pilihan (0 untuk kembali): ").strip()
        cls()

        match edit_pilih:
            case "0":
                return

            case "1":
                try:
                    while True:
                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                        print(Fore.CYAN + Style.BRIGHT+"||"+"Edit Teater, Fnb, dan Film".center(56)+"||")
                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                        print(Fore.CYAN + Style.BRIGHT + "||"+"Daftar Teater dan Film:".center(56)+"||")
                        print(Fore.CYAN + Style.BRIGHT + "="*60)

                        print(Fore.WHITE + "-" * 50)
                        for data in database['teaters']:
                            film_name = film_dict.get(data["film_id"])
                            rating = film_rating.get(data["film_id"])
                            if data['film_id'] is not None:
                                print(Fore.GREEN + Style.BRIGHT + f"  {data['name']}")
                                print(Fore.LIGHTWHITE_EX + f"  ID           : {data['id']}")
                                print(Fore.LIGHTWHITE_EX + f"  Nama Film    : {film_name}")
                                print(Fore.LIGHTWHITE_EX + f"  Rating       : {rating}")
                                print(Fore.LIGHTWHITE_EX + f"  Harga        : Rp.{data['price']}")
                                print(Fore.LIGHTWHITE_EX + f"  Jumlah Kursi : {data['available']}/{data['capacity']}")
                                print(Fore.LIGHTWHITE_EX + f"  Tipe Teater  : {data['type'].capitalize()}")
                                print(Fore.WHITE + "-" * 50)
                        id_teater = int(input(Fore.LIGHTBLUE_EX+">> Masukkan ID teater yang ingin diedit (0 untuk kembali): "))
                        cls()

                        if id_teater == 0:
                            break

                        teater = next((t for t in database["teaters"] if t["id"] == id_teater), None)

                        if teater:
                            print(Fore.CYAN + Style.BRIGHT+"="*60)
                            print(Fore.CYAN + Style.BRIGHT+"||"+"Edit teater".center(56)+"||")
                            print(Fore.CYAN + Style.BRIGHT+"="*60)
                            print()
                            print(Fore.BLUE +"1."+ Fore.GREEN + Style.BRIGHT + "Seluruhnya")
                            print(Fore.BLUE +"2."+ Fore.GREEN + Style.BRIGHT + "Nama Teater")
                            print(Fore.BLUE +"3."+ Fore.GREEN + Style.BRIGHT + "ID Film")
                            print(Fore.BLUE +"4."+ Fore.GREEN + Style.BRIGHT + "Tipe")
                            print(Fore.BLUE +"5."+ Fore.GREEN + Style.BRIGHT + "Kapasitas")
                            print(Fore.BLUE +"6."+ Fore.GREEN + Style.BRIGHT + "Stok Tiket")
                            print(Fore.BLUE +"7."+ Fore.GREEN + Style.BRIGHT + "Harga")
                            print()
                            pilih = input(Fore.LIGHTBLUE_EX+">> Masukkan pilihan(0 untuk kembali): ").strip()
                            cls()

                            match pilih:
                                case "0":
                                    continue

                                case "1":
                                    while True:
                                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                                        print(Fore.CYAN + Style.BRIGHT+"||"+"Edit teater".center(56)+"||")
                                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                                        name = input(Fore.LIGHTBLUE_EX + ">> Nama Teater: ").capitalize().strip()
                                        # cek apakah nama teater kosong
                                        if name == "":
                                            cls()
                                            print(Fore.LIGHTYELLOW_EX + "Nama teater tidak boleh kosong\n")
                                            continue
                                        # cek apakah nama sudah ada
                                        for teater in database["teaters"]:
                                            if teater["name"].lower() == name.lower():
                                                cls()
                                                print(Fore.LIGHTYELLOW_EX + "Teater dengan nama tersebut sudah ada\n")
                                                break

                                        film_id = int(input(Fore.LIGHTBLUE_EX + ">> ID Film (0 untuk None): ").strip())
                                        if film_id == 0:
                                            film_id = None
                                        else:
                                            # Cek apakah id film ada
                                            film_found = False  # Inisialisasi flag untuk ID film
                                            for film in database["films"]:
                                                if film["id"] == film_id:
                                                    film_found = True
                                                    break  # Keluar dari loop jika film ditemukan
                                            
                                            if not film_found:
                                                print(Fore.LIGHTYELLOW_EX + "Film dengan ID tersebut tidak ditemukan\n")
                                                break

                                        type = input(Fore.LIGHTBLUE_EX + ">> Tipe Teater (R untuk Regular, P untuk Premiere): ").capitalize().strip()
                                        match type:
                                            case "R":
                                                type = "Regular"
                                            case "P":
                                                type = "Premiere"
                                            case "Regular":
                                                type = "Regular"
                                            case "Premiere":
                                                type = "Premiere"
                                            case _:
                                                cls()
                                                print(Fore.LIGHTYELLOW_EX + "Input yang anda masukkan salah\n")
                                                continue

                                        capacity = int(input(Fore.LIGHTBLUE_EX + ">> Kapasitas Teater: ").strip())
                                        if capacity <= 0:
                                            cls()
                                            print(Fore.LIGHTYELLOW_EX + "Kapasitas harus lebih dari 0\n")
                                            continue

                                        if film_id is not None:
                                            price = int(input(Fore.LIGHTBLUE_EX + ">> Harga Tiket: ").strip())
                                            if price <= 0:
                                                cls()
                                                print(Fore.LIGHTYELLOW_EX + "Harga harus lebih dari 0\n")
                                                continue
                                        else:
                                            price = None

                                        teater.update({
                                            "id": get_next_id(database["teaters"]),
                                            "name": name,
                                            "film_id": film_id,
                                            "type": type,
                                            "capacity": capacity,
                                            "available": capacity,
                                            "price": price
                                        })
                                        save(database)
                                        cls()
                                        print(Fore.LIGHTBLUE_EX+"Data teater berhasil diubah.\n")
                                        break

                                case "2":
                                    print("="*60)
                                    print(Fore.CYAN + Style.BRIGHT+"||"+"Edit Nama".center(56)+"||")
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print()
                                    name = input(Fore.LIGHTBLUE_EX + ">> Nama Teater: ").capitalize().strip()
                                    # cek apakah nama teater kosong
                                    if name == "":
                                        cls()
                                        print(Fore.LIGHTYELLOW_EX + "Nama teater tidak boleh kosong\n")
                                        break
                                    # cek apakah nama sudah ada
                                    for teater in database["teaters"]:
                                        if teater["name"].lower() == name.lower():
                                            cls()
                                            print(Fore.LIGHTYELLOW_EX + "Teater dengan nama tersebut sudah ada\n")
                                            break 
                                    teater["name"] = name
                                    save(database)
                                    print(Fore.LIGHTBLUE_EX+"Nama teater berhasil diubah.")
                                    input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                                    cls()

                                case "3":
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print(Fore.CYAN + Style.BRIGHT+"||"+"Edit teater".center(56)+"||")
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print()
                                    film_id = int(input(Fore.LIGHTBLUE_EX + ">> ID Film (0 untuk None): ").strip())
                                    if film_id == 0:
                                        film_id = None
                                    else:
                                        # Cek apakah id film ada
                                        film_found = False  # Inisialisasi flag untuk ID film
                                        for film in database["films"]:
                                            if film["id"] == film_id:
                                                film_found = True
                                                break  # Keluar dari loop jika film ditemukan
                                        
                                        if not film_found:
                                            print(Fore.LIGHTYELLOW_EX + "Film dengan ID tersebut tidak ditemukan\n")
                                            break
                                    teater["film_id"] = film_id
                                    save(database)
                                    print(Fore.LIGHTBLUE_EX+"ID film berhasil diubah.")
                                    input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                                    cls()

                                case "4":
                                    os.system('cls')
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print(Fore.CYAN + Style.BRIGHT+"||"+"Edit teater".center(56)+"||")
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print()
                                    type = input(Fore.LIGHTBLUE_EX + ">> Tipe Teater (R untuk Regular, P untuk Premiere): ").capitalize().strip()
                                    match type:
                                        case "R":
                                            type = "Regular"
                                        case "P":
                                            type = "Premiere"
                                        case "Regular":
                                            type = "Regular"
                                        case "Premiere":
                                            type = "Premiere"
                                        case _:
                                            cls()
                                            print(Fore.LIGHTYELLOW_EX + "Input yang anda masukkan salah\n")
                                            continue
                                    teater["type"] = type
                                    save(database)
                                    print(Fore.LIGHTBLUE_EX+"Tipe teater berhasil diubah.")
                                    input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                                    cls()

                                case "5":
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print(Fore.CYAN + Style.BRIGHT+"||"+"Edit teater".center(56)+"||")
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print()
                                    capacity = int(input(Fore.LIGHTBLUE_EX + ">> Kapasitas Teater: ").strip())
                                    if capacity <= 0:
                                        cls()
                                        print(Fore.LIGHTYELLOW_EX + "Kapasitas harus lebih dari 0\n")
                                        continue
                                    teater["capacity"] = capacity
                                    save(database)
                                    print(Fore.LIGHTBLUE_EX+"Kapasitas teater berhasil diubah.")
                                    input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")

                                case "6":
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print(Fore.CYAN + Style.BRIGHT+"||"+"Edit teater".center(56)+"||")
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print()
                                    available = int(input(Fore.LIGHTBLUE_EX + ">> Stok Tiket: ").strip())
                                    if available < 0:
                                        cls()
                                        print(Fore.LIGHTYELLOW_EX + "Stok tiket harus lebih dari 0\n")
                                        continue
                                    elif available > teater["capacity"]:
                                        cls()
                                        print(Fore.LIGHTYELLOW_EX + "Stok tiket tidak boleh melebihi kapasitas teater\n")
                                        continue

                                    teater["available"] = available
                                    save(database)
                                    print(Fore.LIGHTBLUE_EX+"Stok tiket teater berhasil diubah.")
                                    input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")

                                    cls()

                                case "7":
                                    print("="*60)
                                    print(Fore.CYAN + Style.BRIGHT+"||"+"Edit teater".center(56)+"||")
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print()
                                    if film_id is not None:
                                        price = int(input(Fore.LIGHTBLUE_EX + ">> Harga Tiket: ").strip())
                                        if price <= 0:
                                            cls()
                                            print(Fore.LIGHTYELLOW_EX + "Harga harus lebih dari 0\n")
                                            continue
                                    else:
                                        print(Fore.LIGHTYELLOW_EX+"Harap memilih film terlebih dahulu\n")
                                        break
                                    teater["price"] = int(input(Fore.LIGHTBLUE_EX+">> Masukkan harga tiket yang baru: "))
                                    save(database)
                                    print(Fore.LIGHTBLUE_EX+"Harga tiket teater berhasil diubah.")
                                    input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                                    
                                case "":
                                    continue

                                case _:
                                    print(Fore.LIGHTBLUE_EX+"Pilihan tidak ada.")
                                    input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                        else:
                            print(Fore.LIGHTYELLOW_EX+"Teater dengan ID tersebut tidak ditemukan.")
                            input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")

                except ValueError:
                    cls()
                    print(Fore.LIGHTYELLOW_EX + "Input yang anda masukkan harus berupa angka\n")
                except TypeError:
                    cls()
                    print(Fore.LIGHTYELLOW_EX + "Anda memasukkan input yang salah\n")

            case "2":
                try:
                    while True:
                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                        print(Fore.CYAN + Style.BRIGHT+"||"+"Edit Teater, Fnb, dan Film".center(56)+"||")
                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                        print(Fore.CYAN + Style.BRIGHT + "||"+"Daftar FnB".center(56)+"||")
                        print(Fore.CYAN + Style.BRIGHT + "="*60)
                        print(Fore.WHITE + "-" * 50)
                        if not database['fnb']:
                            print(Fore.LIGHTYELLOW_EX + "Tidak ada data FnB\n")
                        else:
                            for data in database['fnb']:
                                print(Fore.LIGHTWHITE_EX + f"  ID     : {data['id']}")
                                print(Fore.LIGHTWHITE_EX + f"  Nama   : {data['name']}")
                                print(Fore.LIGHTWHITE_EX + f"  Stok   : {data['stock']}")
                                print(Fore.LIGHTWHITE_EX + f"  Harga  : Rp.{data['price']}")
                                print(Fore.WHITE + "-" * 50)
                        id_fnb = int(input(Fore.LIGHTBLUE_EX+">> Masukkan ID fnb yang ingin diedit (0 untuk kembali): "))
                        cls()

                        if id_fnb == 0:
                            break

                        fnb = next((t for t in database["fnb"] if t["id"] == id_fnb), None)

                        if fnb:
                            print(Fore.CYAN + Style.BRIGHT+"="*60)
                            print(Fore.CYAN + Style.BRIGHT+"||"+"Edit fnb".center(56)+"||")
                            print(Fore.CYAN + Style.BRIGHT+"="*60)
                            print()
                            print(Fore.BLUE +"1."+ Fore.GREEN + Style.BRIGHT + "Seluruhnya")
                            print(Fore.BLUE +"2."+ Fore.GREEN + Style.BRIGHT + "Nama")
                            print(Fore.BLUE +"3."+ Fore.GREEN + Style.BRIGHT + "Harga")
                            print(Fore.BLUE +"4."+ Fore.GREEN + Style.BRIGHT + "Stok")
                            print()
                            pilih = input(Fore.LIGHTBLUE_EX+">> Masukkan pilihan (0 untuk kembali): ").strip()
                            cls()

                            match pilih:
                                case "0":
                                    continue

                                case "1":
                                    while True:
                                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                                        print(Fore.CYAN + Style.BRIGHT+"||"+"Edit fnb".center(56)+"||")
                                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                                        print()
                                        nama = input(Fore.LIGHTBLUE_EX + ">> Nama: ").strip().capitalize()
                                        # cek apakah nama kosong
                                        if nama == "":
                                            cls()
                                            print(Fore.LIGHTYELLOW_EX + "Nama tidak boleh kosong\n")
                                            continue
                                        # cek apakah nama sudah ada
                                        if nama in [data['name'] for data in database['fnb']]:
                                            cls()
                                            print(Fore.LIGHTYELLOW_EX + "FnB dengan nama tersebut sudah ada di daftar\n")
                                            break

                                        harga = int(input(Fore.LIGHTBLUE_EX + ">> Harga: ").strip())
                                        # cek apakah harga kurang dari atau sama dengan 0
                                        if harga <= 0:
                                            cls()
                                            print(Fore.LIGHTYELLOW_EX + "Harga tidak boleh kurang dari atau sama dengan 0\n")
                                            break

                                        stock = int(input(Fore.LIGHTBLUE_EX + ">> Stok awal: ").strip())
                                        # cek apakah stok kurang dari 0
                                        if stock < 0:
                                            cls()
                                            print(Fore.LIGHTYELLOW_EX + "Stok tidak boleh kurang dari 0\n")
                                            break

                                        fnb.update({
                                            "id": get_next_id(database["fnb"]),
                                            "name": nama,
                                            "price": harga,
                                            "stock": stock
                                        })
                                        save(database)
                                        cls()
                                        print(Fore.LIGHTBLUE_EX+"Seluruh data fnb berhasil diubah.\n")

                                case "2":
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print(Fore.CYAN + Style.BRIGHT+"||"+"Edit fnb".center(56)+"||")
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print()
                                    nama = input(Fore.LIGHTBLUE_EX + ">> Nama: ").strip().capitalize()
                                    # cek apakah nama kosong
                                    if nama == "":
                                        cls()
                                        print(Fore.LIGHTYELLOW_EX + "Nama tidak boleh kosong\n")
                                        continue
                                    # cek apakah nama sudah ada
                                    if nama in [data['name'] for data in database['fnb']]:
                                        cls()
                                        print(Fore.LIGHTYELLOW_EX + "FnB dengan nama tersebut sudah ada di daftar\n")
                                        break
                                    fnb["food"] = nama
                                    save(database)
                                    cls()
                                    print(Fore.LIGHTBLUE_EX+"Data makanan fnb berhasil diubah.\n")

                                case "3":
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print(Fore.CYAN + Style.BRIGHT+"||"+"Edit fnb".center(56)+"||")
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print()
                                    harga = int(input(Fore.LIGHTBLUE_EX + ">> Harga: ").strip())
                                    # cek apakah harga kurang dari atau sama dengan 0
                                    if harga <= 0:
                                        cls()
                                        print(Fore.LIGHTYELLOW_EX + "Harga tidak boleh kurang dari atau sama dengan 0\n")
                                        break
                                    fnb["price"] = harga
                                    save(database)
                                    cls()
                                    print(Fore.LIGHTBLUE_EX+"Data harga fnb berhasil diubah.\n")

                                case "4":
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print(Fore.CYAN + Style.BRIGHT+"||"+"Edit fnb".center(56)+"||")
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print()
                                    stock = int(input(Fore.LIGHTBLUE_EX + ">> Stok awal: ").strip())
                                    # cek apakah stok kurang dari 0
                                    if stock < 0:
                                        cls()
                                        print(Fore.LIGHTYELLOW_EX + "Stok tidak boleh kurang dari 0\n")
                                        break
                                    fnb["stock"] = stock
                                    save(database)
                                    cls()
                                    print(Fore.LIGHTBLUE_EX+"Data stok fnb berhasil diubah.\n")
                                
                                case "":
                                    continue
                                
                                case _:
                                    print(Fore.LIGHTBLUE_EX+"Tidak ada dalam pilihan")
                                    input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")

                        else:
                            print(Fore.LIGHTBLUE_EX+"Fnb dengan ID tersebut tidak ditemukan.")
                            input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                            cls()

                except ValueError:
                    cls()
                    print(Fore.LIGHTYELLOW_EX + "Input yang anda masukkan harus berupa angka\n")
                except TypeError:
                    cls()
                    print(Fore.LIGHTYELLOW_EX + "Anda memasukkan input yang salah\n")

            case "3":
                try:
                    while True:
                        print(Fore.CYAN + Style.BRIGHT + "="*60)
                        print(Fore.CYAN + Style.BRIGHT+"||"+"Edit Teater, Fnb, dan Film".center(56)+"||")
                        print(Fore.CYAN + Style.BRIGHT + "="*60)
                        print(Fore.CYAN + Style.BRIGHT + "||"+"Daftar Film".center(56)+"||")
                        print(Fore.CYAN + Style.BRIGHT + "="*60)
                        print(Fore.WHITE + "-" * 50)
                        if not database['films']:
                            print(Fore.LIGHTYELLOW_EX + "Tidak ada data film\n")
                        else:
                            for data in database['films']:
                                print(Fore.LIGHTWHITE_EX + f"  ID     : {data['id']}")
                                print(Fore.LIGHTWHITE_EX + f"  Nama   : {data['name']}")
                                print(Fore.LIGHTWHITE_EX + f"  Genre  : {', '.join(data['genre'])}")
                                print(Fore.LIGHTWHITE_EX + f"  Rating : {data['filmRating']}")
                                print(Fore.WHITE + "-" * 50)
                        id_film = int(input(Fore.LIGHTBLUE_EX+"Masukkan ID Film (0 untuk kembali): "))
                        cls()

                        if id_film == 0:
                            break

                        films = next((t for t in database["films"] if t["id"] == id_film), None)
                        if films:
                            print(Fore.CYAN + Style.BRIGHT+"="*60)
                            print(Fore.CYAN + Style.BRIGHT+"||"+"Edit Film".center(56)+"||")
                            print(Fore.CYAN + Style.BRIGHT+"="*60)
                            print()
                            print(Fore.BLUE +"1."+ Fore.GREEN + Style.BRIGHT + " Seluruhnya")
                            print(Fore.BLUE +"2."+ Fore.GREEN + Style.BRIGHT + " Nama")
                            print(Fore.BLUE +"3."+ Fore.GREEN + Style.BRIGHT + " Genre")
                            print(Fore.BLUE +"4."+ Fore.GREEN + Style.BRIGHT + " Rating")
                            print()
                            pilih = input(Fore.LIGHTBLUE_EX+">> Masukkan pilihan (0 untuk kembali): ").strip()
                            cls()

                            match pilih:
                                case "0":
                                    continue
                                case "1":
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print(Fore.CYAN + Style.BRIGHT+"||"+"Edit Film".center(56)+"||")
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print()
                                    nama = input(Fore.LIGHTBLUE_EX + ">> Nama Film: ").strip().capitalize()
                                    # cek apakah nama kosong
                                    if nama == "":
                                        cls()
                                        print(Fore.LIGHTYELLOW_EX + "Nama tidak boleh kosong\n")
                                        continue
                                    # cek apakah nama sudah ada
                                    if nama in [data['name'] for data in database['films']]:
                                        cls()
                                        print(Fore.LIGHTYELLOW_EX + "Film dengan nama tersebut sudah ada di daftar\n")
                                        break

                                    genre_input = input(Fore.LIGHTBLUE_EX + ">> Genre film (pisahkan dengan koma jika lebih dari satu): ").strip()
                                    # Memisahkan input berdasarkan koma, menghilangkan spasi di sekitar, dan mengabaikan entri kosong
                                    genre = [g.strip().capitalize() for g in genre_input.split(",") if g.strip()]
                                    
                                    # cek apakah genre kosong
                                    if not genre:
                                        cls()
                                        print(Fore.LIGHTYELLOW_EX + "Genre tidak boleh kosong\n")
                                        continue

                                    filmRating = input(Fore.LIGHTBLUE_EX + ">> Rating Film: ").strip()
                                    # cek apakah rating kosong
                                    if filmRating == "":
                                        cls()
                                        print(Fore.LIGHTYELLOW_EX + "Rating tidak boleh kosong\n")
                                        continue

                                    films.update({
                                        "id": get_next_id(database["films"]),
                                        "name": nama,
                                        "genre": genre,
                                        "filmRating": filmRating
                                    })
                                    save(database)
                                    print(Fore.LIGHTBLUE_EX+"\nSeluruh data film berhasil diubah.")
                                    input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                                    cls()

                                case "2":
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print(Fore.CYAN + Style.BRIGHT+"||"+"Edit Film".center(56)+"||")
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print()
                                    nama = input(Fore.LIGHTBLUE_EX + ">> Nama Film: ").strip().capitalize()
                                    # cek apakah nama kosong
                                    if nama == "":
                                        cls()
                                        print(Fore.LIGHTYELLOW_EX + "Nama tidak boleh kosong\n")
                                        continue
                                    # cek apakah nama sudah ada
                                    if nama in [data['name'] for data in database['films']]:
                                        cls()
                                        print(Fore.LIGHTYELLOW_EX + "Film dengan nama tersebut sudah ada di daftar\n")
                                        break
                                    films["name"] = nama
                                    save(database)
                                    print(Fore.LIGHTBLUE_EX+"\nData nama film berhasil diubah.")
                                    input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                                    cls()

                                case "3":
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print(Fore.CYAN + Style.BRIGHT+"||"+"Edit Film".center(56)+"||")
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print()
                                    genre_input = input(Fore.LIGHTBLUE_EX + ">> Genre film (pisahkan dengan koma jika lebih dari satu): ").strip()
                                    # Memisahkan input berdasarkan koma, menghilangkan spasi di sekitar, dan mengabaikan entri kosong
                                    genre = [g.strip().capitalize() for g in genre_input.split(",") if g.strip()]
                                    
                                    # cek apakah genre kosong
                                    if not genre:
                                        cls()
                                        print(Fore.LIGHTYELLOW_EX + "Genre tidak boleh kosong\n")
                                        continue
                                    films["genre"] = genre
                                    save(database)
                                    print(Fore.LIGHTBLUE_EX+"\nData genre berhasil diubah.")
                                    input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                                    cls()

                                case "4":
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print(Fore.CYAN + Style.BRIGHT+"||"+"Edit Film".center(56)+"||")
                                    print(Fore.CYAN + Style.BRIGHT+"="*60)
                                    print()
                                    filmRating = input(Fore.LIGHTBLUE_EX + ">> Rating Film: ").strip()
                                    # cek apakah rating kosong
                                    if filmRating == "":
                                        cls()
                                        print(Fore.LIGHTYELLOW_EX + "Rating tidak boleh kosong\n")
                                        continue
                                    films["filmRating"] = filmRating
                                    save(database)
                                    print(Fore.LIGHTBLUE_EX+"\nData rating film berhasil diubah.")
                                    input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                                    cls()
                                
                                case "":
                                    continue
                                
                                case _:
                                    print(Fore.LIGHTBLUE_EX+"\nTidak ada dalam pilihan")
                                    input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                                    cls()

                        else:
                            print(Fore.LIGHTBLUE_EX+"Film dengan ID tersebut tidak ditemukan.")
                            input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")

                except ValueError:
                    cls()
                    print(Fore.LIGHTYELLOW_EX + "Input yang anda masukkan harus berupa angka\n")
                except TypeError:
                    cls()
                    print(Fore.LIGHTYELLOW_EX + "Anda memasukkan input yang salah\n")

            case "":
                continue
            
            case _:
                cls()
                print(Fore.LIGHTBLUE_EX+"Tidak ada dalam pilihan")
                input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                cls()

def hapus():
    print(Fore.CYAN + Style.BRIGHT+"="*60)
    print(Fore.CYAN + Style.BRIGHT+"||"+"Hapus Teater, Fnb, dan Film".center(56)+"||")
    print(Fore.CYAN + Style.BRIGHT+"="*60)
    print()
    print(Fore.BLUE +"1."+ Fore.GREEN + Style.BRIGHT + " Teater")
    print(Fore.BLUE +"2."+ Fore.GREEN + Style.BRIGHT + " FnB")
    print(Fore.BLUE +"3."+ Fore.GREEN + Style.BRIGHT + " Film")
    print()
    pilih_hapus = input(Fore.LIGHTBLUE_EX+">> Masukkan Pilihan (pilih 0 untuk kembali): ")
    cls()

    if pilih_hapus == "1":
        print(Fore.CYAN + Style.BRIGHT+"="*60)
        print(Fore.CYAN + Style.BRIGHT+"||"+"Hapus teater".center(56)+"||")
        print(Fore.CYAN + Style.BRIGHT+"="*60)
        print(Fore.CYAN + Style.BRIGHT + "||"+"Daftar Teater".center(56)+"||")
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        print(Fore.WHITE + "-" * 50)
        if not database['teaters']:
            print(Fore.LIGHTYELLOW_EX + "Tidak ada database teater\n")
        else:
            for data in database['teaters']:
                film_name = film_dict.get(data["film_id"])
                print(Fore.LIGHTWHITE_EX + f"  ID           : {data['id']}")
                print(Fore.LIGHTWHITE_EX + f"  Nama Teater  : {data['name']}")
                print(Fore.LIGHTWHITE_EX + f"  Nama Film    : {film_name}")
                print(Fore.LIGHTWHITE_EX + f"  Harga        : {'None' if data['price'] is None else 'Rp.' + str(data['price'])}")
                print(Fore.LIGHTWHITE_EX + f"  Jumlah Kursi : {data['available']}/{data['capacity']}")
                print(Fore.LIGHTWHITE_EX + f"  Tipe Teater  : {data['type'].capitalize()}")
                print(Fore.WHITE + "-" * 50)
        try:
            id_teater = int(input(Fore.LIGHTBLUE_EX+">> Masukkan ID teater: "))
            cls()
        except ValueError:
            print(Fore.LIGHTRED_EX + "Input harus berupa angka")
            input(Fore.LIGHTBLUE_EX + "\nTekan Enter untuk kembali")
            cls()
            return
        teater = next((t for t in database["teaters"] if t["id"] == id_teater), None)

        if not teater:
                print(Fore.LIGHTRED_EX + "Teater dengan ID tersebut tidak ditemukan.")
                input(Fore.LIGHTBLUE_EX + "\nTekan Enter untuk kembali.")
                cls()
                return
        while True:
            print(Fore.CYAN + Style.BRIGHT+"="*60)
            print(Fore.CYAN + Style.BRIGHT+"||"+"Hapus teater".center(56)+"||")
            print(Fore.CYAN + Style.BRIGHT+"="*60)
            print()
            print(Fore.BLUE +"1."+ Fore.GREEN + Style.BRIGHT + " Yes")
            print(Fore.BLUE +"2."+ Fore.GREEN + Style.BRIGHT + " No")
            menghapus = input(Fore.LIGHTBLUE_EX+">> Masukkan pilihan: ")

            try:
                match menghapus:
                    case "0":
                        os.system('cls')
                        return
                    case "1":
                        database["teaters"].remove(teater)
                        save(database)
                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                        print(Fore.CYAN + Style.BRIGHT+f"Teater dengan ID {id_teater} berhasil dihapus".center(56))
                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                        print()              
                        input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                        cls()
                        return

                    case "2":
                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                        print(Fore.CYAN + Style.BRIGHT+"Anda batal menghapus".center(56))
                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                        print()             
                        input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                        cls()
                        return

            except ValueError:
                print(Fore.LIGHTRED_EX + "Input salah")
                input(Fore.LIGHTBLUE_EX + "\nTekan Enter untuk mencoba lagi") 
                cls()


    elif pilih_hapus == "2":
        print(Fore.CYAN + Style.BRIGHT+"="*60)
        print(Fore.CYAN + Style.BRIGHT+"||"+"Hapus Fnb".center(56)+"||")
        print(Fore.CYAN + Style.BRIGHT+"="*60)
        print(Fore.CYAN + Style.BRIGHT + "||"+"Daftar FnB".center(56)+"||")
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        print(Fore.WHITE + "-" * 50)
        if not database['fnb']:
            print(Fore.LIGHTYELLOW_EX + "Tidak ada database FnB\n")
        else:
            for data in database['fnb']:
                print(Fore.LIGHTWHITE_EX + f"  ID     : {data['id']}")
                print(Fore.LIGHTWHITE_EX + f"  Nama   : {data['name']}")
                print(Fore.LIGHTWHITE_EX + f"  Stok   : {data['stock']}")
                print(Fore.LIGHTWHITE_EX + f"  Harga  : Rp.{data['price']}")
                print(Fore.WHITE + "-" * 50)
        try:
            id_fnb = int(input(Fore.LIGHTBLUE_EX+">> Masukkan ID fnb: "))
            cls()
        except ValueError:
            print(Fore.LIGHTRED_EX + "Input harus berupa angka.")
            input(Fore.LIGHTBLUE_EX + "\nTekan Enter untuk kembali.")
            cls()
            return
        fnb = next((t for t in database["fnb"] if t["id"] == id_fnb), None)

        if not fnb:
                print(Fore.LIGHTRED_EX + "Fnb dengan ID tersebut tidak ditemukan.")
                input(Fore.LIGHTBLUE_EX + "\nTekan Enter untuk kembali.")
                cls()
                return
        while True:
            print(Fore.CYAN + Style.BRIGHT+"="*60)
            print(Fore.CYAN + Style.BRIGHT+"||"+"Hapus fnb".center(56)+"||")
            print(Fore.CYAN + Style.BRIGHT+"="*60)
            print()
            print(Fore.BLUE +"1."+ Fore.GREEN + Style.BRIGHT + " Yes")
            print(Fore.BLUE +"2."+ Fore.GREEN + Style.BRIGHT + " No")
            menghapus = input(Fore.LIGHTBLUE_EX+">> Masukkan pilihan (pilih 0 untuk kembali): ")
            try:
                match menghapus:
                    case "0":
                        os.system('cls')
                        return
                    case "1":
                        database["fnb"].remove(fnb)
                        save(database)
                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                        print(Fore.CYAN + Style.BRIGHT+f"Fnb dengan ID {id_fnb} berhasil dihapus".center(56))
                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                        print()             
                        input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                        cls()
                        return

                    case "2":
                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                        print(Fore.CYAN + Style.BRIGHT+"Anda batal menghapus")
                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                        print()             
                        input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                        cls()
                        return

            except ValueError:
                print(Fore.LIGHTRED_EX + "Input salah")
                input(Fore.LIGHTBLUE_EX + "\nTekan Enter untuk mencoba lagi") 
                cls()

    elif pilih_hapus == "3":
        print(Fore.CYAN + Style.BRIGHT+"="*60)
        print(Fore.CYAN + Style.BRIGHT+"||"+"Hapus Film".center(56)+"||")
        print(Fore.CYAN + Style.BRIGHT+"="*60)
        print(Fore.CYAN + Style.BRIGHT + "||"+"Daftar Film".center(56)+"||")
        print(Fore.CYAN + Style.BRIGHT + "="*60)
        print(Fore.WHITE + "-" * 50)
        if not database['films']:
            print(Fore.LIGHTYELLOW_EX + "Tidak ada database film\n")
        else:
            for data in database['films']:
                print(Fore.LIGHTWHITE_EX + f"  ID     : {data['id']}")
                print(Fore.LIGHTWHITE_EX + f"  Nama   : {data['name']}")
                print(Fore.LIGHTWHITE_EX + f"  Genre  : {', '.join(data['genre'])}")
                print(Fore.LIGHTWHITE_EX + f"  Rating : {data['filmRating']}")
                print(Fore.WHITE + "-" * 50)
        try:
            id_film = int(input(Fore.LIGHTBLUE_EX+">> Masukkan ID film: "))  
            cls()
        except ValueError:
            print(Fore.LIGHTRED_EX + "Input harus berupa angka.")
            input(Fore.LIGHTBLUE_EX + "\nTekan Enter untuk kembali.")
            cls()
            return
        film = next((t for t in database["films"] if t["id"] == id_film), None)  

        if not film:
                print(Fore.LIGHTRED_EX + "Film dengan ID tersebut tidak ditemukan.")
                input(Fore.LIGHTBLUE_EX + "\nTekan Enter untuk kembali.")
                cls()
                return
        while True:
            print(Fore.CYAN + Style.BRIGHT+"="*60)
            print(Fore.CYAN + Style.BRIGHT+"||"+"Hapus Film".center(56)+"||")
            print(Fore.CYAN + Style.BRIGHT+"="*60)
            print()
            print(Fore.BLUE +"1."+ Fore.GREEN + Style.BRIGHT + " Yes")
            print(Fore.BLUE +"2."+ Fore.GREEN + Style.BRIGHT + " No")
            menghapus = input(Fore.LIGHTBLUE_EX+"> Masukkan pilihan (pilih 0 untuk kembali): ")

            try:
                match menghapus:
                    case "0":
                        os.system('cls')
                        return
                    case "1":
                        database["films"].remove(film) 
                        save(database)
                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                        print(Fore.CYAN + Style.BRIGHT+f"Film dengan ID {id_film} berhasil dihapus".center(56))
                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                        print()             
                        input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                        cls()
                        return

                    case "2":
                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                        print(Fore.CYAN + Style.BRIGHT+"Anda batal menghapus".center(56))
                        print(Fore.CYAN + Style.BRIGHT+"="*60)
                        print()             
                        input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
                        cls()
                        return

            except ValueError:
                print(Fore.LIGHTRED_EX + "Input salah")
                input(Fore.LIGHTBLUE_EX + "\nTekan Enter untuk mencoba lagi")
                cls()

    else:
        print(Fore.LIGHTBLUE_EX+"Tidak ada dalam pilihan")
        input(Fore.LIGHTBLUE_EX+"\nSilahkan tekan enter untuk kembali")
        cls()

# --------------------------------------------------> PROGRAM < --------------------------------------------------
cls()
while True:
    level, masuk, username = menuawal()
    masuk = 2

    while masuk == 2 and level == "user":
        kamus()
        inputmenu = menuuser().strip()
        cls()
            
        match inputmenu:
            case "1":
                menutiket(username, 3)
            case "2":
                menumakanan()
            case "3":
                menutopup()
            case "4":
                for database in database['users']:
                    if username == database['username']:
                        print(Fore.LIGHTGREEN_EX + f"Saldo Anda adalah Rp.{database['balance']}\n")
                input(Fore.LIGHTBLUE_EX + ">> Klik enter untuk kembali ke halaman utama\n")
                cls()
            case "5":
                menuhistorymakanan()
            case "6":
                menuhistorytiket()
            case "7":
                menukomentar(username)
            case "8":
                break
            case "9":
                print(Fore.LIGHTGREEN_EX + "Terima kasih! Program selesai.")
                quit()
            case "":
                continue
            case _:
                print(Fore.LIGHTYELLOW_EX + "Pilihan tidak tersedia.\n")

    while masuk == 2 and level == "admin":
        kamus()
        inputmenu = menuadmin().strip()
        cls()
        match inputmenu:
            case "1":
                lihatadmin()
            case "2":
                tambahadmin(username)
            case "3":
                edit()
            case "4":
                hapus()
            case "5":
                break
            case "6":
                print(Fore.LIGHTGREEN_EX + "Terima kasih! Program selesai.")
                quit()
            case "":
                continue
            case _:
                print(Fore.LIGHTYELLOW_EX + "Pilihan tidak tersedia.\n")
