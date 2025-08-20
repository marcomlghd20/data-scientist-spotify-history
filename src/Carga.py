import pandas as pd

# Ruta absoluta del archivo CSV
CSV_FILE = r"C:\Users\marco\Desktop\repositorio_remoto\data-scientist-spotify-history\data\spotify_history.csv"

def cargar_datos():
    try:
        df = pd.read_csv(CSV_FILE)
        print("✅ Archivo cargado correctamente.")
        return df
    except FileNotFoundError:
        print(f"❌ Archivo no encontrado en: {CSV_FILE}")
        return None