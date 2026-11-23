import json

def ler_livros():
    try:
        with open("acervo.json","r", encoding = "utf-8") as arquivo:
            livros = json.load(arquivo)
        return livros
    except FileNotFoundError:
        print("Arquivo não encontrado")
        return []

def adicionar_livros(novo_livro):

    livros = ler_livros()
    livros.append(novo_livro)
    try:
        with open("acervo.json", "w", encoding = "utf-8") as arquivo:
            json.dump(livros, arquivo)
    except:        
        print("Erro ao salvar o arquivo.")