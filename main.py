from arquivos import carregar_produtos, registrar_log, salvar_produtos
from estoque import Estoque


def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Entrada obrigatoria. Tente novamente.")


def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem).strip())
        except ValueError:
            print("Digite um numero inteiro valido.")


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem).strip().replace(",", "."))
        except ValueError:
            print("Digite um numero valido.")


def mostrar_produtos(produtos, tamanho_pagina=5):
    if not produtos:
        print("Nenhum produto encontrado.")
        return

    for indice, produto in enumerate(produtos, start=1):
        print(produto)
        if indice % tamanho_pagina == 0 and indice < len(produtos):
            input("Pressione Enter para continuar...")


def cadastrar_produto(estoque):
    codigo = ler_inteiro("Codigo: ")
    nome = ler_texto("Nome: ")
    categoria = ler_texto("Categoria: ")
    preco = ler_float("Preco: ")
    quantidade = ler_inteiro("Quantidade: ")
    produto = estoque.cadastrar(codigo, nome, categoria, preco, quantidade)
    registrar_log(f"Produto cadastrado: {produto.codigo} - {produto.nome}")
    print("Produto cadastrado com sucesso.")


def editar_produto(estoque):
    codigo = ler_inteiro("Codigo do produto: ")
    produto = estoque.buscar_por_codigo(codigo)
    if produto is None:
        print("Produto nao encontrado.")
        return

    print("Deixe em branco para manter o valor atual.")
    nome = input(f"Nome ({produto.nome}): ").strip() or None
    categoria = input(f"Categoria ({produto.categoria}): ").strip() or None
    preco_texto = input(f"Preco ({produto.preco:.2f}): ").strip()
    quantidade_texto = input(f"Quantidade ({produto.quantidade}): ").strip()

    preco = None if preco_texto == "" else float(preco_texto.replace(",", "."))
    quantidade = None if quantidade_texto == "" else int(quantidade_texto)
    estoque.editar(codigo, nome, categoria, preco, quantidade)
    registrar_log(f"Produto editado: {codigo}")
    print("Produto atualizado com sucesso.")


def remover_produto(estoque):
    codigo = ler_inteiro("Codigo do produto: ")
    produto = estoque.remover(codigo)
    registrar_log(f"Produto removido: {produto.codigo} - {produto.nome}")
    print("Produto removido com sucesso.")


def buscar_por_codigo(estoque):
    codigo = ler_inteiro("Codigo do produto: ")
    produto = estoque.buscar_por_codigo(codigo)
    if produto is None:
        print("Produto nao encontrado.")
    else:
        print(produto)


def buscar_por_nome(estoque):
    termo = ler_texto("Nome ou parte do nome: ")
    mostrar_produtos(estoque.buscar_por_nome(termo))


def registrar_venda(estoque):
    codigo = ler_inteiro("Codigo do produto: ")
    quantidade = ler_inteiro("Quantidade vendida: ")
    produto = estoque.registrar_venda(codigo, quantidade)
    registrar_log(f"Venda registrada: {codigo} - quantidade {quantidade}")
    print(f"Venda registrada. Estoque atual de {produto.nome}: {produto.quantidade}")


def listar_por_categoria(estoque):
    categoria = ler_texto("Categoria: ")
    mostrar_produtos(estoque.listar_por_categoria(categoria))


def relatorio_estoque_baixo(estoque):
    limite = ler_inteiro("Limite de estoque baixo: ")
    mostrar_produtos(estoque.estoque_baixo(limite))


def relatorio_precos(estoque):
    menor = estoque.menor_preco()
    maior = estoque.maior_preco()
    if menor is None:
        print("Nenhum produto cadastrado.")
        return

    print("Menor preco:")
    print(menor)
    print("Maior preco:")
    print(maior)


def salvar_dados(estoque):
    salvar_produtos(estoque.listar_ordenados())
    registrar_log("Dados salvos em arquivo")
    print("Dados salvos com sucesso.")


def carregar_dados(estoque):
    produtos = carregar_produtos()
    estoque.carregar_produtos(produtos)
    registrar_log("Dados carregados do arquivo")
    print(f"{len(produtos)} produto(s) carregado(s).")


def mostrar_menu():
    print("\n=== Sistema de Estoque e Vendas ===")
    print("1. Cadastrar produto")
    print("2. Editar produto")
    print("3. Remover produto")
    print("4. Buscar produto por codigo")
    print("5. Buscar produtos por nome")
    print("6. Registrar venda")
    print("7. Listar produtos ordenados por codigo")
    print("8. Listar produtos por categoria")
    print("9. Relatorio de estoque baixo")
    print("10. Relatorio menor/maior preco")
    print("11. Salvar dados")
    print("12. Carregar dados")
    print("0. Sair")


def executar_opcao(opcao, estoque):
    acoes = {
        "1": cadastrar_produto,
        "2": editar_produto,
        "3": remover_produto,
        "4": buscar_por_codigo,
        "5": buscar_por_nome,
        "6": registrar_venda,
        "7": lambda est: mostrar_produtos(est.listar_ordenados()),
        "8": listar_por_categoria,
        "9": relatorio_estoque_baixo,
        "10": relatorio_precos,
        "11": salvar_dados,
        "12": carregar_dados,
    }

    acao = acoes.get(opcao)
    if acao is None:
        print("Opcao invalida.")
        return

    try:
        acao(estoque)
    except ValueError as erro:
        print(f"Erro: {erro}")


def main():
    estoque = Estoque()
    carregar_dados(estoque)

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "0":
            salvar_dados(estoque)
            print("Ate logo!")
            break

        executar_opcao(opcao, estoque)


if __name__ == "__main__":
    main()
