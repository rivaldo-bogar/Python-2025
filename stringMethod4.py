# menggunakan function string find()
text = "jangan membeli gold karena kita tidak tahu berapa jumlah inflasi sebernanya dan harus memmerhatikan data yang valid"
input_user = str(input("masukan kata : "))
serching_func = text.find(input_user) # mencari suatu kata ada pada index berapa
print(f'kata yang anda cari di index {serching_func}')