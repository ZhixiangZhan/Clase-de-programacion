import random

# Constantes
BARAJA = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
VALORES = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

# Función para crear una baraja
def crear_baraja():
    baraja = []
    for _ in range(4):
        for carta in BARAJA:
            baraja.append(carta)
    random.shuffle(baraja)
    return baraja

# Función para calcular el valor de una mano
def calcular_valor(mano):
    valor = 0
    aces = 0
    for carta in mano:
        if carta == 'A':
            aces += 1
            valor += 11
        else:
            valor += VALORES[carta]
    while valor > 21 and aces:
        valor -= 10
        aces -= 1
    return valor

# Función para jugar una ronda
def jugar_ronda(baraja, banca):
    jugador_mano = [baraja.pop(), baraja.pop()]
    banca_mano = [baraja.pop(), baraja.pop()]
    
    print("Tu mano:", jugador_mano)
    print("Mano del banquero:", [banca_mano[0], 'X'])
    
    while True:
        accion = input("¿Qué deseas hacer? (1) Pedir carta, (2) Plantarse: ")
        if accion == '1':
            jugador_mano.append(baraja.pop())
            print("Tu mano:", jugador_mano)
            if calcular_valor(jugador_mano) > 21:
                print("Te has pasado! Pierdes.")
                return
        elif accion == '2':
            break
    
    print("Mano del banquero:", banca_mano)
    while calcular_valor(banca_mano) < 17:
        banca_mano.append(baraja.pop())
        print("Mano del banquero:", banca_mano)
    
    if calcular_valor(banca_mano) > 21:
        print("El banquero se ha pasado! Ganaste.")
    elif calcular_valor(banca_mano) < calcular_valor(jugador_mano):
        print("Ganaste!")
    elif calcular_valor(banca_mano) > calcular_valor(jugador_mano):
        print("Pierdes.")
    else:
        print("Empate.")

# Función principal
def main():
    baraja = crear_baraja()
    banca = 1000
    while True:
        print("Dinero en la banca:", banca)
        apuesta = int(input("¿Cuánto deseas apostar?: "))
        if apuesta > banca:
            print("No tienes suficiente dinero para apostar eso.")
            continue
        banca -= apuesta
        jugar_ronda(baraja, banca)
        if calcular_valor([baraja[-1]]) == 11:
            baraja = crear_baraja()
        if banca <= 0:
            print("Te has quedado sin dinero. Game over.")
            break

if __name__ == "__main__":
    main()