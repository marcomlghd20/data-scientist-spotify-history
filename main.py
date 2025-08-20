from src.Carga import cargar_datos
from src.Datos.limpieza import limpieza_basica
from src.preprocesamiento.analisis import (
    crear_carpeta_reportes,
    top_artistas,
    top_canciones,
    canciones_saltadas,
    generar_reporte_excel
)

if __name__ == "__main__":
    # 1️⃣ Cargar y limpiar datos
    df = cargar_datos()
    df_limpio = limpieza_basica(df)

    if df_limpio is not None:
        # 2️⃣ Crear carpeta de reportes
        carpeta = crear_carpeta_reportes()

        # 3️⃣ Generar análisis y gráficos
        top_artistas(df_limpio, carpeta)
        top_canciones(df_limpio, carpeta)
        canciones_saltadas(df_limpio, carpeta)

        # 4️⃣ Preparar datos para Excel
        conteo_artistas = df_limpio['artist_name'].value_counts().head(5)

        # 5️⃣ Generar Excel con datos y gráficos
        generar_reporte_excel(
            df_limpio=df_limpio,
            conteo=conteo_artistas,
            ruta=f"{carpeta}/reporte_spotify.xlsx",
            imagen=f"{carpeta}/top_artistas.png"
        )

        print("\n✅ Todo el análisis y el reporte Excel han sido generados.")
