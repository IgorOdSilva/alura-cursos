from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praca', 'gourmet')
restaurante_chaves = Restaurante('chaves', 'mexicano')
restaurante_nagatomo = Restaurante('nagatomo', 'japones')

bebida_suco = Bebida('Suco de Melancia', 5.00   , 'Grande')
prato_pao = Prato('Pão', 2.00, 'O melhor pão da cidade.')

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()