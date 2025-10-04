buah = ['mangga', 'apel', 'alvocado', 'sirsak', 'lemon', 'salak', 'manggis', 'anggur']

buah.append('kenari') #akan otomatis menambahkan pada list paling akhir
print(f"{buah}")

# tambahkan item di list pada index spesifik atau gantikan
# Konsepnya dia akan menggeserkan obj sebelumnya kedepan dan disisipkan,coba running code agar kamu mengerti valdo
buah.insert(1,"mangga fresh")# Perhatikan format function
print(f'list update {buah}')