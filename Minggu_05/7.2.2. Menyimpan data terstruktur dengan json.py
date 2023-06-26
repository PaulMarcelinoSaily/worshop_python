'''Jika Anda memiliki objek x, 
Anda dapat melihat representasi 
string JSON dengan baris kode sederhana:'''

import json
x = [1, 'simple', 'list']
json.dumps(x)

'''Varian lain dari dumps()fungsi, 
disebut dump(), cukup membuat serial 
objek menjadi file teks . Jadi jika 
fobjek file teks dibuka untuk menulis,
 kita dapat melakukan ini:'''

 json.dump(x, f)

 '''Untuk mendekode ulang objek, 
 jika ffile biner atau objek file 
 teks yang telah dibuka untuk dibaca:'''

 x = json.load(f)

 