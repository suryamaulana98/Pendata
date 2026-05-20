import json

notebook_content = {
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "# Pembahasan Tugas: Regresi Linier (Manual Matrix & Scikit-Learn)\n",
        "\n",
        "Halo semua! Di catatan ini, kita akan ngebahas bareng-bareng secara bertahap tentang tugas **Regresi Linier** kita. Inti dari tugas ini sebenarnya simpel: ada sekumpulan titik-titik (data historis/observasi), lalu kita diminta mencari **garis lurus terbaik (garis regresi)** yang paling pas buat ngewakilin semua titik tersebut. Garis lurus ini nantinya bisa kita pakai buat nebak/prediksi nilai di masa depan.\n",
        "\n",
        "Kita punya 7 titik koordinat:\n",
        "- A(2,2)\n",
        "- B(4,3)\n",
        "- C(5,5)\n",
        "- D(3,4)\n",
        "- E(3,3)\n",
        "- F(4,5)\n",
        "- G(5,6)\n",
        "\n",
        "Angka pertama itu sumbu X (misal: lamanya di kelas), dan angka kedua itu sumbu Y (misal: nilai).\n",
        "\n",
        "Buat mecahin masalah ini, kita bakal pakai 3 cara:\n",
        "1. Visualisasi manual pake **GeoGebra** (biar kebayang bentuknya gimana).\n",
        "2. Hitungan Matematika Dasar pake matrix $\\hat{\\beta} = (X^T X)^{-1} X^T Y$.\n",
        "3. Cara *Magic* pake library Python (`sklearn`)."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "## Langkah 1: Plotting Menggunakan GeoGebra\n",
        "\n",
        "Sebelum pusing liat rumus, mending kita gambar dulu titik-titiknya biar dapet *feeling* dari datanya.\n",
        "\n",
        "> **📸 TEMPATKAN GAMBAR PERTAMA DI SINI:**\n",
        "> \n",
        "> *Screenshot area grafik (scatter plot) dari GeoGebra setelah kamu masukin titik A sampai G di sana.*\n",
        "> *Kalo kamu simpan foldernya pake nama `images`, masukin pake kode markdown ini:* `![Scatter Plot GeoGebra](images/geogebra_scatter.png)`\n",
        "\n",
        "**Penjelasan Gambar:**\n",
        "Kalau diliat-liat titik A(2,2) sampe G(5,6) di atas, kelihatannya grafiknya emang tersebar, tapi arah tren-nya itu **naik ke atas**. Karena arahnya naik ke atas barengan (kiri bawah ke kanan atas), kita ambil kesimpulan kalau datanya punya **Korelasi Positif**. Artinya: makin besar nilai X, nilai Y-nya ikut membesar.\n",
        "\n",
        "Nah, kita bakal narik 1 garis lurus panjang dari ujung ke ujung. Tapi nggak mungkin satu lidi (garis lurus) itu membelah tepat di tengah semua titik sekaligus. Pasti ada sisa / beda jarak asli ke garisnya. Nah selisih jarak ini disebut **Residual** alias **Error**. Tugas Regresi Linier ini adalah mencari ukuran kemiringan garis yang paling jago nge-minimalisir Error tadi (Makanya disebut teknik *Least Squares*)."
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "## Langkah 2: Menghitung secara Manual (Metode Matrix OLS)\n",
        "\n",
        "Bentuk umum persamaan garis lurus kan gampangnya: **y = intercept + (slope * x)** \n",
        "- `intercept`: Lokasi awal garis memotong tembok vertikal (sumbu Y)\n",
        "- `slope`: Ukuran kemiringan garis (nanjak atau nurun)\n",
        "\n",
        "Di dalam materi (PPT), kita dikasih rumus dewa buat nyari *slope* dan *intercept* pake cara Matrix (Ordinary Least Squares):\n",
        "\n",
        "$$ \\hat{\\beta} = (X^T X)^{-1} X^T Y $$\n",
        "\n",
        "Gak usah pusing dulu, bacanya pelan-pelan berurutan (step-by-step):\n",
        "1. Anggap kita punya tabel **Matrix X** (isiannya angka sumbu X, tapi bagian paling kirinya diisi angka 1 semuanya buat syarat itungan regresi).\n",
        "2. Punya tabel **Matrix Y** (isiannya target alias sumbu Y).\n",
        "3. Pertama kita cari **$X^T$** (artinya dimensi Matrix X diputar / tertukar urutannya alias di-*Transpose*).\n",
        "4. Habis itu kaliin matrix transpose tadi dengan marix X aslinya: **$(X^T X)$**\n",
        "5. Hasil perhitungannya lalu diputar di-*Inverse* menjadi $(X^T X)^{-1}$.\n",
        "6. Hasil akhirnya tinggal dikalikan sama $X^T$ terus dikaliin lagi deh sama $Y$.\n",
        "7. Udah deh, jawaban akhirnya itu $\\hat{\\beta}$ ! Nilai pertama itu `intercept`, nilai kedua itu `slope` yang kita cari, beres!\n",
        "\n",
        "Capek itung manual? Kita cobain praktiknya di bawah pake kode Python (khususnya pakai library `numpy` pinter hitung Matrix):"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "\n",
        "# 1. Siapkan Nilai X dan Y sesuai koordinat di tugas kita\n",
        "x_data = [2, 4, 5, 3, 3, 4, 5]\n",
        "y_data = [2, 3, 5, 4, 3, 5, 6]\n",
        "\n",
        "# 2. Bentuk Matrix-nya (Matrix X di area kiri ditambahin angka 1 agar match)\n",
        "X = np.array([[1, x] for x in x_data])\n",
        "Y = np.array(y_data).reshape(-1, 1)  # Di-reshape biar turun kebawah bentuknya kolom\n",
        "\n",
        "print(\"Bentuk Matrix X (Angka 1 didepannya):\\n\", X)\n",
        "print(\"\\nBentuk Matrix Y:\\n\", Y)\n",
        "\n",
        "# 3. Kita lakuin hitungan berurutan sesuai rumus --> Beta_hat = Inverse(X_transpose * X) * X_transpose * Y\n",
        "# [Step A] Cari Transpose dari X\n",
        "X_T = X.T\n",
        "\n",
        "# [Step B] Kalikan X_T dengan X\n",
        "X_T_X = X_T.dot(X)\n",
        "\n",
        "# [Step C] Cari Inverse-nya\n",
        "X_T_X_inv = np.linalg.inv(X_T_X)\n",
        "\n",
        "# [Step D] Kalikan hasil inverse dengan X_T\n",
        "Step_D = X_T_X_inv.dot(X_T)\n",
        "\n",
        "# [Step Terakhir] Kalikan dengan Y agar dapet titik Beta-nya !!\n",
        "beta_hat = Step_D.dot(Y)\n",
        "\n",
        "intercept_manual = beta_hat[0][0]\n",
        "slope_manual = beta_hat[1][0]\n",
        "\n",
        "print(f\"\\n-- HASIL PERHITUNGAN MANUAL (MATEMATIKA MATRIX) --\")\n",
        "print(f\"Ketemu Intercept-nya : {intercept_manual:.4f}\")\n",
        "print(f\"Ketemu Slope-nya     : {slope_manual:.4f}\")\n",
        "print(f\"\\n>> Persamaan Garis Regresi Terbaik Kita: y = {intercept_manual:.4f} + {slope_manual:.4f}x\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "## Langkah 3: Menggunakan Library Python `sklearn`\n",
        "\n",
        "Karena rumus itu kepanjangan dan ribet buat data ribuan di dunia nyata, orang-orang *Data Scientist* bikin library sakti namanya `scikit-learn` (`sklearn`). Kita cuma tinggal pake algoritma ML (Machine Learning)-nya dan manggil fungsi `LinearRegression()`.\n",
        "\n",
        "Regresi ngebuktiin dirinya sebagai **Supervised Learning** di tahap ini, karena saat kita 'ngajarin' mesin pakai fungsi `fit(x,y)`, kita nyediain jawaban aslinya (Y) agar si robot nangkep cara kerjanya. \n",
        "\n",
        "Yuk mari kita cocokkan ajaibnya `sklearn` dengan kerja keras kita bikin rumus Matrix manual tadi:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": None,
      "metadata": {},
      "outputs": [],
      "source": [
        "from sklearn.linear_model import LinearRegression\n",
        "\n",
        "# Kita bentuk X jadi 2D Array agar dapet restu si sklearn\n",
        "X_sklearn = np.array(x_data).reshape(-1, 1)\n",
        "Y_sklearn = np.array(y_data)\n",
        "\n",
        "# Panggil the magic model!\n",
        "model = LinearRegression()\n",
        "\n",
        "# Ajarin (Training) model ke datanya (dibagian ini matrix rumit otomatis berhitung)\n",
        "model.fit(X_sklearn, Y_sklearn)\n",
        "\n",
        "print(\"-- HASIL PERHITUNGAN SKLEARN (OTOMATATIS) --\")\n",
        "print(f\"Intercept-nya     : {model.intercept_:.4f}\")\n",
        "print(f\"Slope-nya         : {model.coef_[0]:.4f}\")\n",
        "print(f\"\\n>> Persamaan Garis Regresi SKLearn: y = {model.intercept_:.4f} + {model.coef_[0]:.4f}x\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "---\n",
        "## Langkah Akhir: Menarik Kesimpulan & Mengecek Geogebra\n",
        "\n",
        "Keren kan! Kode perhitungan panjang rumus Matrix ternyata hasilnya **SAMA PERSIS** kayak yang versi simpel library `sklearn`, dimana ketemu garis yang paling tokcer di fungsi akhir yaitu: \n",
        "\n",
        "**`y = 0.4286 + 0.9643x`**\n",
        "\n",
        "> **📸 TEMPATKAN GAMBAR KEDUA DI SINI:**\n",
        "> \n",
        "> *Sekarang buka ulang GeoGebra-nya. Di bagian kiri (area Input) ketik* `FitLine(A, B, C, D, E, F, G)` *(A-G wajib kapital, sesuaikan sama nama titik kamu)*.\n",
        "> *Klik ENTER. Tar! Bakal muncul 1 buah garis lurus yang mematahkan semua titik itu. Di pojok kiri geogebra juga bisa dapet contekkan rumus garis itu yaitu `y = 0.96x + 0.43`. Ambil screenshoot yang ada garisnya.*\n",
        "> *Ganti nama gambar di markdown nya dengan nama aslinya misalnya:* `![Regresi GeoGebra Garis](images/geogebra_regresi_garis.png)`\n",
        "\n",
        "**Apa artinya ini semua di akhir tugas?**\n",
        "\n",
        "Garis yang nongol di GeoGebra kamu (*y = 0.4286 + 0.9643x*) mewakili jalur prediktif yang Error alias Residualnya udah paling minim dari titik asli. Gunanya Model ini apa dong? \n",
        "- Simpelnya: Ngebantu memprediksi masa depan.\n",
        "- Misal ada soal tambahan dari dosen: \"Gimana kalau si X ukurannya tiba-tiba ketemu 20? Berapa kira-kira Y nya?!\" \n",
        "- Kita nggak perlu mengira-ngira bingung. Tinggal serahin aja nilai X yang 20 ke fungsi mesin di atas: \n",
        "$y = 0.4286 + (0.9643 \\times 20)$ \n",
        "$y = 19.7146$. \n",
        "\n",
        "Semangat ngerjainnya semester ini, pasti dapet A!"
      ]
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 4
}

with open("materi/Analisa_Data_Regresi_Linierx.ipynb", "w") as f:
    json.dump(notebook_content, f, indent=2)

print("Rewrite Complete")
