from modelos.restaurante import Restaurante

restaurante_praça = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()