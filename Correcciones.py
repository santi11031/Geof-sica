import math

GravedadTeorica = lambda Latitud: (978.049 * 1000) * (1 + 0.0052884 * math.sin(math.radians(Latitud))**2 + 0.0000059 * math.sin(2 * math.radians(Latitud))**2)

def GravedadObservada(Anomalia, Altura, GT):

    if Altura < 0:
        Gobservada = Anomalia + 0.30856 * Altura + GT
    else:
        Gobservada = Anomalia - 0.30856 * Altura + GT
    return Gobservada

def CorreccionTopografica(Altura, RI=50, RE=100):
    CorreccionTotal = 0

    if Altura > 0:
        for x in range(0, Altura + 1, 150):
            for y in range(RE, 0, -50):
                for z in range(RI, 0, -25):
                    CorreccionT = 2 * (6.67 * 10 ** -6) * math.pi * 2670 * (y - z + (z ** 2 + x ** 2) ** 0.5 - (y ** 2 + x ** 2) ** 0.5)
                    CorreccionTotal += CorreccionT
    else:
        for x in range(0, Altura - 1, -150):
            for y in range(RE, 0, -50):
                for z in range(RI, 0, -25):
                    CorreccionT = 2 * (6.67 * 10 ** -6) * math.pi * 1000 * (y - z + (z ** 2 + x ** 2) ** 0.5 - (y ** 2 + x ** 2) ** 0.5)
                    CorreccionTotal += CorreccionT

    return CorreccionTotal

def CorreccionBouguer(Altura):
    K = 6.67e-6  # 6.67 x 10^-11
    DensidadCorteza = 2670
    DensidadAgua = 1000

    if Altura > 0:
        Correccion = 2 * math.pi * K * Altura * DensidadCorteza * -1
    else:
        Correccion = 2 * math.pi * K * Altura * DensidadAgua * -1

    return Correccion

def CorreccionLatitud(Latitud):
    Correccion = 0.79 * math.sin(math.radians(Latitud))
    return Correccion

def CorreccionMareas(Altura):
    RadioTierra = 6371000
    DistanciaTierraLuna = 384400000
    DistanciaTierraSol = 149597870700
    MasaLuna = 7.349e22
    MasaSol = 1.989e30
    k = 6.67e-6

    CatetoTierraLuna = ((RadioTierra + Altura)**2 + (DistanciaTierraLuna + RadioTierra)**2)**0.5
    ThetaLuna = ((-1 * (CatetoTierraLuna**2)) + (RadioTierra + Altura)**2 + (DistanciaTierraLuna)**2) / (2 * (RadioTierra + Altura) * DistanciaTierraLuna)

    CatetoTierraSol = ((RadioTierra + Altura)**2 + (DistanciaTierraSol + RadioTierra)**2)**0.5
    ThetaSol = ((-1 * (CatetoTierraSol**2)) + (RadioTierra + Altura)**2 + (DistanciaTierraLuna)**2) / (2 * (RadioTierra + Altura) * DistanciaTierraLuna)

    CorreccionFinal = (((3 * k * RadioTierra * MasaLuna) / (2 * DistanciaTierraLuna**3)) * math.cos(ThetaLuna) + 0.3) - (((3 * k * RadioTierra * MasaSol) / (2 * DistanciaTierraSol**3)) * math.cos(ThetaSol) + 0.3)

    return CorreccionFinal

def CorreccionAiry(Altura):
    NivelCompensacion = 50000
    DensidadOceanica=3000
    DensidadManto = 3500
    DensidadCorteza = 2700
    CilindroCompensacion = 10000
    DensidadAgua = 1000
    k=6.67*10e-11

    if Altura > 0:
        Raiz = (Altura * DensidadCorteza) / (DensidadManto - DensidadCorteza)
        a = CilindroCompensacion
        b = Raiz
        c = NivelCompensacion + Raiz + Altura

        Correccion = (2 * math.pi * k * (DensidadManto - DensidadCorteza) * (b + (a**2 + (c - b)**2)**0.5 - (a**2 + c**2)**0.5))*100000
    else:
        AntiRaiz = ((Altura*-1) * (DensidadOceanica - DensidadAgua)) / (DensidadManto - DensidadOceanica)
        a = CilindroCompensacion
        b = AntiRaiz
        c = NivelCompensacion + AntiRaiz + (Altura*-1)  # Corregir Raiz a AntiRaiz

        Correccion = (2 * math.pi * k * (DensidadOceanica - DensidadManto) * (b + (a**2 + (c - b)**2)**0.5 - (a**2 + c**2)**0.5))*100000


    if Altura > 0:
      return Raiz, Correccion

    else:
      return AntiRaiz, Correccion


def CorreccionPratt(Altura):
  DensidadManto=3270
  DensidadCorteza=2670
  DensidadAgua=1000
  NivelCompensacion=50000
  EspesorCorteza=20000
  EspesorManto=30000
  k=6.67*10e-11
  CilindroCompensacion=10000

  if Altura>0:
    Densidad1=(EspesorCorteza*DensidadCorteza+EspesorManto*DensidadManto)/(EspesorCorteza+EspesorManto)
    Densidad2=(EspesorCorteza*DensidadCorteza+DensidadManto*EspesorManto)/(NivelCompensacion+Altura)
    a=CilindroCompensacion
    b=NivelCompensacion
    c=NivelCompensacion+Altura
    CorreccionPratt=(2 * math.pi * k * (Densidad1 - Densidad2) * (b + (a**2 + (c - b)**2)**0.5 - (a**2 + c**2)**0.5))*100000
  else:
    AlturaCompensada=Altura*-1
    #Densidad0=(EspesorCorteza*DensidadCorteza)+((NivelCompensacion-EspesorCorteza)*DensidadManto)
    Densidad1=(EspesorCorteza*DensidadCorteza+EspesorManto*DensidadManto)/(NivelCompensacion+AlturaCompensada)
    Densidad2Agua=(EspesorCorteza*DensidadCorteza+EspesorManto*DensidadManto-AlturaCompensada*DensidadAgua)/(NivelCompensacion-AlturaCompensada)
    a=CilindroCompensacion
    b=NivelCompensacion
    c=NivelCompensacion+Altura
    CorreccionPratt=(2 * math.pi * k * (Densidad2Agua-Densidad1) * (b + (a**2 + (c - b)**2)**0.5 - (a**2 + c**2)**0.5))*100000

  if Altura>0:
    return Densidad1,Densidad2,CorreccionPratt
  else:
    return  Densidad1,Densidad2Agua,CorreccionPratt

def CorreccionAireLibre(Altura):
  if  Altura>0:

     Correccion=-0.30856*Altura
  else:
    Correccion=0.30856*Altura

  return Correccion
