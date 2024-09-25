print ("Selamat datang di program untuk menghitung diskon barang ")
Nama_barang = input("Masukkan nama barang: ")
Harga_barang = float(input("Masukkan harga barang: "))
Jumlah_barang = int(input("Masukkan jumlah barang: "))
Diskon = float(input(" Masukkan Diskon sesuai dengan NIM: "))
print (f"selamat anda mendapatkan diskon {Diskon}% sesuai dengan NIM anda yaitu {Diskon} ")

Totalhargasebelumdiskon = Harga_barang * Jumlah_barang
Totaldiskon = (Diskon/100) * Totalhargasebelumdiskon
Totalhargasetelahdiskon = Totalhargasebelumdiskon - Totaldiskon
Sisabagidiskon = Diskon % 3

print (f"Anda membeli sebuah {Nama_barang} dengan total sejumlah {Jumlah_barang} total harga sebelum diskon adalah Rp{Totalhargasebelumdiskon} lalu anda mendapat total diskon yang anda dapat adalah Rp{Totaldiskon}\nanda mendapatkan total harga setelah diskon sebesar Rp{Totalhargasetelahdiskon} \n {Diskon} dibagi dengan 3 sisanya adalah {Sisabagidiskon}")
