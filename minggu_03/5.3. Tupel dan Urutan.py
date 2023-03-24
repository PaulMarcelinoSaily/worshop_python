'''Kami melihat bahwa daftar dan string memiliki banyak properti umum,
 seperti operasi pengindeksan dan pemotongan. Mereka adalah dua contoh 
 tipe data sequence (lihat Tipe Sequence — list, tuple, range ). 
 Karena Python adalah bahasa yang berkembang, tipe data urutan lainnya 
 dapat ditambahkan. Ada juga tipe data urutan standar lainnya: tuple .'''

 #Sebuah tuple terdiri dari sejumlah nilai yang dipisahkan dengan koma, misalnya:
 t = 12345, 54321, 'hello!'
print(t[0])

print(t)

# Tuple mungkin bersarang:
u = t, (1, 2, 3, 4, 5)
print(u)

# Tuple tidak dapat diubah:
print(t[0] = 88888)


# tetapi mereka dapat berisi objek yang bisa berubah:
v = ([1, 2, 3], [3, 2, 1])
print(v)

'''Masalah khusus adalah pembuatan tupel yang berisi 0 atau 1 item:
   sintaks memiliki beberapa keanehan tambahan untuk mengakomodasi ini.
   Tupel kosong dibangun oleh sepasang tanda kurung kosong; 
   tuple dengan satu item dibangun dengan mengikuti nilai dengan koma 
   (tidak cukup untuk menyertakan satu nilai dalam tanda kurung). 
   Jelek, tapi efektif. Misalnya:'''

empty = ()
singleton = 'hello',    # <-- note trailing comma
print(len(empty))

print(len(singleton))

print(singleton)

'''Pernyataan tersebut adalah contoh pengepakan tuple : nilai-nilai , 
dan dikemas bersama dalam sebuah tuple. Operasi sebaliknya juga 
dimungkinkan:t = 12345, 54321, 'hello!'1234554321'hello!''''

x, y, z = t

'''Ini disebut, cukup tepat, membongkar urutan dan berfungsi untuk 
setiap urutan di sisi kanan. Pembongkaran urutan mensyaratkan bahwa ada
 banyak variabel di sisi kiri tanda sama dengan jumlah elemen dalam urutan. '''