mytext = "    Rivaldo Bogar"
data = """Token turun lebih dari 3% di bawah $ 112,000 pada hari Senin tetapi kemudian memangkas beberapa kerugian. Data dari Coinglass menunjukkan sekitar $1,5 miliar posisi long di seluruh mata uang kripto dilikuidasi pada hari Senin, pencairan terbesar dalam satu hari dalam beberapa bulan."""

print(f"Convert to upper case {mytext.upper()}")
print(f"Convert to lower case {mytext.lower()}")
print(f"Convert to delete space start character {mytext.strip()}") # menghapus space di awal kata atau character / coba run agar terlihat
print(f"Convert to replace character  {mytext.replace("R","B")}") # jadi replace character--formatnya : "chracter awal","character pengganti"

# pemisah kata menggunakan split
print(f"Convert to lower case {data.split(" ")}") # untuk sebagai pemisah kata,contohnya saya yaitu space " " <--jadi akant terpisah jika ada space
# berguna jika ingin membuat typelist,sangat berguna