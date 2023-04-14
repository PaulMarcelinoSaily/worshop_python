'''Saat nama modul spamdiimpor, interpreter pertama-tama akan mencari modul bawaan dengan nama tersebut.
 Nama modul ini tercantum dalam sys.builtin_module_names. Jika tidak ditemukan, ia akan mencari file bernama spam.pydalam daftar direktori
   yang diberikan oleh variabel sys.path. sys.pathdiinisialisasi dari lokasi berikut:

Direktori yang berisi skrip input (atau direktori saat ini ketika tidak ada file yang ditentukan).

PYTHONPATH(daftar nama direktori, dengan sintaks yang sama dengan variabel shellPATH).

Default yang bergantung pada penginstalan (berdasarkan konvensi termasuk site-packagesdirektori, ditangani oleh sitemodul).'''