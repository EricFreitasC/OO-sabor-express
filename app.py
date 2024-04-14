from modelos.restaurante import Restaurante

restaurante_praça = Restaurante('Praça', 'Gourmet')
restaurante_praça.receber_avaliacao('gui', 10)
restaurante_praça.receber_avaliacao('larissa', 8)
restaurante_praça.receber_avaliacao('emy', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()