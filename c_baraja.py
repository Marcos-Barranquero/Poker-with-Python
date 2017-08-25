# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""Contiene la definición de la clase baraja."""

from random import shuffle
from c_carta import Carta


class Baraja():
    """Representación de una baraja de 52 cartas"""

    def __init__(self):
        """Genera una baraja desordenada de cartas"""

        # Atributos:
        self.Cartas = []

        # Creación de la baraja
        palos = 4
        figuras = 13

        for palo in range(palos):
            for figura in range(figuras):
                # Se crea una carta para cada palo y figura.
                self.Cartas.append(Carta(palo, figura))

        # Se desordenan las cartas con un shuffle:
        shuffle(self.Cartas)

    def generaMano(self):
        """Genera una mano de 5 cartas "robadas" del fondo de la baraja, y la devuelve."""
        mano = []
        for _ in range(5):
            mano.append(self.Cartas.pop())

        return mano


# @ Tests


if __name__ == "__main__":
    baraja = Baraja()
    print("\nBaraja: ")
    for carta in baraja.Cartas:
        print(carta)

    manoj1 = baraja.generaMano()
    print("\nMANO: ")
    for carta in manoj1:
        print(carta)

    print("\nBaraja sin la mano: ")
    for carta in baraja.Cartas:
        print(carta)
