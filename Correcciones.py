Ejemplo=[]
for x,y,z in zip(Topografia['Gravedad'], Topografia['Altura'], Topografia['GravedadTeorica(Miligales)']):
  Iterador=GravedadObservada(x,y,z)
  Ejemplo.append(Iterador)

CorrecionB=[]
for i in  Topografia['Altura']:
  Iterador=CorreccionBouguer(i)
  CorrecionB.append(Iterador)


print(CorreccionTopografica(5400,100,500))
print(CorreccionBouguer(-1900))
Anomalia=-87.7
Altura=200
GravedadTeorica=978171.966

print(GravedadObservada(Anomalia,Altura,GravedadTeorica)

#Corrección por latitud

CorreccionL=[]

for i in Topografia['y']:
  Iterador=CorreccionLatitud(i)
  CorreccionL.append(Iterador)


Topografia['CorreccionLatitud']=CorreccionL

#Correccion por mareas

CorreccionM=[]

for i in Topografia['Altura']:
  Iterador=CorreccionMareas(i)
  CorreccionM.append(Iterador)


Topografia['CorreccionMareas']=CorreccionM

#CorreccionAiry

resultados = []


for altura in Topografia['Altura']:

     correccion,j = CorreccionAiry(altura)
     resultados.append((correccion,j))



Raiz_AntiRaiz=[]
CorreccionAiry=[]

for x,y in resultados:
  Raiz_AntiRaiz.append(x)
  CorreccionAiry.append(y)

Topografia['Raiz_Antiraiz']=Raiz_AntiRaiz
Topografia['CorreccionAiry']=CorreccionAiry

#CORRECCION PRATT

resultados1 = []

# Iterar a través de las alturas en tu dataset Topografia
for altura in Topografia['Altura']:
    # Llamar a la función CorreccionAiry con la altura actual
     Densidad1,Densidad2,Correccion = CorreccionPratt(altura)
     resultados1.append((Densidad1,Densidad2,Correccion))

Densidad1=[]
Densidad2=[]
CorreccionPratt=[]

for x,y,z in resultados1:
  Densidad1.append(x)
  Densidad2.append(y)
  CorreccionPratt.append(z)

Topografia['Densidad1']=Densidad1
Topografia['Densidad2']=Densidad2
Topografia['CorreccionPratt']=CorreccionPratt

#Correccion Aire libre

CorreccionAireL=[]

for x in Topografia['Altura']:
  Iterador=CorreccionAireLibre(x)
  CorreccionAireL.append(Iterador)

Topografia['CorreccionAireLibre']=CorreccionAireL

#Correccion Topografica

CorreccionTopograficaA=[]

for x in Topografia['Altura']:
    Iterador=CorreccionTopografica(x)
    CorreccionTopograficaA.append(Iterador)


Topografia['CorreccionTopografica']=CorreccionTopograficaA
