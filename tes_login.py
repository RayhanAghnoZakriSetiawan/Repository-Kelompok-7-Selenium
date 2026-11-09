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
