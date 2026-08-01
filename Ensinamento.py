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

def filtrar_usuarios_por_cidade(usuarios):
    usuarios_filtrados = [] 
    for usuario in usuarios:
        nome = usuario['name']
        username = usuario['username']
        cidade = usuario['address']['city']
        cidade_com_apenas_10_ou_mais = len(cidade) >= 10
        if cidade_com_apenas_10_ou_mais:
            usuarios_filtrados.append({'nome': nome,
                                       'username': username,
                                       'cidade': cidade})
    return usuarios_filtrados

usuarios = buscar_usuarios("https://jsonplaceholder.typicode.com/users")
filtro = filtrar_usuarios_por_cidade(usuarios)

for usuario in filtro:
    print('Nome do Usuario:', usuario['nome'])
    print('Username do Usuario:', usuario['username'])
    print('Cidade do Usuario:', usuario['cidade'])
    print('-' * 20)
