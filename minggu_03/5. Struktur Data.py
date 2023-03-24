#5.1. Selengkapnya tentang Daftar

'''Tipe data daftar memiliki beberapa metode lagi. Berikut ini semua metode objek daftar:
1. daftar. tambahkan ( x ) 
2. daftar. memperpanjang ( dapat diubah )
3. daftar. sisipkan ( i , x )
4. daftar. hapus ( x )
5. daftar. pop ( [ i ] )
6. daftar. jelas ( )
7. daftar. indeks ( x [ , awal [ , akhir ] ] )
8. daftar. hitung ( x )
9. daftar. urutkan ( * , kunci = Tidak ada , mundur = Salah )
10. daftar. terbalik ( )
11. daftar. salin ( ) '''

#Contoh yang menggunakan sebagian besar metode daftar:

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana', 4)) 

print(fruits.reverse())
print(fruits)

print(fruits.append('grape'))
print(fruits)

print(fruits.sort())
print(fruits)
print(fruits.pop())

