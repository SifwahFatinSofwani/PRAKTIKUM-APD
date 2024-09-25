# Masukkan input tinggi badan dan berat badan dan konversikan

print("Selamat datang di program menghitum BMI")
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

# Mengkategorikan jenis berat badan sesuai BMI

if bmi < 18.5:
    print("""﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒
          Berat badan anda bedasarkan BMI adalah kurang
﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒""")
elif bmi < 24.9:
    print("""﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒
          Berat badan anda bedasarkan BMI adalah normal
﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒""")
elif bmi < 29.9:
    print("""﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒
          Berat badan anda bedasarkan BMI adalah berlebih
﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒""")
else:
    print("""﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒
          Berat badan anda bedasarkan BMI adalah obesitas
﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒﹒⪩⪨﹒""")
