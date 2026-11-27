from utils import (
    obter_texto,
    obter_isbn,
    obter_opcao,
    obter_preco,
    obter_quantidade,
)
from dados import GENEROS, ESTADO, isbn_cadastrados
from arquivos import ler_livros, adicionar_livros

def cadastrar_livros():
    livros_existentes = ler_livros()

    isbn_cadastrados = {
    livro["isbn"] for livro in livros_existentes
    }

    titulo = obter_texto("Digite o título: ")
    autor = obter_texto("Digite o autor: ")
    isbn = obter_isbn(isbn_cadastrados)
    genero = obter_opcao("Escolha o gênero: ", GENEROS)
    estado = obter_opcao("Escolha o estado de conservação do livro: ", ESTADO)
    preco = obter_preco()
    quantidade = obter_quantidade()

    codigo = 1

    for livro in livros_existentes:
        if livro["codigo"] >= codigo:
            codigo = livro["codigo"] + 1


    novo_livro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "genero": genero,
        "estado": estado,
        "preco": preco,
        "quantidade": quantidade
    }

    adicionar_livros(novo_livro)

    print("Livro cadastrado com sucesso!")
    print("Código:", codigo)

    def mostrar_livros ():
        livros = ler_livros()
        if not livros:
            print("O acervo está vazio.")
            return

        print("======== ACERVO DE LIVROS ========\n")
        print(
            f"{'CÓDIGO':<8}"
            f"{'TÍTULO':<28}"
            f"{'AUTOR':<25}"
            f"{'GÊNERO':<15}"
            f"{'PREÇO (R$)':>10}"
            f"{'QTD':>6}"
        )