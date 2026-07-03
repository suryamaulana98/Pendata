import json

file_path = r"d:\materi_kuliah\SEMESTER 4\penambangan data\Pendata\materi\UAS_Data_Mining_KNIME.ipynb"
with open(file_path, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

new_workflow = [
    "Workflow untuk proses *training* dan *testing* dibentuk dengan rangkaian node berikut:\n",
    "- **CSV Reader:** Gerbang awal untuk mengimpor dataset berformat .csv ke dalam KNIME.\n",
    "- **Number to String:** Mengubah tipe data kolom target (`OUTPUT Grade`) dari numerik (Integer) menjadi kategorikal (String) untuk target klasifikasi.\n",
    "- **Table Partitioner:** Membagi dataset secara acak menjadi dua bagian: Data Latih (Train 80%) dan Data Uji (Test 20%).\n",
    "- **Decision Tree Learner:** Melatih data *Train* untuk membangun algoritma pohon keputusan dan memodelkan pola.\n",
    "- **Decision Tree Predictor:** Menerapkan model yang telah dibuat untuk memprediksi target kelas pada Data Uji yang belum pernah dilihat model.\n",
    "- **Decision Tree View:** Menampilkan visualisasi bentuk pohon keputusan (*tree*) untuk memudahkan membaca aturan (rules).\n",
    "- **Scorer:** Membandingkan nilai tebakan dari node Predictor dengan nilai aslinya di Data Uji, lalu menghitung tingkat keberhasilan (akurasi) model.\n"
]

new_interpretasi = """**Interpretasi Hasil dan Perhitungan Akurasi (Berdasarkan Output Node Scorer):**

**1. Pembuktian Data Uji (Test Set)**
Jika kita menjumlahkan elemen pada salah satu baris Confusion Matrix, kita akan mendapatkan total data uji:
- **Rumus:** True Positive (TP) + False Positive (FP) + True Negative (TN) + False Negative (FN)
- **Baris 1:** 5 + 2 + 19 + 3 = **29 data**
Ini membuktikan *Table Partitioner* (rasio 80:20) telah berjalan, karena 20% dari 145 baris data adalah 29 data untuk diuji.

**2. Perhitungan Overall Accuracy (0.379)**
Akurasi keseluruhan diperoleh dari jumlah total tebakan benar (Total True Positive) dibagi total data uji.
- **Total Tebakan Benar (Semua TP):** 5 + 2 + 2 + 0 + 0 + 0 + 0 + 2 = **11**
- **Akurasi:** 11 / 29 = 0.3793... (**0.379** atau **37.9%**)
Angka 37.9% ini menunjukkan model hanya menebak benar 11 dari 29 data. Akurasi ini rendah dikarenakan dataset menargetkan klasifikasi kompleks **8 kelas nilai (multi-class)** (Fail hingga AA), di mana terdapat tumpang tindih (*overlap*) pola kebiasaan mahasiswa pada *grade* yang berdekatan.

**3. Cohen's Kappa (0.27)**
Nilai *Cohen's Kappa* sebesar 0.27 berada dalam rentang **"Fair Agreement"** (Tingkat kesesuaian wajar). Ini menegaskan bahwa meskipun akurasi 37.9%, model tidak sekadar menebak jawaban secara acak (random guess), melainkan sudah memprediksi berdasarkan *rules* algoritma pohon keputusan yang valid.
"""

for cell in notebook['cells']:
    if cell['cell_type'] == 'markdown':
        source = cell['source']
        
        # Replace workflow section
        for i, line in enumerate(source):
            if "Workflow untuk proses *training* dan *testing* dibentuk dengan rangkaian node berikut:" in line:
                # the following lines are the list. We delete them and insert our new list.
                # Find how many lines to delete
                end_idx = i + 1
                while end_idx < len(source) and source[end_idx].startswith("- **"):
                    end_idx += 1
                
                # Replace the block
                source[i:end_idx] = new_workflow
                break
                
        # Replace interpretasi section
        for i, line in enumerate(source):
            if "**Interpretasi Hasil:**" in line:
                source[i] = new_interpretasi
                if i+1 < len(source):
                    source[i+1] = ""
                break

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1, ensure_ascii=False)
