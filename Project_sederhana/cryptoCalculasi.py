print('CALCULATOR CRYPTO PRIBADI\n\n')
higher_price_usdt = float(input("Enter higher price coin : "))
lower_price_usdt = float(input("Enter lower price coin : "))
entry_price_usdt = float(input("Enter entry price : "))
#-------------------------------------------------
one_usdt_price = float(16.400)
higher_price = one_usdt_price * higher_price_usdt
lower_price = one_usdt_price * lower_price_usdt
entry_price = one_usdt_price * entry_price_usdt

per_takeprofit = ((higher_price - entry_price)/entry_price)*100
per_stoplose = ((lower_price - entry_price)/entry_price)*100
# Information 
print(f"Harga tertinggi 1 Hari = Rp.{higher_price:.3f}")
print(f"Harga terendah 1 Hari = Rp.{lower_price:.3f}")
print(f"Harga Masuk market = Rp.{entry_price:.3f}\n\n")
# hasilnya
print(f"Percentase untuk TAKE PROFIT market yaitu : {per_takeprofit:.2f}%")
print(f"Percentase untuk STOP LOSE market yaitu : {per_stoplose:.2f}%")

