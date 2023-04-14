#mengimpor nama dari modul langsung ke ruang nama modul pengimpor.
from fibo import fib, fib2
print(fib(500))

# mengimpor semua nama yang ditentukan modul:
from fibo import 
print(fib(500))

#Jika nama modul diikuti oleh as, maka nama berikut asterikat langsung ke modul yang diimpor.

import fibo as fib
print(fib.fib(500))

#juga dapat digunakan saat menggunakan fromdengan efek serupa:

from fibo import fib as fibonacci
print(fibonacci(500))

