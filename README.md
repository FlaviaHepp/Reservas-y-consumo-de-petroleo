# 🛢️Análisis de reservas y consumo de petróleo en el mundo (1995–2022)

Este proyecto analiza la evolución de las **reservas mundiales de petróleo** y el **consumo global de petróleo** entre 1995 y 2022, utilizando datos históricos de múltiples fuentes oficiales.

El objetivo es **identificar tendencias de largo plazo**, analizar la relación entre consumo y reservas, y explorar implicancias para **seguridad energética y sostenibilidad**.

---

## 🌍 Contexto del problema

El petróleo continúa siendo una de las principales fuentes de energía a nivel mundial.  
Comprender cómo evolucionan sus **reservas** y su **consumo** es clave para:

- planificación energética
- formulación de políticas públicas
- análisis económico y ambiental
- evaluación de la transición energética

Este proyecto aborda el problema desde una perspectiva **data-driven y exploratoria**.

---

## 🎯 Objetivos del análisis

- Analizar la evolución temporal del consumo mundial de petróleo
- Estudiar la tendencia de las reservas probadas de petróleo
- Comparar consumo y reservas en un mismo período
- Detectar años pico de consumo y de reservas
- Preparar datasets limpios para futuros modelos predictivos

---

## 📊 Fuentes de datos

Se utilizaron dos datasets principales:

1. **Consumo de petróleo por país (1965–2023)**  
   - Medido en TWh (o unidades equivalentes)
2. **Reservas mundiales de petróleo crudo (1995–2021)**  
   - Medidas en miles de millones de barriles

Los datos provienen de **fuentes confiables del sector energético** y organismos internacionales.

---

## 🧹 Limpieza y transformación de datos

- Eliminación de columnas irrelevantes
- Conversión de valores a formato numérico
- Manejo de valores faltantes
- Remodelado de datos (`melt`) para análisis temporal
- Unificación de datasets mediante la variable `Year`
- Exportación de datasets limpios para uso posterior

---

## 🔍 Análisis realizados

### Análisis exploratorio (EDA)
- Estadísticas descriptivas
- Detección de valores nulos y duplicados
- Visualización de distribuciones y outliers
- Análisis de calidad de datos con `missingno`

### Análisis temporal
- Evolución del consumo mundial de petróleo
- Evolución de las reservas mundiales de petróleo
- Comparación consumo vs. reservas en el tiempo

### Análisis de tendencias
- Identificación de años de mayor consumo
- Identificación de años con mayores reservas
- Observación de divergencias entre crecimiento del consumo y estabilidad de reservas

---

## 📈 Visualizaciones

- Series temporales (line plots)
- Comparación consumo vs. reservas
- Histogramas y diagramas de caja
- Mapas de calor de valores faltantes

Las visualizaciones permiten **interpretar patrones macroeconómicos y energéticos**.

---

## 📌 Principales insights

- El consumo mundial de petróleo muestra una tendencia creciente en el largo plazo
- Las reservas mundiales presentan mayor estabilidad relativa frente al crecimiento del consumo
- Existen años específicos con picos de consumo y reservas
- La brecha entre consumo y reservas plantea desafíos para la seguridad energética futura

---

## 🛠️ Tecnologías utilizadas

- **Python**
- **pandas, numpy**
- **matplotlib, `seaborn**`
- **scikit-learn**
- `**missingno**`

---

## 📂 Estructura del repositorio

├── Oil Consumption by Country 1965 to 2023.csv
├── World Crude Oil Reserves from 1995 to 2021.csv
├── cleaned_oil_consumption.csv
├── cleaned_oil_reserves.csv
├── Análisis de reservas y consumo de petróleo en el mundo.py
├── README.md


---

## 🚀 Próximos pasos

- Modelos de regresión para proyección de consumo
- Comparación con otras fuentes energéticas
- Análisis por regiones o países
- Incorporación de variables económicas y ambientales
- Visualización interactiva (dashboard)

---

## 👤 Autor

**Flavia Hepp**  
Data Analyst / Data Scientist en formación  
