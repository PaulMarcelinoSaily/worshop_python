'''Berikut tabel kotak dan kubus yang sama, diformat secara manual:'''
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))


'''Ada metode lain, str.zfill(), yang mengisi string numerik 
di sebelah kiri dengan nol. Ia mengerti tentang tanda plus dan minus:'''
'12'.zfill(5)

'-3.14'.zfill(7)

'3.14159265359'.zfill(5)

