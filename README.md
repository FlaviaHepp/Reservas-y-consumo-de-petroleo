# Reservas-y-consumo-de-petroleo
Análisis de Reservas y Consumo Mundial de Petróleo (1995-2022)

Este conjunto de datos proporciona información completa sobre las reservas mundiales de petróleo y las tendencias de consumo desde 1995 hasta 2022. Incluye puntos de datos de varios países o entidades, y detalla tanto las cantidades de reservas de petróleo probadas como el consumo anual de petróleo medido en teravatios-hora (TWh) o unidades equivalentes.

**Características principales del conjunto de datos:**
*Entidad:* Nombres de países o regiones incluidos en el conjunto de datos.
*Año:* Período de tiempo que va de 1995 a 2022, capturando puntos de datos anuales.
*Reservas de petróleo:* Cantidades de reservas probadas de petróleo, normalmente medidas en barriles o toneladas métricas, que reflejan la cantidad estimada de petróleo económicamente recuperable.
*Consumo de petróleo (TWh):* Consumo anual de petróleo representado en teravatios-hora (TWh) o unidades equivalentes, que indica la cantidad de petróleo utilizada para diversas necesidades energéticas, incluido el transporte, los procesos industriales y el uso residencial.

**Análisis de tendencias:** 
Explore la evolución de las reservas mundiales de petróleo y los patrones de consumo a lo largo del tiempo, identificando cambios influenciados por factores económicos, avances tecnológicos y políticas ambientales.

**Comparaciones regionales:**
Compare los niveles de reservas de petróleo y las tasas de consumo en diferentes países y regiones para comprender las variaciones geográficas y las dependencias de los recursos de combustibles fósiles.

Desarrollo de un análisis técnico de datos históricos sobre reservas probadas y consumo global de petróleo desde 1995 hasta 2022, con el objetivo de identificar tendencias clave, patrones regionales y relaciones entre el consumo y las reservas.
Limpieza, transformación y visualización de datos usando Python y librerías como Pandas, Seaborn y Matplotlib.
Implementación de técnicas de análisis exploratorio para manejar valores faltantes, identificar duplicados y normalizar datos.
Creación de modelos predictivos utilizando algoritmos de aprendizaje supervisado (Regresión Lineal, Árboles de Decisión, Random Forest).
Uso de GridSearchCV para optimizar hiperparámetros de los modelos predictivos.
Visualización de tendencias históricas mediante gráficos de líneas y diagramas de cajas.
*Herramientas utilizadas:* Python, Pandas, Matplotlib, Seaborn, Scikit-learn y Missingno.
*Modelos de regresión:* Regresión lineal, Random Forest, Árboles de decisión.
*Gestión y limpieza de datos:* Manejo de valores faltantes y transformación de datos con NumPy.

***Resultados clave:***
Identificación del año de mayor consumo de petróleo (en TWh) y el año con mayores reservas probadas (en miles de millones de barriles).
Generación de conjuntos de datos limpios y listos para análisis futuros, exportados en formato CSV.
Comparación visual y cuantitativa entre tendencias de consumo y reservas globales, proporcionando insights sobre la sostenibilidad energética.
*Impacto:* Este análisis puede informar decisiones estratégicas relacionadas con la seguridad energética, formulación de políticas públicas y estudios sobre el impacto ambiental del consumo de combustibles fósiles.

# Análisis de reservas y consumo de petróleo en el mundo (1995–2022)

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
- **matplotlib, seaborn**
- **scikit-learn**
- **missingno**

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
