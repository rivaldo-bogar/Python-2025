data = "rivaldo bogar"
data_capital = "THE KING OF CRYPTO"

print(f"{data.capitalize()}") # mengubah string character awal menjadi huruf capital
print(f"{data_capital.casefold()}") # memerhatikan bahasa,jadi kalau ada huruf asing dari neagara lain akan diterjemahkan (lower():tidak memerhatikan)


# menggunakan center
print(f"{data_capital.center(70," ")}") # jadi penggunaannya jarak dari kiri dan kanan yaitu 100,lalu di timpan dengan *

# Menghitung jumlah kemunculan kata
data = """Persis empat bulan hingga Natal. Bagaimana kinerja Bitcoin di periode ini? Naik 70% dari waktu yang ada dengan rata-rata kenaikan 44%," ujar Peterson dalam laporannya. Perhitungan ini berpotensi mendorong harga Bitcoin hingga US$160.000 pada akhir 2025, menurut data Cointelegraph Markets Pro dan TradingView.
Baca artikel CNBC Indonesia "Meski Tertekan,Aset Ini Diprediksi Naik Tinggi Akhir Tahun" selengkapnya di sini: https://www.cnbcindonesia.com/market/20250828141401-17-662202/meski-tertekanaset-ini-diprediksi-naik-tinggi-akhir-tahun
Download Apps CNBC Indonesia sekarang https://app.cnbcindonesia.com/"""
convert_tolower = data.lower()
input_search = str(input("Masukan kata : "))
function_filter = convert_tolower.count(input_search)
print(f"sebanyak {function_filter} kali")


