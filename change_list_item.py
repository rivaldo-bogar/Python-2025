buah = ['mangga', 'apel', 'alvocado', 'sirsak', 'lemon', 'salak', 'manggis', 'anggur']
# Dalam artian disini yang diganti apel ke Backdoor.virus, karena apel berada di index 1
buah[1]="Backdoor.virus"
print(f'berikut daftar buah {buah} dengan  {type(buah)}{len(buah)}')



# akan mengganti dua nilai yang ada pada index 1 dan 2,karena tidak batas..
buah[1:3]=['valdo', 'developer']
print(f'berikut daftar buah {buah} dengan  {type(buah)}{len(buah)}')

# list akan bertambah dikarenakan hapus 1 index ditambhakan/sisipkan 2 new value
buah[1:2]=['valdo', 'index3']
print(f'berikut daftar buah {buah} dengan  {type(buah)}{len(buah)}')

# list akan berkurang dikarenakan dihapus 2 index ditambhakan/sisipkan 1
buah[1:3]=['valdo']
print(f'berikut daftar buah {buah} dengan  {type(buah)} list_jum {len(buah)}')

# coba run valdo biar lebih ngerti