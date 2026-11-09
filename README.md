Disusun Oleh :
Abdul Hafid rr (11230910000056)
Rayhan Aghno Zakri Setiawan (12409011030042)

Topik: Selenium (Web Test Automation) | Disusun: 3 November 2026

# 5W + 1H

## Pendahuluan 

Selenium adalah framework sumber terbuka (open source) untuk mengotomatisasi browser web. Pemakaian yang paling umum adalah pengujian fungsional aplikasi web secara otomatis. Dokumen ini berisi analisis 5W + 1H tentang Selenium, daftar skripsi/tesis dari luar negeri sebagai referensi, dan contoh program sederhana.

## Analisis 5W + 1H

| Pertanyaan | Jawaban | 
|----|------|
| What (Apa)  | Selenium adalah framework open source untuk mengotomatisasi browser web, terutama untuk pengujian fungsional aplikasi web. Komponen utamanya: Selenium WebDriver, Selenium IDE (record & playback), dan Selenium Grid (eksekusi paralel di banyak mesin/browser). |
| Why (Mengapa)  | Pengujian manual lambat, berulang, dan rawan salah. Selenium gratis, mendukung banyak browser (Chrome, Firefox, Edge, Safari) dan banyak bahasa pemrograman (Java, Python, C#, JavaScript, dll.), punya komunitas besar, dan cocok untuk regression testing serta CI/CD.  |
| Who (Siapa)  | Dipakai oleh QA engineer/tester, software developer, dan DevOps. Proyeknya dikelola komunitas open source (Selenium Project), awalnya dibuat oleh Jason Huggins pada 2004.  | 
| When (Kapan)  | Berjalan di komputer lokal, server CI (Jenkins, GitHub Actions, GitLab CI), atau cloud (Selenium Grid, BrowserStack, Sauce Labs). Hanya untuk aplikasi berbasis web (browser), bukan aplikasi desktop native.  | 
| Where (Di mana)  | Berjalan di komputer lokal, server CI (Jenkins, GitHub Actions, GitLab CI), atau cloud (Selenium Grid, BrowserStack, Sauce Labs). Hanya untuk aplikasi berbasis web (browser), bukan aplikasi desktop native  | 
| How (Bagaimana)  | Skrip kode (mis. Python) mengirim perintah ke driver browser melalui WebDriver API. Browser menjalankan aksi seperti membuka URL, klik, dan mengisi form, lalu skrip memverifikasi hasilnya dengan assertion. Alur: Skrip → WebDriver → Driver browser → Browser → Aplikasi web.  | 

## Referensi Skripsi/Tesis dari Luar Negeri

Berikut 8 skripsi/tesis dari berbagai negara. Beberapa berbahasa non-Inggris, tetapi abstraknya umumnya tersedia dalam bahasa Inggris di halaman repositori.

1.	**Lehtola, T. (2023). Järjestelmän web-sovellustestaus Selenium-työkalulla.** Master's thesis, Tampere University, Finlandia. Menyelidiki seberapa luas Selenium dapat dipakai untuk menguji berbagai karakteristik kualitas sistem dengan antarmuka berbasis web. Tautan: https://trepo.tuni.fi/handle/10024/153121
2.	**Balogović, I. (2019). Agilni razvoj i automatizirano testiranje web aplikacije primjenom alata Selenium.** Master's thesis, University of Osijek, Kroasia. Membahas pengembangan agile dan pengujian otomatis aplikasi web dengan Selenium. Tautan: https://urn.nsk.hr/urn:nbn:hr:200:207838
3.	**Bujalka, M. (2022). Automatizované testování webových aplikací.** Master's thesis, Czech University of Life Sciences Prague, Ceko. Membahas pengujian otomatis aplikasi web dengan Selenium WebDriver, disertai landasan teori pengembangan dan pengujian perangkat lunak. Tautan: https://theses.cz/id/k06qla
4.	**Avci, S. (2010). Evaluieren von automatisierten Tests bei Web-Applikationen.** Diploma Thesis, TU Wien, Austria. Mengotomatisasi tes Selenium dengan skrip shell Linux agar hasil lebih akurat dan waktu eksekusi lebih singkat. Tautan: https://repositum.tuwien.at/handle/20.500.12708/10531
5.	**Lattikas, P. Test automation for web applications with authentication.** Master thesis, Tallinn University of Technology, Estonia. Menganalisis skema autentikasi umum pada aplikasi web dan kemungkinan mengotomatisasinya dalam tes dengan Selenium. Tautan: https://digikogu.taltech.ee/en/Download/e310dbb1-c44f-4b56-ab70-1145b3bde9e1
6.	**Politecnico di Torino. Test scripting language selection for web-based automated testing.** Master Thesis, Italia. Membandingkan Selenium IDE dan Selenium WebDriver (Java dan C#) pada berbagai jenis aplikasi web. Tautan: https://webthesis.biblio.polito.it/18668/1/tesi.pdf
7.	**Jaroš, J. (2019). Framework pro tvorbu generovatelných automatizovaných funkčních testů s využitím nástroje Selenium WebDriver.** Master's thesis, University of Economics Prague, Ceko. Membuat prototipe framework berbasis Python dengan Selenium WebDriver untuk tes fungsional otomatis yang dapat dibaca mesin dan mudah dipahami manusia. Tautan: https://theses.cz/id/mw0pgh
8.	**Thapar Institute of Engineering and Technology. Automation Testing, Selenium Tool (Quality Analysis).** Master of Engineering thesis, India. Membahas Selenium WebDriver Framework, functional/object libraries, dan otomatisasi berbagai situs dengan test case Selenium. Tautan: https://tudr.thapar.edu/bitstreams/d989b2aa-dc50-4eaa-9f2e-cf19b7680be2/download

## Contoh Sederhana Selenium (Python)
Skenario: otomatis login ke situs latihan the-internet.herokuapp.com, lalu memverifikasi bahwa login berhasil.

### Persiapan

```
pip install selenium
```

Selenium 4 sudah memiliki Selenium Manager yang mengunduh driver browser secara otomatis. Yang diperlukan hanya Google Chrome terpasang.

### Kode: tes_login.py

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Buka browser
driver = webdriver.Chrome()

try:
    # 2. Buka halaman login
    driver.get("https://the-internet.herokuapp.com/login")

    # 3. Isi username & password
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

    # 4. Klik tombol login
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # 5. Tunggu pesan sukses muncul
    pesan = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    # 6. Verifikasi (assertion)
    assert "You logged into a secure area!" in pesan
    print("TEST LULUS: Login berhasil")

except AssertionError:
    print("TEST GAGAL: Pesan login tidak sesuai")

finally:
    # 7. Tutup browser
    driver.quit()
```

### Menjalankan

```
python tes_login.py
```

### Penjelasan Alur

1.	webdriver.Chrome() membuka browser Chrome.
2.	driver.get() membuka URL.
3.	find_element(By.ID, ...) mencari elemen HTML; send_keys() mengetik; click() mengklik.
4.	WebDriverWait menunggu elemen muncul (lebih andal daripada sleep).
5.	assert memeriksa hasil aktual sesuai harapan.
6.	driver.quit() menutup browser.

## Ide Pengembangan

•	Tambahkan kasus uji login gagal (password salah).

•	Gunakan pytest dan pola Page Object Model agar kode lebih rapi dan mudah dirawat.

•	Jalankan lewat Selenium Grid atau pipeline CI/CD.

•	Bandingkan efisiensi waktu dan akurasi dengan pengujian manual sebagai bahan analisis skripsi.
