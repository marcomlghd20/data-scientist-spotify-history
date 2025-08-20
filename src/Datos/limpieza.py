
def limpieza_basica(df):
    if df is None:
        return None

    print("\n🔍 Información general:")
    print(df.info())

    print("\n📌 Valores nulos por columna:")
    print(df.isnull().sum())

    print("\n🧹 Eliminando duplicados...")
    df = df.drop_duplicates()

    print("\n📏 Filtrando canciones con menos de 1000 ms reproducidos...")
    df = df[df['ms_played'] > 1000]

    print("\n✅ Datos limpios. Primeras 5 filas:")
    print(df.head())

    return df


