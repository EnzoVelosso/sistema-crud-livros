from utils import (
    obter_isbn,
    obter_preco,
    obter_quantidade,
    obter_texto
)

titulo = obter_texto("Digite o título do livro: ")

print("Título recebido:", titulo)

isbns_cadastrados = {
    "9788535910663"
}

isbn = obter_isbn(isbns_cadastrados)

print("ISBN recebido:", isbn)