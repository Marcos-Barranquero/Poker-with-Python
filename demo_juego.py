"""Demo de lo que sería el juego de poker."""

from c_jugador import Jugador
from c_apuesta import Apuesta
from c_baraja import Baraja

# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods


print("Bienvenido al juego de poker")

nombre = input("Introduce nombre: ")
saldo = float(input("Introduce saldo: "))
password = input("Introduce contraseña: ")

j1 = Jugador(nombre, password, saldo)

menu = 0  # Controla la decisión del jugador al seleccionar acción en el menú.

while menu != 3:
    print("Elije: ")
    print("1.- Apostar")
    print("2.- Ver datos")
    print("3.- Salir")

    menu = int(input("Decide: "))

    if menu == 1:
        baraja = Baraja()
        j1.mano = baraja.generaMano()
        while True:
            dinero_apostado = float(input("¿Cuánto dinero quieres apostar?: "))
            if dinero_apostado > 0 and dinero_apostado <= j1.saldo:
                break
            print("Debes introducir un número mayor que 0 y menor ó igual que tu saldo.")
        Apuesta(j1, dinero_apostado)
        j1.limpiar_mano()

    if menu == 2:
        print(j1)
