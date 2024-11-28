# tablero.py
import numpy as np
from variables import DIMENSIONES, CARACTER_AGUA, CARACTER_BARCO, CARACTER_IMPACTO, CARACTER_FALLO, BARCOS

class Tablero:
    def __init__(self, id_jugador):
        """
        Constructor para la clase Tablero
        - `id_jugador`: identifica a qué jugador pertenece el tablero (jugador o máquina)
        """
        self.id_jugador = id_jugador
        self.dimensiones = DIMENSIONES  
        # Crear dos tableros: uno visible para el jugador y otro interno para la máquina
        self.tablero_interno = np.full((DIMENSIONES, DIMENSIONES), CARACTER_AGUA)  
        self.tablero_visible = np.full((DIMENSIONES, DIMENSIONES), CARACTER_AGUA)  
        self.barcos = BARCOS  
        self.colocar_barcos_iniciales()

    def colocar_barcos_iniciales(self):
        """
        Coloca todos los barcos en el tablero de acuerdo a los tipos de barcos definidos en `BARCOS`
        """
        for tipo, eslora in self.barcos.items():
            # Colocar la cantidad de barcos de cada tipo en el tablero
            for _ in range(self.barcos[tipo]):
                self._colocar_barco(eslora)

    def _colocar_barco(self, eslora):
        """
        Intenta colocar un barco de longitud 'eslora' de forma aleatoria en el tablero.
        """
        while True:
            # Generamos la orientación y las coordenadas aleatorias
            orientacion = np.random.choice(['H', 'V'])  
            x, y = self._generar_coordenadas_aleatorias()

            if orientacion == 'H' and y + eslora <= DIMENSIONES:
                # Comprobamos que no haya barcos en la fila horizontal seleccionada
                if np.all(self.tablero_interno[x, y:y+eslora] == CARACTER_AGUA):
                    self.tablero_interno[x, y:y+eslora] = CARACTER_BARCO
                    return
            elif orientacion == 'V' and x + eslora <= DIMENSIONES:
                # Comprobamos que no haya barcos en la columna vertical seleccionada
                if np.all(self.tablero_interno[x:x+eslora, y] == CARACTER_AGUA):
                    self.tablero_interno[x:x+eslora, y] = CARACTER_BARCO
                    return

    def _generar_coordenadas_aleatorias(self):
        """
        Genera coordenadas aleatorias (x, y) dentro de los límites del tablero.
        """
        x = np.random.randint(0, self.dimensiones)
        y = np.random.randint(0, self.dimensiones)
        return x, y

    def imprimir_tablero(self, visible=False):
        """
        Imprime el tablero en la consola. Si 'visible' es True, muestra el tablero visible para el jugador.
        De lo contrario, muestra el tablero interno para el jugador.
        """
        tablero = self.tablero_visible if visible else self.tablero_interno
        print("   " + " ".join(str(i) for i in range(self.dimensiones)))
        print("  " + "-" * (self.dimensiones * 2))
        for i, fila in enumerate(tablero):
            print(f"{i} | " + " ".join(fila))
        print()

    def recibir_disparo(self, x, y):
        """
        Recibe un disparo en la coordenada (x, y) y actualiza el tablero según el resultado.
        - Si hay un barco, marca el impacto.
        - Si es agua, marca el fallo.
        """
        if self.tablero_interno[x, y] == CARACTER_BARCO:
            self.tablero_interno[x, y] = CARACTER_IMPACTO
            self.tablero_visible[x, y] = CARACTER_IMPACTO
            return True  # Impacto
        else:
            self.tablero_visible[x, y] = CARACTER_FALLO
            return False  # Agua

    def barcos_restantes(self):
        """
        Devuelve la cantidad de posiciones de barco sin impactar en el tablero.
        """
        return np.sum(self.tablero_interno == CARACTER_BARCO)

print(Tablero)
