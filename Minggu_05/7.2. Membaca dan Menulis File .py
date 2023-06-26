'''open()mengembalikan objek file , 
dan paling sering digunakan dengan 
dua argumen posisi dan satu argumen 
kata kunci: open(filename, mode, 
encoding=None)'''
f = open('workfile', 'w', encoding="utf-8")

'''Menggunakan withjuga jauh lebih pendek
 daripada menulis yang setara try- finallyblok:'''

 with open('workfile', encoding="utf-8") as f:
    read_data = f.read()

# We can check that the file has been automatically closed.
f.closed

'''Setelah objek file ditutup,
 baik dengan withpernyataan atau 
 dengan memanggil f.close(), 
 upaya untuk menggunakan objek
  file akan gagal secara otomatis.
'''
f.close()
f.read()

