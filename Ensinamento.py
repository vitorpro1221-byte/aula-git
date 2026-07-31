import requests

def buscar_usuarios(link):
    resposta = requests.get(link)
    if resposta.status_code == 200:
        print("-" * 20)
        print("Requisição Concluida")
        print("-" * 20)
        dados = resposta.json()
        return dados
         
    else:
        print("Requisição falhou")
        return None
    

usuarios = buscar_usuarios("https://jsonplaceholder.typicode.com/users")

if usuarios is not None:
    for usuario in usuarios:
        Empresa = usuario['address']['street']
        Empresa_10 = len(Empresa) >= 10
        Nome = usuario['name']
        Username = usuario['username']
        if Empresa_10:
            print("Nome:", Nome)
            print("Username:", Username)
            print("Cidade:", Empresa)
            print('-' * 20)

    
else:
    print('usuarios veio vazio')