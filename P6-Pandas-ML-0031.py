import pandas as pd
import numpy as np
# --- Arevalo Rafael NC:0031 ---

Serie_Amigos=["Pedro", "Morgan", "Farfan","El Adrian", "Jesse", "Eliseo", "Mario"]
print(" --- Serie listado de amigos NC:0031 ---")
Amigos=pd.Series(Serie_Amigos)
print(Amigos)

Serie_Billetes=[20,50,100,200,500,1000]
print(" --- Serie listado valor de billetes MX NC:0031 ---")
Billetes=pd.Series(Serie_Billetes)
print(Billetes)

Serie_Billetes=[20,50,100,200,500,1000]
Serie_Letras=["Veinte","Cincuenta","Cien","Docientos","Quinientos","Mil"]
print(" --- Serie listado nombre y valor de billetes MX NC:0031 ---")
TablaBilletes=pd.Series(Serie_Billetes,Serie_Letras)
print(TablaBilletes)
# Diccionario DataFrame
# diccionario de valor monedas y nombre
print("Datos de diccionario a DataFrame en Pandas")
Dic_Monedas={
    "Serie_Billetes":[20,50,100,200,500,1000],
    "Serie_Letras" :["Veinte","Cincuenta","Cien","Docientos","Quinientos","Mil"]
}

TablaBilletes=pd.DataFrame(Dic_Monedas,index=["A","B","C","D","E","F"])
print(TablaBilletes)

print("Casa de cambio de Arevalo Rafael NC:0031")