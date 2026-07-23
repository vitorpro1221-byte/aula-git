import requests
from bs4 import BeautifulSoup
import pandas as pd # importamos o pandas

url = "http://books.toscrape.com/"

# 1. fazemos a requisição e o parse do html
respota = requests.get(url)
# Ajustamos o enconding para nao aparecer os caracteres estranhos como Â£
respota.encoding = "utf-8"

site = BeautifulSoup(respota.text, "html.parser")

# 1. Procuramos todos os livros (Artigos) da pagina
livros = site.find_all("article", class_="product_pod")

# 2. Criamos uma lista vazia para guardar o livros organizados
lista_livros = []

print(f"Encontramos {len(livros)} livros nesta pagina!\n")

# 2. fazermos um loop (for) para passar de livro em livro
for livro in livros:
    # Pegamos o titulo dentro da h3
    titulo = livro.h3.a["title"]

    # pegamos o preço dentro da class 'price_color'
    preco = livro.find("p", class_="price_color").text

# adicionamos um dicionario com Titulo e Preço na nossa linha
    lista_livros.append({"Titulo": titulo, "Preço": preco})
#4. O PANDAS ENTRA EM AÇÃo
# Transformamos nossa liusta em uma tabela (DataFrame)
df = pd.DataFrame(lista_livros)

# Salva a tabela num arquivo chamado "meus_livros.csv"
df.to_csv("meus_livros.csv", index=False, encoding="utf-8-sig")

print("✅ Sucesso! Os livros foram salvos na planilha 'meus_livros.csv'!")