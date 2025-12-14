# cpu-zamanlama-projesi
İşletim Sistemleri dersi CPU zamanlama algoritmaları proje ödevi

## 🌐 Etkileşimli Proje Raporu

# CPU Zamanlama Algoritmaları Projesi

Bu proje, **İşletim Sistemleri** dersi kapsamında CPU zamanlama algoritmalarının performans analizini yapmak amacıyla geliştirilmiştir. Python dili kullanılarak farklı zamanlama algoritmaları uygulanmış, **Case1 ve Case2** senaryoları altında karşılaştırmalı sonuçlar elde edilmiştir.

---

## 📌 Projenin Amacı

Bu çalışmanın amacı, farklı CPU zamanlama algoritmalarının:

* Bekleme süreleri
* Dönüş süreleri
* İşlemci verimliliği
* Throughput değerleri
* Context switch maliyetleri

üzerindeki etkilerini incelemek ve karşılaştırmaktır.

---

## ⚙️ Kullanılan Zamanlama Algoritmaları

Projede aşağıdaki algoritmalar uygulanmıştır:

* **FCFS (First Come First Served)**
* **SJF (Shortest Job First – Preemptive)**
* **SJF (Shortest Job First – Non-Preemptive)**
* **Round Robin (RR)**
* **Priority Scheduling (Preemptive)**
* **Priority Scheduling (Non-Preemptive)**

---

## 🧪 Senaryolar (Case1 & Case2)

* **Case1:** Düşük yoğunluklu işlem senaryosu
* **Case2:** Yüksek yoğunluklu ve karmaşık işlem senaryosu

Her iki senaryo için algoritmalar ayrı ayrı çalıştırılmış ve sonuçlar tablolar halinde raporlanmıştır.

---

## 📂 Proje Dosya Yapısı

```text
cpu-scheduling-project/
├─ main.py              # CPU zamanlama algoritmaları
├─ processes.csv        # Giriş veri seti (process listesi)
├─ README.md            # Proje açıklaması
├─ index.html           # Etkileşimli web proje raporu
└─ docs/
   ├─ kullanici_kilavuzu.pdf
   └─ proje_raporu.pdf
```

---

## ▶️ Projenin Çalıştırılması

1. Gerekli kütüphaneleri kurun:

```bash
pip install -r requirements.txt
```

2. Programı çalıştırın:

```bash
python main.py
```

3. Sonuçlar `.txt` dosyaları olarak oluşturulacaktır.

---

## 📊 Başarım Kriterleri

Her algoritma için aşağıdaki metrikler hesaplanmıştır:

* Ortalama bekleme süresi
* Maksimum bekleme süresi
* Ortalama dönüş süresi
* Maksimum dönüş süresi
* Throughput (50, 100, 150, 200 zaman birimi)
* CPU verimliliği
* Context switch sayısı

Sonuçlar proje raporunda tablo ve yorumlar ile sunulmuştur.

---

## 🌐 Etkileşimli Proje Raporu (BONUS)

Proje raporunun **etkileşimli web sayfası** versiyonuna aşağıdaki bağlantıdan erişilebilir:

🔗 **GitHub Pages Linki:**
👉 [https://nurbuyukk.github.io/REPOADI/](https://KULLANICIADI.github.io/REPOADI/)

---

## 👩‍🎓 Öğrenci Bilgileri

* **Ad Soyad:** FATMA NUR BÜYÜK
* ÖĞRENCİ NO: 20222013236
* BÖLÜM: BİLGİSAYAR MÜHENDİSLİĞİ
* **Ders:** İşletim Sistemleri
* **Konu:** CPU Zamanlama Algoritmaları

---

## 📌 Not

Bu proje eğitim amaçlıdır ve akademik değerlendirme kapsamında hazırlanmıştır.
