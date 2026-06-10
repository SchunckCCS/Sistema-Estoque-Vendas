class Estoques:

    def __init__(self):
        self.produtos_ordenados = []
        self.produtos_cadastro = []

    def cadastrar(self, codigo, nome, categoria, preco, quantidade):
        produto = Produto(codigo, nome, categoria, preco, quantidade)
        if self.buscar_por_codigo(produto.codigo) is not None:
            raise ValueError("Ja existe produto com esse codigo.")
        
        posicao = self._posicao_insercao(produto.codigo)
        self.produtos_ordenados.insert(posicao, produto)
        self.produtos_cadastro.append(produto)
        return produto
    
    def editar(self, codigo, nome=None, categoria=None, preco=None, quantidade=None):
            produto = self.buscar_por_codigo(codigo)
            if produto is None:
                raise ValueError("Produto nao encontrado.")

            produto.atualizar(nome, categoria, preco, quantidade)
            return produto
        
    def remover(self, codigo):
        """Remove produto pelo codigo."""
        codigo = validar_codigo(codigo)
        indice = self._indice_busca_binaria(codigo)
        if indice == -1:
            raise ValueError("Produto nao encontrado.")

        produto = self.produtos_ordenados.pop(indice)
        self.produtos_cadastro.remove(produto)
        return produto

    def buscar_por_codigo(self, codigo):
        """Busca binaria em vetor ordenado por codigo. O(log n)."""
        indice = self._indice_busca_binaria(validar_codigo(codigo))
        if indice == -1:
            return None
        return self.produtos_ordenados[indice]
    
    def _indice_busca_binaria(self, codigo):
        inicio = 0
        fim = len(self.produtos_ordenados) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2
            produto = self.produtos_ordenados[meio]

            if produto.codigo == codigo:
                return meio
            if produto.codigo < codigo:
                inicio = meio + 1
            else:
                fim = meio - 1

        return -1