# Data dictionary
new_user = {
    "nama": "Rivaldo Bogar",
    "Hobi" : "Coding python",
    "Umur" : 23,
}
text = "Anak berumum {Umur}, atas nama {nama},memiliki asset bitcoin dengna hobinya yaitu {Hobi}"
cetak_info = text.format_map(new_user)
print(f"\n\n\t{cetak_info}")

# kesimpulannya kegunaanya format_map() untuk memanggil data yang diberikan alias/keyword pada suatu variabel dictionary
# testing code untuk lebih mudah dipahami