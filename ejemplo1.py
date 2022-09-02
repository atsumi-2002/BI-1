import pandas as pd
import statistics as stats

archivo = pd.read_csv('Panamericanos_Lima.csv')
print(archivo)
def suma_oro():
    print("El total de medallas de oro entregadas es: "+ str(archivo.Oro.sum()))

def conteo_paises():
    print(str(len(archivo.Oro))+" paises participaron en las olimpiadas")

def media_oro():
    print("El total de medallas de oro entregadas es: "+str(archivo.Oro.mean()))

def mediaRedond_oro(redo):
    media = archivo.Oro.mean()
    print("El total de medallas de oro entregadas es: "+str(round(media,redo)))

def mediana_oro():
    print(stats.median(archivo.Oro))

def moda_oro():
    print("El numero de medallas de oro ganadas por la mayoria de paises ganaron fueron entre: "+str(archivo.Oro.mode()))

def percentil_oro():
    print("Los percentiles de medallas de oro son: "+str(stats.quantiles(archivo.Oro,n=100)))

def varianza_oro():
    print("La varianza de medallas de oro es: " + str(stats.variance(archivo.Oro)))
suma_oro()
conteo_paises()
media_oro()
mediaRedond_oro(2)
mediana_oro()
moda_oro()
percentil_oro()
varianza_oro()