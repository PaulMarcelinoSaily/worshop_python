'''Untuk menggunakan literal string terformat ,
 awali string dengan fatau Fsebelum tanda kutip 
 pembuka atau tanda kutip tiga.'''
year = 2016
event = 'Referendum'
f'Results of the {year} {event}'

'''Metode str.format()string membutuhkan lebih banyak usaha manual.
 Anda masih akan menggunakan {dan }untuk menandai di mana
variabel akan diganti dan dapat memberikan arahan
 pemformatan yang mendetail'''

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
'{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)

'''Fungsi ini str()dimaksudkan untuk mengembalikan 
representasi nilai yang dapat dibaca oleh manusia, 
sementara repr()dimaksudkan untuk menghasilkan 
representasi yang dapat dibaca oleh penafsir 
(atau akan memaksa a SyntaxErrorjika tidak ada 
sintaks yang setara).'''

s = 'Hello, world.'
str(s)

repr(s)

str(1/7)

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)

# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))

