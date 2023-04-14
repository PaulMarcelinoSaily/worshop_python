'''Paket adalah cara menyusun ruang nama modul Python dengan 
menggunakan "nama modul bertitik". Misalnya, nama modul 
A. B menunjukkan submodule yang dinamai Bdalam paket bernama 
A. Sama seperti penggunaan modul menyelamatkan pembuat modul 
yang berbeda dari harus khawatir tentang nama variabel global 
satu sama lain, penggunaan nama modul bertitik menyelamatkan 
penulis paket multi-modul seperti NumPy atau Pillow dari harus 
khawatir tentang nama modul satu sama lain .'''

sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...

'''Ini adalah contoh struktur direktori untuk paket "sound". Paket "sound" terdiri dari tiga subpakel, yaitu "formats", "effects", dan "filters".

Subpakel "formats" berisi modul yang digunakan untuk mengkonversi format file audio, termasuk "wavread.py" dan "wavwrite.py" untuk membaca dan menulis file format .wav, "aiffread.py" dan "aiffwrite.py" untuk format .aiff, dan sebagainya.

Subpakel "effects" berisi modul untuk efek suara, seperti "echo.py", "surround.py", dan "reverse.py".

Subpakel "filters" berisi modul untuk filter suara, seperti "equalizer.py", "vocoder.py", dan "karaoke.py".

File "init.py" adalah file inisialisasi yang akan dijalankan ketika paket "sound" diimpor. Ini memungkinkan Anda untuk menentukan apa yang akan terjadi saat paket diimpor.'''

#Pengguna paket dapat mengimpor modul individual dari paket, misalnya:
import sound.effects.echo

#memuat submodul sound.effects.echo. Itu harus dirujuk dengan nama lengkapnya.
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

#Cara alternatif mengimpor submodul
from sound.effects import echo

#memuat submodule echo, dan membuatnya tersedia tanpa awalan paketnya, sehingga dapat digunakan sebagai berikut:
echo.echofilter(input, output, delay=0.7, atten=4)

#memuat submodule echo, tetapi ini membuat fungsinya echofilter()langsung tersedia:
echofilter(input, output, delay=0.7, atten=4)