# Relatorio curto: buscas e ordenacao

O sistema usa dois vetores para atender ao objetivo do projeto.

## Vetor ordenado por codigo

O vetor `produtos_ordenados` fica sempre em ordem crescente pelo codigo do
produto. Ao cadastrar um novo produto, o sistema encontra a posicao correta por
busca binaria e insere o item nessa posicao. Ao remover, o item tambem sai desse
vetor, preservando a ordenacao.

Essa estrutura permite buscar produto por codigo com busca binaria, cuja
complexidade e O(log n). Ela e adequada porque o codigo e unico e o vetor esta
ordenado exatamente por esse campo.

## Vetor nao ordenado para cadastro e nomes

O vetor `produtos_cadastro` guarda os produtos na ordem em que foram
cadastrados. Para busca por nome, o sistema usa busca linear, com complexidade
O(n), porque os nomes nao estao ordenados e a busca aceita parte do texto. Nesse
caso, pode ser necessario verificar todos os produtos para encontrar todas as
ocorrencias.

## Outras operacoes

Listagens por categoria, relatorio de estoque baixo e menor/maior preco tambem
percorrem os produtos, pois precisam analisar varios itens. Essas operacoes tem
complexidade O(n).
