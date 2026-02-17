# Data Understanding (Pemahaman Data)

## 1. Cara Memulai Proses Data Mining

Langkah awal dalam melakukan data mining adalah:

1.  Memastikan dataset telah tersedia dan dapat dibaca dengan benar.
2.  Memahami struktur data (jumlah baris, kolom, dan tipe data).
3.  Melakukan pemeriksaan kualitas data (missing value dan duplikasi).
4.  Melakukan eksplorasi awal melalui statistik deskriptif dan
    visualisasi.

Tahap ini sangat penting karena kesalahan dalam memahami data dapat
menyebabkan kesalahan dalam proses modeling.

------------------------------------------------------------------------

## 2. Struktur Dataset

Dataset Iris memiliki:

-   150 baris data
-   4 fitur numerik
-   1 label kategorikal (species)

Seluruh fitur numerik bertipe float dan label bertipe object.

------------------------------------------------------------------------

## 3. Pemeriksaan Kualitas Data

Hasil pemeriksaan menunjukkan:

-   Tidak terdapat missing value.
-   Tidak terdapat data duplikat.
-   Nilai berada dalam rentang biologis yang wajar.

Dataset berada dalam kondisi bersih dan siap untuk tahap berikutnya.

------------------------------------------------------------------------

## 4. Visualisasi Data

### 4.1 Distribusi Jumlah Data per Species

![Jumlah Data per Species](visualisasi_jumlah_species.png)

Berdasarkan grafik di atas, setiap spesies memiliki jumlah data yang
sama, yaitu 50 data. Hal ini menunjukkan dataset dalam kondisi seimbang
(balanced dataset).

------------------------------------------------------------------------

### 4.2 Distribusi Sepal Length

![Histogram Sepal Length](histogram_sepal_length.png)

Histogram menunjukkan distribusi panjang sepal. Sebaran data relatif
normal dan tidak menunjukkan anomali ekstrem.

------------------------------------------------------------------------

### 4.3 Hubungan Petal Length dan Petal Width

![Scatter Plot Petal](scatter_petal.png)

Scatter plot menunjukkan adanya pola pemisahan antar data berdasarkan
ukuran petal. Variabel petal_length dan petal_width berpotensi kuat
digunakan dalam proses klasifikasi.

------------------------------------------------------------------------

## 5. Kesimpulan Tahap Data Understanding

Dari proses eksplorasi yang telah dilakukan dapat disimpulkan:

1.  Dataset memiliki kualitas yang baik.
2.  Tidak ditemukan kesalahan data.
3.  Dataset seimbang antar kelas.
4.  Terdapat pola awal yang menunjukkan potensi klasifikasi.

Dengan demikian, dataset siap untuk masuk ke tahap Data Preparation.
