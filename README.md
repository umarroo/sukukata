# Suku Kata

Projek ini adalah usulan bagi tim [kbbi](https://kbbi.kemdikbud.go.id/) untuk perbaikan bentuk dasar suku kata dalam bahasa Indonesia. 
Terimakasih khusus kepada [Efan Fauzi](https://github.com/efenfauzi/django_kbbi)

## Menjalankan Program #1

1. Hasilkan `kata.txt` dengan command `$ python getKBBIdb.py > kata.txt`
2. Kemudian jalankan `$ python cleaning.py > sukukata.txt` untuk menghasilkan `sukukata.txt`
3. `$ python sukukata.py > unik.txt` dipakai untuk menghasilkan `unik.txt`(hasil akhir) 

## Menjalankan Program #2

```
$ chmod +x run.sh
$ ./run.sh
```

`unik.txt` ditampilkan dengan visualisasi dan pengelompokan kata berdasarkan penyusun kata(_vokal_ dan _konsonan_) paling dasar.
