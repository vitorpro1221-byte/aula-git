# Exemplo de estrutura do While
url_base = "http://quotes.toscrape.com"
url_atual = "/"

while url_atual:
    # 1. Faz o resquest juntando: url_base + url_atual
    # 2. BeautilfulSoup le a pagina
    # 3. Faz o loop 'for' para pegar frases e autores (Igual ja fez!)

    # 4. Busca pelo botão da proxima pagina:
    botao_proximo = site.find("li", class_="next")
