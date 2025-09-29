# Contoh penggunaan boolean example
print(10>5)# True -- output prediksi
print(10 == 2)# False -- output prediksi
print(10 < 2)# False -- output prediksi

uang_dompet = float(200)
tiket_bioskop = float(90)
if uang_dompet >= tiket_bioskop:
    print(f"Selamat menonton,sisa saldo anda = {uang_dompet-tiket_bioskop:.3f}")
else:
    print(f"Maaf uang anda tidak mencukupi")


# testing casting boolean
print(f"\n\n")
print(f"Hasil Boolean : {bool("Hello")}\nHasil Boolean : {bool(0    )}") # akan selalu True jika terdapat nilai 1 ke atas,kalau 0 false

# percobaan lain 
call_this = bool(["mouse","monitor","Cpu","Keyboard"])
print(call_this) # sudah saya coba panggil akan bernilai true,kecuali list kosong,jika ada tanda kutip dua dan tidak ada string tetap True karena terhitung ada nilai kosong..ingat kosong bukan 0

# Beberapa False value wajib diketahui

type2 = bool(None)
type4 = bool(0)
type5 = bool([])
type6 = bool({})
type7 = bool(())
making_list = [bool(False),bool(""),bool(0),bool([]),bool({}),bool(())] # beberapa contoh untuk booleans dengan nilai false semua
print("\n\n baris baru : ")

for x in range(5):
    x +=0
    print(f"\n Boolean result type{x} = {making_list[x]}")
    
