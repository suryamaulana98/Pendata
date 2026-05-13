import json

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Analisa Data Menggunakan Random Forest (Dataset Play Tennis)\n",
                "\n",
                "Jupyter notebook ini berisi penjelasan mengenai analisis data menggunakan algoritma Random Forest untuk dataset *Play Tennis*. Analisis ini mengacu pada tahapan alur (workflow) di KNIME Analytics Platform, serta implementasi kodenya menggunakan Python.\n",
                "\n",
                "## Alur KNIME (Workflow)\n",
                "\n",
                "Berikut adalah penjelasan untuk setiap node yang digunakan di KNIME berdasarkan gambar yang Anda berikan:\n",
                "\n",
                "1. **Excel Reader**\n",
                "   Node ini berfungsi untuk membaca dataset berformat `.xlsx` (dalam hal ini `play_tennis_knime.xlsx`). Node akan memuat data ke dalam *workflow* agar siap diproses.\n",
                "   > *(Silakan tambahkan gambar / hasil dari node Excel Reader di sini)*\n",
                "\n",
                "2. **Table Partitioner**\n",
                "   Node ini digunakan untuk membagi (partitioning) dataset menjadi dua bagian, yaitu data latih (training data) dan data uji (testing data). Misalnya, proporsi 80% untuk latih dan 20% untuk uji.\n",
                "   > *(Silakan tambahkan gambar konfigurasi / hasil pembagian di sini)*\n",
                "\n",
                "3. **Random Forest Learner**\n",
                "   Node ini merupakan inti untuk melatih (training) model machine learning menggunakan algoritma Random Forest. Algoritma ini akan membangun sekumpulan pohon keputusan (Decision Trees) berdasarkan **data latih**.\n",
                "   > *(Silakan tambahkan gambar model/pohon yang terbentuk di sini)*\n",
                "\n",
                "4. **Random Forest Predictor**\n",
                "   Setelah model belajar pada tahap sebelumnya, node ini akan menerima model dari Learner dan mengaplikasikannya terhadap **data uji**. Node ini menghasilkan prediksi (misalnya prediksi apakah akan bermain tenis atau tidak).\n",
                "   > *(Silakan tambahkan hasil dari prediksi di sini)*\n",
                "\n",
                "5. **Scorer**\n",
                "   Node terakhir ini bertugas mengevaluasi kinerja dan kualitas model. Ia membandingkan hasil kelas aktual dari data uji dengan kelas tebakan (prediksi), lalu menghasilkan metrik performa seperti **Akurasi (Accuracy)** dan matriks kebingungan (Confusion Matrix).\n",
                "   > *(Silakan tambahkan gambar metrik evaluasi/Scorer di sini)*\n",
                "\n",
                "---\n",
                "\n",
                "## Implementasi dengan Python"
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "outputs": [],
            "source": [
                "import pandas as pd\n",
                "import numpy as np\n",
                "from sklearn.model_selection import train_test_split\n",
                "from sklearn.ensemble import RandomForestClassifier\n",
                "from sklearn.metrics import accuracy_score, classification_report, confusion_matrix\n",
                "from sklearn.preprocessing import LabelEncoder"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 1 & 2. Excel Reader dan Pre-processing Sederhana\n",
                "Membaca file data 'play_tennis_knime.xlsx'. Karena dataset *Play Tennis* umumnya berupa kategorikal (teks), algoritma di scikit-learn membutuhkan format numerik, sehingga kita mengonversinya (Label Encoding)."
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "outputs": [],
            "source": [
                "# Mengasumsikan file ada di direktori yang sama\n",
                "# df = pd.read_excel('play_tennis_knime.xlsx')\n",
                "\n",
                "# Karena kita belum meload file excel secara langsung di code ini, kita buat dummy struktur dataset *Play Tennis* \n",
                "data = {\n",
                "    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast','Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],\n",
                "    'Temperature': ['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild'],\n",
                "    'Humidity': ['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal','Normal','High','Normal','High'],\n",
                "    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Strong'],\n",
                "    'PlayTennis': ['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']\n",
                "}\n",
                "df = pd.DataFrame(data)\n",
                "print(\"Tampilan Awal Dataset:\")\n",
                "print(df.head())\n",
                "\n",
                "# --- Label Encoding (Prapemrosesan) ---\n",
                "le = LabelEncoder()\n",
                "df['Outlook'] = le.fit_transform(df['Outlook'])\n",
                "df['Temperature'] = le.fit_transform(df['Temperature'])\n",
                "df['Humidity'] = le.fit_transform(df['Humidity'])\n",
                "df['Wind'] = le.fit_transform(df['Wind'])\n",
                "df['PlayTennis'] = le.fit_transform(df['PlayTennis'])\n",
                "\n",
                "X = df.drop('PlayTennis', axis=1)\n",
                "y = df['PlayTennis']\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 3. Table Partitioner \n",
                "Sama seperti Table Partitioner di KNIME, kita bagi menjadi Data Latih dan Data Uji (80% / 20%)."
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "outputs": [],
            "source": [
                "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 4 & 5. Random Forest Learner & Predictor\n",
                "Melatih model Random Forest menggunakan fungsi Fit, lalu melakukan predisksi menggunakan Predict."
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "outputs": [],
            "source": [
                "model = RandomForestClassifier(n_estimators=100, random_state=42)\n",
                "# Evaluasi seperti model Learner (melatih data)\n",
                "model.fit(X_train, y_train)\n",
                "\n",
                "# Menghasilkan input seperti Random Forest Predictor\n",
                "y_pred = model.predict(X_test)\n",
                "print(\"Prediksi:\", y_pred)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### 6. Scorer\n",
                "Mengukur akurasi dan kinerja model akhir."
            ]
        },
        {
            "cell_type": "code",
            "metadata": {},
            "execution_count": None,
            "outputs": [],
            "source": [
                "print(\"Akurasi Model:\", accuracy_score(y_test, y_pred))\n",
                "print(\"\\nClassification Report:\\n\", classification_report(y_test, y_pred))\n",
                "print(\"\\nConfusion Matrix:\\n\", confusion_matrix(y_test, y_pred))"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("materi/analisa-data-menggunakan-random-forest.ipynb", "w") as f:
    json.dump(notebook, f, indent=2)
