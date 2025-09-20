val,bogar,andros= "lamborgini","ferari","Mclaren" # multiple variabel & value
print(f"{val}\n{bogar}\n{andros}")

# multiple variabel one value
data1 = data2 = data3 = "Data setting"
print(data1)
print(data2)
print(data3) # nilainya tetap sama Walaupun dipanggil variabel name berbedas


# Unpack collection
hardware = ["Harddisk","Ram","Processor"] # data set collection utuh
h1,h2,h3 = hardware # kita unpacking data collection ke setiap variabel
print(f"Saya ingin menampilkan hardware: {h1}")