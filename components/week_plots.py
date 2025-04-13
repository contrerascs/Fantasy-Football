import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def pts_week_plots(week_data):
    week_data = week_data[week_data['Pts*'] >= 1]

    # Configurar la gráfica
    plt.figure(figsize=(10, 5))
    plt.bar(week_data['Player'], week_data['Pts*'], color=['skyblue', 'lightgreen', 'salmon'])
    plt.title('Puntos de Jugadores (Pts*)', fontweight='bold')
    plt.xlabel('Jugador')
    plt.ylabel('Puntos')
    plt.xticks(rotation=45)  # Rotar nombres si son largos

    # Mostrar valores encima de las barras
    for i, pts in enumerate(week_data['Pts*']):
        plt.text(i, pts + 0.5, str(pts), ha='center')

    return plt