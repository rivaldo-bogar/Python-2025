# Topic access list part 2
fruit_name = ['Apel','Mangga','Pepaya','Semangka']
print("{} makanan kesukaan".format(fruit_name[0]))
print("{} Index mundur dengan value minus".format(fruit_name[-3]))

alt_coin = ['Etherium', 'Binance', 'Polkadot', 'Cardano', 'Solana', 'Avax', 'Xrp', 'Stellar']

print(f"{alt_coin[:4]}")# INDEX AWAL/0 TO 3, BATAS 4
print(f"{alt_coin[1:4]}")# INDEX 1 TO 3 SHOW 4 SEBAGAI BATAS
print(f"{alt_coin[5:]}") # INDEX 5 TO END
print("\n\n")
print(f"{alt_coin[-6:-2]}") 
# cara bacanya, awal index belakang hitungan dari minus berapa sampai ke minus berapa dari hitungan belakang
con_coin = 0
# contoh menggunakan if statemen
for con_coin in range(8):
    lower_convert = alt_coin[con_coin].lower()
    print('Debuging coin : {}',format(alt_coin[con_coin]))
    con_coin += 1
    # saya conversi dulu sehingga tidak ada terjadi error karena sensitive case

search_coin = input("name coin : \t")


if search_coin in alt_coin:
    print("coin anda tersedia ---> {}".format(search_coin))
else:
    print("Maaf coin tersebut tidak tersedia")