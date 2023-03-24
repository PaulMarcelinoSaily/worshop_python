'''Melakukan list(d)di kamus mengembalikan daftar semua kunci 
yang digunakan dalam kamus, dalam urutan penyisipan 
(jika Anda ingin diurutkan, gunakan saja sorted(d)). 
Untuk memeriksa apakah satu kunci ada di kamus, gunakan inkata kunci.'''

#Berikut adalah contoh kecil menggunakan kamus:
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)

print(tel['jack'])

del tel['sape']
tel['irv'] = 4127
print(tel)

print(list(tel))

print(sorted(tel))

print('guido' in tel)

print('jack' not in tel)

#Konstruktor dict()membangun kamus langsung dari urutan pasangan kunci-nilai:
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

#Selain itu, pemahaman dict dapat digunakan untuk membuat kamus dari ekspresi kunci dan nilai arbitrer:
print({x: x**2 for x in (2, 4, 6)})

# Saat kunci berupa string sederhana, 
# terkadang lebih mudah untuk menentukan pasangan menggunakan argumen kata kunci:

print(dict(sape=4139, guido=4127, jack=4098))
