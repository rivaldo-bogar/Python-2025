# Penggunaan format untuk penampilkan nilai dengan cara berbeda

data1 = "burger"
data2 = "pizza"
data3 = "hot dog"
bitcoin = 23.04344
print("hari ini saya ingin makan {}, besoknya {}, dan lusanya {}".format(data1,data2,data3))

# bisa juga berdasarkan index posisi
print("Di manado terdapat {1}, dan dibagian kawasan pada mobil berjalan ada {2}".format(data1,data2,data3))# berdasarkan index
# kalau dilihat pada format belakang hitaungan variabelnya berawal dari = 0,1,2 <...itu sudah 3 variabel


# berikut juga bisa berdasarkan keyboard,semacam diberikan alias
print("Apakah kamu tahu membuat {piz} atau lebih mudah {bur}".format(piz=data2,bur=data1))
# jika dilihat dari code ini saya membuat alias pada format dan memanggil pada pada setiap kurung kurawal.

# Pengformatan pada nilai
# jadi casenya ini saya akan menetukan angka decimal belakang koma
print("saya memiliki sejumlah {:.2f} bitcoin".format(bitcoin)) # disini saya set hanya mengambil 2 angka belakang koma