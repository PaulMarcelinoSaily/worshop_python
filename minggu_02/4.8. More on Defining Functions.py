def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
print('****************************************')

i = 5

def f(arg=i):
    print(arg)

i = 6
f()

print('****************************************')

#4.8.2. Argumen Kata Kunci

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

print('****************************************')

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print('****************************************')

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

print('****************************************')

parrot(1000)                                          # 1 argumen posisional
parrot(voltage=1000)                                  # 1 argumen kata kunci
parrot(voltage=1000000, action='VOOOOOM')             # 2 argumen kata kunci
parrot(action='VOOOOOM', voltage=1000000)             # 2 argumen kata kunci
parrot('a million', 'bereft of life', 'jump')         # 3 argumen posisional
parrot('a thousand', state='pushing up the daisies')

print('****************************************')

parrot()                     # argumen yang diperlukan hilang
parrot(voltage=5.0, 'dead')  # argumen non-kata kunci setelah argumen kata kunci
parrot(110, voltage=220)     # duplikat nilai untuk argumen yang sama
parrot(actor='John Cleese')  # argumen kata kunci yang tidak diketahui

print('****************************************')

def function(a):
    pass

function(0, a=0)

print('****************************************')

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

print('****************************************')

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

print('****************************************')

print('****************************************')

#4.8.3. Parameter khusus

"""perlu melihat definisi fungsi untuk menentukan apakah item diteruskan oleh posisi, posisi atau kata kunci, atau kata kunci.

Definisi fungsi mungkin terlihat seperti:"""

""" def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only """

#4.8.3.1. Argumen Posisi atau Kata Kunci
"""Jika /dan *tidak ada dalam definisi fungsi, argumen dapat diteruskan ke fungsi berdasarkan posisi atau kata kunci."""

#4.8.3.2. Parameter Hanya-Posisi 
"""Parameter khusus posisi ditempatkan sebelum /(garis miring). The /digunakan untuk secara logis memisahkan parameter hanya posisional dari parameter lainnya. Jika tidak ada /dalam definisi fungsi, tidak ada parameter hanya posisi.
Parameter yang mengikuti /mungkin berupa posisi-atau-kata kunci atau kata kunci saja ."""

#4.8.3.3. Argumen Kata Kunci Saja

"""Untuk menandai parameter sebagai hanya kata kunci ,
 yang menunjukkan bahwa parameter harus diteruskan oleh argumen kata kunci, tempatkan an *di daftar argumen tepat sebelum parameter khusus kata kunci pertama """

#4.8.3.4. Contoh Fungsi 

def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

""" fungsi pertama, standard_arg, bentuk yang paling umum, tidak membatasi konvensi pemanggilan dan argumen dapat diteruskan oleh posisi atau kata kunci:"""

standard_arg(2)


standard_arg(arg=2)

"""Fungsi kedua pos_only_argdibatasi untuk hanya menggunakan parameter posisi seperti yang ada /dalam definisi fungsi:"""
pos_only_arg(1)


pos_only_arg(arg=1)

"""Fungsi ketiga kwd_only_argshanya mengizinkan argumen kata kunci seperti yang ditunjukkan oleh a *dalam definisi fungsi:"""
kwd_only_arg(3)



kwd_only_arg(arg=3)

"""Dan yang terakhir menggunakan ketiga konvensi pemanggilan dalam definisi fungsi yang sama:"""

combined_example(1, 2, 3)



combined_example(1, 2, kwd_only=3)


combined_example(1, standard=2, kwd_only=3)


combined_example(pos_only=1, standard=2, kwd_only=3)

"""pertimbangkan definisi fungsi ini yang memiliki potensi benturan antara argumen posisi name dan **kwdsyang memiliki namekunci:"""

def foo(name, **kwds):
    return 'name' in kwds

"""Tidak ada kemungkinan panggilan yang membuatnya kembali Truekarena kata kunci 'name' akan selalu mengikat ke parameter pertama. Misalnya:"""
foo(1, **{'name': 2})

"""menggunakan /(argumen hanya posisi), itu dimungkinkan karena memungkinkan namesebagai argumen posisi dan 'name'sebagai kunci dalam argumen kata kunci:"""

def foo(name, /, **kwds):
    return 'name' in kwds

foo(1, **{'name': 2})

#4.8.3.5. Rekap

"""menentukan parameter mana yang akan digunakan dalam definisi fungsi:"""
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

#4.8.4. Daftar Argumen Sewenang-wenang 
""" menentukan bahwa suatu fungsi dapat dipanggil dengan jumlah argumen 
yang berubah-ubah. Argumen ini akan dibungkus dalam sebuah tuple (lihat Tuples and Sequences). 
Sebelum jumlah argumen variabel, nol atau lebih argumen normal dapat terjadi. """

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

"""argumen variadik ini akan menjadi yang terakhir dalam daftar parameter formal,
 karena mereka meraup semua argumen masukan yang tersisa yang diteruskan ke fungsi. 
 Parameter formal apa pun yang muncul setelah *args parameter adalah argumen 'kata kunci saja'"""

def concat(*args, sep="/"):
    return sep.join(args)

concat("earth", "mars", "venus")

concat("earth", "mars", "venus", sep=".")

#4.8.5. Membongkar Daftar Argumen\
"""fungsi bawaan range()mengharapkan argumen start dan stop yang terpisah. 
Jika tidak tersedia secara terpisah, tulis pemanggilan fungsi dengan -operator 
*untuk membongkar argumen dari daftar atau tupel:"""

list(range(3, 6))            # panggilan normal dengan argumen terpisah

args = [3, 6]
list(range(*args))            # panggilan dengan argumen yang dibongkar dari daftar

"""mengirimkan argumen kata kunci dengan -operator **:"""

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

#4.8.6. Ekspresi Lambda
"""Fungsi ini mengembalikan jumlah dari dua argumennya: 
fungsi lambda dapat mereferensikan variabel dari cakupan yang memuat:lambda a, b: a+b"""

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)

f(1)

"""Contoh di atas menggunakan ekspresi lambda untuk mengembalikan fungsi. 
Kegunaan lain adalah untuk melewatkan fungsi kecil sebagai argumen:"""

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

#4.8.7. String Dokumentasi

"""Berikut adalah contoh docstring multi-baris:"""

def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)

#4.8.8. Anotasi Fungsi 

"""Anotasi fungsi adalah informasi metadata yang sepenuhnya opsional tentang jenis yang digunakan oleh fungsi yang ditentukan pengguna
Contoh berikut memiliki argumen yang diperlukan, argumen opsional, dan nilai pengembalian yang dianotasi:"""

def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')

