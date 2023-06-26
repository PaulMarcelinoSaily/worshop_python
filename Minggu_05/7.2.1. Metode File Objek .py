f.read()

f.read()

'''f.readline()membaca satu baris dari
 file; karakter baris baru ( \n) 
 dibiarkan di akhir string, dan 
 hanya dihilangkan di baris terakhir
  file jika file tidak diakhiri di
   baris baru.'''
f.readline()

f.readline()

f.readline()

'''Untuk membaca baris dari file, Anda dapat 
mengulang objek file. Ini hemat memori, cepat, 
dan mengarah ke kode sederhana:'''

for line in f:
    print(line, end='')

'''f.write(string)menulis konten string ke file,
 mengembalikan jumlah karakter yang ditulis.'''

f.write('This is a test\n')

'''Jenis objek lain perlu dikonversi – baik menjadi string 
(dalam mode teks) atau objek byte (dalam mode biner) – sebelum 
menulisnya:'''
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)

f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')

f.seek(5)      # Go to the 6th byte in the file

f.read(1)

f.seek(-3, 2)  # Go to the 3rd byte before the end

f.read(1)

