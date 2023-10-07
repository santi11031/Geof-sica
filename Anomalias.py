# Creación de la anomalía de aire libre
AnomaliaAireLibre = []

for x, y, z, a in zip(Topografia['Observada'], Topografia['CorreccionAireLibre'],
                      Topografia['GravedadTeorica(Miligales)'], Topografia['Altura']):
    if a < 0:
        Iterador = x + y - z
        AnomaliaAireLibre.append(Iterador)
    else:
        Iterador = x - y - z
        AnomaliaAireLibre.append(Iterador)

Topografia['AnomaliaAireLibre'] = AnomaliaAireLibre

#Creación de la anomalía de Bouguer Total

AnomaliaBouguerT = []

for x, a, b, c, d, e, z, f in zip(Topografia['Observada'], Topografia['CorreccionAireLibre'],
                                 Topografia['CorreccionBouguer'], Topografia['CorreccionTopografica'],
                                 Topografia['CorreccionLatitud'], Topografia['CorreccionMareas'],
                                 Topografia['GravedadTeorica(Miligales)'], Topografia['Altura']):
    if f < 0:
        Iterador = x + a + b + c + d + e - z
        AnomaliaBouguerT.append(Iterador)
    else:
        Iterador = x - a - b + c + d + e - z
        AnomaliaBouguerT.append(Iterador)

#Creación de la anomalía de Airy total
AnomaliaAiryT = []

for x, a, b, c, d, e, z, f, h in zip(Topografia['Observada'], Topografia['CorreccionAireLibre'],
                                    Topografia['CorreccionBouguer'], Topografia['CorreccionTopografica'],
                                    Topografia['CorreccionLatitud'], Topografia['CorreccionMareas'],
                                    Topografia['GravedadTeorica(Miligales)'], Topografia['Altura'],
                                    Topografia['CorreccionAiry']):
    if f < 0:
        Iterador = x + a + b + c + d + e + h - z
        AnomaliaAiryT.append(Iterador)
    else:
        Iterador = x - a - b + c + d + e + h - z
        AnomaliaAiryT.append(Iterador)

Topografia['AnomaliaAiry'] = AnomaliaAiryT

#Creación de la anomalia de Pratt Total

AnomaliaPrattT = []

for x, a, b, c, d, e, z, f, h in zip(Topografia['Observada'], Topografia['CorreccionAireLibre'],
                                     Topografia['CorreccionBouguer'], Topografia['CorreccionTopografica'],
                                     Topografia['CorreccionLatitud'], Topografia['CorreccionMareas'],
                                     Topografia['GravedadTeorica(Miligales)'], Topografia['Altura'],
                                     Topografia['CorreccionPratt']):
    if f < 0:
        Iterador = x + a + b + c + d + e + h - z
        AnomaliaPrattT.append(Iterador)
    else:
        Iterador = x - a - b + c + d + e + h - z
        AnomaliaPrattT.append(Iterador)

Topografia['AnomaliaPratt'] = AnomaliaPrattT
