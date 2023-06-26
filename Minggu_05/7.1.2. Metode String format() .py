'''Penggunaan dasar metode ini str.format()terlihat seperti ini:'''
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

'''Tanda kurung dan karakter di dalamnya 
(disebut bidang format) diganti dengan 
objek yang diteruskan ke str.format()metode'''

print('{0} and {1}'.format('spam', 'eggs'))

print('{1} and {0}'.format('spam', 'eggs'))

'''Jika argumen kata kunci digunakan dalam 
str.format()metode, nilainya dirujuk dengan
 menggunakan nama argumen.'''

 print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

'''Argumen posisi dan kata kunci dapat digabungkan secara sewenang-wenang:'''

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))

'''Jika Anda memiliki format string yang sangat 
panjang yang tidak ingin Anda pisahkan, alangkah
 baiknya jika Anda dapat mereferensikan variabel 
 untuk diformat dengan nama, bukan dengan posisi.
 Ini dapat dilakukan hanya dengan meneruskan dict dan menggunakan tanda kurung siku '[]'untuk mengakses kunci.'''

 table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))

'''Ini juga bisa dilakukan dengan mengirimkan tablekamus sebagai argumen kata kunci dengan ** notasi.
'''

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

'''Ini sangat berguna dalam kombinasi dengan fungsi bawaan vars(), yang mengembalikan kamus yang berisi semua variabel lokal.
'''
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))





