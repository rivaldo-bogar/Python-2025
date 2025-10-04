buah = ['mangga', 'apel', 'alvocado', 'sirsak', 'lemon', 'salak', 'manggis', 'anggur']
print(f"Total list : {len(buah)}")
buah.remove('apel') # untuk list value apel sudah tidak ada jika dilihat dari print()
x = 0
print(f"Total list : {len(buah)}")
cover_nilai_list = len(buah)
for x in range(cover_nilai_list):
    print(f"cetak buah = {buah[x]} index-{x}")
    x +=1

# Menggunakan function pop(),menghapus spesifik index()
buah.pop(0)
print(f'{buah} jumlah total = {len(buah)}')

#menghapus item paling terakhir dengan pop(),tanpa input index..
buah.pop()
print(f'{buah} jumlah total = {len(buah)}') # anggur hilang

# menghapus item pertama dengan del 
del buah[0]
print(f'{buah} jumlah total = {len(buah)}') # Alvocado dihapus

# menghapus semua content pada list,tapi variabel atau wadah masih tersedia
buah.clear()
print(f'{buah} jumlah total = {len(buah)}') # 0 conten



#-------------------------------------------
# menghapus variabel list dan content
del buah # Sampai variabel langsung undifined,atau tidak dideklarasi

# jika saya call variabel akan ada error,karena undifined sudah saya hapus
#print(f'{buah} jumlah total = {len(buah)}') # Alvocado dihapus
