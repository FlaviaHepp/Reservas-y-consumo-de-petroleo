
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
import warnings
warnings.filterwarnings('ignore')
import numpy as np 
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV
import os
import missingno as msno


# Cargar los conjuntos de datos
consumption_df = pd.read_csv("Oil Consumption by Country 1965 to 2023.csv")
reserves_df = pd.read_csv("World Crude Oil Reserves from 1995 to 2021.csv")

# Muestre las primeras filas para comprender la estructura
print(consumption_df.head())
print(reserves_df.head())

# Elimine columnas irrelevantes y filtre los años relevantes
consumption_df = consumption_df.drop(['Entity'], axis=1)
consumption_df = consumption_df.loc[:, '1995':'2022'].apply(pd.to_numeric, errors='coerce')
consumption_df = consumption_df.dropna()

# Remodelar los datos para el análisis
consumption_df = consumption_df.melt(var_name='Year', value_name='Consumption')
consumption_df['Year'] = consumption_df['Year'].astype(int)
# Convierta los datos de reservas a numéricos y maneje los valores faltantes
reserves_df.iloc[:, 1:] = reserves_df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')
reserves_df = reserves_df.dropna()

# Remodelar los datos para el análisis
reserves_df = reserves_df.melt(id_vars=['World Crude Oil Reserves (billion)'], var_name='Year', value_name='Reserves')
reserves_df['Year'] = reserves_df['Year'].astype(int)
plt.style.use('dark_background')
plt.figure(figsize=(14, 7))
sns.lineplot(data=consumption_df, x='Year', y='Consumption', color = "fuchsia")
plt.title('Consumo mundial de petróleo (1995-2022)\n', fontsize = '16', fontweight = 'bold')
plt.xlabel('Año\n')
plt.ylabel('Consumo de Petróleo (TWh)\n')
plt.show()

plt.figure(figsize=(14, 7))
sns.lineplot(data=reserves_df, x='Year', y='Reserves', color = "fuchsia")
plt.title('Reservas mundiales de petróleo (1995-2022)\n', fontsize = '16', fontweight = 'bold')
plt.xlabel('Año\n')
plt.ylabel('Reservas de petróleo (miles de millones de barriles)\n')
plt.show()

# Fusionar los conjuntos de datos en la columna 'Año'
merged_df = pd.merge(consumption_df, reserves_df, on='Year')

plt.figure(figsize=(14, 7))
sns.lineplot(data=merged_df, x='Year', y='Consumption', label='Consumo (TWh)', color = "lime")
sns.lineplot(data=merged_df, x='Year', y='Reserves', label='Reservas (miles de millones de barriles)', color = "cyan")
plt.title('Comparación del consumo y las reservas mundiales de petróleo (1995-2022)\n', fontsize = '16', fontweight = 'bold')
plt.xlabel('Año\n')
plt.ylabel('Valor\n')
plt.legend()
plt.show()

# Imprimir estadísticas resumidas
print(consumption_df.describe())
print(reserves_df.describe())

# Destacar tendencias u observaciones clave
# Ejemplo: Identificar el año de mayor consumo
peak_consumption_year = consumption_df.loc[consumption_df['Consumption'].idxmax()]
print(f"Año de consumo máximo: {peak_consumption_year['Year']} with {peak_consumption_year['Consumption']} TWh")

# Ejemplo: Identificar el año de reservas máximas
peak_reserves_year = reserves_df.loc[reserves_df['Reserves'].idxmax()]
print(f"Año pico de reservas: {peak_reserves_year['Year']} con {peak_reserves_year['Reserves']} mil millones de barriles")

# Guardar conjuntos de datos limpios
consumption_df.to_csv('cleaned_oil_consumption.csv', index=False)
reserves_df.to_csv('cleaned_oil_reserves.csv', index=False)
     
df = pd.read_csv("World Crude Oil Reserves from 1995 to 2021.csv")
print(df.head())

print(df.tail())

print(df.info())

df.describe().T

df.describe().T.plot(kind='bar')

df.isnull().sum()

sns.heatmap(df.isnull())

df=df.fillna(df.median)
df.duplicated().sum()

msno.bar(df)

df.columns.to_list()


plt.style.use('dark_background')

# Lista de columnas
columns = ['World Crude Oil Reserves (billion)', '1995', '1996', '1997', '1998', '1999',
           '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', 
           '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', 
           '2018', '2019', '2020', '2021']

for column in columns:
    if column in df.columns:
        if df[column].dtype == 'float64' or df[column].dtype == 'int64':
            fig, (ax_box, ax_hist) = plt.subplots(1, 2, figsize=(10, 5))

            # Manejar los valores faltantes si los hay
            data = df[column].dropna()

            # Diagrama de caja
            ax_box.boxplot(data, vert=False, whis=1.5)
            ax_box.set_xlabel('Value')
            ax_box.set_title(f'{column} Box')

            # Histograma
            sns.histplot(data, bins=50, color='blue', kde=True, ax=ax_hist)
            ax_hist.set_xlabel('Value')
            ax_hist.set_ylabel('Frequency')
            ax_hist.set_title(f'{column} Distribution')

            # Mostrar trama
            plt.tight_layout()
            plt.show()
    else:
        print(f"Columna '{column}' no existe en el DataFrame")
        


