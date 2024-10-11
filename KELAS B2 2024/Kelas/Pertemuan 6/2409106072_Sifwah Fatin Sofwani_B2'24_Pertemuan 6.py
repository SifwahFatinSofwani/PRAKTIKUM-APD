# daftar_buku = {
# "Buku1" : "Harry Potter",
# "Buku2" : "Percy Jackson",
# "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# printnya tidak boleh menggunakan indeks melainkan menggunakan key
# dictionary bisa diisi dengan kosong dahulu

# daftarbuku = {}
# daftarbuku[1] = "Matahari"
# daftarbuku["novel 1"] = "Senyum pertama di pagi hari airin"

# print(daftarbuku)

# Biodata = {
# "Nama" : "Aldy Ramadhan Syahputra",
# "NIM" : 2109106079,
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" :True,
# "Social Media" : {
# "Instagram" : "@aldyrmdhns_",
# "Discord" : "\'Izanami#6848"
# }
# }

# print(Biodata)

# daftarbuku = dict(Buku1 = "Naruto", Buku2 = "kukirakaurumah")
# print(daftarbuku)

# # mengakses data dictionary ada get dan kurung siku 

# print(daftarbuku.get("Buku2"))

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# Nilai["struktur adata"] = 90
# Nilai.update({"MTL COY" : "200000"})
# Nilai.update({"MTL COY" : "99"})


# print(Nilai)

# hapus = Nilai.pop("Kimia")
# print(Nilai)
# print(hapus)

# del Nilai["MTL COY"]
# print(Nilai)

# Nilai.clear()


# update bisa untuk edit juga


# for i in Nilai:
#     print(i)


# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

# nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# nilai["struktur adata"] = 90
# nilai.update({"MTL COY" : "200000"})
# nilai.update({"MTL COY" : "99"})

# # print(f"jumlah matpel yang ada adalah {len(Nilai)}")

# # for i in Nilai:
# #     print(i)

# Nilaisifwah = nilai.copy()
# print(Nilaisifwah)

# key = "naga", "binatang", "mitologi"
# value = 99
# datanaga = dict.fromkeys(key, value)

# print(datanaga)

# nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }
# nilai["struktur adata"] = 90
# nilai.update({"MTL COY" : "200000"})
# nilai.update({"MTL COY" : "99"})

# for i in nilai.values():
#     print(i)



    


# bisa menggunakan fungsi key atau value agar jikahanya value or key yang ingin anda print

# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# # mengakses value dan key dari dictionary
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#         print("")

mahasiswa = {
101 : {"Nama" : "Aldy", "Umur" : 19},
111 : {"Nama" : "Abdul", "Umur" : 18, "Hobi" : ["Membaca", "KOding "]}
}
# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)
#     for key_a, value_a in value.items():
#         print (key_a, " : ", value_a)
#         print("")


print(mahasiswa[111]["Umur"])


