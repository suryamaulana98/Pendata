import json

file_path = r"d:\materi_kuliah\SEMESTER 4\penambangan data\Pendata\materi\UAS_Data_Mining_KNIME.ipynb"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '     "- **CSV Reader:** Input data sumber asli.\\n",\n     "- **Partitioning:** Membagi data menjadi kelompok *Train* (misalnya 80%) untuk pelatihan dan *Test* (20%) untuk pengujian.\\n",\n     "- **Decision Tree Learner:** Melatih data *Train* untuk membangun algoritma pohon keputusan dan menghasilkan model akhir.\\n",\n     "- **Decision Tree Predictor:** Menggunakan model yang telah dibuat dan memprediksi target untuk data set *Test* yang belum pernah \\"dilihat\\" model.\\n",\n     "- **Scorer:** Menghitung akurasi prediksi hasil tebakan dibandingkan nilai aslinya.\\n",',
    '     "- **CSV Reader:** Gerbang awal untuk mengimpor dataset berformat .csv ke dalam KNIME.\\n",\n     "- **Number to String:** Mengubah tipe data kolom target (`OUTPUT Grade`) dari tipe numerik (Integer) menjadi tipe kategorikal (String) agar algoritma menganggapnya sebagai target klasifikasi.\\n",\n     "- **Table Partitioner:** Membagi dataset secara acak menjadi dua bagian: Data Latih (Train) dan Data Uji (Test).\\n",\n     "- **Decision Tree Learner:** Melatih data *Train* untuk membangun algoritma pohon keputusan dan menghasilkan pola hubungan antara variabel input dengan nilai akhir.\\n",\n     "- **Decision Tree Predictor:** Menerapkan model yang telah dibuat untuk memprediksi target kelas pada Data Uji yang belum pernah dilihat model.\\n",\n     "- **Decision Tree View:** Menampilkan visualisasi bentuk pohon keputusan (*tree*) untuk memudahkan membaca aturan (rules) IF-THEN.\\n",\n     "- **Scorer:** Membandingkan nilai tebakan dari node Predictor dengan nilai aslinya di Data Uji, lalu menghitung tingkat keberhasilan (akurasi) model.\\n",'
)

content = content.replace(
    '     "**Interpretasi Hasil:**\\n",\n     "Nilai akurasi yang diperoleh menggambarkan kekuatan model kita dalam menangani data yang terbatas ini. Berdasarkan analisis di *Confusion Matrix*, dapat dilihat adanya konsentrasi nilai di garis diagonal yang membuktikan bahwa kemampuan model *Decision Tree* dalam memprediksi nilai mahasiswa cukup tangguh. Beberapa klasifikasi yang meleset seringkali disebabkan tumpang tindih pola perilaku antara nilai yang sangat dekat (misalnya CC dengan CB).\\n",',
    '     "**Interpretasi Hasil:**\\n",\n     "Berdasarkan hasil output dari node Scorer (Accuracy statistics), diperoleh **Overall Accuracy sebesar 0.379 atau 37.9%**. Angka ini menunjukkan bahwa secara keseluruhan, model hanya mampu memprediksi kategori kelas nilai mahasiswa dengan tepat sasaran sebesar 37.9%. Meskipun terlihat rendah, hal ini wajar karena model harus memprediksi **8 kelas nilai yang berbeda (multi-class classification)** (Fail hingga AA). Akurasi yang rendah ini disebabkan oleh **tumpang tindih pola perilaku** (seperti *Attendance* dan *Study Hours*) antara mahasiswa dengan nilai yang berdekatan (misalnya CC dengan CB, atau BA dengan AA). Karena batas kebiasaannya sangat mirip, model Decision Tree seringkali kesulitan membedakan dan memprediksi *Grade* secara spesifik, sehingga terjadi misklasifikasi pada kelas-kelas yang berdekatan.\\n",'
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Berhasil update!")
