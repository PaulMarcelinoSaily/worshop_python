'''Literal string terformat (disingkat juga disebut f-string)
 memungkinkan Anda menyertakan nilai ekspresi Python di dalam 
 string dengan mengawali string denganforFdan menulis ekspresi 
 sebagai {expression}.'''

 import math
print(f'The value of pi is approximately {math.pi:.3f}.')

'''Melewati bilangan ':'bulat setelah akan menyebabkan
 bidang itu menjadi jumlah minimum karakter. Ini berguna 
 untuk membuat kolom berbaris.'''

 table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

'''Pengubah lain dapat digunakan untuk mengonversi
 nilai sebelum diformat. '!a'berlaku ascii(), 
 '!s'menerapkan str(), dan '!r' menerapkan repr():'''

 animals = 'eels'
print(f'My hovercraft is full of {animals}.')

print(f'My hovercraft is full of {animals!r}.')

'''Penspesifikasi =dapat digunakan untuk memperluas 
ekspresi ke teks ekspresi, tanda sama dengan, lalu 
representasi ekspresi yang dievaluasi:'''

bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')