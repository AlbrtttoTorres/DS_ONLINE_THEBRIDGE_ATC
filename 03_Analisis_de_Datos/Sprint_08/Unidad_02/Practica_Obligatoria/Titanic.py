import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df_titanic = pd.read_csv("./data/titanic.csv")
df_titanic

# Gráfico 1: Tasa de mortalidad alta
survival_counts = df_titanic['survived'].value_counts()
plt.figure(figsize=(8, 6))
survival_counts.plot.pie(
    autopct='%1.1f%%',
    labels=['Fallecido', 'Superviviente'],
    colors=['lightcoral', 'lightblue']
)
plt.title("Supervivencia en el Titanic")
plt.ylabel("")
plt.show()

# Gráfico 2 : Tasa de supervivencia por genero
plt.figure(figsize=(8, 6))
sns.barplot(
    data=df_titanic,
    x='sex',
    y='survived',
    hue='class',  # Asigna alguna columna como 'hue'
    errorbar=None,
    palette='pastel'
)
plt.title("Tasa de Supervivencia por Género")
plt.ylabel("Tasa de Supervivencia")
plt.xlabel("Género")
plt.show()

# Gráfico 3: Supervivencia por clase
plt.figure(figsize=(8, 6))
sns.barplot(
    data=df_titanic,
    x='pclass',
    y='survived',
    hue='group',
    errorbar=None,
    palette='pastel'
)
plt.title("Tasa de Supervivencia por Clase")
plt.ylabel("Tasa de Supervivencia")
plt.xlabel("Clase")
plt.xticks(ticks=[0, 1, 2], labels=['Primera', 'Segunda', 'Tercera'])
plt.show()

# Gráfico 4: Mujeres y niños según la clase
df_titanic['group'] = df_titanic.apply(
    lambda row: 'Niño' if row['age'] < 18 else row['sex'], axis=1
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=df_titanic,
    x='pclass',
    y='survived',
    hue='group',
    errorbar=None,
    palette='muted'
)
plt.title("Tasa de Supervivencia por Clase (Mujeres y Niños)")
plt.ylabel("Tasa de Supervivencia")
plt.xlabel("Clase")
plt.xticks(ticks=[0, 1, 2], labels=['Primera', 'Segunda', 'Tercera'])
plt.legend(title="Grupo")
plt.show()

# Gráfico 5: Influencia del puerto de embarque
plt.figure(figsize=(8, 6))
sns.barplot(
    data=df_titanic,
    x='embarked',
    y='survived',
    hue='class',
    errorbar=None,
    palette='viridis'
)
plt.title("Tasa de Supervivencia por Puerto de Embarque")
plt.ylabel("Tasa de Supervivencia")
plt.xlabel("Puerto de Embarque")
plt.xticks(ticks=[0, 1, 2], labels=['Cherburgo (C)', 'Queenstown (Q)', 'Southampton (S)'])
plt.show()
 