import sqlite3

# Crear conexión a la base de datos (o archivo .db)
conn = sqlite3.connect("proveedores.db")
cursor = conn.cursor()

# 1. Crear la tabla Proveedores
cursor.execute("""
CREATE TABLE IF NOT EXISTS Proveedores (
    codigo_proveedor INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    direccion TEXT,
    ciudad TEXT,
    provincia TEXT
);
""")

# 2. Crear la tabla Categorías
cursor.execute("""
CREATE TABLE IF NOT EXISTS Categorias (
    codigo_categoria INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL
);
""")

# 3. Crear la tabla Piezas
cursor.execute("""
CREATE TABLE IF NOT EXISTS Piezas (
    codigo_pieza INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    color TEXT,
    precio REAL NOT NULL,
    codigo_categoria INTEGER NOT NULL,
    FOREIGN KEY (codigo_categoria) REFERENCES Categorias(codigo_categoria)
);
""")

# 4. Crear la tabla Suministros
cursor.execute("""
CREATE TABLE IF NOT EXISTS Suministros (
    codigo_proveedor INTEGER NOT NULL,
    codigo_pieza INTEGER NOT NULL,
    fecha_suministro DATE NOT NULL,
    cantidad INTEGER NOT NULL,
    PRIMARY KEY (codigo_proveedor, codigo_pieza, fecha_suministro),
    FOREIGN KEY (codigo_proveedor) REFERENCES Proveedores(codigo_proveedor),
    FOREIGN KEY (codigo_pieza) REFERENCES Piezas(codigo_pieza)
);
""")

# Insertar datos representativos en las tablas
# 1. Proveedores
proveedores = [
    (1, "Proveedor A", "Calle Falsa 123", "Ciudad A", "Provincia A"),
    (2, "Proveedor B", "Calle Verdadera 456", "Ciudad B", "Provincia B"),
]
cursor.executemany("INSERT OR IGNORE INTO Proveedores VALUES (?, ?, ?, ?, ?)", proveedores)

# 2. Categorías
categorias = [
    (1, "Electrónica"),
    (2, "Mecánica"),
    (3, "Química"),
]
cursor.executemany("INSERT OR IGNORE INTO Categorias VALUES (?, ?)", categorias)

# 3. Piezas
piezas = [
    (1, "Resistor", "Rojo", 0.10, 1),
    (2, "Capacitor", "Azul", 0.20, 1),
    (3, "Tornillo", "Plata", 0.05, 2),
    (4, "Lubricante", "Transparente", 5.00, 3),
]
cursor.executemany("INSERT OR IGNORE INTO Piezas VALUES (?, ?, ?, ?, ?)", piezas)

# 4. Suministros
suministros = [
    (1, 1, "2024-11-01", 500),
    (1, 2, "2024-11-02", 300),
    (2, 3, "2024-11-03", 1000),
    (2, 4, "2024-11-04", 50),
    (1, 1, "2024-11-05", 200),  # Histórico del mismo proveedor suministrando la misma pieza
]
cursor.executemany("INSERT OR IGNORE INTO Suministros VALUES (?, ?, ?, ?)", suministros)

# Confirmar cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos creada y datos insertados correctamente.")
