# Nombre del archivo: modelo_transmilenio.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
import joblib # Para guardar el modelo entrenado (opcional)

# --- 1. Carga de Datos ---
try:
    df = pd.read_csv('transmilenio_synthetic_data.csv')
    print("Dataset cargado exitosamente.")
except FileNotFoundError:
    print("Error: El archivo 'transmilenio_synthetic_data.csv' no fue encontrado.")
    print("Por favor, ejecuta primero el script 'generar_dataset.py'.")
    exit() # Salir si no se encuentra el archivo

print("\nPrimeras filas del dataset:")
print(df.head())

print("\nInformación del dataset:")
df.info()

# --- 2. Preprocesamiento de Datos ---

# Separar características (X) y variable objetivo (y)
# Excluimos id_viaje porque no es una característica predictiva
features = ['hora_pico', 'dia_semana', 'troncal', 'evento_especial', 'condicion_clima']
target = 'retraso_significativo'

X = df[features]
y = df[target]

# Codificación de variables categóricas
# Usaremos One-Hot Encoding para las categóricas nominales
X = pd.get_dummies(X, columns=['dia_semana', 'troncal', 'condicion_clima'], drop_first=True)

print("\nDataset después de One-Hot Encoding (primeras filas):")
print(X.head())
print("\nColumnas después del preprocesamiento:")
print(X.columns)

# --- 3. División en Conjuntos de Entrenamiento y Prueba ---
# Divide los datos: 80% para entrenamiento, 20% para prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y) # stratify para mantener proporción de clases

print(f"\nTamaño del conjunto de entrenamiento: {X_train.shape[0]} muestras")
print(f"Tamaño del conjunto de prueba: {X_test.shape[0]} muestras")

# --- 4. Selección y Entrenamiento del Modelo ---
# Usaremos un clasificador Random Forest
print("\nEntrenando el modelo RandomForestClassifier...")
# n_estimators: número de árboles en el bosque
# random_state: para reproducibilidad
# class_weight='balanced': útil si las clases están desbalanceadas
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced', n_jobs=-1) # n_jobs=-1 usa todos los procesadores

model.fit(X_train, y_train)
print("Modelo entrenado.")

# --- 5. Predicción en el Conjunto de Prueba ---
print("\nRealizando predicciones en el conjunto de prueba...")
y_pred = model.predict(X_test)

# --- 6. Evaluación del Modelo ---
print("\n--- Evaluación del Modelo ---")

# Accuracy (Exactitud)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy (Exactitud): {accuracy:.4f}")

# Matriz de Confusión
print("\nMatriz de Confusión:")
# Muestra: Verdaderos Negativos (TN), Falsos Positivos (FP)
#          Falsos Negativos (FN), Verdaderos Positivos (TP)
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Reporte de Clasificación
print("\nReporte de Clasificación:")
# Incluye Precision, Recall, F1-score por clase
# Precision: De todos los que predije como positivos, cuántos realmente lo eran? TP / (TP + FP)
# Recall (Sensibilidad): De todos los que eran realmente positivos, cuántos identifiqué? TP / (TP + FN)
# F1-score: Media armónica de Precision y Recall
print(classification_report(y_test, y_pred))

# --- 7. Importancia de Características (Opcional pero útil) ---
print("\nImportancia de las características (según Random Forest):")
feature_importances = pd.DataFrame(model.feature_importances_,
                                   index = X_train.columns,
                                   columns=['importance']).sort_values('importance', ascending=False)
print(feature_importances)

# --- 8. Guardar el modelo entrenado (Opcional) ---
# Guarda el modelo para poder usarlo después sin re-entrenar
# model_filename = 'modelo_retraso_transmilenio.joblib'
# joblib.dump(model, model_filename)
# print(f"\nModelo guardado como '{model_filename}'")

# Para cargarlo después: loaded_model = joblib.load(model_filename)