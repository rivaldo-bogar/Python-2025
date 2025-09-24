#mencoba menggunakan function not in /= tidak sama dengan atau tidak ada
name = "Rivaldo Bogar"
print(f"Hello my boss {name}")
print(f"pencarian = {"Bogar" not in name}") # Sensitive case diperhatikan

user_input = str(input("masukan nama : "))
if user_input not in name:
    print("belum ada dalam pendataan")
else :
    print("Sepertinya itu sudah ada.")