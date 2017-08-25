# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods

"""Contiene la definición de la clase carta"""


class Carta():
    """Abstracción de la clase carta."""

    def __init__(self, palo, figura):  # Constructor
        """Constructor que crea una carta.
            @palo(str) -> Representación del palo de la carta.
            @figura(str) -> Representación de la figura de la carta.
        """
        self.palo = palo
        self.figura = figura

    def __str__(self):  # toString
        """Devuelve una representación de la carta mediante una string."""
        # Variables locales:
        palos = ["Corazones", "Rombos", "Picas", "Treboles"]
        figuras = ["As", "Dos", "Tres", "Cuatro", "Cinco", "Seis",
                   "Siete", "Ocho", "Nueve", "Diez", "Sota", "Caballo", "Rey"]

        return "{} de {}".format(figuras[self.figura], palos[self.palo])

    __repr__ = __str__  # Para poder mostrar la lista de cartas con un print.


# @Tests


if __name__ == "__main__":
    carta1 = Carta(1, 3)
    print(carta1)
