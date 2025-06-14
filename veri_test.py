import sqlite3

def ogrenci_bilgilerini_getir(ogrenci_id):
    conn = sqlite3.connect('kocluk_takip.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ogrenciler WHERE id = ?", (ogrenci_id,))
    ogrenci = cursor.fetchone()
    conn.close()

    if ogrenci:
        print("Öğrenci Bilgileri Giriniz:")
        print(f"ID: {ogrenci[0]}")
        print(f"Ad: {ogrenci[1]}")
        print(f"Soyad: {ogrenci[2]}")
        print(f"Yaş: {ogrenci[3]}")
        print(f"Hedefleriniz: {ogrenci[4]}")
    else:
        print("Öğrenci bulunamadı kardesim.")

def seans_bilgilerini_getir(ogrenci_id):
    conn = sqlite3.connect('kocluk_takip.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seanslar WHERE ogrenci_id = ?", (ogrenci_id,))
    seanslar = cursor.fetchall()
    conn.close()

    if seanslar:
        print("Seanslar:")
        for seans in seanslar:
            print(f"Seans ID: {seans[0]}")
            print(f"Tarih: {seans[2]}")
            print(f"Hedefler: {seans[3]}")
            print(f"Notlar: {seans[4]}")
            print("---")
    else:
        print("Bu öğrenci için seans bulunamadı.")

if __name__ == "__main__":
    # Örnek Veri Testi
    ogrenci_bilgilerini_getir(1)
    seans_bilgilerini_getir(1)
