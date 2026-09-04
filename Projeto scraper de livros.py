import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

url_atual = "http://books.toscrape.com/"
continuar = True

lista_dados = []



while continuar:
        responde = requests.get(url_atual)
        responde.encoding = 'utf-8'
        site = BeautifulSoup(responde.text, "html.parser")

        if responde.status_code == 200:
            print("Requisição feita com sucesso.")

            livros = site.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
            for livro in livros:
                titulo = livro.find("h3").find("a").get("title")
                preco = livro.find("div", class_="product_price").find("p", class_="price_color").text
                avaliacao = livro.find("p", class_="star-rating").get("class")[1]
                estoque = livro.find("p", class_="instock availability").text
                estoque_limpo = estoque.strip()
                lista_dados.append({"Titulo": titulo, "Preço": preco, "Avaliação": avaliacao, "Estoque": estoque_limpo})

            proximo = site.find("li", class_="next")
        else:
            print("Requisição Falhou")
            continuar = False

        if proximo:
            proximo = proximo.find("a").get("href")
            url_atual = urljoin(url_atual, proximo)

        else:
            continuar = False
df = pd.DataFrame(lista_dados)
df["Avaliação"] = df["Avaliação"].fillna("Sem Avaliação")
df = df.dropna(subset=["Preço"])
df.to_csv("Livros_Tratados.csv", index=False, encoding="utf-8")
