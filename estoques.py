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
        codigo = validar_codigo(codigo)
        indice = self._indice_busca_binaria(codigo)
        if indice == -1:
            raise ValueError("Produto nao encontrado.")

        produto = self.produtos_ordenados.pop(indice)
        self.produtos_cadastro.remove(produto)
        return produto

    def buscar_por_codigo(self, codigo):
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
    
    def buscar_por_nome(self, termo):
        termo = str(termo).strip().lower()
        if termo == "":
            raise ValueError("Nome para busca nao pode ficar vazio.")
        
    def listar_ordenados(self):
        """Retorna produtos ordenados por codigo."""
        return list(self.produtos_ordenados)
    
    def listar_por_categoria(self, categoria):
        """Filtra produtos por categoria."""
        categoria = str(categoria).strip().lower()
        if categoria == "":
            raise ValueError("Categoria nao pode ficar vazia.")

        return [
            produto
            for produto in self.produtos_ordenados
            if produto.categoria.lower() == categoria
        ]
        
    def estoque_baixo(self, limite):
        limite = validar_quantidade(limite)
        return [
            produto
            for produto in self.produtos_ordenados
            if produto.quantidade < limite
        ]
        
    def menor_preco(self):
        if not self.produtos_ordenados:
            return None
        return min(self.produtos_ordenados, key=lambda produto: produto.preco)

    def maior_preco(self):
        if not self.produtos_ordenados:
            return None
        return max(self.produtos_ordenados, key=lambda produto: produto.preco)
    
    def registrar_venda(self, codigo, quantidade):
        quantidade = validar_quantidade(quantidade)
        if quantidade == 0:
            raise ValueError("Quantidade vendida deve ser maior que zero.")

        produto = self.buscar_por_codigo(codigo)
        if produto is None:
            raise ValueError("Produto nao encontrado.")
        if produto.quantidade < quantidade:
            raise ValueError("Estoque insuficiente para essa venda.")

        produto.quantidade -= quantidade
        return produto
    
    