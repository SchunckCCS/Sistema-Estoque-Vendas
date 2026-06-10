class Produto:

    def __init__(self, codigo, nome, categoria, preco, quantidade):
        self.codigo = validar_codigo(codigo)
        self.nome = validar_texto(nome, "nome")
        self.categoria = validar_texto(categoria, "categoria")
        self.preco = validar_preco(preco)
        self.quantidade = validar_quantidade(quantidade)

    def atualizar(self, nome=None, categoria=None, preco=None, quantidade=None):
        if nome is not None:
            self.nome = validar_texto(nome, "nome")
        if categoria is not None:
            self.categoria = validar_texto(categoria, "categoria")
        if preco is not None:
            self.preco = validar_preco(preco)
        if quantidade is not None:
            self.quantidade = validar_quantidade(quantidade)

    def para_dict(self):
        return {
            "codigo": self.codigo,
            "nome": self.nome,
            "categoria": self.categoria,
            "preco": self.preco,
            "quantidade": self.quantidade,
        }

    @classmethod
    def de_dict(cls, dados):
        return cls(
            dados["codigo"],
            dados["nome"],
            dados["categoria"],
            dados["preco"],
            dados["quantidade"],
        )

    def __str__(self):
        return (
            f"Codigo: {self.codigo} | Nome: {self.nome} | "
            f"Categoria: {self.categoria} | Preco: R$ {self.preco:.2f} | "
            f"Qtd: {self.quantidade}"
        )


def validar_codigo(codigo):
    try:
        codigo = int(codigo)
    except (TypeError, ValueError) as erro:
        raise ValueError("Codigo deve ser um numero inteiro.") from erro

    if codigo <= 0:
        raise ValueError("Codigo deve ser positivo.")
    return codigo


def validar_texto(valor, campo):
    if valor is None or str(valor).strip() == "":
        raise ValueError(f"{campo.capitalize()} nao pode ficar vazio.")
    return str(valor).strip()


def validar_preco(preco):
    try:
        preco = float(preco)
    except (TypeError, ValueError) as erro:
        raise ValueError("Preco deve ser um numero.") from erro

    if preco <= 0:
        raise ValueError("Preco deve ser positivo.")
    return preco


def validar_quantidade(quantidade):
    try:
        quantidade = int(quantidade)
    except (TypeError, ValueError) as erro:
        raise ValueError("Quantidade deve ser um numero inteiro.") from erro

    if quantidade < 0:
        raise ValueError("Quantidade nao pode ser negativa.")
    return quantidade
