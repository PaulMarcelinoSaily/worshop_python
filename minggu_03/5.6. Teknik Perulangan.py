#Saat mengulang kamus, kunci dan nilai yang sesuai dapat
#diambil pada saat yang sama menggunakan items()metode ini.

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# Saat mengulang urutan, indeks posisi dan nilai terkait dapat
#  diambil pada saat yang sama menggunakan enumerate()fungsi.

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

#Untuk mengulangi dua urutan atau lebih secara bersamaan,
#  entri dapat dipasangkan dengan fungsi zip().

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

#Untuk mengulang urutan secara terbalik, pertama-tama tentukan
#  urutan dalam arah maju dan kemudian panggil fungsinya reversed().

for i in reversed(range(1, 10, 2)):
    print(i)

#Untuk mengulang urutan dalam urutan terurut, gunakan sorted()fungsi 
# yang mengembalikan daftar terurut baru sambil membiarkan sumbernya tidak berubah.

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
    print(i)

#Menggunakan set()urutan menghilangkan elemen duplikat. 
# Penggunaan sorted()dalam kombinasi dengan set()urutan 
# adalah cara idiomatis untuk mengulang elemen unik dari 
# urutan dalam urutan yang diurutkan.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

#Terkadang tergoda untuk mengubah daftar saat Anda mengulanginya; namun, 
# seringkali lebih mudah dan lebih aman untuk membuat daftar baru.

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

