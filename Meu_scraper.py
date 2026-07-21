import requests

meus_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64 x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

minha_url = "https://httpbin.org/user-agent"


resposta = requests.get(minha_url, headers=meus_headers)


print(resposta.text)