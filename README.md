# Kelime Defteri

İngilizce öğrenirken yeni kelimeleri bir deftere yazarız ama çoğu zaman tekrar etmeyiz, bu yüzden unuturuz.
**Kelime Defteri**, öğrendiğin İngilizce kelimeleri anlamlarıyla birlikte kaydeden ve sonra sana bir oyun gibi
"Bu kelimenin anlamı ne?" diye soran, terminalde çalışan küçük bir uygulamadır.

**Kimin için?** İngilizce kelime dağarcığını geliştirmek isteyen, hızlı ve internetsiz tekrar yapmak isteyen öğrenciler.

## Proje panosu

Pano: https://github.com/users/emirgenc35/projects/3

## Çalıştırma

Gereksinim: Python 3.8+ (ek kütüphane yok)

```bash
git clone https://github.com/emirgenc35/kelime-defteri.git
cd kelime-defteri
python3 kelime_defteri.py
```

Windows'ta `python3` yerine `python` yazın.

## Özellikleri deneme

### 1. Kelime ekleme ve listeleme
1. Programı çalıştırın, menüden `1` seçin.
2. Kelime olarak `orange`, anlam olarak `portakal` yazın.
3. `0` ile çıkın, programı tekrar açın ve `2` seçin.
4. **Beklenen:** Listede `orange - portakal` görünür (kelimeler `kelimeler.json` dosyasında saklanır).

### 2. Anlam bulma oyunu
Depoda hazır 100 örnek kelime var, her oyunda rastgele 5 tanesi sorulur.
1. Programı çalıştırın, menüden `3` seçin.
2. Sorulan 5 kelimenin Türkçe anlamını yazın (örn. `book` → `kitap`).
3. **Beklenen:** Her cevaptan sonra doğru/yanlış yazar, sonunda `Skor: x/5` gösterilir. Büyük/küçük harf fark etmez.
