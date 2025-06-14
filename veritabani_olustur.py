import sqlite3

def veritabani_olustur():
    # Veritabanı bağlantısı
    conn = sqlite3.connect('kocluk_uygulamasi.db')
    c = conn.cursor()

    # Öğrenci Tablosu
    c.execute('''
        CREATE TABLE IF NOT EXISTS ogrenciler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kullanici_adi TEXT UNIQUE NOT NULL,
            ad TEXT NOT NULL,
            soyad TEXT NOT NULL,
            yas INTEGER NOT NULL,
            hedefler TEXT NOT NULL
        )
    ''')

    # Seans Tablosu
    c.execute('''
        CREATE TABLE IF NOT EXISTS seanslar (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ogrenci_id INTEGER NOT NULL,
            seans_tarihi TEXT NOT NULL,
            hedefler TEXT NOT NULL,
            notlar TEXT,
            FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler(id)
        )
    ''')

    # Ders ve Soru Çözüm Tablosu
    c.execute('''
        CREATE TABLE IF NOT EXISTS ders_soru_cozum (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ogrenci_id INTEGER NOT NULL,
            ders_ad TEXT NOT NULL,
            konu TEXT NOT NULL,
            soru_sayisi INTEGER NOT NULL,
            dogru_sayisi INTEGER NOT NULL,
            yanlis_sayisi INTEGER NOT NULL,
            FOREIGN KEY (ogrenci_id) REFERENCES ogrenciler(id)
        )
    ''')

    # Bağlantıyı kaydet
    conn.commit()
    conn.close()

# Veritabanı oluşturma işlemi
if __name__ == "__main__":
    veritabani_olustur()
