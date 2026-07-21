import requests

# Fingindo ser um navegador Google Chrome num Windows
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://httpbin.org/headers"

resposta = requests.get(url, headers=headers)

print(resposta.text)