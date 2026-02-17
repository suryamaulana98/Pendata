# Data Understanding (Pemahaman Data)

## 2.1 Deskripsi Dataset

Dataset yang digunakan dalam proses penambangan data ini adalah **Iris
Flower Dataset**. Dataset ini terdiri dari 150 data observasi bunga iris
yang terbagi ke dalam tiga spesies, yaitu:

-   Iris-setosa
-   Iris-versicolor
-   Iris-virginica

Setiap data memiliki empat fitur numerik yang merepresentasikan ukuran
morfologi bunga dalam satuan centimeter (cm), serta satu kolom label
yang menunjukkan spesiesnya.

------------------------------------------------------------------------

## 2.2 Struktur Dataset

Dataset memiliki struktur sebagai berikut:

  No   Nama Atribut   Tipe Data   Keterangan
  ---- -------------- ----------- --------------------
  1    sepal_length   Float       Panjang sepal (cm)
  2    sepal_width    Float       Lebar sepal (cm)
  3    petal_length   Float       Panjang petal (cm)
  4    petal_width    Float       Lebar petal (cm)
  5    species        Object      Jenis spesies iris

Jumlah total data: **150 baris**\
Jumlah total atribut: **5 kolom**

Empat atribut pertama bertipe numerik (float), sedangkan kolom *species*
bertipe kategorikal (object).

------------------------------------------------------------------------

## 2.3 Statistik Deskriptif

Statistik deskriptif dilakukan untuk memahami distribusi dasar setiap
fitur numerik, seperti nilai minimum, maksimum, rata-rata (mean), dan
standar deviasi.

Secara umum hasil analisis menunjukkan:

-   Tidak terdapat nilai negatif pada fitur numerik.
-   Rentang nilai berada dalam batas biologis yang wajar.
-   Distribusi data relatif stabil dan tidak menunjukkan anomali
    ekstrem.

Statistik ini penting untuk memastikan bahwa tidak ada kesalahan input
data seperti angka yang tidak masuk akal atau format yang keliru.

------------------------------------------------------------------------

## 2.4 Pemeriksaan Missing Value

Pemeriksaan dilakukan untuk memastikan tidak terdapat nilai kosong
(missing value) pada dataset.

Hasil pemeriksaan menunjukkan:

-   Tidak terdapat missing value pada seluruh kolom.
-   Dataset lengkap sebanyak 150 data.

Hal ini menunjukkan bahwa dataset berada dalam kondisi yang baik dan
tidak memerlukan proses imputasi data.

------------------------------------------------------------------------

## 2.5 Pemeriksaan Duplikasi Data

Selanjutnya dilakukan pemeriksaan untuk memastikan tidak terdapat baris
data yang identik (duplikat).

Hasil analisis menunjukkan:

-   Tidak terdapat data duplikat.
-   Seluruh 150 baris data bersifat unik.

Dengan demikian, dataset tidak memerlukan proses penghapusan duplikasi.

------------------------------------------------------------------------

## 2.6 Pemeriksaan Konsistensi dan Kualitas Data

Tahap ini bertujuan untuk memastikan bahwa:

-   Semua nilai numerik berada dalam rentang logis.
-   Tidak terdapat nilai ekstrem yang tidak wajar.
-   Penulisan label spesies konsisten dan tidak mengandung kesalahan
    pengetikan.

Hasil pemeriksaan menunjukkan bahwa:

-   Nilai fitur numerik konsisten dan berada dalam rentang normal.
-   Tidak ditemukan nilai anomali yang mencurigakan.
-   Label spesies konsisten pada seluruh data.

------------------------------------------------------------------------

## 2.7 Kesimpulan Tahap Data Understanding

Berdasarkan proses pemahaman data yang telah dilakukan, dapat
disimpulkan bahwa:

1.  Dataset memiliki struktur yang jelas dan terdefinisi dengan baik.
2.  Tidak terdapat missing value.
3.  Tidak terdapat data duplikat.
4.  Tidak ditemukan inkonsistensi atau kesalahan data.
5.  Dataset dalam kondisi siap untuk masuk ke tahap Data Preparation.

Tahap Data Understanding ini menjadi fondasi penting sebelum dilakukan
proses pembersihan dan transformasi data pada tahap berikutnya.
