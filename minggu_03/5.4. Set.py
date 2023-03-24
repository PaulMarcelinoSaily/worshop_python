'''Kurung kurawal atau set()fungsi dapat digunakan untuk membuat 
himpunan. Catatan: untuk membuat himpunan kosong Anda harus 
menggunakan set(), bukan {}; yang terakhir membuat kamus kosong, 
struktur data yang akan kita bahas di bagian selanjutnya.'''

#Berikut demonstrasi singkatnya:
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # menunjukkan bahwa duplikat telah dihapus
print('orange' in basket)             # pengujian keanggotaan cepat

print('crabgrass' in basket)


# Peragakan operasi set pada huruf unik dari dua kata

a = set('abracadabra')
b = set('alacazam')
print(a)                                  
print(a - b)                             

print(a | b)                              

print(a & b)                             

print(a ^ b)                            

#Sama halnya dengan pemahaman daftar , pemahaman set juga didukung:
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

