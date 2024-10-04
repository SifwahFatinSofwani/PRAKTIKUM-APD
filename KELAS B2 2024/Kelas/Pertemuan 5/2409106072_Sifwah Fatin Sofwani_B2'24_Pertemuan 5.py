# list = ["a", 2, True,[1,2,3]]

# print(list[-1][2])

# dalam list bisa ditaruh list lagi

# list = ["a", 
#         2, 
#         True,
#         [1,2,3]]

# print (list)

# tas = ["buku", 32, True, 3.14, ["IF", 24]]
# for i in tas:
#     print(i)
# print(len(tas))

# for i in range(len(tas)):
#     print(tas[i])
  
matkul = ["kalkulus", "fisdas", "pti"]
# print(matkul)

# nambahin variable

# # matkul.append("sastra mesin")
# # print(matkul)
# matkul.insert(1, "test")
# print(matkul)

# mengubah variable

# matkul[1] = "fisika quantum"
# print(matkul)


# menghapus data di list

# del matkul[2]
# print(matkul)

# buang = matkul.pop(1)
# print(matkul)

# print(f"variable buangan = {buang}")

# prodi = ["it", "si", "arsi", "lingkunga", "tambang", "elektro", "industri", "sipil", "geo", "kimia"]

# untuk menentukan jaraknya sorang
# print(prodi[1:8:2])

# untuk jarak 1
# print(prodi[::2],"\n")

# meta = ["dyrot", "miya"]
# nonmeta = ["kalkulus", "kocak"]

# semua = meta + nonmeta
# print(semua)

# barang = [["sepatu", "tas", "baju"],["pulpen", "pensil", "laptop"]]
# # print(barang[1])
# for i in barang:
#     for j in i:
#         print(j)


# perabotan = []
# print(perabotan)

# perabotan.append("meja")
# print(perabotan)

# tupple tidak bisa ditambah data apapun

# barang = ["sepatu", "tas", "baju"]
# barang2 = ["pulpen", "pensil", "laptop"]
# barangtotal = [barang, barang2]
# print(barangtotal)

mahasiswa = (69, "Informatika", "2209106044", "Aldy septian ")
print(mahasiswa)
mahasiswa = list(mahasiswa)
mahasiswa[2] = "2409106072"
print(mahasiswa)
# absen, prodi = mahasiswa

# print(absen)
# print(nama)

# mahasiswa(list)
# mahasiswa.append("kocak")
# print(mahasiswa)

# bikin unpacking tidak boleh lebih