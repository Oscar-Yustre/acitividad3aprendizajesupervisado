# Nombre del archivo: generar_dataset.py
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Parámetros para la generación
num_registros = 5000
fecha_inicio = datetime(2024, 1, 1)
dias_a_simular = 365 # Simular un año

# Listas de categorías
dias_semana_lista = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
troncales_lista = ['Caracas', 'NQS', 'Autonorte', 'Suba', 'Calle 80', 'Americas', 'Calle 26', 'Eldorado']
clima_lista = ['Soleado', 'Nublado', 'Lluvia']

data = []

# Generar datos
current_date = fecha_inicio
for i in range(num_registros):
    # Simular fecha y hora
    # Aseguramos una distribución más o menos uniforme a lo largo del año y las horas
    simulated_datetime = fecha_inicio + timedelta(days=random.randint(0, dias_a_simular - 1),
                                                  hours=random.randint(5, 22), # Horario de operación aproximado
                                                  minutes=random.randint(0, 59))

    hora = simulated_datetime.hour
    dia_semana = dias_semana_lista[simulated_datetime.weekday()]

    # Definir hora pico (6-9 AM, 4-7 PM)
    es_hora_pico = 1 if (6 <= hora < 9) or (16 <= hora < 19) else 0

    # Seleccionar troncal y clima aleatoriamente
    troncal = random.choice(troncales_lista)
    clima = random.choice(clima_lista)

    # Simular evento especial (baja probabilidad)
    evento_especial = 1 if random.random() < 0.05 else 0 # 5% de probabilidad

    # --- Lógica para generar el retraso (variable objetivo) ---
    # Esta es la parte clave donde simulamos la dependencia
    prob_retraso = 0.1 # Probabilidad base de retraso

    if es_hora_pico == 1:
        prob_retraso += 0.25 # Más probable en hora pico
    if dia_semana in ['Viernes']:
        prob_retraso += 0.1 # Viernes suele ser más congestionado
    if dia_semana in ['Sábado', 'Domingo']:
        prob_retraso -= 0.05 # Menos probable fines de semana (ajustar si es necesario)
    if troncal in ['Caracas', 'NQS']:
        prob_retraso += 0.15 # Troncales más congestionadas
    if clima == 'Lluvia':
        prob_retraso += 0.20 # Lluvia aumenta probabilidad
    if evento_especial == 1:
        prob_retraso += 0.30 # Evento especial aumenta mucho la probabilidad

    # Asegurar que la probabilidad esté entre 0 y 1
    prob_retraso = max(0, min(1, prob_retraso))

    # Generar el resultado basado en la probabilidad
    retraso_significativo = 1 if random.random() < prob_retraso else 0

    data.append({
        'id_viaje': i + 1,
        'hora_pico': es_hora_pico,
        'dia_semana': dia_semana,
        'troncal': troncal,
        'evento_especial': evento_especial,
        'condicion_clima': clima,
        'retraso_significativo': retraso_significativo
    })

# Crear DataFrame y guardar en CSV
df = pd.DataFrame(data)
df.to_csv('transmilenio_synthetic_data.csv', index=False)

print(f"Dataset 'transmilenio_synthetic_data.csv' generado con {len(df)} registros.")
print(df.head())
print("\nDistribución de la variable objetivo (retraso_significativo):")
print(df['retraso_significativo'].value_counts(normalize=True))