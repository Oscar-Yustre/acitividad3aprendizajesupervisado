# acitividad3aprendizajesupervisado
Actividad 3  metedos de aprendizajes supervisado

##oscar david yustre trujillo

##materia inteligencia artificial Actividad 3
# Descripción del Dataset Sintético: transmilenio_synthetic_data.csv

Este dataset fue generado sintéticamente para simular registros de viajes en el sistema TransMilenio de Bogotá, con el objetivo de entrenar un modelo de aprendizaje automático para predecir retrasos significativos.

**Fecha de Generación:** 2025-04-09 (o la fecha real de ejecución)
**Número de Registros:** 5000 (configurable en el script `generar_dataset.py`)

## Columnas del Dataset

1.  **id_viaje**:
    * **Tipo:** Entero (Integer)
    * **Descripción:** Identificador numérico único asignado a cada registro de viaje simulado. No se utiliza como característica predictiva.

2.  **hora_pico**:
    * **Tipo:** Numérico (Binario: 0 o 1)
    * **Descripción:** Indica si el viaje ocurrió durante una hora pico.
    * **Valores:**
        * `1`: Sí (viaje entre 6:00-8:59 AM o 4:00-6:59 PM)
        * `0`: No (fuera de esos rangos horarios)

3.  **dia_semana**:
    * **Tipo:** Categórico (Texto/String)
    * **Descripción:** El día de la semana en que ocurrió el viaje.
    * **Valores Posibles:** `Lunes`, `Martes`, `Miércoles`, `Jueves`, `Viernes`, `Sábado`, `Domingo`.

4.  **troncal**:
    * **Tipo:** Categórico (Texto/String)
    * **Descripción:** La troncal principal asociada al viaje simulado.
    * **Valores Posibles:** `Caracas`, `NQS`, `Autonorte`, `Suba`, `Calle 80`, `Americas`, `Calle 26`, `Eldorado`.

5.  **evento_especial**:
    * **Tipo:** Numérico (Binario: 0 o 1)
    * **Descripción:** Indica si había algún evento especial reportado en la ciudad (manifestación, concierto, partido, etc.) que podría afectar el tráfico. La ocurrencia se simuló con baja probabilidad.
    * **Valores:**
        * `1`: Sí (evento especial reportado)
        * `0`: No (día normal)

6.  **condicion_clima**:
    * **Tipo:** Categórico (Texto/String)
    * **Descripción:** Condición climática general simulada durante el viaje.
    * **Valores Posibles:** `Soleado`, `Nublado`, `Lluvia`.

7.  **retraso_significativo** (**Variable Objetivo / Target**):
    * **Tipo:** Numérico (Binario: 0 o 1)
    * **Descripción:** Indica si el viaje simulado experimentó un retraso considerado significativo (ej. > 15 minutos). Este es el valor que el modelo de aprendizaje automático intenta predecir.
    * **Valores:**
        * `1`: Sí (hubo retraso significativo)
        * `0`: No (no hubo retraso significativo)
    * **Generación:** La probabilidad de que este valor sea `1` se calculó en base a las otras características (mayor probabilidad en hora pico, lluvia, eventos especiales, ciertas troncales, etc.) para simular dependencias realistas.

## Notas Adicionales

* Este dataset es una **simplificación** de la realidad. Un sistema real involucraría muchas más variables (ocupación del bus, incidentes específicos en estaciones, estado exacto del tráfico, etc.).
* La relación entre las características y el retraso fue **definida artificialmente** en el script `generar_dataset.py` para asegurar que el modelo tuviera patrones que aprender.
