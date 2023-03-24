#4.3. Fungsi range()
"""Jika Anda perlu mengulangi urutan angka, 
fungsi bawaan range()akan berguna. Ini menghasilkan progresi aritmatika:"""

for i in range(5):
    print(i)

print('**************************')

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
