# Proyecto de Machine Learning con Python y Flask

Este proyecto es parte de mi viaje de aprendizaje en el campo del Machine Learning y Python. El objetivo principal es construir un modelo de Machine Learning y desplegarlo como una API web usando Flask.

## Descripción

El proyecto consiste en un modelo de clasificación (o regresión, puedes ajustarlo) que se entrena con datos de ejemplo y luego se expone a través de una API RESTful. Esto permite que otras aplicaciones consuman las predicciones del modelo a través de solicitudes HTTP.

## Estructura del Proyecto

El repositorio está organizado de la siguiente manera:

```
/
├── __init__.py        # Inicializador del paquete Python.
├── .gitignore         # Archivos y directorios ignorados por Git.
├── main.py            # Script principal para entrenar y evaluar el modelo.
├── models.py          # Definición de la arquitectura del modelo de Machine Learning.
├── server.py          # Implementación del servidor web con Flask para servir el modelo.
├── utils.py           # Funciones de utilidad (ej. carga de datos, preprocesamiento).
├── in/
│   └── data.csv       # Datos de entrada para el entrenamiento del modelo.
├── models/
│   └── best_model.pkl # Modelo entrenado y guardado.
└── out/
    └──                # Directorio para guardar resultados o salidas.
```

### Descripción de Archivos Clave

*   **`main.py`**: Contiene el flujo principal del proyecto. Carga los datos, entrena el modelo utilizando las definiciones de `models.py` y guarda el artefacto del modelo entrenado en la carpeta `models/`.
*   **`models.py`**: Define la clase o funciones para el modelo de Machine Learning. Aquí es donde se encapsula la lógica del algoritmo.
*   **`server.py`**: Utiliza Flask para cargar el modelo serializado (`best_model.pkl`) y exponer un endpoint (por ejemplo, `/predict`) que recibe datos y devuelve predicciones.
*   **`utils.py`**: Mantiene el código organizado al separar funciones auxiliares que se usan en varias partes del proyecto.

## Cómo Empezar

### Prerrequisitos

*   Python 3.x
*   pip

### Instalación

1.  Clona este repositorio:
    ```bash
    git clone <URL-DEL-REPOSITORIO>
    cd <NOMBRE-DEL-DIRECTORIO>
    ```

2.  Crea un entorno virtual e instala las dependencias:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```
    *(Nota: Necesitarás crear un archivo `requirements.txt` con las librerías que usas, como pandas, scikit-learn, flask, etc.)*

### Uso

1.  **Entrenar el modelo**:
    ```bash
    python main.py
    ```
    Esto ejecutará el script de entrenamiento y guardará el `best_model.pkl` en la carpeta `models/`.

2.  **Iniciar el servidor**:
    ```bash
    python server.py
    ```
    Esto iniciará un servidor de desarrollo de Flask en `http://127.0.0.1:5000`.

3.  **Realizar predicciones**:
    Puedes enviar una solicitud POST al endpoint `/predict` con los datos necesarios en formato JSON.
    ```bash
    curl -X POST -H "Content-Type: application/json" -d \'\'\'{"features": [1, 2, 3]}\'\'\' http://127.0.0.1:5000/predict
    ```

## Aprendizajes Clave

*   **Fundamentos de Python**: Estructura de proyectos, módulos, y entornos virtuales.
*   **Manipulación de Datos**: Uso de librerías como Pandas y NumPy para la carga, limpieza y preprocesamiento de datos.
*   **Machine Learning**: Implementación y entrenamiento de modelos de clasificación/regresión con Scikit-learn.
*   **Serialización de Modelos**: Guardar y cargar modelos entrenados para su uso en producción.
*   **Desarrollo de APIs**: Creación de una API RESTful con Flask para servir el modelo de Machine Learning.
*   **Control de Versiones**: Uso de Git y GitHub para gestionar el código fuente del proyecto.

---

¡Gracias por revisar mi proyecto!