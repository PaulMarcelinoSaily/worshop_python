# Modul bilangan Fibonacci

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# masukkan juru bahasa Python dan impor modul ini dengan perintah berikut:
import fibo

# Menggunakan nama modul Anda dapat mengakses fungsi:

print(fibo.fib(1000))
print(fibo.fib2(100))
print(fibo.__name__)

# contoh menetapkannya ke nama lokal:
fib = fibo.fib
 print(fib(500))
