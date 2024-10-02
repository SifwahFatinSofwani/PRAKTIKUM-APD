    # Masukkan username dan password yang ingin dijadikan syarat agar login berhasil

username = "SIFWAH FATIN SOFWANI"
password = "72"

salah = 1

while salah <= 3:
    # Memilih ingin login atau tidak
    loginatautidak = input("jawab dalam bentuk ya atau tidak \napakah anda ingin login atau tidak : ")
    if loginatautidak == "tidak":
        break
    # Memasukkan username dan password yang benar agar login berhasil
    else:
        usernamelogin = input("masukkan nama anda dalam bentuk kapital dari awal hingga akhir \nmasukkan username anda : ")
        passwordlogin = input("masukkan password : ")
        if usernamelogin == username and password == passwordlogin:

            print("login berhasil")
            print("selamat datang di program menghitung bmi : ")

            # Masukkan input tinggi badan dan berat badan dan konversikan
            tinggibadan = float(input("Masukkan tinggi badan anda \nContoh untuk 178 cm = 0.00178 \nMasukkan tinggi anda dalam km : "))
            beratbadan = float(input("Masukkan berat badan anda \nContoh 58 kg = 58000000 \nMasukkan berat badan anda dalam mg :"))
            print(f"Tinggi badan yang anda masukkan : {tinggibadan}")
            print(f"Berat badan yang anda masukkan : {beratbadan}")

            tinggibadanm = tinggibadan * 1000
            beratbadankg = beratbadan / 1000000
            print(f"Hasil konversi berat badan ke kg adalah {beratbadankg:.2f}")
            print(f"Hasil konversi tinggi badan ke m adalah {tinggibadanm:.2f}")

            # Menghitung BMI
            bmi = beratbadankg / tinggibadanm ** 2
            print(f"BMI yang anda dapat adalah {bmi:.2f}")
            
            
            # Mengklasifikasikan jenis berat badan bedasarkan BMI
            if bmi < 18.5:
                print("""﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒
            Berat badan anda bedasarkan BMI adalah kurang
﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒""")
                break
            elif bmi < 24.9:
                print("""﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒
            Berat badan anda bedasarkan BMI adalah normal
﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒""")
                break
            elif bmi < 29.9:
                print("""﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒
            Berat badan anda bedasarkan BMI adalah berlebih
﹒ ⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒""")
                break
            else:
                print("""﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒
            Berat badan anda bedasarkan BMI adalah obesitas
﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒""")
                break
        else:
            print("login gagal \nanda salah dalam username atau password")
            print(f"anda sudah salah sebanyak {salah} kali")
        salah+=1
if loginatautidak == "tidak" or salah == 3:
    print("anda telah salah sebanyak 3 kali atau anda telah memilih untuk tidak melanjutkan login")
else:
    print("program selesai")