#4.2. forPernyataan
"""pernyataan Python mengulangi item dari urutan apa pun 
(daftar atau fora string), dalam urutan yang muncul dalam urutan. 
Misalnya (tidak ada permainan kata-kata):"""

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategi: Ulangi salinan
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategi: Buat koleksi baru
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status