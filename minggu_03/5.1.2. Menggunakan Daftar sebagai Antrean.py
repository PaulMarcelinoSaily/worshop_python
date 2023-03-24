#5.1.2. Menggunakan Daftar sebagai Antrean

'''Untuk mengimplementasikan antrean, gunakan collections.dequewhich 
dirancang untuk menambahkan dan muncul dengan cepat dari kedua ujungnya. Misalnya:'''

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           
queue.append("Graham")          
print(queue.popleft())                
print(queue.popleft())              

print(queue)                            

