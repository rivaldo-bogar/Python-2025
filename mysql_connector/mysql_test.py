import mysql.connector

# detail koneksi atau ingin diintegrasikan
my_connector = {
    'host':'localhost',
    'user':'root',
    'password':'root',
    'database':'account' # jika ingin pada database spesifik silahkan saya deklarasi,tapi jika ingin membuat baru jangan di deklarasi

   
}
# buat koneksi
try:
    connecting = mysql.connector.connect(**my_connector)
    # pengecekan apakah mysql terkoneksi

    if connecting.is_connected():
        print(f"anda sudah terkoneksi...")
        # pembuatan cursor() untuk menjalankan eksekusi query database
        kursor = connecting.cursor()




        # pastikan selalu menutup koneksi
        connecting.close()
        kursor.close()
except mysql.connector.Error as err:
    print(f"Maaf anda tidak bisa terhubung : {err}")
    