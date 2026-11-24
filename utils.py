def obter_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto != "":
            return texto

        
        print("Digite algo.")

def obter_isbn():
    '''O ISBN deve possuir exatamente 13 dígitos.
       O ISBN não pode pertencer a outro livro já cadastrado.'''