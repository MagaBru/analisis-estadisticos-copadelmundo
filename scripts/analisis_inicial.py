import pandas as pd
ruta='datos/copas_del_mundo.csv'
datos= pd.read_csv(ruta, sep= '\t')
print (datos.head())