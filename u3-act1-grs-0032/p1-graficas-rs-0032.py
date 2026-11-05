import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de redes sociales con 4 elementos pór lista
fb = ['Facebook', 8833, True, 2006]
twt = ['Twitter', 8575, False, 2008]
ig = ['Instagram', 7575, True, 2010]
wsp = ['Whatsapp', 8828, True, 2009]
tel = ['Telegram', 2992, False, 2010]
lkn = ['Linkdin', 7277, False, 2012]
# Creamos una lista de listas (conformando la tabla)
lista_redes_sociales=[fb ,twt,ig ,wsp,tel,lkn]
#print(lista_redes_sociales)
# Utilizar panda para organizar la tabla (dataframe o marco de datos)
df_redes_sociales=pd.DataFrame(lista_redes_sociales,columns=["Nombre", "Cantidad", "Es_FB", "Año"])
print(df_redes_sociales)
# creamos el archivo CSV y lo guardamos en CSV
df_redes_sociales.to_csv("redessociales.csv", index=False)
# crear grafica de lineas
# donde x es nombre en el eje central
# donde y es nombre en el eje vertical
plt.plot(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.title("Grafica redes sociales 0032")
plt.xlabel("Nombre de las redes sociales")
plt.ylabel("Cantidad de ussuarios")
plt.show()
# creamos una grafica de puntos
plt.scatter(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.show()
# grafica de barras
plt.bar(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
# Etiquetas y titulo
plt.title("Redes Sociales 0032")
plt.xlabel("Nombre de las redes")
plt.ylabel("Cantidad de usuarios")
# Mostrar la grafica
plt.show()
# ordenar grafica de barras de manera decendente
# de la mas grande a la mas pequeña
df_rs_ordenar=df_redes_sociales.sort_values("Cantidad", ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"])
plt.show()
# coloreando la grafica
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"],
        color=["b", "g", "c", "m", "y", "r"])
plt.show()
# grafica de pastel
# plt.plot(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.pie(df_redes_sociales["Cantidad"],labels=df_redes_sociales["Nombre"])
plt.show()