# SmartBuild Streamlit

Aplicación de ejemplo para demostrar un flujo DevSecOps con Streamlit y pruebas automatizadas.

## Requisitos

- Python 3.11+
- pip

Instala dependencias:

```bash
pip install -r requirements.txt
```

## Ejecutar la app

```bash
streamlit run app/main.py
```

La aplicación despliega un panel con dos funcionalidades:
- Registrar reservas.
- Estimar tiempo de preparación de pedidos.

## Pruebas y cobertura

Genera pruebas y reporte de cobertura para SonarCloud:

```bash
pytest --cov=app --cov-report=xml
```

Esto crea `coverage.xml` en la raíz del proyecto.
