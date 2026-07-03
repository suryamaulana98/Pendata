import json

file_path = r"d:\materi_kuliah\SEMESTER 4\penambangan data\Pendata\materi\UAS_Data_Mining_KNIME.ipynb"
with open(file_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Find the modeling cell (Cell 6 usually)
for cell in notebook['cells']:
    if cell['cell_type'] == 'markdown' and any('## 7. Modeling' in line for line in cell['source']):
        # Find where "### Workflow KNIME" starts
        source = cell['source']
        for i, line in enumerate(source):
            if "### Workflow KNIME" in line:
                start_idx = i
                break
        
        # Rewrite from "### Workflow KNIME" to the end of the cell
        # Let's keep the image "![Workflow KNIME](images/auas.png)"
        # And add the new detailed explanation.
        
        new_content = [
            "### Workflow KNIME\n",
            "\n",
            "Workflow untuk proses *training* dan *testing* dibentuk dengan rangkaian node berikut:\n",
            "- **CSV Reader:** Pintu masuk (gerbang awal) untuk membaca dan mengimpor file dataset mentah berformat .csv ke dalam KNIME.\n",
            "- **Number to String:** Bertugas mengubah tipe data kolom target (`OUTPUT Grade`) dari Angka (Integer) menjadi Teks/Kategori (String). Ini sangat wajib dilakukan agar algoritma tahu bahwa angka 0-7 adalah nama kelas/kategori nilai, bukan angka matematis untuk regresi.\n",
            "- **Table Partitioner:** Membagi total data (145 baris) menjadi dua kubu secara acak. Jalur atas adalah **Data Latih (80% = 116 data)** untuk mengajari model, dan jalur bawah adalah **Data Uji (20% = 29 data)** untuk mengetes model.\n",
            "- **Decision Tree Learner:** Sebagai \"otak\" dari model. Node ini menerima Data Latih (116 data) dan belajar mencari pola untuk membentuk algoritma Pohon Keputusan (*Decision Tree*).\n",
            "- **Decision Tree View:** Node visualisasi untuk melihat bentuk percabangan pohon keputusan (*If-Then rules*) yang dipelajari oleh *Learner*.\n",
            "- **Decision Tree Predictor:** Berfungsi sebagai \"pemberi ujian\". Menerapkan model yang sudah dilatih pada Data Uji (29 data yang belum pernah dilihat) untuk menebak *Grade* masing-masing mahasiswa.\n",
            "- **Scorer:** Sebagai penilai (*Grader*). Node ini membandingkan kunci jawaban asli dengan hasil tebakan dari *Predictor*, lalu menghitung akurasinya.\n",
            "\n",
            "![Workflow KNIME](images/auas.png)\n",
            "\n",
            "### Hasil Decision Tree Predictor (Classified Data)\n",
            "\n",
            "Berikut adalah penjelasan mengenai cara membaca tabel hasil prediksi (*Classified Data*) dari node **Decision Tree Predictor**:\n",
            "1. **Bukti Data Uji 29 Baris:** Tabel prediksi menghasilkan `Rows: 29`. Ini adalah bukti fisik mutlak bahwa *Table Partitioner* benar-benar bekerja memisahkan 20% data dari total 145 data untuk dijadikan soal ujian (*Test Set*).\n",
            "2. **Kolom GRADE (Kunci Jawaban Asli):** Merupakan nilai atau kelas aktual yang sebenarnya didapatkan oleh mahasiswa.\n",
            "3. **Kolom Prediction(GRADE) (Hasil Tebakan):** Merupakan tebakan yang dihasilkan oleh model *Decision Tree*.\n",
            "- **Tebakan Benar (TP/TN):** Jika nilai asli dan hasil prediksi sama (misalnya nilai asli `2`, ditebak `2`).\n",
            "- **Tebakan Meleset (FP/FN):** Jika nilai asli berbeda dengan hasil tebakan (misalnya nilai asli `3`, ditebak `0`).\n",
            "\n",
            "Tabel *Classified Data* inilah yang nantinya disetorkan ke node **Scorer** untuk menghitung akurasi akhir. *Scorer* memindai bahwa dari 29 baris, model berhasil menebak tepat sasaran di 11 baris, sehingga menghasilkan akurasi **11/29 = 37.9%**.\n"
        ]
        
        source[start_idx:] = new_content
        break

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)
