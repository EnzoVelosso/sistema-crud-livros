
from arquivos import ler_livros, adicionar_livros

livro1 = {
    "codigo": 1,
    "titulo": "Vidas Secas",
    "autor": "Graciliano Ramos",
    "isbn": "9788535902778",
    "genero": "Romance",
    "estado": "Bom",
    "preco": 32.00,
    "quantidade": 12
}

livro2 = {
    "codigo": 7,
    "titulo": "O Pequeno Príncipe",
    "autor": "Antoine de Saint-Exupéry",
    "isbn": "9788522031445",
    "genero": "Infantil",
    "estado": "Ótimo",
    "preco": 25.00,
    "quantidade": 3
}

adicionar_livros(livro1)
adicionar_livros(livro2)

print("\nLivros cadastrados:")

livros = ler_livros()

for livro in livros:
    print(livro)