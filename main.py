<<<<<<< HEAD
from utils import (
    obter_isbn,
    obter_preco,
    obter_quantidade,
    obter_texto
)
=======

from arquivos import ler_livros, adicionar_livros
>>>>>>> 3e3f1e9c783c908e17e52e7af3c41aa66c8b48b2

titulo = obter_texto("Digite o título do livro: ")

print("Título recebido:", titulo)

isbns_cadastrados = {
    "9788535910663"
}

isbn = obter_isbn(isbns_cadastrados)

print("ISBN recebido:", isbn)