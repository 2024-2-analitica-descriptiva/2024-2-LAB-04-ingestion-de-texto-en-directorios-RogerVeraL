# pylint: disable=import-outside-toplevel
# pylint: disable=linea-too-long
# flake8: noqa
"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""
import zipfile
import pandas as pd
import os

def pregunta_01():
    """
    La información requerida para este laboratio esta almacenada en el
    archivo "files/input.zip" ubicado en la carpeta raíz.
    Descomprima este archivo.

    Como resultado se creara la carpeta "input" en la raiz del
    repositorio, la cual contiene la siguiente estructura de archivos:


    ```
    train/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    test/
        negative/
            0000.txt
            0001.txt
            ...
        positive/
            0000.txt
            0001.txt
            ...
        neutral/
            0000.txt
            0001.txt
            ...
    ```

    A partir de esta informacion escriba el código que permita generar
    dos archivos llamados "train_dataset.csv" y "test_dataset.csv". Estos
    archivos deben estar ubicados en la carpeta "output" ubicada en la raiz
    del repositorio.

    Estos archivos deben tener la siguiente estructura:

    * phrase: Texto de la phrase. hay una phrase por cada archivo de texto.
    * sentiment: Sentimiento de la phrase. Puede ser "positive", "negative"
      o "neutral". Este corresponde al nombre del directorio donde se
      encuentra ubicado el archivo.

    Cada archivo tendria una estructura similar a la siguiente:

    ```
    |    | phrase                                                                                                                                                                 | target   |
    |---:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|
    |  0 | Cardona slowed her vehicle , turned around and returned to the intersection , where she called 911                                                                     | neutral  |
    |  1 | Market data and analytics are derived from primary and secondary research                                                                                              | neutral  |
    |  2 | Exel is headquartered in Mantyharju in Finland                                                                                                                         | neutral  |
    |  3 | Both operating profit and net sales for the three-month period increased , respectively from EUR16 .0 m and EUR139m , as compared to the corresponding quarter in 2006 | positive |
    |  4 | Tampere Science Parks is a Finnish company that owns , leases and builds office properties and it specialises in facilities for technology-oriented businesses         | neutral  |
    ```


    """
    def descomprimir_archivo(ruta_zip, carpeta_salida):
        if not ruta_zip.endswith('.zip'):
            raise ValueError("El archivo proporcionado no es un ZIP.")
        
        if not os.path.exists(carpeta_salida):
            os.makedirs(carpeta_salida)
        
        with zipfile.ZipFile(ruta_zip, 'r') as archivo_zip:
            archivo_zip.extractall(carpeta_salida)
        print(f"Archivos extraídos en: {carpeta_salida}")

    def leer_archivos_txt(carpeta):
        etiqueta_sentimiento = os.path.basename(os.path.normpath(carpeta))
        datos = []

        for archivo in os.listdir(carpeta):
            if archivo.endswith('.txt'):
                ruta_archivo = os.path.join(carpeta, archivo)
                with open(ruta_archivo, 'r', encoding='utf-8') as archivo_txt:
                    for linea in archivo_txt:
                        datos.append({'phrase': linea.strip(), 'target': etiqueta_sentimiento})

        return pd.DataFrame(datos)

    def procesar_y_guardar_datos(directorio_entrada, ruta_csv_salida):
        datos_combinados = []

        for subcarpeta in os.listdir(directorio_entrada):
            ruta_subcarpeta = os.path.join(directorio_entrada, subcarpeta)
            if os.path.isdir(ruta_subcarpeta):
                df = leer_archivos_txt(ruta_subcarpeta)
                datos_combinados.append(df)

        df_final = pd.concat(datos_combinados, ignore_index=True)

        carpeta_salida = os.path.dirname(ruta_csv_salida)
        if not os.path.exists(carpeta_salida):
            os.makedirs(carpeta_salida)
        
        df_final.to_csv(ruta_csv_salida, index=False, encoding='utf-8')
        print(f"Archivo guardado en: {ruta_csv_salida}")

    ### Inicio del código ###

    archivo_zip = './files/input.zip'
    carpeta_extraida = './files'
    carpeta_salida = './files/output'

    descomprimir_archivo(archivo_zip, carpeta_extraida)
    for i in os.listdir('./files/input'):
        procesar_y_guardar_datos(os.path.join(carpeta_extraida+'/input/', i), os.path.join(carpeta_salida, i+'_dataset.csv'))

pregunta_01()



