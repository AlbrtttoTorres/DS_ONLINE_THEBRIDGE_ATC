import pandas as pd
import sqlite3
# Conectamos con la base de que vamos a crear
conexion = sqlite3.connect('Taller_Gadget.db')
# # Obtenemos un cursor que utilizaremos para ejecutar comandos SQL
cursor = conexion.cursor()

# TABLA 1: Crear tabla Proveedores
cursor.execute('''
CREATE TABLE IF NOT EXISTS Proveedores (
    ID_Proveedor INTEGER PRIMARY KEY,
    Nombre TEXT NOT NULL,
    Direccion TEXT,
    Ciudad TEXT,
    Provincia TEXT
)
''')
print("Tabla Proveedores creada correctamente.")

proveedores = [
    (1, 'Patricia', 'Calle Alcalá 24', 'Madrid', 'Madrid'),
    (2, 'Alberto', 'Calle de Principe 75', 'Vigo', 'Pontevedra'),
    (3, 'Quique', 'Gran Vía 57', 'Madrid', 'Madrid'),
    (4, 'Carolina', 'Avenida de Las Canteras 8', 'Las Palmas', 'Las Palmas'),
    (5, 'Antonio', 'La Rambla 157', 'Barcelona', 'Barcelona')
]
cursor.executemany('''
INSERT OR IGNORE INTO Proveedores (ID_Proveedor, Nombre, Direccion, Ciudad, Provincia)
VALUES (?, ?, ?, ?, ?)
''', proveedores)
print("Proveedores: Datos insertados correctamente.")

# TABLA 2: Crear tabla Suministros
cursor.execute('''
CREATE TABLE IF NOT EXISTS Suministros (
    ID_Suministro INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_Proveedor INTEGER NOT NULL,
    ID_Pieza INTEGER NOT NULL,
    Cantidad INTEGER NOT NULL,
    Fecha DATE NOT NULL,
    FOREIGN KEY (ID_Proveedor) REFERENCES Proveedores (ID_Proveedor),
    FOREIGN KEY (ID_Pieza) REFERENCES Piezas (ID_Pieza)
)
''')
print("Tabla Suministros creada correctamente.")

suministros = [
    (1, 1, 5, '2024-01-10'),
    (2, 2, 3, '2024-02-15'),
    (3, 3, 1, '2024-03-01'),
    (4, 4, 2, '2024-04-05'),
    (5, 5, 15, '2024-05-12'),
    (4, 5, 12, '2024-06-18'),
    (2, 1, 10, '2024-07-01'),
    (5, 3, 20, '2024-08-05'),
    (3, 2, 15, '2024-09-12'),
    (1, 4, 12, '2024-10-18')
]
cursor.executemany('''
INSERT INTO Suministros (ID_Proveedor, ID_Pieza, Cantidad, Fecha)
VALUES (?, ?, ?, ?)
''', suministros)
print("Suministros: Datos insertados correctamente.")

# TABLA 3: Crear tabla Categorías
cursor.execute('''
CREATE TABLE IF NOT EXISTS Categorias (
    ID_Categoria INTEGER PRIMARY KEY,
    Nombre_pieza TEXT NOT NULL
)
''')
print("Tabla Categorías creada correctamente.")

categorias = [
    (1, 'Motor'),
    (2, 'Freno'),
    (3, 'Carrocería'),
    (4, 'Suspensión'),
    (5, 'Eléctrico')
]
cursor.executemany('''
INSERT OR IGNORE INTO Categorias (ID_Categoria, Nombre_pieza)
VALUES (?, ?)
''', categorias)
print("Categorías: Datos insertados correctamente.")

# TABLA 4: Crear tabla Piezas
cursor.execute('''
CREATE TABLE IF NOT EXISTS Piezas (
    ID_Pieza INTEGER PRIMARY KEY,
    Nombre_pieza TEXT NOT NULL,
    Color TEXT,
    Precio REAL,
    ID_Categoria INTEGER NOT NULL,
    FOREIGN KEY (ID_Categoria) REFERENCES Categorias (ID_Categoria)
)
''')
print("Tabla Piezas creada correctamente.")

piezas = [
    (1, 'Correa de alternador', 'Negro', 750.10, 1),
    (2, 'Pastillas de freno', 'Negro', 150.05, 2),
    (3, 'Tapa de motor', 'Blanco', 981.50, 3),
    (4, 'Caja de muelles', 'Rojo', 80.50, 4),
    (5, 'Elevalunas', 'Gris', 622.75, 5)
]
cursor.executemany('''
INSERT OR IGNORE INTO Piezas (ID_Pieza, Nombre_pieza, Color, Precio, ID_Categoria)
VALUES (?, ?, ?, ?, ?)
''', piezas)
print("Piezas: Datos insertados correctamente.")

# Guardar cambios y cerrar conexión
conexion.commit()
conexion.close()
print("Base de datos configurada y datos insertados correctamente.")
conexion = sqlite3.connect('Taller_Gadget.db')
cursor = conexion.cursor()

# Consulta para mostrar los suministros
cursor.execute('''
SELECT 
    p.Nombre AS Proveedor,
    pi.Nombre_pieza AS Pieza,
    s.Cantidad,
    s.Fecha
FROM Suministros s
JOIN Proveedores p ON s.ID_Proveedor = p.ID_Proveedor
JOIN Piezas pi ON s.ID_Pieza = pi.ID_Pieza
ORDER BY s.Fecha
''')

resultados = cursor.fetchall()
print("Historial de Suministros:")
for fila in resultados:
    print(fila)

conexion.close()
# Conectar a la base de datos
connection = sqlite3.connect('Taller_Gadget.db')

# Lista de tablas que deseas consultar
tablas = ['Proveedores', 'Suministros', 'Categorias', 'Piezas']

# Consultar y mostrar los datos de cada tabla
for tabla in tablas:
    query = f"SELECT * FROM {tabla}"  # Construir la consulta para cada tabla
    df = pd.read_sql(query, connection)  # Leer los datos en un DataFrame
    print(f"\nDatos de la tabla {tabla}:\n")
    print(df)

# Cerrar conexión
connection.close()
