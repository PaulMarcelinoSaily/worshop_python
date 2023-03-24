'''Ekspresi awal dalam pemahaman daftar dapat berupa sembarang ekspresi,
 termasuk pemahaman daftar lainnya.'''
# contoh matriks 3x4 berikut yang diimplementasikan sebagai daftar 3 daftar dengan panjang 4:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

#daftar berikut akan mengubah posisi baris dan kolom:
print([[row[i] for row in matrix] for i in range(4)])

#Seperti yang kita lihat di bagian sebelumnya, 
#pemahaman daftar dalam dievaluasi dalam konteks yang formengikutinya, 
# jadi contoh ini setara dengan:
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)

#yang, pada gilirannya, sama dengan:
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

# Di dunia nyata, Anda harus memilih fungsi bawaan daripada pernyataan 
# alur yang rumit. Fungsi ini zip()akan bekerja dengan baik untuk kasus 
# penggunaan ini:

print(list(zip(*matrix)))
