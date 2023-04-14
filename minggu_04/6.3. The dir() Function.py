import fibo, sys
print(dir(fibo))

print(dir(sys))

'''kode import fibo, sys; dir(fibo); 
dir(sys) akan menampilkan dua daftar nama: 
daftar nama-nama yang didefinisikan di dalam 
modul fibo dan daftar nama-nama yang didefinisikan di dalam modul sys.'''

a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
dir()

ertama, variabel a didefinisikan dan diisi dengan daftar angka 1 hingga 5. 
Kemudian, modul fibo diimpor dan variabel fib ditetapkan ke fungsi fib() 
dari modul fibo. Akhirnya, fungsi bawaan dir() dipanggil tanpa argumen, 
sehingga menghasilkan daftar nama-nama yang didefinisikan saat ini di lingkungan 
pemanggilan, termasuk nama-nama dalam modul fibo yang diimpor dan nama-nama bawaan Python.

