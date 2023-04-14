''' Python menggunakan caching untuk mempercepat pemuatan modul. 
Setiap modul yang dikompilasi akan di-cache di pycache direktori 
dengan nama yang mengandung versi yang dikodekan. Python memeriksa
tanggal modifikasi sumber terhadap versi yang dikompilasi untuk melihat 
apakah sudah kedaluwarsa dan perlu dikompilasi ulang. Modul yang dikompilasi 
tidak bergantung pada platform, sehingga pustaka yang sama dapat digunakan bersama 
di antara sistem dengan arsitektur yang berbeda.

Ada beberapa tips yang disediakan untuk para ahli, termasuk penggunaan opsi -O atau -OO
untuk mengurangi ukuran modul yang dikompilasi. Modul "Dioptimalkan" memiliki opt-tag dan
biasanya berukuran lebih kecil. Program tidak berjalan lebih cepat saat dibaca dari .pyc file 
daripada saat dibaca dari .py file, dan satu-satunya hal yang lebih cepat tentang .pyc file 
adalah kecepatan pemuatannya.

Terakhir, ada modul compileall yang dapat membuat file .pyc untuk semua modul dalam direktori.
Detail lebih lanjut tentang proses caching dapat ditemukan di PEP 3147.'''