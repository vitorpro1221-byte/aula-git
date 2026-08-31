from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

drive = webdriver.Chrome()
drive.get("https://demoqa.com/dynamic-properties")

espera = WebDriverWait(drive, 10)
botao = espera.until(Ec.element_to_be_clickable((By.ID, "colorChange")))

botao.click()
print("O click foi certeiro")

drive.quit()