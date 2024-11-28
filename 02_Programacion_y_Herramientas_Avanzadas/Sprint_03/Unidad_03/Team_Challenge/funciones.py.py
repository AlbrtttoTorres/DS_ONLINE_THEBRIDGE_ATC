# funciones.py
import numpy as np
from variables import DIMENSIONES, CARACTER_AGUA, CARACTER_BARCO, CARACTER_IMPACTO, CARACTER_FALLO

def generar_coordenadas_aleatorias():
    """
    Genera y devuelve una coordenada aleatoria (x, y) dentro de los límites del tablero.
    """
    x = np.random.randint(0, DIMENSIONES)
    y = np.random.randint(0, DIMENSIONES)
    return x, y

def colocar_barco(tablero, eslora):
    """
    Coloca un barco de longitud 'eslora' en el tablero de forma aleatoria.
    Se asegura de que el barco no salga del tablero ni se superponga con otro barco.
    """
    while True:
        orientacion = np.random.choice(['H', 'V'])  
        x, y = generar_coordenadas_aleatorias()

        if orientacion == 'H' and y + eslora <= DIMENSIONES:
            # Comprobamos que no haya barcos en el área seleccionada
            if np.all(tablero[x, y:y+eslora] == CARACTER_AGUA):
                tablero[x, y:y+eslora] = CARACTER_BARCO
                return True
        elif orientacion == 'V' and x + eslora <= DIMENSIONES:
            # Comprobamos que no haya barcos en el área seleccionada
            if np.all(tablero[x:x+eslora, y] == CARACTER_AGUA):
                tablero[x:x+eslora, y] = CARACTER_BARCO
                return True

def inicializar_barcos(tablero, barcos):
    """
    Inicializa todos los barcos en el tablero dado.
    'barcos' es un diccionario con el tipo de barco y su eslora.
    """
    for tipo, eslora in barcos.items():
        for _ in range(barcos[tipo]):
            colocar_barco(tablero, eslora)

def imprimir_tablero(tablero, visible=False):
    """
    Imprime el tablero en un formato de cuadrícula en la consola.
    - `tablero`: El tablero a imprimir (array de numpy).
    - `visible`: Si es True, oculta la ubicación de los barcos que no han sido impactados.
    """
    print("   " + " ".join(str(i) for i in range(DIMENSIONES)))  
    print("  " + "-" * (DIMENSIONES * 2)) 
    for i in range(DIMENSIONES):
        # Fila con índices y contenido del tablero
        fila = []
        for j in range(DIMENSIONES):
            # Mostrar solo los impactos y fallos si el tablero es el visible del jugador
            if visible and tablero[i, j] == CARACTER_BARCO:
                fila.append(CARACTER_AGUA)  
            else:
                fila.append(tablero[i, j])  
        print(f"{i} | " + " ".join(fila))
    print()  

def obtener_coordenadas_usuario():
    """
    Solicita al usuario una coordenada para disparar y la valida.
    """
    while True:
        try:
            x, y = map(int, input("Introduce las coordenadas de disparo (x y): ").split())
            if 0 <= x < DIMENSIONES and 0 <= y < DIMENSIONES:
                return x, y
            else:
                print(f"Por favor, introduce coordenadas dentro del rango (0-{DIMENSIONES-1}).")
        except ValueError:
            print("Entrada inválida. Introduce dos números separados por un espacio.")

def turno_usuario(tablero_maquina, tablero_usuario):
    """
    Permite al jugador realizar su turno. Ofrece opciones como disparar, imprimir tableros o salir.
    """
    while True:
        print("\nOpciones:")
        print("1. Disparar a una coordenada")
        print("2. Ver mi tablero")
        print("3. Ver el tablero de la máquina")
        print("4. Salir del juego")
        
        opcion = input("Elige una opción (1-4): ")
        
        if opcion == '1':
            # Opción 1: El jugador dispara a una coordenada
            x, y = obtener_coordenadas_usuario()  
            if tablero_maquina.tablero[x, y] == CARACTER_BARCO:  
                tablero_maquina.tablero[x, y] = CARACTER_IMPACTO  
                print(f"¡Impacto en ({x}, {y})!")
            else:
                tablero_maquina.tablero[x, y] = CARACTER_FALLO  
                print(f"Fallaste en ({x}, {y})")
            return x, y  
        elif opcion == '2':
            # Opción 2: Imprimir el tablero del jugador
            imprimir_tablero(tablero_usuario.tablero)  
        elif opcion == '3':
            # Opción 3: Imprimir el tablero de la máquina 
            imprimir_tablero(tablero_maquina.tablero, visible=True)
        elif opcion == '4':
            # Opción 4: Salir del juego
            print("Saliendo del juego... ¡Hasta pronto!")
            exit()  # Sale del juego
        else:
            # Si el jugador introduce una opción incorrecta
            print("Opción inválida. Elige entre 1 y 4.")

def turno_maquina(tablero_usuario, dificultad):
    """
    Permite a la máquina realizar su turno. La máquina dispara de manera aleatoria.
    """
    num_disparos = 1  # Nivel fácil
    if dificultad == 2:
        num_disparos = 2  # Nivel normal
    elif dificultad == 3:
        num_disparos = 3  # Nivel difícil

    for _ in range(num_disparos):
        x, y = generar_coordenadas_aleatorias()  # Genera una coordenada aleatoria
        print(f"La máquina dispara a ({x}, {y})")

        if tablero_usuario.tablero[x, y] == CARACTER_BARCO:
            tablero_usuario.tablero[x, y] = CARACTER_IMPACTO  # Marca el impacto
            print(f"¡La máquina ha impactado en ({x}, {y})!")
            break  # Si la máquina acierta, termina el turno
        else:
            tablero_usuario.tablero[x, y] = CARACTER_FALLO  # Marca el fallo
            print(f"La máquina falló en ({x}, {y})")
