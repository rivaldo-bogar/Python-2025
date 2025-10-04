from pycoingecko import CoinGeckoAPI
import time

#untuk inisialisasi klien
cg = CoinGeckoAPI()

# Contoh jika Anda mengambil data berulang kali
for i in range(100):
    try:
        # Lakukan permintaan API
        harga = cg.get_price(ids='bitcoin', vs_currencies='usd')
        showing = harga['bitcoin']['usd']
        print(f"dataype dari {showing} adalah {type(showing)}")
        print(f"Bitcoin price update checking ID-{i+1}: {harga}")
        
        # WAJIB: Beri jeda sebelum permintaan berikutnya
        time.sleep(15)  # perhatikan ini,suka crash kadang

    except Exception as e:
        print(f"Terjadi error: {e}")
        break