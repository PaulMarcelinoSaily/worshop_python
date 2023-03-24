'''Objek urutan biasanya dapat dibandingkan dengan objek lain dengan
 tipe urutan yang sama. Perbandingannya menggunakan 
 leksikografispengurutan: pertama dua item pertama dibandingkan, 
 dan jika berbeda, ini menentukan hasil perbandingan; jika sama, 
 dua item berikutnya dibandingkan, dan seterusnya, sampai salah 
 satu urutannya habis. '''

 (1, 2, 3)              < (1, 2, 4)
[1, 2, 3]              < [1, 2, 4]
'ABC' < 'C' < 'Pascal' < 'Python'
(1, 2, 3, 4)           < (1, 2, 4)
(1, 2)                 < (1, 2, -1)
(1, 2, 3)             == (1.0, 2.0, 3.0)
(1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

'''Perhatikan bahwa membandingkan objek dari jenis yang berbeda 
dengan <atau >legal asalkan objek tersebut memiliki metode perbandingan
 yang sesuai. Misalnya, tipe numerik campuran dibandingkan berdasarkan
   nilai numeriknya, jadi 0 sama dengan 0,0, dll.'''