# ❄️ Soğuk Kalpli Kraliçe ❄️

Bu proje, **Python** ve **PgZero** kullanılarak geliştirilmiş basit bir **yılbaşı temalı kaçış oyunudur**. Oyunda Kar Kraliçesi tarafından atılan kar/buz toplarından kaçmaya çalışırız. Bize değen her buz topu canımızı azaltır. Canımız bittiğinde oyun sona erer.

---

## 🎮 Oyun Hikâyesi

Soğuk bir kış gecesinde, **Soğuk Kalpli Kar Kraliçesi** şatosunu korumak için gökyüzünden buz topları fırlatmaktadır.  
Biz ise bu tehlikeli buz toplarından **sağa ve sola hareket ederek kaçmaya çalışırız**.  
Her çarpışmada canımız azalır ve canımız sıfıra düştüğünde oyun kaybedilir.

---

## 🕹️ Oynanış

- Karakter sağa ve sola hareket edebilir.
- Yukarıdan rastgele buz topları düşer.
- Buz topları karaktere çarptığında can azalır.
- Can 0 olursa oyun biter.
- Oyunu yeniden başlatmak mümkündür.

---

## 🎯 Kontroller

| Tuş | İşlev |
|----|------|
| ⬅️ Sol Ok | Sola hareket |
| ➡️ Sağ Ok | Sağa hareket |
| 🖱️ Fare | Menü ve yeniden başlatma |

---

## 🧠 Oyun Modları

- **Start Menu**: Oyunun başladığı ekran
- **Game**: Oynanış ekranı
- **Game Over**: Can bittiğinde çıkan ekran

---

## 🛠️ Kullanılan Teknolojiler

- **Python 3**
- **PgZero**
- **Pygame**
- Rastgele buz topu üretimi (`random`)

---

## 📁 Proje Yapısı

- `main.py` : Oyunun ana kod dosyası
- `images/` : Oyun görselleri (arka plan, karakter, düşman, buz topları vb.)
- `sounds/` : Oyun müzikleri ve ses efektleri

---

## 🚀 Çalıştırma

1. Python yüklü olmalıdır.
2. PgZero kurulu değilse:
   ```bash
   pip install pgzero
