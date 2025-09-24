# untuk pengambil string pada area tertentu
data = "Monokai Pro: Tema ini memiliki skema warna yang cerah dan enak dilihat. Versi gratisnya sudah sangat bagus, tapi ada juga versi berbayar dengan fitur tambahan."

inp1 = int(input("masukan nilai awal : "))
inp2 = int(input("masukan nilai akhir : "))
print(f"Result final : {data[-inp1:-inp2]}") # jika menggunakan minus "-", perhitungan akan dimulai dari belakang string

# catatan tambahan,jika perhitungan dari belakang atau minus,awalnya bukan index 0, tapi 1
# pastikan selalu mengasa logika