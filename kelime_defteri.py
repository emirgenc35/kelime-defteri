"""Kelime Defteri: İngilizce kelimeleri kaydet, listele ve kendini test et."""

import json
import os

DOSYA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kelimeler.json")


def yukle():
    """Kelimeleri dosyadan okur. Dosya yoksa boş defter döner."""
    if not os.path.exists(DOSYA):
        return {}
    with open(DOSYA, encoding="utf-8") as f:
        return json.load(f)


def kaydet(defter):
    """Defteri dosyaya yazar."""
    with open(DOSYA, "w", encoding="utf-8") as f:
        json.dump(defter, f, ensure_ascii=False, indent=2)


def kelime_ekle(defter):
    kelime = input("İngilizce kelime: ").strip().lower()
    anlam = input("Türkçe anlamı: ").strip().lower()
    if not kelime or not anlam:
        print("Kelime ve anlam boş olamaz.")
        return
    if kelime in defter:
        print(f"'{kelime}' zaten vardı, anlamı güncellendi.")
    defter[kelime] = anlam
    kaydet(defter)
    print(f"Eklendi: {kelime} - {anlam}")


def kelimeleri_listele(defter):
    if not defter:
        print("Defter boş. Önce kelime ekleyin.")
        return
    print(f"\n--- Defterdeki kelimeler ({len(defter)}) ---")
    for kelime, anlam in sorted(defter.items()):
        print(f"  {kelime} - {anlam}")


def main():
    defter = yukle()
    while True:
        print("\n=== KELİME DEFTERİ ===")
        print("1) Kelime ekle")
        print("2) Kelimeleri listele")
        print("0) Çıkış")
        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            kelime_ekle(defter)
        elif secim == "2":
            kelimeleri_listele(defter)
        elif secim == "0":
            print("Görüşmek üzere!")
            break
        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    main()
