import sys
sys.ps1

sys.ps2

sys.ps1 = 'C> '

'''import sys adalah perintah di Python 
untuk mengimpor modul sistem sys. Modul 
sys mengandung beberapa variabel, fungsi, 
dan metode yang memberikan akses ke beberapa 
aspek dari interpreter Python.'''

'''sys.ps1 dan sys.ps2 adalah variabel yang digunakan
 oleh interpreter Python saat bekerja dengan prompt interaktif. 
 sys.ps1 adalah prompt baris pertama dan sys.ps2 adalah prompt untuk 
 setiap baris tambahan ketika Python meminta pengguna untuk menyelesaikan 
 sebuah blok kode. Secara default, sys.ps1 adalah >>> dan sys.ps2 adalah ....'''

 '''Dengan menetapkan sys.ps1 ke 'C> ' di baris ketiga, prompt baris pertama akan 
 berubah dari >>> menjadi C> , tetapi sys.ps2 tetap sama dan akan menampilkan ... untuk 
 setiap baris tambahan.'''

 import sys
sys.path.append('/ufs/guido/lib/python')

'''/ufs/guido/lib/python setelah mencari di direktori standar yang ditentukan oleh sistem. 
Hal ini berguna jika Anda ingin menambahkan direktori khusus Anda sendiri yang berisi modul 
yang ingin Anda gunakan dalam program Python Anda.

Setelah kita menambahkan direktori baru ke sys.path, Python akan mencari modul di direktori tersebut sebelum mencari di direktori lain. Namun, penting untuk diingat bahwa menambahkan direktori ke sys.path tidak selalu disarankan, terutama jika Anda tidak yakin apa yang Anda lakukan.'''