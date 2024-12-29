import numpy as np
import pandas as pd
#import matplotlib as mpl
#import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

# Configuración de Enlaces de los Datasets del Proyecto en Github
URL1 = 'https://github.com/Leonardo-rodcas/Proyecto-DS-61190-E-Commerce/raw/refs/heads/main/Distribuidor.xlsx'
#URL2 = 'https://github.com/Leonardo-rodcas/Proyecto-DS-61190-E-Commerce/blob/ee7a3c683a36e1727090261010f98a6dd1053c1e/Periodo_Distribuidor.xlsx'
#URL3 = 'https://github.com/Leonardo-rodcas/Proyecto-DS-61190-E-Commerce/blob/ee7a3c683a36e1727090261010f98a6dd1053c1e/Periodo_Zona.xlsx'
#URL4 = 'https://github.com/Leonardo-rodcas/Proyecto-DS-61190-E-Commerce/blob/ee7a3c683a36e1727090261010f98a6dd1053c1e/Provincia_Distribuidor.xlsx'
#URL5 = 'https://github.com/Leonardo-rodcas/Proyecto-DS-61190-E-Commerce/blob/ee7a3c683a36e1727090261010f98a6dd1053c1e/Zona.xlsx'


df_dist = pd.read_excel(URL1)
print(df_dist)
#df.plot(kind='line', x='Mes', y='Ventas', marker='o', title='Ventas Mensuales')
#plt.ylabel('Ventas en Pesos')
#plt.xlabel('Mes')
#plt.grid(True)  
#plt.show()  

#st.write("""
# Mi primera aplicación interactiva
## Histograma sobre el eje X e Y
#""")

# Using "with" notation
#with st.sidebar:
    # Titulo
#    st.write("# Opciones")
    # slider
 #   div = st.slider('Número de bins:', 0, 130, 25)
  #  st.write("Bins=", div)

# Desplegamos un histograma con los datos del eje X
#fig, ax = plt.subplots(1, 2, figsize=(10, 3))
#ax[0].hist(df["X"], bins=div, color= "lightcoral")
#ax[0].set_xlabel('Posición en metros')
#ax[0].set_ylabel('Frecuencia')
#ax[0].set_title('Histograma posiciónes en el eje X')

#ax[1].hist(df["Y"], bins=div, color= "indianred")
#ax[1].set_xlabel('Posición en metros')
#ax[1].set_ylabel('Frecuencia')
#ax[1].set_title('Histograma posiciónes en el eje Y')

# Desplegamos el gráfico
#st.pyplot(fig)

st.write("""
## Muestra de datos cargados
#""")
# Graficamos una tabla
st.table(df_dist.head())