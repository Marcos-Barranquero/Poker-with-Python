# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

"""Contiene la definición de la clase jugador."""

from c_baraja import Baraja


class Jugador():
    """Jugador de poker."""

    def __init__(self, nombre, password, saldo=0):
        """Instancia al jugador con su nombre y su saldo"""
        self.nombre = nombre
        self.password = password
        self.saldo = saldo

        self.mano = []

    def __str__(self):
        if self.mano == []:
            return "Nombre: {} ; Saldo: {}".format(self.nombre, self.saldo)

        cartas = []
        for i in range(5):
            cartas.append(self.mano[i])
        return "Nombre: {} ; Saldo: {} \nCartas: {}".format(self.nombre, self.saldo, cartas)

    def limpiar_mano(self):
        """Resetea la mano del jugador a ninguna carta."""
        self.mano = []

# @ Tests:


if __name__ == "__main__":
    j1 = Jugador("Mariano", "contras", 500)

    baraja = Baraja()

    print(j1)
    j1.mano = baraja.generaMano()

    for j in range(len(j1.mano)):
        print(j1.mano[j])

    print(j1)
