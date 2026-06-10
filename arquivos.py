import json
from datetime import datetime
from pathlib import Path

from produto import Produto

ARQUIVO_DADOS = Path("dados_estoque.json")
ARQUIVO_LOG = Path("operacoes.log")

def salvar_produtos(produtos, caminho=ARQUIVO_DADOS):
    """Salva produtos em arquivo JSON."""
    dados = [produto.para_dict() for produto in produtos]
    Path(caminho).write_text(
        json.dumps(dados, indent=4, ensure_ascii=False),
        encoding="utf-8",
    )


def carregar_produtos(caminho=ARQUIVO_DADOS):
    """Carrega produtos de arquivo JSON, se existir."""
    caminho = Path(caminho)
    if not caminho.exists():
        return []

    conteudo = caminho.read_text(encoding="utf-8").strip()
    if conteudo == "":
        return []

    dados = json.loads(conteudo)
    return [Produto.de_dict(item) for item in dados]

def registrar_log(mensagem, caminho=ARQUIVO_LOG):
    momento = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with Path(caminho).open("a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{momento}] {mensagem}\n")