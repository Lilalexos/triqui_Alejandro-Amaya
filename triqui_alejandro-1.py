#Luis Alejandro Amaya Corredor
def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-" * 5)

def verificar_ganador(tablero):
    # Verificar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != ' ':
            return fila[0]

    # Verificar columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return tablero[0][i]

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return tablero[0][2]

    return None

def jugar_triqui():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugador_actual = 'X'

    while True:
        imprimir_tablero(tablero)
        fila = int(input(f"jugador {jugador_actual}, elige una fila (0, 1, 2): "))
        columna = int(input(f"jugador {jugador_actual}, elige una columna (0, 1, 2): "))

        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = jugador_actual
            ganador = verificar_ganador(tablero)
            if ganador:
                imprimir_tablero(tablero)
                print(f"¡jugador {ganador} ha ganado!")
                break
            elif all(tablero[i][j] != ' ' for i in range(3) for j in range(3)):
                imprimir_tablero(tablero)
                print("¡empate!")
                break
            jugador_actual = 'O' if jugador_actual == 'X' else 'X'
        else:
            print("esa casilla ya esta ocupada. Intenta de nuevo.")

if __name__ == "__main__":
    jugar_triqui()
