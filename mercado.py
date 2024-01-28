from typing import List, Dict
from time import sleep

from models.produto import Produto
from utils.helper import formata_float_str_moeda


produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('---------------------------------')
    print('--- Sistema Market de Compras ---')
    print('---------------------------------')

    print('Selecione uma opção abaixo: ')
    print('1 - Para cadastrar um novo produto')
    print('2 - Para listar os produtos')
    print('3 - Para comprar um produto')
    print('4 - Para visualizar o carrinho de compras')
    print('5 - Para remover um produto do sistema')
    print('6 - Para remover um produto do carrinho')
    print('7 - Para concluir o pedido')
    print('8 - Para sair do sistema')

    opcao: int = int(input())

    if opcao == 1:
        cadastrar_produto()
    elif opcao == 2:
        listar_produtos()
    elif opcao == 3:
        comprar_produto()
    elif opcao == 4:
        visualizar_carrinho()
    elif opcao == 5:
        remover_produto_sistema()
    elif opcao == 6:
        remover_produto_carrinho()
    elif opcao == 7:
        fechar_pedido()
    elif opcao == 8:
        print('Volte sempre ao Market :)')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        menu()


def cadastrar_produto() -> None:
    print('Cadastro de novos produtos')
    print('--------------------------')

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'O produto \'{produto.nome}\' foi cadastrado com sucesso!')
    sleep(2)
    menu()


def listar_produtos() -> None:
    if len(produtos) > 0:
        print('Listagem de produtos')
        print('--------------------')
        for produto in produtos:
            print(produto)  # Executa o produto.__str__
            print('--------------------')
            sleep(1)
    else:
        print('Atualmente não existem produtos cadastrados no sistema. Voltando ao menu ...')

    sleep(2)
    menu()


def comprar_produto() -> None:
    if len(produtos) > 0:
        print('--------------------------------------------------------------')
        print('=================== Produtos Disponíveis =====================')
        for produto in produtos:
            print(produto)
            print('----------------------------------------------------------')
            sleep(1)
        codigo: int = int(input('Informe o código do produto que deseja adicionar ao carrinho: '))

        produto: Produto = pega_produto_por_codigo(codigo)

        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    qtde: int = item.get(produto)
                    if qtde:
                        item[produto] = qtde + 1
                        print(f'O produto \'{produto.nome}\' agora possui {qtde + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(f'O produto \'{produto.nome}\' foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}  # Adicionando o primeiro produto no carrinho
                carrinho.append(item)
                print(f'O produto \'{produto.nome}\' foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f'O produto com código \"{codigo}\" não foi encontrado. Voltando ao menu ...')
            sleep(2)
            menu()
    else:
        print('Ainda não existem produtos para vender. Voltando ao menu ...')
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)
    else:
        print('Ainda não existem produtos no carrinho. Voltando ao menu ...')

    sleep(2)
    menu()


def remover_produto_sistema() -> None:
    if len(produtos) > 0:
        print('=================== Produtos Disponíveis =====================')
        for produto in produtos:
            print(produto)
            print('----------------------------------------------------------')
            sleep(1)

        codigo: int = int(input('Informe o código produto que você que remover do sistema: '))

        produtos_novo: List[Produto] = []
        encontrou_produto = False

        for produto in produtos:
            if produto.codigo == codigo:
                print(f'O produto \'{produto.nome}\' de código \"{produto.codigo}" e preço {produto.preco} será removido do sistema.')
                encontrou_produto = True
            else:
                produtos_novo.append(produto)

        if not encontrou_produto:
            print('Não foi encontrado o código nos produtos no sistema. Voltando ao menu ...')
            sleep(2)
            menu()

        produtos.clear()
        produtos.extend(produtos_novo)
        print('Nova listagem de produtos do sistema: ')
        listar_produtos()

    else:
        print('Não existem produtos cadastrados no sistema. Voltando ao menu ...')
        sleep(2)
        menu()


def remover_produto_carrinho() -> None:
    if len(carrinho) > 0:
        print('Produtos no carrinho: ')

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print('-----------------------')
                sleep(1)

        codigo: int = int(input('Informe o código produto que você que remover do carrinho: '))

        encontrou_produto = False

        for item in carrinho:
            if list(item.keys())[0].codigo == codigo:
                produto_removido = list(item.keys())[0]
                carrinho.remove(item)
                print(f'O produto \'{produto_removido.nome}\' de código \"{produto_removido.codigo}\" e preço {produto_removido.preco} será removido do carrinho.')
                encontrou_produto = True

        if not encontrou_produto:
            print('Não foi encontrado o produto no carrinho. Voltando ao menu ... ')
            sleep(2)
            menu()

        if len(carrinho) > 0:
            print('Nova listagem de produtos do carrinho')
            visualizar_carrinho()
        else:
            print('O carrinho está vazio agora. Voltando ao menu ...')
            sleep(2)
            menu()

    else:
        print('Não existem produtos no carrinho. Voltando ao menu ...')
        sleep(2)
        menu()


def fechar_pedido() -> None:
    if len(carrinho) <= 0:
        print('Ainda não existem produtos no carrinho.')
        sleep(2)
        menu()
    else:
        valor_total: float = 0

        print('Produtos do carrinho')
        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print('------------------')
                sleep(1)

        print(f'O valor do seu carrinho é {formata_float_str_moeda(valor_total)}')
        print('Obrigado por comprar com a gente :)')
        carrinho.clear()
        sleep(5)


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
