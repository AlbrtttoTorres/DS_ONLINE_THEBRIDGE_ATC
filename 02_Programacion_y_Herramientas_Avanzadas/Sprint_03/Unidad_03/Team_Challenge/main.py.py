# main.py
import numpy as np
from tablero import Tablero
from funciones import generar_coordenadas_aleatorias, imprimir_tablero
from variables import DIMENSIONES, BARCOS
# Definición de reglas del juego
regla_juego = """Bienvenid@ a Hundir la Flota! Tu contrincante va a ser una máquina. Cada uno disparará a una coordenada.
Si logras disparar en una posición de un barco de la máquina, aparecerá una 'X' en el tablero del
adversario y podrás seguir disparando mientras aciertes. Si, por el contrario, disparas al agua, aparecerá un '-' en
el tablero del adversario y el turno será de la máquina. Para ganar, se tienen que "hundir" todos los barcos del adversario."""
# Función para iniciar el juego y solicitar el nombre del jugador
def empezar_juego():
    """Inicia la partida y solicita el nombre del jugador.Si el jugador no desea jugar, termina el programa."""
    while True:
        pregunta_01 = input("Hola, ¿quieres iniciar una partida? (Contesta si o no): ")
        # Convertimos la respuesta a minúsculas para hacerla insensible a mayúsculas/minúsculas
        if pregunta_01.strip().lower() == "si":
            pregunta_02 = input("¿Cómo te llamas? ")
            print(regla_juego)
            return pregunta_02
        elif pregunta_01.strip().lower() == "no":
            print("Veo que no quieres jugar, ¡Hasta la próxima!")
            return None
        else:
            print("Respuesta no válida. Por favor, contesta 'si' o 'no'.")
# Pedir al jugador que seleccione el nivel de dificultad
def nivel_juego():
    while True:
        try:
            dificultad = int(input("Selecciona el nivel de dificultad (1 - Fácil, 2 - Normal, 3 - Difícil): "))
            if dificultad in [1, 2, 3]:
                return dificultad  # Devuelve el nivel de dificultad
            else:
                print("Por favor, elige un número entre 1 y 3.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
# Función de incio del juego
def main():
    nombre_jugador = empezar_juego()
    if not nombre_jugador:
        return  # Sale si el jugador no quiere iniciar la partida
    print(f"¡Buena suerte, {nombre_jugador}!")
# Inicializar tableros de jugador y máquina
    tablero_jugador = Tablero(id_jugador="jugador")
    tablero_maquina = Tablero(id_jugador="máquina")
# Mostrar el tablero del jugador al iniciar el juego, con posiciones de barcos visibles
    print("\nEste es tu tablero inicial con tus posiciones de barcos:")
    imprimir_tablero(tablero_jugador.tablero_interno)
# Pedir al jugador que seleccione el nivel de dificultad
    dificultad = nivel_juego()
    print(f"Nivel de dificultad seleccionado: {dificultad}")
    juego_terminado = False
    turno_jugador = True  # El jugador empieza primero
    while not juego_terminado:
        if turno_jugador:
            print("\nTu turno:")
            print("Opciones:")
            print("1. Disparar a una coordenada")
            print("2. Ver mi tablero")
            print("3. Ver el tablero de la máquina")
            print("4. Salir del juego")
            while True:
                try:
                    opcion = input("Elige una opción (1-4): ")
                    if opcion == '1':
                        # Opción 1: El jugador dispara a una coordenada
                        while True:
                            try:
                                x, y = map(int, input("Introduce las coordenadas de disparo (x y): ").split())
                                if not (0 <= x < DIMENSIONES and 0 <= y < DIMENSIONES):
                                    print(f"Las coordenadas deben estar entre 0 y {DIMENSIONES-1}. Intenta de nuevo.")
                                    continue
                                if tablero_maquina.recibir_disparo(x, y):
                                    print("¡Impacto! Vuelve a disparar.")
                                    break
                                else:
                                    print("Agua... le toca a la máquina.")
                                    turno_jugador = False
                                    break
                            except ValueError:
                                print("Entrada no válida. Por favor, ingresa dos números separados por un espacio.")
                        break
                    elif opcion == '2':
                        # Opción 2: Imprimir el tablero del jugador
                        imprimir_tablero(tablero_jugador.tablero_interno)
                        break
                    elif opcion == '3':
                        # Opción 3: Imprimir el tablero de la máquina (con los impactos visibles)
                        imprimir_tablero(tablero_maquina.tablero_visible, visible=True)
                        break
                    elif opcion == '4':
                        # Opción 4: Salir del juego
                        print("Saliendo del juego... ¡Hasta pronto!")
                        juego_terminado = True
                        break
                    else:
                        print("Opción inválida. Elige entre 1 y 4.")
                except ValueError:
                    print("Opción no válida. Por favor, elige entre 1 y 4.")
        else:
            # Opción para la máquina
            print("\nEl turno de la máquina:")
            x, y = generar_coordenadas_aleatorias()
            print(f"La máquina dispara a ({x}, {y})...")
            if tablero_jugador.recibir_disparo(x, y):
                print("¡La máquina te ha dado! Vuelve a disparar.")
            else:
                print("La máquina falló... ¡Tu turno!")
                turno_jugador = True
        # Comprobación de fin de juego
        if tablero_maquina.barcos_restantes() == 0:
            print("¡Felicidades! Has hundido todos los barcos enemigos. ¡Ganaste!")
            juego_terminado = True
        elif tablero_jugador.barcos_restantes() == 0:
            print("La máquina ha hundido todos tus barcos. Has perdido.")
            juego_terminado = True
if __name__ == "__main__":
    main()