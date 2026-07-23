import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://quotes.toscrape.com"
url_atual = "/"
Frases = []

while url_atual:
    # 1. Faz o resquest juntando: url_base + url_atual
    # 2. BeautilfulSoup le a pagina
    # 3. Faz o loop 'for' para pegar frases e autores (Igual ja fez!)
    respota = requests.get(url + url_atual)
    respota.encoding = "utf-8"
    site = BeautifulSoup(respota.text, "html.parser")
    Frases_Autores = site.find_all("div", class_="quote")

    for Frase in Frases_Autores:
        A_Frase = Frase.find("span", class_="text").text
        Autor = Frase.find("small", class_="author").text

        Frases.append({"Frase": A_Frase, "Autor": Autor})

    # 4. Busca pelo botão da proxima pagina:
    botao_proximo = site.find("li", class_="next")
    if botao_proximo:
        # se achou o botão, atualiza url_atual com o link do botão (href)
        url_atual = botao_proximo.find("a")["href"]
    else:
        # se nao achou (chegou na ultima pagina), zera a variavel para parar o while
        url_atual = None

print(f"Encontrado {len(Frases)} Frases nesse site")

df = pd.DataFrame(Frases)
df.to_csv("frases_famosas.csv", index=False, encoding="utf-8-sig")
print("Salvo com Sucesso")