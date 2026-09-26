# Sistem Pakar BBLR menggunakan IT2FLS

**Prediksi Bayi Berat Lahir Rendah (BBLR) berbasis Interval Type-2 Fuzzy Logic System**

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen)]()

---

## 📋 Daftar Isi
- [Tentang Proyek](#tentang-proyek)
- [Fitur Utama](#fitur-utama)
- [Teknologi yang Digunakan](#teknologi-yang-digunakan)
- [Persyaratan Sistem](#persyaratan-sistem)
- [Instalasi](#instalasi)
- [Struktur Proyek](#struktur-proyek)
- [Dataset](#dataset)
- [Penggunaan](#penggunaan)
- [Knowledge Base & Rules](#knowledge-base--rules)
- [Hasil & Evaluasi](#hasil--evaluasi)
- [Kontributor](#kontributor)

---

## 📖 Tentang Proyek

Sistem Pakar BBLR adalah aplikasi berbasis **Interval Type-2 Fuzzy Logic System (IT2FLS)** yang dirancang untuk memprediksi risiko **Bayi Berat Lahir Rendah (BBLR)** berdasarkan data kesehatan ibu hamil. 

BBLR merupakan kondisi medis serius yang memerlukan penanganan khusus. Proyek ini mengintegrasikan:
- **19 aturan (rules) IF-THEN** dari pakar medis
- **Fuzzy Logic** untuk menangani ketidakpastian dalam data klinis
- **Machine Learning** untuk validasi dan optimasi model

---

## ✨ Fitur Utama

- ✅ **Prediksi Berbasis Pakar**: 19 rules dikembangkan bersama ahli kesehatan
- ✅ **IT2FLS (Interval Type-2 Fuzzy Logic)**: Menangani ketidakpastian dan variabilitas data
- ✅ **Multiple Variables**: 8+ variabel kesehatan ibu hamil
- ✅ **Validasi Pakar**: Lembar validasi dari ahli medis
- ✅ **Comprehensive Testing**: Confusion matrix dan performance metrics
- ✅ **Decision Tree Visualization**: Visualisasi pengambilan keputusan

### Variabel Input Sistem:
| Variabel | Kategori | Keterangan |
|----------|----------|-----------|
| Hemoglobin (Hb) | Anemia / Tidak Anemia | Status anemia ibu |
| IMT | BB Kurang / Normal / BB Lebih / Obesitas | Indeks Massa Tubuh |
| LILA | KEK / Normal | Lingkar Lengan Atas (gizi ibu) |
| Usia Ibu | Berisiko Muda / Tidak Berisiko / Berisiko Tua | Kategori usia kehamilan |
| ANC Kunjungan | Lengkap / Tidak Lengkap | Antenatal Care |
| Jarak Kehamilan | Berisiko Dekat / Tidak Berisiko / Berisiko Jauh | Jarak antar kehamilan |
| Kehamilan Ke- | Primigravida / Multigravida / Grandemultipara | Jumlah kehamilan |
| Status Imunisasi | TT Lengkap / TT Tidak Lengkap | Vaksinasi tetanus |

### Output Prediksi:
- 🔴 **BBLR** (Bayi Berat Lahir Rendah) - Memerlukan intervensi khusus
- 🟢 **NORMAL** - Berat lahir normal

---

## 🛠️ Teknologi yang Digunakan

| Komponen | Teknologi | Versi |
|----------|-----------|-------|
| **Bahasa Pemrograman** | Python | 3.11+ |
| **Environment** | Jupyter Notebook | - |
| **Data Processing** | Pandas, NumPy | Latest |
| **ML/AI** | scikit-learn | - |
| **Fuzzy Logic** | IT2FLS | Custom Implementation |
| **Visualisasi** | Matplotlib, Seaborn | - |
| **Data Storage** | Excel (.xlsx) | - |

---

## 📋 Persyaratan Sistem

- **OS**: Windows, macOS, atau Linux
- **Python**: 3.11 atau lebih baru
- **Memory**: Minimal 4GB RAM
- **Disk**: 500MB untuk virtual environment dan dependencies

---

## 🚀 Instalasi

### 1. Clone Repository
```bash
git clone <repository-url>
cd Skripsi
```

### 2. Buat Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

Jika file `requirements.txt` belum ada, install packages berikut:
```bash
pip install jupyter pandas numpy scikit-learn matplotlib seaborn openpyxl scipy
```

### 4. Jalankan Jupyter Notebook
```bash
jupyter notebook SistemPakarBBLR.ipynb
```

---

## 📁 Struktur Proyek

```
Skripsi/
├── README.md                                    # Dokumentasi proyek
├── .gitignore                                   # Git ignore rules
│
├── SistemPakarBBLR.ipynb                        # Main notebook - Implementasi sistem pakar
├── knowledge_base_rules.py                      # Knowledge base dengan 19 rules IF-THEN
│
├── dataset/                                     # Data training & testing
│   ├── 03OtakatikGabunganRill.xlsx              # Dataset gabungan
│   ├── 4NewData_Ibu_Hamil_FINAL_CLEAN.xlsx     # Dataset ibu hamil (cleaned)
│   └── testingFinal/                            # Testing dataset
│       └── 13. Laporan_HasilAkhir_Testing_...   # Hasil testing final
│
├── excel/                                       # Output & laporan
│   ├── Data_Ibu_Hamil_BBLR_CLEAN_FINAL.xlsx    # Data BBLR final
│   ├── Hasil_TestingFinal_20Data.xlsx           # Hasil testing 20 data
│   ├── AutoTestingLaporan_Hasil_Testing_...     # Laporan testing otomatis
│   ├── lembar_validasi_pakar.xlsx               # Lembar validasi ahli
│   ├── parameter_it2_hybrid.xlsx                # Parameter IT2 hybrid
│   └── rules_if_then_final.xlsx                 # Kumpulan rules final
│
├── images/                                      # Visualisasi & grafik
│   ├── confusion_matrix.png                     # Confusion matrix hasil
│   ├── decision_tree_full.png                   # Pohon keputusan
│   ├── decision_tree_full.svg                   # Format SVG
│   └── [visualisasi lainnya]
│
└── venv/                                        # Virtual environment (ignored)
```

---

## 📊 Dataset

### Sumber Data
- **Jumlah Record**: 600+ data ibu hamil
- **Tahun Pengumpulan**: 2024-2025
- **Status**: Cleaned dan validated

### File Dataset Utama
- `4NewData_Ibu_Hamil_FINAL_CLEAN.xlsx`: Dataset training & validation (final dan clean)
- `03OtakatikGabunganRill.xlsx`: Dataset gabungan dari berbagai sumber
- `testingFinal/`: Dataset testing untuk evaluasi model final

### Struktur Data
Setiap record berisi:
```
ID | Nama | Usia | IMT | Hb | LILA | ANC_Total | Jarak_Kehamilan | 
Kehamilan_Ke | Status_Imunisasi | Hasil_Prediksi | Confidence
```

---

## 💻 Penggunaan

### Quick Start
1. Buka dan jalankan `SistemPakarBBLR.ipynb` di Jupyter Notebook
2. Ikuti cell-by-cell untuk:
   - Load data
   - Initialize IT2FLS model
   - Training & testing
   - Evaluasi hasil

### Prediksi Manual
```python
from knowledge_base_rules import KNOWLEDGE_BASE

# Input data ibu hamil
patient_data = {
    'ibu_Hb': 'Tidak Anemia',
    'ibu_Usia Ibu': 'Tidak Berisiko',
    'ibu_IMT': 'BB Normal',
    'LILA_angka': 'Normal',
    'kunjungan_anc_total': 'Lengkap',
    'jarak_kehamilan_bulan': 'Tidak Berisiko',
    'ibu_Kehamilan Ke-': 'Multigravida',
    'ibu_statusImunisasi_encoded': 'TT Lengkap'
}

# Output: NORMAL atau BBLR dengan confidence level
```

### Command Line Testing (jika tersedia)
```bash
python test_system.py --input <patient_data.json>
```

---

## 📚 Knowledge Base & Rules

### Struktur Rule
```python
{
    'rule_id': 1,
    'prediksi': 'BBLR',  # Output: BBLR atau NORMAL
    'antecedent': [      # Kondisi IF
        {'variabel': 'ibu_Hb', 'kategori': ['Tidak Anemia']},
        {'variabel': 'ibu_Usia Ibu', 'kategori': ['Berisiko Tua']},
        # ... kondisi lainnya
    ]
}
```

### Total Rules: 19
- **11 Rules untuk BBLR** (Rule ID: 1-11)
- **8 Rules untuk NORMAL** (Rule ID: 12-19)

### Contoh Rule BBLR
```
Rule 10: IF Hemoglobin = Anemia THEN Prediksi = BBLR
```

### Contoh Rule NORMAL
```
Rule 12: IF IMT = (BB Lebih/Obesitas) AND Usia = Tidak Berisiko 
         AND LILA = Normal THEN Prediksi = NORMAL
```

**Sumber Rules**: Dikembangkan berdasarkan expert knowledge dari praktisi kesehatan dan literature review mengenai faktor risiko BBLR.

---

## 📈 Hasil & Evaluasi

### Performance Metrics
- **Accuracy**: Lihat di `Hasil_TestingFinal_20Data.xlsx`
- **Sensitivity/Recall**: Kemampuan mendeteksi kasus BBLR
- **Specificity**: Kemampuan mendeteksi kasus NORMAL
- **Precision**: Keakuratan prediksi positif

### Validation Results
- ✅ Lembar validasi pakar tersedia di `lembar_validasi_pakar.xlsx`
- ✅ Confusion matrix: `images/confusion_matrix.png`
- ✅ Decision tree visualization: `images/decision_tree_full.png`

### Testing Dataset
- **20 data** testing final dengan hasil tracking

---

## 👥 Kontributor

- **Developer**: Afif Imam Rahadi
- **Expert Advisor**: Praktisi kesehatan & ahli gizi
- **Validator**: Pakar kesehatan (Ibu Hamil & BBLR)

---

## 📄 Lisensi

Proyek ini **belum memiliki lisensi**. Proyek dibuat sebagai bagian dari penelitian skripsi, dan seluruh hak cipta dipegang oleh penulis.

Tanpa izin tertulis dari penulis, kode dan data dalam repository ini tidak boleh disalin, diubah, atau didistribusikan ulang. Jika ingin menggunakan sebagian isi proyek ini, silakan hubungi penulis melalui kontak di bawah.

---

## 📞 Kontak & Support

Untuk pertanyaan atau saran:
- 📧 Email: [afif0901rahadi@gmail.com](mailto:afif0901rahadi@gmail.com)
- 📌 Issues: Silakan buka issue di repository ini

---

## 🔗 Referensi

### Materi Terkait BBLR
- WHO Guidelines on Low Birth Weight (LBW)
- CDC - Low Birth Weight & Prematurity
- Panduan Nasional Pelayanan Kesehatan Ibu & Bayi Baru Lahir

### Fuzzy Logic & IT2FLS
- Interval Type-2 Fuzzy Logic Systems
- Mendel, J.M. (2007). "Advances in Type-2 Fuzzy Sets and Systems"
- Karnik, U.N., & Mendel, J.M. (1998). "An Introduction to Type-2 Fuzzy Logic Systems"

---

## ✅ Checklist Pengembangan

- [x] Data cleaning & preparation
- [x] Rule elicitation & validation
- [x] IT2FLS implementation
- [x] Model training & testing
- [x] Performance evaluation
- [x] Documentation
- [ ] Deployment ke production (opsional)
- [ ] API development (opsional)

---

**Last Updated**: September 2026  
**Status**: ✅ Aktif & Ready for Use
