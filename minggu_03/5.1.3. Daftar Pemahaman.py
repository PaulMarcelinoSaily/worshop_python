'''Pemahaman daftar menyediakan cara ringkas untuk membuat daftar. 
Aplikasi umum adalah membuat daftar baru di mana setiap elemen adalah 
hasil dari beberapa operasi yang diterapkan ke setiap anggota urutan
lain atau iterable, atau untuk membuat urutan elemen yang memenuhi kondisi tertentu.'''

#Sebagai contoh, misalkan kita ingin membuat daftar kotak, seperti:

squares = []
for x in range(10):
    squares.append(x**2)

print(squares)

#menghitung daftar kotak tanpa efek samping menggunakan:
squares = list(map(lambda x: x**2, range(10)))

#atau, ekuivalen:
squares = [x**2 for x in range(10)]

'''Daftar pemahaman terdiri dari tanda kurung yang berisi 
ekspresi diikuti oleh forklausa, kemudian nol atau lebih foratau 
if klausa.'''

#Misalnya, listcomp ini menggabungkan elemen dari dua daftar jika tidak sama:
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

#Perhatikan urutan for dan if, Jika ekspresinya adalah sebuah tuple (misalnya pada contoh sebelumnya), maka harus diberi tanda kurung.(x, y)
vec = [-4, -2, 0, 2, 4]
# buat daftar baru dengan nilai dua kali lipat
print([x*2 for x in vec])

# filter daftar untuk mengecualikan angka negatif
print([x for x in vec if x >= 0])

# menerapkan fungsi ke semua elemen
print([abs(x) for x in vec])

# memanggil metode pada setiap elemen
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print([weapon.strip() for weapon in freshfruit])

# buat daftar 2-tupel seperti (angka, persegi)
print([(x, x**2) for x in range(6)])

# tuple harus diberi tanda kurung, jika tidak, kesalahan akan muncul
print([x, x**2 for x in range(6)])

# ratakan daftar menggunakan listcomp dengan dua 'untuk'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

#Daftar pemahaman dapat berisi ekspresi kompleks dan fungsi bersarang:
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])