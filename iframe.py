from selenium import webdriver
from selenium.webdriver.common.by import By
import time

drive = webdriver.Chrome()
drive.get("https://demoqa.com/frames")

iframes = drive.find_elements(By.TAG_NAME, "iframe")
lista_dos_texto_iframe = []

for iframe in iframes:
    drive.switch_to.frame(iframe)
    extrair_texto = drive.find_element(By.TAG_NAME, "h1").text
    drive.switch_to.default_content()
    lista_dos_texto_iframe.append(extrair_texto)
print(lista_dos_texto_iframe)

time.sleep(5)
drive.quit()

