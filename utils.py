def obter_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto != "":
            return texto
        elif texto == "":
            print("Digite algo.")

def obter_isbn(isbns_cadastrados):
    while True:
        isbn = input("Digite o ISBN do livro: ").strip()

        if len(isbn) != 13:
            print("O ISBN tem que possuir 13 dígitos(FAZ O L)")

        elif isbn in isbns_cadastrados:
            print("O ISBN já está cadastrado")
        else: return isbn 

def obter_preco():
    while True:
        try:
            preco = float(input("Digite o preço do livro: "))

            if preco > 0:
                return preco 
            elif preco < 0:
                print("O preço deve ser positivo.")
            else:
                print("O preço deve ser maior que zero.")
        except ValueError:
            print("Digite um valor válido.")  

def obter_quantidade():
    while True:
        try:
            quantidade = int(input("Digite a quantidade de livros: "))

            if quantidade >= 0:
                return quantidade    
            elif quantidade < 0:
                print("A quantidade deve ser positiva.")

        except ValueError:
            print("Digite um valor válido.")     

def obter_opcao(mensagem,opcoes ):
    while True:
        while True:
            numero = 1 
            for opcao in opcoes:
                print(f"{numero} - {opcao}")
                numero = numero + 1

            try:
                escolha = int(input(mensagem))
                if escolha >= 1 and escolha <= len(opcao):
                    return opcoes[escolha]

                else:
                    print("opção inválida.")
            except ValueError:
                print("Digite um numero válido.")

                