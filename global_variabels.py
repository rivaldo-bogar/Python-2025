global_var = "Mission complete" # Global variabel

def text_win():
    print(f"Hello rivaldo you'r {global_var}")

text_win() # call function

to_convert = "valdo" # bisa dipanggil dalam function dan diluar function

def call_name():
    to_convert = "bogar" # ketika anda memanggil variabel ini diluar function tidak akan berfungsi
    print("Hello my name " + to_convert)
# Convert global to local variabel

call_name()
print("nama belakang saya adalah " + to_convert) # ketika saya mencoba panggil,dia akan otomatis memanggil variabel diluar function