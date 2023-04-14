# saat menjalankan modul Python dengan
python fibo.py <arguments>

#kode dalam modul akan dieksekusi, sama seperti jika kita mengimpornya, tetapi dengan set __name__ke "__main__". Itu artinya dengan menambahkan kode ini di akhir

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

'''Anda dapat menjadikan file tersebut dapat 
digunakan sebagai skrip dan juga sebagai modul
 yang dapat diimpor, karena kode yang mem-parsing 
 baris perintah hanya berjalan jika modul dijalankan 
 sebagai file "utama"'''

 print(python fibo.py 50)

#Jika modul diimpor, kode tidak dijalankan:
import fibo


