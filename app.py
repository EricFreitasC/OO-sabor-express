from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praça = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de manga', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'o melhor pão da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praça.adicionar_no_cardapio(bebida_suco)
restaurante_praça.adicionar_no_cardapio(prato_paozinho)

def main():
    restaurante_praça.exibir_cardapio

if __name__ == '__main__':
    main()