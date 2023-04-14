'''Pernyataan "from sound.effects import *" mengimpor semua modul dalam subpak sound.effects. 
Namun, ini mungkin tidak efisien karena bisa memakan waktu dan memiliki efek samping yang tidak diinginkan. 
Solusinya adalah dengan menggunakan indeks eksplisit yang didefinisikan dalam kode paket init.py. 
Jika init.pymendefinisikan sebuah daftar bernama all, maka hanya modul yang tercantum dalam daftar 
tersebut yang akan diimpor saat ditemui. Ini memberi pembuat paket kendali atas apa yang diimpor saat 
menggunakan pernyataan "from package import *".'''

__all__ = ["echo", "surround", "reverse"]

#Ini berarti akan mengimpor tiga submodul bernama dari paket tersebut.from sound.effects import *sound.effects

'''Jika daftar all tidak ditentukan di init.py, pernyataan from sound.effects import * tidak akan mengimpor semua 
submodul dari paket effects ke dalam namespace saat ini. Sebaliknya, hanya akan memastikan bahwa paket effects telah 
diimpor dan kemudian mengimpor nama apa pun yang telah ditentukan dalam paket tersebut. Ini juga termasuk submodul apa 
pun yang dimuat secara eksplisit oleh pernyataan sebelumnya. Dalam kasus ini, karena tidak ada daftar all yang ditentukan 
di init.py, pengguna sebaiknya mengimpor submodul yang diperlukan secara eksplisit, daripada mengimpor semuanya menggunakan 
pernyataan from sound.effects import *.'''

import sound.effects.echo
import sound.effects.surround
from sound.effects import *

