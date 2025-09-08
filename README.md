**Análisis y clasificación de trayectorias marítimas mediante aprendizaje profundo**

**- Introducción:**

Este trabajo consiste en representar las trayectorias seguidas por distintos tipos de embarcaciones para su posterior clasificación mediante técnicas de aprendizaje profundo, en concreto, redes de neuronas convolucionales (CNNs).

**- Objetivos:**

El objetivo principal de este trabajo es encontrar un modelo basado en aprendizaje profundo que sea capaz de asociar distintas trayectorias marítimas con distintos tipos de barcos. Ya que esta hipótesis no es segura, en este proyecto también se abordará la detección de anomalías en las trayectorias estudiadas. Es decir, el modelo elegido no solo tendrá que asociar una trayectoria con un tipo de embarcación (Problema de clasificación de embarcaciones), también tendrá que determinar si la trayectoria estudiada se trata o no de una anomalía (Problema de clasificación de anomalías).

**- Pasos:**

Los pasos seguidos en este proyecto han sido los siguientes:

- **PASO 1:** Preprocesamiento de los datos.
- **PASO 2:** Como es necesario que todas las trayectorias tengan la misma estructura, es decir, que su nº de mediciones sea el mismo, se aplicará una compresión de trayectorias.
- **PASO 3:** Una vez se han comprimido las trayectorias, buscaremos la forma más adecuada de representarlas. Para ello, se probarán 3 tipos distintos de representaciones (R1, R2 y R3).
- **PASO 4:** Dependiendo de la representación elegida, se hará uso de una arquitectura CNN concreta (1D CNN vs 2D CNN).
- **PASO 5:** Se hará un estudio de los modelos seleccionados, probándolos con los distintos conjuntos de datos, compresiones y representaciones, hasta dar con el modelo que obtenga los mejores resultados en los problemas de clasificación propuestos.

**- Tecnologías utilizadas:**

- Python
- TensorFlow
- NumPy, Pandas, Matplotlib
