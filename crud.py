#conversar c a prof

from utils import obter_opcao
from dados import GENEROS, ESTADOS

genero = obter_opcao("Escolha o gênero do livro: ", GENEROS)

print("\nGênero selecionado:", genero)

estado = obter_opcao("Escolha o estado de conservação: ", ESTADOS)

print("\nEstado selecionado:", estado)