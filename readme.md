# Data Cleaning

Proyecto que automatiza el proceso de obtención, limpieza y preparación de datos, comenzando desde el web scraping de información cruda (archivos HTML) hasta la construcción de un dataset limpio listo para análisis.

## Estructura general del proyecto

```
.
├── data/
│   ├── institutions.csv         # Datos crudos exportados del scrapper
│   └── institutions_clean.csv   # Dataset final limpio
│
├── scripts/
│   ├── scrapper.py              # Script de scraping web
│   └── dataCleaning.ipynb       # Notebook de limpieza y preprocesamiento
│
├── src/
│   ├── AltaVerapaz.html
│   ├── BajaVerapaz.html
│   ├── Chimaltenango.html
│   ├── ...                      # Archivos HTML de cada departamento
│
|
└── README.txt
```

## Requisitos

Instalar las librerías necesarias:

```bash
pip install pandas numpy requests beautifulsoup4 lxml
```

## scrapper.py — Extracción de datos

Script dentro de scripts/ que recorre los archivos HTML ubicados en src/ y extrae campos relevantes para construir un archivo CSV crudo.

Pasos que realiza:
- Lee cada archivo .html dentro de la carpeta src/.
- Analiza el contenido con BeautifulSoup.
- Extrae información (instituciones, campos, ubicaciones, etc.).
- Genera un archivo institutions.csv dentro de la carpeta data/.

Uso:

```bash
python scripts/scrapper.py
```

## dataCleaning.ipynb — Limpieza de datos

Notebook ubicado en scripts/ encargado de limpiar y transformar data/institutions.csv.

Procedimiento de limpieza:
- Cargar el CSV crudo.
- Eliminar columnas innecesarias.
- Estandarizar formatos.
- Tratar valores faltantes.
- Generar nuevas variables útiles para análisis.
- Exportar el resultado final como institutions_clean.csv.

## Cómo ejecutar el flujo completo

1. Ejecutar el scrapper para construir el CSV crudo:
   ```bash
   python scripts/scrapper.py
   ```

2. Abrir el notebook:
   ```bash
   jupyter notebook scripts/dataCleaning.ipynb
   ```

3. Ejecutar todas las celdas y obtener el archivo limpio en:
   ```
   data/institutions_clean.csv
   ```



## **Github** 

https://github.com/DanielRasho/DS-Project1

## **Libro de códigos** 

https://docs.google.com/document/d/1x7qu9egTgv8HQS96KP4HhaGYLymynbP_NrE_sevAIF0/edit?usp=sharing