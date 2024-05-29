
produtos = [] # Criação de lista vazia.

def menu():
    print('Bem vindo, o deseja?')
    print('[1] Adicionar produto.')
    print('[2] Ler produto.')    
    print('[3] Buscar produto.')
    print('[4] Sair.')
    opcao = input('O que deseja fazer: ')
    return opcao

def main():
    while True:
        opcao = menu()
        match opcao:
            case '1': adcProdutos()
            case '2': lerProdutos()
            case '3': buscarProdutos()
            case '4': break
            case __: print('Opção Inválida.') #Usa default caso não as opções.

def adcProdutos(): 
    nome = input('Qual nome do produto: ')
    preco = float(input('Qual valor: '))
    quantidade = int(input('Qual a quantidade: '))
    produto = {'nome': nome, 'preco': preco, 'quantidade': quantidade} #Dicionário.
    produtos.append(produto)
    print('Produto adicionado com sucesso.')

def lerProdutos():
    for produto in produtos:
        print(f"{produto['nome']}, {produto['preco']}, {produto['quantidade']}")

def buscarProdutos():
    busca = input('O que você está procurando: ')
    for produto in produtos:
        if produto['nome'] == busca:
            print(f"{produto['nome']}, {produto['preco']}, {produto['quantidade']}")
            
if __name__ == '__main__':
    main()