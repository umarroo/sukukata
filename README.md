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
## Contoh _Output_

`unik.txt` ditampilkan dengan visualisasi dan pengelompokan kata berdasarkan penyusun kata(_vokal_ dan _konsonan_) paling dasar.


```
ma      1604 ['abai-ma-na', 'ab-nor-ma-li-tas', 'ade-no-ma', 'adi-ta-ma', 'afir-ma-si', 'afir-ma-tif', 'aga-ma', 'ber-a-ga-ma', 'ke-ber-a-ga-ma-an', 'meng-a-ga-ma-kan', 'ke-a-ga-ma-an', 'aga-ma-is', 'aga-ma-wi', 'ak-la-ma-si', 'ak-li-ma-ti-sa-si', 'ak-si-o-ma', 'ak-si-o-ma-tis', 'aku-a-ma-rin', 'alak-ri-ma', 'ala-ma-tul-ha-yat', 'al-ma-lik', 'al-ma-ma-ter', 'al-ma-ma-ter', 'al-ma-nak', 'al-ma-sih', 'amal-ga-ma-si', 'amal-ga-ma-tor', 'meng-a-ma-nah-kan', 'peng-a-ma-nah', 'ber-a-ma-nat', 'meng-a-ma-nat-kan', 'meng-a-ma-nati', 'peng-a-ma-nat-an', 'meng-am-bek-pa-ra-ma-ar-ta-kan', 'peng-am-bek-pa-ra-ma-ar-ta-an', 'an-gi-o-sper-ma', 'ani-ma-si', 'ano-ma-li', 'an-ta-ke-su-ma', 'an-ti-ma-te-ri', 'apo-kro-ma-tik', 'apo-se-ma-tik', 'ar-ma-da', 'aro-ma', 'aro-ma-tik', 'as-ma-ra', 'ber-as-ma-ra', 'as-ma-ra-dan-ta', 'as-ma-ra-ga-ma', 'as-ma-ra-ga-ma']
mab        3 ['de-mab-ra-si', 'mab-ri-uk', 'mab-rur']
mad        5 ['mad-ma-dah', 'mad-ras', 'mad-ra-sah', 'muk-ta-mad', 'sa-mad']
mae        2 ['mae-san', 'mae-se-nas']
maes       1 ['maes-tro']
                                                                              .
                                                                              .
                                                                              .
                                                                              .
kui        7 ['meng-a-kui', 're-kui-em', 're-kui-si-si', 're-kui-si-tor', 're-li-kui', 'se-kui', 'so-li-lo-kui']
kuk       55 ['ter-a-kuk', 'ang-kuk', 'be-kuk', 'mem-be-kuk', 'pem-be-kuk-an', 'bung-kuk', 'mem-bung-kuk', 'mem-bung-kuk-bung-kuk', 'mem-bung-kuk-bung-kuk', 'ter-bung-kuk-bung-kuk', 'ter-bung-kuk-bung-kuk', 'men-cang-kuk', 'ce-kuk', 'ki-kuk', 'ke-ki-kuk-an', 'le-kak-le-kuk', 'le-kuk', 'ber-le-kuk', 'ber-le-kuk-le-kuk', 'ber-le-kuk-le-kuk', 'me-le-kuk', 'me-le-kuk-kan', 'mang-kuk', 'se-mang-kuk', 'pa-kuk', 'me-ma-kuk', 'pa-ne-kuk', 'pe-kik-pe-kuk', 'me-me-kuk', 'pe-le-kuk', 'ra-kuk', 'be-ra-kuk', 'ring-kuk', 'me-ring-kuk', 'me-ring-kuk-kan', 'ru-kuk', 'me-ru-kuk', 'se-pe-kuk', 'spe-kuk', 'sung-kuk', 'ter-sung-kuk', 'ter-sung-kuk-sung-kuk', 'ter-sung-kuk-sung-kuk', 'ta-kuk', 'ber-ta-kuk', 'me-na-kuk', 'tang-kuk', 'me-nang-kuk', 'ber-te-kuk', 'me-ne-kuk']
kul       82 ['aku-a-kul-tur', 'ang-kul-ang-kul', 'ang-kul-ang-kul', 'an-tar-mo-le-kul', 'api-kul-tur', 'ar-bo-ri-kul-tur', 'aus-kul-ta-si', 'avi-kul-tur', 'bung-kul', 'men-cang-kul', 'deng-kul', 'men-deng-kul', 'dis-kul-pa-si', 'en-kul-tu-ra-si', 'fa-kul-tas', 'fa-kul-ta-tif', 'ha-kul-ya-kin', 'hor-ti-kul-tu-ra', 'hor-ti-kul-tu-ris', 'in-kul-tu-ra-si', 'in-tra-mo-le-kul', 'kes-kul', 'kul-kas', 'kul-mi-na-si', 'kul-ti-var', 'kul-ti-va-si', 'kul-tu-ral', 'kul-tu-ri-sa-si', 'kul-tus', 'kul-zum', 'mak-ro-mo-le-kul', 'ma-kul', 'ma-li-kul-ja-bar', 'ma-li-kul-mu-luk', 'ma-ri-kul-tur', 'min-ta-kul-bu-ruj', 'mo-le-kul', 'mo-no-kul-tur', 'mul-ti-kul-tur', 'mul-ti-kul-tu-ral-is-me', 'pi-kul', 'ber-pi-kul-pi-kul', 'ber-pi-kul-pi-kul', 'me-mi-kul', 'me-mi-kul-kan', 'pi-kul-an', 'pe-mi-kul', 'po-li-kul-tur', 'me-mu-kul', 'pu-kul-me-mu-kul']
kum       58 ['ar-ke-o-zo-i-kum', 'ar-se-ni-kum', 'as-sa-la-mu-a-la-i-kum', 'azoi-kum', 'cang-kum', 'men-cang-kum', 'eo-zoi-kum', 'hu-kum', 'ber-hu-kum', 'meng-hu-kum', 'meng-hu-kum-kan', 'hu-kum-an', 'ke-hu-kum-an', 'kum-bah', 'kum-bar', 'kum-bik', 'kum-bu', 'kum-buh', 'ber-kum-pai', 'ter-kum-pal-kum-pal', 'ter-kum-pal-kum-pal', 'kum-par', 'kum-par-an', 'kum-pi', 'kum-pul', 'ber-kum-pul', 'ter-kum-pul', 'kum-pul-an', 'per-kum-pul-an', 'kung-kum', 'la-kum', 'le-kum', 'le-kum-le-kum', 'le-kum-le-kum', 'lung-kum', 'me-ga-li-ti-kum', 'me-so-li-ti-kum', 'me-so-zo-i-kum', 'mung-kum', 'ne-o-li-ti-kum', 'ne-o-zo-i-kum', 'pa-le-o-li-ti-kum', 'pa-le-o-zo-i-kum', 'pan-op-ti-kum', 'prak-ti-kum', 'rang-kum', 'me-rang-kum', 'me-rang-kum-kan', 'rang-kum-an', 'sir-kum-fiks']
kun       61 ['per-a-kun-an', 'per-a-kun-tan-an', 'ci-kun', 'ber-ci-kun-ci-kun', 'ber-ci-kun-ci-kun', 'de-kun-ci', 'du-kun', 'ber-du-kun', 'men-du-kun-kan', 'pen-du-kun-an', 'per-du-kun-an', 'fe-kun-da-si', 'fe-kun-di-tas', 'ja-kun', 'je-ru-kun', 'men-je-ru-kun', 'kal-kun', 'kar-kun', 'kun-cah', 'kun-cen', 'kun-ci', 'ter-kun-ci', 'kun-cir', 'kun-cit', 'kun-cung', 'kun-cup', 'kun-dai', 'kun-dang-an', 'ber-kun-dang', 'kun-dang-an', 'kun-dang-an', 'kun-dur', 'kun-dur-an', 'ber-kun-jung', 'ber-kun-jung-kun-jung-an', 'ber-kun-jung-kun-jung-an', 'kun-jung-an', 'kun-ta', 'kun-tau', 'kun-ti-la-nak', 'kun-tit', 'kun-tu-an', 'kun-tum', 'ter-kun-tum', 'kun-tung', 'le-kun', 'mu-kun', 'pa-kun-cen', 'pi-kun', 'me-ru-kun-kan']
kung      73 ['an-tar-ling-kung-an', 'ba-kung', 'beng-kang-beng-kung', 'ber-beng-kung', 'mem-beng-kung', 'ber-kung', 'bu-kung', 'cang-kung', 'men-cang-kung', 'ce-kung', 'ber-ceng-kung', 'ber-dang-kung', 'men-dang-kung', 'de-kung', 'deng-kung', 'ber-deng-kung', 'men-deng-kung', 'du-kung', 'ber-du-kung', 'men-du-kung', 'du-kung-an', 'pen-du-kung', 'pen-du-kung-an', 'ja-lang-kung', 'jang-kung-an', 'je-lang-kung', 'je-rung-kung', 'men-je-rung-kung', 'kung-fu', 'kung-ki', 'kung-kum', 'kung-kung', 'kung-kung', 'me-ngung-kung', 'ter-kung-kung', 'ter-kung-kung', 'kung-kung-an', 'kung-kung-an', 'le-kung', 'me-leng-kung', 'me-leng-kung-kan', 'ter-leng-kung', 'leng-kung-an', 'pe-leng-kung', 'ke-leng-kung-an', 'ling-kung', 'me-ling-kung', 'ter-ling-kung', 'ling-kung-an', 'se-ling-kung']
kup       93 ['ang-kup-ang-kup', 'ang-kup-ang-kup', 'meng-ang-kup', 'ter-ang-kup-ang-kup', 'ter-ang-kup-ang-kup', 'ba-kup', 'men-ca-kup', 'pen-ca-kup', 'ca-kup-men-ca-kup', 'ca-kup-men-ca-kup', 'ter-ca-kup', 'ca-kup-an', 'cang-kup', 'men-cang-kup', 'men-ce-kup', 'cu-kup', 'men-cu-kup-kan', 'cu-kup-an', 'ke-cu-kup-an', 'ber-ke-cu-kup-an', 'se-cu-kup', 'se-cu-kup-nya', 'cung-kup', 'je-ru-kup', 'men-je-ru-kup', 'ke-lu-kup', 'ker-kup', 'ku-kup', 'kup-let', 'kup-luk', 'kup-nat', 'kup-ro-pro-te-in', 'kup-rum', 'ter-lang-kup', 'lang-kup-an', 'le-kap-le-kup', 'le-kup-le-kap', 'me-ling-kup', 'ter-ling-kup', 'me-lang-kup', 'pi-kup', 'me-rang-kup', 'me-rang-kup', 'te-rang-kup', 'rung-kup', 'me-rung-kup', 'se-lang-kup', 'se-ling-kup', 'me-nye-ling-kup', 'se-lung-kup']
kur       85 ['meng-a-kur-kan', 'ke-a-kur-an', 'ang-kur', 'be-lung-kur', 'bu-kur', 'ce-kur', 'cu-kur', 'ber-cu-kur', 'pen-cu-kur', 'pen-cu-kur-an', 'deng-kur', 'ber-deng-kur', 'men-deng-kur', 'deng-kur-an', 'dis-kur-sif', 'eks-kur-si', 'ber-eks-kur-si', 'eks-kur-sif', 'ke-lu-kur', 'ber-ke-lu-kur', 'ber-ke-lu-kur-an', 'me-ngu-kur', 'ku-kur-an', 'me-ngu-kur', 'kur-ban', 'ber-kur-ban', 'kur-ka-to-vi-um', 'kur-ku-ma', 'kur-ma', 'kur-se-ma-ngat', 'kur-si', 'kur-sif', 'kur-sor', 'kur-sus', 'kur-ta-se', 'kur-va', 'kur-va-li-ni-er', 'kur-va-tur', 'me-la-kur-kan', 'leng-kur', 'me-leng-kur', 'li-kur', 'ber-li-kur-li-kur', 'ber-li-kur-li-kur', 'li-kur-an', 'ma-ni-kur', 'maz-kur', 'ter-maz-kur', 'mung-kur', 'me-mang-kur']
kurs       2 ['kon-kurs', 're-kurs']
kus       76 ['aka-de-mi-kus', 'al-kus', 'ang-kus', 'bo-ta-ni-kus', 'bron-kus', 'bung-kus', 'mem-bung-kus', 'pem-bung-kus', 'men-ca-kus', 'de-kus', 'ber-de-kus', 'men-de-kus', 'deng-kus', 'ber-deng-kus', 'men-deng-kus', 'di-dak-ti-kus', 'dra-ma-ti-kus', 'ek-lek-ti-kus', 'es-te-ti-kus', 'fi-kus', 'fo-kus', 'ber-fo-kus', 'mem-fo-kus', 'mem-fo-kus-kan', 'pem-fo-kus-an', 'ter-fo-kus', 'go-no-ko-kus', 'hi-bis-kus', 'his-to-ri-kus', 'ka-kus', 'kau-kus', 'ke-mung-kus', 'ke-ra-mi-kus', 'ki-kus', 'kle-ri-kus', 'ko-kus', 'ko-mi-kus', 'kri-ti-kus', 'ku-kus', 'ber-ku-kus', 'me-ngu-kus', 'ku-kus-an', 'kus-kus', 'kus-kus', 'kus-pis', 'kus-ruk', 'kus-ta', 'kus-ti', 'la-kus-trin', 'lo-kus']
kut       81 ['ang-kut', 'ang-kut-an', 'peng-ang-kut', 'peng-ang-kut-an', 'ang-kut-ang-kut', 'ang-kut-ang-kut', 'ba-kut', 'bang-kut', 'be-lu-kut', 'bu-kut', 'pem-bu-kut', 'ce-kut', 'men-ce-kut', 'ci-kut', 'ci-kut-an', 'de-kut', 'ber-de-kut', 'men-de-kut', 'hos-kut', 'meng-i-kut-ser-ta-kan', 'peng-i-kut-ser-ta-an', 'ke-i-kut-ser-ta-an', 'meng-i-kut', 'meng-i-kut-kan', 'mem-per-i-kut', 'mem-per-i-kut-kan', 'peng-i-kut', 'ju-kut', 'ke-de-kut', 'ke-re-kut', 'ke-ru-kut', 'me-nge-ru-kut', 'me-nge-ru-kut-kan', 'li-kut', 'ber-li-kut', 'me-li-kut', 'ma-la-kut', 'me-lu-kut', 'pe-ti-kut', 'ra-kut', 'me-ra-kut', 'rang-kut', 'me-rang-kut', 'me-nyang-kut-pa-ut-kan', 'sang-kut', 'ber-sang-kut-an', 'me-nyang-kut', 'sang-kut-me-nyang-kut', 'sang-kut-me-nyang-kut', 'me-nyang-kut-kan']
kwa        1 ['kwa-si-or-kor']
kwar       2 ['kwar-tet', 'kwar-tir']
kwe        2 ['kwe-ni', 'kwe-ti-au']
```
