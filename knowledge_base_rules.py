# ============================================
#  ISI KNOWLEDGE BASE SISTEM PAKAR IT2FLS 
# ============================================

KNOWLEDGE_BASE = [
    # ---------------------------------------------------------
    # RULE PREDIKSI: BBLR
    # ---------------------------------------------------------
    {
        'rule_id'   : 1,
        'prediksi'  : 'BBLR',
        'antecedent': [
            {'variabel': 'ibu_Hb', 'kategori': ['Tidak Anemia']},
            {'variabel': 'ibu_Usia Ibu', 'kategori': ['Berisiko Tua']},
            {'variabel': 'kunjungan_anc_total', 'kategori': ['Tidak Lengkap']},
        ]
    },
    {
        'rule_id'   : 2,
        'prediksi'  : 'BBLR',
        'antecedent': [
            {'variabel': 'ibu_Hb', 'kategori': ['Tidak Anemia']},
            {'variabel': 'ibu_Usia Ibu', 'kategori': ['Berisiko Tua']},
            {'variabel': 'jarak_kehamilan_bulan', 'kategori': ['Berisiko Dekat']},
        ]
    },
    {
        'rule_id'   : 3,
        'prediksi'  : 'BBLR',
        'antecedent': [
            {'variabel': 'ibu_IMT', 'kategori': ['BB Kurang']},
            {'variabel': 'ibu_Usia Ibu', 'kategori': ['Berisiko Muda']},
            {'variabel': 'LILA_angka', 'kategori': ['KEK']},
        ]
    },
    {
        'rule_id'   : 4,
        'prediksi'  : 'BBLR',
        'antecedent': [
            {'variabel': 'ibu_Hb', 'kategori': ['Tidak Anemia']},
            {'variabel': 'ibu_IMT', 'kategori': ['BB Kurang']},
            {'variabel': 'ibu_Usia Ibu', 'kategori': ['Berisiko Tua']},
            {'variabel': 'jarak_kehamilan_bulan', 'kategori': ['Berisiko Dekat']},
            {'variabel': 'kunjungan_anc_total', 'kategori': ['Tidak Lengkap']},
        ]
    },
    {
        'rule_id'   : 5,
        'prediksi'  : 'BBLR',
        'antecedent': [
            {'variabel': 'ibu_Hb', 'kategori': ['Tidak Anemia']},
            {'variabel': 'ibu_Usia Ibu', 'kategori': ['Berisiko Tua']},
            {'variabel': 'jarak_kehamilan_bulan', 'kategori': ['Berisiko Dekat']},
            {'variabel': 'kunjungan_anc_total', 'kategori': ['Tidak Lengkap']},
        ]
    },
    {
        'rule_id'   : 6,
        'prediksi'  : 'BBLR',
        'antecedent': [
            {'variabel': 'ibu_Hb', 'kategori': ['Tidak Anemia']},
            {'variabel': 'ibu_Usia Ibu', 'kategori': ['Berisiko Tua']},
            {'variabel': 'jarak_kehamilan_bulan', 'kategori': ['Berisiko Dekat']},
            {'variabel': 'ibu_Kehamilan Ke-', 'kategori': ['Grandemultipara']},
            {'variabel': 'kunjungan_anc_total', 'kategori': ['Tidak Lengkap']},
        ]
    },
    {
        'rule_id'   : 7,
        'prediksi'  : 'BBLR',
        'antecedent': [
            {'variabel': 'ibu_Hb', 'kategori': ['Tidak Anemia']},
            {'variabel': 'ibu_Usia Ibu', 'kategori': ['Berisiko Tua']},
            {'variabel': 'jarak_kehamilan_bulan', 'kategori': ['Berisiko Jauh']},
            {'variabel': 'kunjungan_anc_total', 'kategori': ['Tidak Lengkap']},
            {'variabel': 'LILA_angka', 'kategori': ['KEK']},
        ]
    },
    {
        'rule_id'   : 8,
        'prediksi'  : 'BBLR',
        'antecedent': [
            {'variabel': 'ibu_Hb', 'kategori': ['Anemia']},
            {'variabel': 'ibu_Usia Ibu', 'kategori': ['Tidak Berisiko', 'Berisiko Tua']},
        ]
    },

    # TAMBAHAN ATURAN DARI PAKAR UNTUK BBLR
    {
        'rule_id'   : 9,
        'prediksi'  : 'BBLR',
        'antecedent': [
            {'variabel': 'LILA_angka', 'kategori': ['KEK']},
        ]
    },

    {
        'rule_id'   : 10,
        'prediksi'  : 'BBLR',
        'antecedent': [
            {'variabel': 'ibu_Hb', 'kategori': ['Anemia']},
        ]
    },

    {
        'rule_id'   : 11,
        'prediksi'  : 'BBLR',
        'antecedent': [
            {'variabel': 'LILA_angka', 'kategori': ['KEK']},
            {'variabel': 'ibu_Hb', 'kategori': ['Anemia']},
        ]
    },

    # ---------------------------------------------------------
    # RULE PREDIKSI: NORMAL
    # ---------------------------------------------------------
    {
        'rule_id'   : 12,
        'prediksi'  : 'NORMAL',
        'antecedent': [
            {'variabel': 'ibu_IMT', 'kategori': ['BB Lebih', 'Obesitas']},
            {'variabel': 'ibu_Usia Ibu', 'kategori': ['Tidak Berisiko']},
            {'variabel': 'LILA_angka', 'kategori': ['Normal']},
        ]
    },
    {
        'rule_id'   : 13,
        'prediksi'  : 'NORMAL',
        'antecedent': [
            {'variabel': 'ibu_IMT', 'kategori': ['BB Normal']},
            {'variabel': 'ibu_Usia Ibu', 'kategori': ['Berisiko Muda']},
            {'variabel': 'LILA_angka', 'kategori': ['Normal']},
        ]
    },
    {
        'rule_id'   : 14,
        'prediksi'  : 'NORMAL',
        'antecedent': [
            {'variabel': 'ibu_Usia Ibu', 'kategori': ['Berisiko Muda', 'Tidak Berisiko']},
            {'variabel': 'LILA_angka', 'kategori': ['Normal']},
            # # TAMBAHAN DARI PAKAR
            {'variabel': 'ibu_Hb', 'kategori': ['Tidak Anemia']},

        ]
    },
    {
        'rule_id'   : 15,
        'prediksi'  : 'NORMAL',
        'antecedent': [
            {'variabel': 'ibu_Usia Ibu', 'kategori': ['Tidak Berisiko']},
            # # TAMBAHAN DARI PAKAR
            {'variabel': 'LILA_angka', 'kategori': ['Normal']},
            {'variabel': 'ibu_Hb', 'kategori': ['Tidak Anemia']},
        ]
    },
    {
        'rule_id'   : 16,
        'prediksi'  : 'NORMAL',
        'antecedent': [
            {'variabel': 'ibu_Hb', 'kategori': ['Tidak Anemia']},
            {'variabel': 'ibu_IMT', 'kategori': ['BB Normal']},
            {'variabel': 'ibu_Usia Ibu', 'kategori': ['Tidak Berisiko']},
            {'variabel': 'ibu_statusImunisasi_encoded', 'kategori': ['TT Lengkap']},
            {'variabel': 'kunjungan_anc_total', 'kategori': ['Lengkap']},
        ]
    },
    {
        'rule_id'   : 17,
        'prediksi'  : 'NORMAL',
        'antecedent': [
            {'variabel': 'ibu_Hb', 'kategori': ['Tidak Anemia']},
            {'variabel': 'ibu_IMT', 'kategori': ['BB Lebih']},
            {'variabel': 'ibu_Usia Ibu', 'kategori': ['Tidak Berisiko']},
            {'variabel': 'ibu_statusImunisasi_encoded', 'kategori': ['TT Lengkap']},
        ]
    },
    {
        'rule_id'   : 18,
        'prediksi'  : 'NORMAL',
        'antecedent': [
            {'variabel': 'ibu_Hb', 'kategori': ['Tidak Anemia']},
            {'variabel': 'ibu_Usia Ibu', 'kategori': ['Tidak Berisiko']},
            {'variabel': 'jarak_kehamilan_bulan', 'kategori': ['Tidak Berisiko']},
            {'variabel': 'ibu_Kehamilan Ke-', 'kategori': ['Multigravida']},
            {'variabel': 'kunjungan_anc_total', 'kategori': ['Lengkap']},
        ]
    },
    {
        'rule_id'   : 19,
        'prediksi'  : 'NORMAL',
        'antecedent': [
            {'variabel': 'ibu_Hb', 'kategori': ['Tidak Anemia']},
            {'variabel': 'ibu_Usia Ibu', 'kategori': ['Tidak Berisiko']},
            {'variabel': 'jarak_kehamilan_bulan', 'kategori': ['Tidak Berisiko']},
            {'variabel': 'ibu_Kehamilan Ke-', 'kategori': ['Multigravida']},
            {'variabel': 'kunjungan_anc_total', 'kategori': ['Lengkap']},
            {'variabel': 'LILA_angka', 'kategori': ['Normal']},
        ]
    },
]