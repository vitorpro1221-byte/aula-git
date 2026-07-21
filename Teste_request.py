import requests

# Fazendo a requisição GET para um site de testes
resposta = requests.get("https://httpbin.org/status/404")

# 1. Verificando o código de status (200 = Sucesso)
print("Status Code:", resposta.status_code)

# 2. Vendo o conteúdo que o site respondeu
print("\nConteúdo da Resposta:")
print(resposta.text)