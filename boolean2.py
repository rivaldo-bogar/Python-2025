def making_data():
     return True 

print(making_data())# nilainya akan true karena return dikembalikan langsung saya patok ke True

if making_data():
     print("Nilai dihasilkan function Benar")
else :
     print("False value")

# menggunakan instance apakah nilai variabel sudah benar
take_input = input("masukan kata : ")
take_input = 0 # nilai akan false karena sudah pasing disini dengan angka 0,jadi biar di input berapapun
checking = isinstance(take_input,str)
print(f"Hasilnya : {checking}")