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