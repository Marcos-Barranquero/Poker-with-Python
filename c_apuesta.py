# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""Contiene la definición de la clase apuesta"""

from c_baraja import Baraja
from c_jugador import Jugador


class Apuesta():
    """Abstracción de la apuesta de un jugador realizada en la app de Póker"""

    def __init__(self, jugador, apuesta):
        """
        Crea una apuesta de un jugador.
        @jugador (c_jugador: clase Jugador) -> Jugador que realiza la apuesta.
        @apuesta (double) -> Dinero apostado por el jugador.
        """

        # Se retira el dinero de la apuesta:
        jugador.saldo -= apuesta

        # Se almacena la mano del jugador para operar con ella en compruebapremio.
        self.mano = jugador.mano

        # Se comprueba si se tiene premio:
        multiplicador_apuesta, premio = self.comprueba_premio()

        # Se añade el dinero premiado al saldo del jugador.
        jugador.saldo += (multiplicador_apuesta * apuesta)

        # Se imprime resumen de la jugada:
        print("Tu mano: ")
        for carta_de_mano in jugador.mano:
            print(carta_de_mano)

        print("Has apostado {} y tu premio es {} y ha multiplicado tu apuesta por {}".format(
            apuesta, premio, multiplicador_apuesta))

    def comprueba_premio(self):
        """Comprueba si la mano recibida tiene premio y cuál es este."""
        # Variables locales
        multiplicador = 0

        # Valor por defecto de premio:
        premio = "Ninguno"

        figuras = []  # Almacena todas las figuras de la mano. (Repetidas)
        palos = []  # Almacena todos los palos de la mano. (Repetidas)
        # Almacena la cantidad de cada tipo de figura que hay en la mano:
        nfiguras = []
        # Almacena la cantidad de cada tipo de palo que hay en la mano:
        npalos = []

        # Almaceno los palos y figuras de la mano:
        for cada_carta in self.mano:
            figuras.append(cada_carta.figura)
            palos.append(cada_carta.palo)

        # Creo dos listas sin elementos repetidos para compararlos con
        # la cantidad de elemenos que hay en figuras y palos.
        setfiguras = list(set(figuras))
        setpalos = list(set(palos))

        # Cuento las figuras iguales:
        for cada_figura in setfiguras:
            nfiguras.append(figuras.count(cada_figura))

        # Cuento los palos iguales:
        for cada_palo in setpalos:
            npalos.append(palos.count(cada_palo))

        # Premios:
        # Pareja:
        if nfiguras.count(2) == 1:
            premio = "Pareja"
            multiplicador = 1

        # Doble pareja:
        if nfiguras.count(2) == 2:
            premio = "Doble pareja"
            multiplicador = 2

        # Trío: tres cartas con misma figura
        if nfiguras.count(3) == 1:
            premio = "Trío"
            multiplicador = 3

        # Color: Cinco cartas del mismo palo y de diferente figura.
        if npalos.count(5) == 1:
            premio = "Color"
            multiplicador = 4

        # Full: Tres cartas de la misma figura y una pareja de una misma figura diferente.
        if nfiguras.count(3) == 1 and nfiguras.count(2) == 1:
            premio = "Full"
            multiplicador = 5

        # Poker: Cuatro cartas con la misma figura.
        if nfiguras.count(4) == 1:
            premio = "Poker"
            multiplicador = 6

        return multiplicador, premio

# @ Tests:


if __name__ == "__main__":
    baraja = Baraja()
    mano = baraja.generaMano()
    player = Jugador("Marcos", 200)
    print(player.mano)
    print(player)

    Apuesta(player, 50)
    print(player)
