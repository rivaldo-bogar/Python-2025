# menggunakan function endswith() ---> untuk mengetahui format atau string akhiran suatu string/file name.
directory1 = "valdo.py" # saya mencoba memberikan data file seperti directory
directory2 = "report.pdf"
directory3 = "monthly.pdf"
user_inp = str(input("format ingin dicari : "))
cover_input = directory1.endswith(user_inp)
print(f'{directory1} formatnya adalah : {cover_input}') # endswith() akan membaca file dari belakang character akhir terlebih dahulu

name_test = "riv\taldo\tbo\tgar" # penjelasan sederhananya,ketika anda sudah meletakan \t dan guanakan expantabs() untuk tambah atau default jarak tabnya diukur menggunakan expandtabs
testing = name_test.expandtabs(10)
print(f'{testing}')