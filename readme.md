# Sistema de Estoque e Vendas

Projeto de linha de comando em Python para cadastrar produtos, controlar vendas,
consultar estoque e gerar relatorios simples.

## Como executar

Requisitos:

- Python 3 instalado.

No terminal, dentro da pasta do projeto, execute:

```bash
python main.py
```

Ao iniciar, o sistema tenta carregar automaticamente o arquivo
`dados_estoque.json`. Ao sair pelo menu, os dados sao salvos novamente.

## Funcionalidades

- Cadastrar produto com codigo unico.
- Editar nome, categoria, preco e quantidade.
- Remover produto por codigo.
- Buscar produto por codigo com busca binaria.
- Buscar produtos por nome com busca linear.
- Registrar venda e reduzir estoque.
- Listar produtos ordenados por codigo.
- Filtrar produtos por categoria.
- Gerar relatorio de estoque baixo.
- Mostrar menor e maior preco.
- Salvar e carregar dados em JSON.
- Registrar logs simples em `operacoes.log`.

## Exemplo de uso

1. Escolha `1` para cadastrar um produto.
2. Informe codigo, nome, categoria, preco e quantidade.
3. Escolha `6` para registrar uma venda.
4. Informe o codigo do produto e a quantidade vendida.
5. Escolha `7` para conferir a lista ordenada por codigo.
6. Escolha `0` para salvar e sair.

## Arquivos principais

- `main.py`: menu e fluxo do sistema.
- `produto.py`: classe Produto e validacoes.
- `estoque.py`: cadastro, edicao, remocao, buscas e relatorios.
- `arquivos.py`: salvar, carregar e registrar logs.
- `dados_estoque.json`: dados de exemplo.
- `relatorio.md`: explicacao curta sobre busca linear, busca binaria e
  ordenacao.

## Complexidade

A busca por codigo usa busca binaria em um vetor ordenado por codigo, com custo
O(log n). A busca por nome usa busca linear em um vetor nao ordenado, com custo
O(n), pois precisa comparar o texto informado com cada produto.

## Versionamento

O projeto foi organizado para uso com Git e commits pequenos. Caso o Git esteja
instalado, um fluxo recomendado e:

```bash
git init
git add .
git commit -m "Cria sistema de estoque e vendas"
```
