#4.7. Mendefinisikan Fungsi
"""membuat fungsi yang menulis deret Fibonacci ke batas arbitrer:"""
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

print(fib(2000))

print('*************************************')

fib
f = fib
f(100)

print('*************************************')

fib(0)
print(fib(0))

print('*************************************')

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)
f100 