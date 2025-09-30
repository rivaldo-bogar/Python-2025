text = ['registration text','pola editor text']
print(f"{text[1]}")
data1 = [23,22,11,34,12,34,22]
data2 = [True,False,False,True]
data3 = ["python","C++","C#","kotlin"]
data4 = ["python",True,23,33+2]
# Akan bertype data list walaupun isinya berbeda
print("{} type is : {}".format(data1,type(data1)))
print("{} type is : {}".format(data2,type(data2)))
print("{} type is : {}".format(data3,type(data3)))

# test tampilkan data type campur di list data4
print("{} type is : {}".format(data4,type(data4))) # tetap tipe list

# dibawah ini saya coba print spesifik type
print(f"index 1 type data4 = {data4[2]} --type is--{type(data4[1])}") # jika saya call index spesifik akan memunculkan data typenya