'''Ada cara untuk menghapus item dari daftar yang diberikan 
indeksnya alih-alih nilainya: pernyataan del.
Ini berbeda dari pop()metode yang mengembalikan nilai. 
Pernyataan itu deljuga dapat digunakan untuk menghapus 
irisan dari daftar atau menghapus seluruh daftar 
(yang kita lakukan sebelumnya dengan menugaskan daftar kosong ke irisan). 
Misalnya:'''

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

#deljuga dapat digunakan untuk menghapus seluruh variabel:
del a
