# Mercado
Aplicação de um sistema de um supermercado denominado "Market". Nele, é capaz de cadastrar, remover ou listar os produtos do sistema, adicionar, remover ou listar os produtos do carrinho de compras, fechar o pedido e sair do sistema do mercado. Existem 4 arquivos no diretório, que são:

## produto.py
É a criação da classe Produto, que é a base do sistema. O Produto tem um código, que se inicializa em 1 e vai incrementando a cada novo produto adicionado no sistema.
Na criação de um produto deve ser informado o nome do produto e o valor (esse que vai ser informado pela formatação americana, com '.' no lugar da ',' nas casas decimais).
Além disso, possui 3 propriedades, codigo, nome e preco, que serve para informar as respectivas informações. Possui também uma função que tabela o Produto, informando suas informações.

## teste.py
É um código apenas para teste de criação de produtos, para verificar se a classe foi bem implementada e funciona da maneira esperada.

## helper.py
É uma função de auxílio, na qual possui uma função que vai converter o valor do produto passado como se fosse em reais (R$) e dividindo pelas unidades, para ficar mais fácil de ser entendido o valor.

## mercado.py
É o código principal, o da aplicação. Inicialmente cria 2 listas, uma de Produto, importando da classe produto.py, que vai ser a listagem de produtos do sistema e uma lista de dicionário, que vai conter o Produto e a quantidade, que vai ser o carrinho de compras.
Existem várias funções dentro dele, que são:
- main:
A função inicial do programa, executa a função menu.
- menu:
A função principal do programa, executa as demais. Oferece ao usuário as ações disponíveis para se fazer no sistema.
- cadastrar_produto:
Como o nome já diz, é a função que cadastra novos produtos no sistema, instanciando um objeto Produto novo com um nome e um valor informado pelo usuário e acrescentando na lista de produtos do sistema. Ao fim, volta ao menu de opções.
- listar_produtos:
Lista os produtos já inseridos no sistema ou avisa o usuário que não existem produtos cadastrados. No fim, volta ao menu de opções do sistema.
- comprar_produto:
Fornece a lista de produtos disponíveis no sistema ao usuário, se não houver produtos disponíveis no sistema o usuário é informado, se não, o usuário precisa fornecer o código de um produto que consta no sistema, caso contrário ele será informado que o código fornecido não existe no sistema e retornará ao menu. Caso o código exista, ele insere uma unidade do produto no carrinho e, por fim, retorna ao menu.
- visualizar_carrinho:
Se houverem produtos no carrinho de compras, ele vai informar ao usuário quais produtos tem e quantos produtos de cada tem, caso contrário, o usuário será informado que não há produtos no carrinho de compras. Igual as funções anteriores, retorna ao menu.
- remover_produto_sistema:
Caso não haja produtos no sistema, o usuário será informado e retornará ao menu, se houver, vai ser informado ao usuário a lista de produtos existentes no sistema e solicitado para fornecer o código do produto que ele quer remover do sistema, caso o código não exista no sistema irá aparecer um aviso e retornará ao menu, caso contrário, o produto será excluído do sistema, será informado a nova listagem de itens do sistema e retornará ao menu.
- remover_produto_carrinho:
Com a mesma explicação da função anterior, remove um produto do carrinho desde que ele se encontre nele, remove todas as unidades do produto do carrinho, por fim, retorna ao menu.
- fechar_produto:
Caso o carrinho não tiver produtos, o usuário será informado e será retornado ao menu, caso contrário, faz a listagens dos itens que há no carrinho e o preço total de cada item, por fim, informa a soma total do carrinho ao usuário e retorna ao menu.
- pega_produto_por_codigo:
É uma função de auxílio para procurar um produto de determinado código dentro da lista de produtos do sistema, retornando o objeto Produto do código fornecido, caso houver, se não, retorna None.

Vale ressaltar que como é uma aplicação que consiste em usuário e administrador, o próprio consumidor do mercado poderia inserir ou remover itens do mercado. 