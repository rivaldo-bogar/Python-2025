# penggunaan endcode
data = "Rivaldo Bogar"
using_utf_8 = data.encode('utf-8')
using_ascii = data.encode('ascii')
using_latit1 = data.encode('latin1')
print(f"{using_utf_8}")
print(f"{using_ascii}")
print(f"{using_latit1}")

# penjelasan singkatnya encode akan mengubah data dari string menjadi biner,dan data unicode menjadi bytes yang akan dibaca oleh kompter