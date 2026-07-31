from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# 1 e abre o navegador chrome
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# acessa um site
navegador.get("https:quotes.toscrape.com/")

# espera 5 segundos para conseguires ver a janela aberta
time.sleep(5)
# fecha o navegador
navegador.quit