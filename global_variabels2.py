nilx = "valdo" # saya mencoba conversi variabel dari global ke local dan ke global ternyat bisa
def controller():
    global nilx # walaupun variabel dalam function tetap bisa panggil secara global,karena sudah menggunakan function global
    nilx =  "AUTOMATICAL"
    print("Category : ", nilx)

controller()

print(f"Global akses : {nilx}")# jika di coba nilainya bisa diakses
    