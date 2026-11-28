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

def consultar_livros():
    livros = ler_livros()

    if not livros:
        print("O acervo está vazio.")
        return

    busca = obter_texto("Digite o código ou trecho do título: ").lower()

    livros_encontrados = []

    for livro in livros:
        codigo = str(livro["codigo"])
        titulo = livro["titulo"].lower()

        if busca == codigo or busca in titulo:
            livros_encontrados.append(livro)

    if not livros_encontrados:
        print("Nenhum livro encontrado.")
        return

    for livro in livros_encontrados:
        print("RESULTADO DA PROCURA:\n")
        print("Código:", livro["codigo"])
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Gênero:", livro["genero"])
        print("Preço: R$", livro["preco"])
        print("Qauantidade:", livro["quantidade"])

def modificar_livro():
    livros = ler_livros
    try:
        codigo = int(input("Digite o código do livro: "))

    except ValueError:
        print("Digite um código válido.")
        return

    livro_encontrado = None

    for livro in livros:
        if livro["codigo"] == codigo:
            livro_encontrado = livro
            break

    if livro_encontrado is None:
        print("Não existe este livro nos dados.")
        return

    print("======= DADOS DO LIVRO =======")

    for chave, valor in livro_encontrado.items():
        print(f"{chave}: {valor}")
        