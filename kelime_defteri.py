import json
import os
import random

DOSYA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kelimeler.json")
SORU_SAYISI = 5


def yukle():
    if not os.path.exists(DOSYA):
        return {}
    with open(DOSYA, encoding="utf-8") as f:
        return json.load(f)


def kaydet(defter):
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


def oyun(defter):
    if len(defter) < SORU_SAYISI:
        print(f"Oyun için en az {SORU_SAYISI} kelime gerekli. Şu an {len(defter)} kelime var.")
        return

    sorular = random.sample(list(defter.keys()), SORU_SAYISI)
    dogru = 0
    print(f"\n--- Anlam bulma oyunu ({SORU_SAYISI} soru) ---")
    for i, kelime in enumerate(sorular, 1):
        cevap = input(f"{i}) '{kelime}' kelimesinin anlamı nedir? ").strip().lower()
        if cevap == defter[kelime]:
            print("Doğru!")
            dogru += 1
        else:
            print(f"Yanlış. Doğru cevap: {defter[kelime]}")

    print(f"\nSkor: {dogru}/{SORU_SAYISI}")


def main():
    defter = yukle()
    while True:
        print("\n=== KELİME DEFTERİ ===")
        print("1) Kelime ekle")
        print("2) Kelimeleri listele")
        print("3) Oyun oyna")
        print("0) Çıkış")
        secim = input("Seçiminiz: ").strip()

        if secim == "1":
            kelime_ekle(defter)
        elif secim == "2":
            kelimeleri_listele(defter)
        elif secim == "3":
            oyun(defter)
        elif secim == "0":
            print("Görüşmek üzere!")
            break
        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    main()
