import Normal as normalDistribution
import Weibull as weibullDistribution
import Exponential as exponDistribution
import Uniform as uniformDistribution
import Erlang as erlangDistribution
import Triangular as triangularDistribution
import ChiSquare as chiDistribution
import Binomial as binomialDistribution
import Poisson as poissonDistribution


import scipy.stats as st
import numpy as np
import math
import os


def returnToMenu():
    print("\n:::::::::::::::::::::::::::::")
    print("1) Regresar al menú principal")
    print("2) Salir")
    option = int(input("\n------>Opcion :"))

    if option == 1:
        return True

    return False

#MENU PRINCIPAL DEL PROGRAMA

backToMenu = True
optionSelected = 0
while backToMenu:
    os.system ("cls")
    print("\n\t::::Simulación de variables aleatorias según una distribución propuesta::::")
    print("\n--Opciones de Distribuciones--")
    print("\n1) Distribución Normal.")
    print("2) Distribución Weibull.")
    print("3) Distribución Exponecial.")
    print("4) Distribución Erlang.")
    print("5) Distribución Uniforme Continua.")
    print("6) Distribución Triangular.")
    print("7) Distribución Chi cuadrado.")
    print("8) Distribución Binomial.")
    print("9) Distribución Poisson.")

    print("\n0) Salir.")

    optionSelected = int(input("\n------>Opcion :"))

    # DISTRIBUCION NORMAL
    if optionSelected == 1 :

        os.system("cls")
        nombreDistribucion = "Distribución Normal"

        print("\t::",nombreDistribucion,"::")

        #Parametros necesarios para la generació1n
        media = float(input("\n->Ingrese la media :"))
        desviacion = float(input("->Ingrese la desviación estandar :"))
        numeroDatos = int(input("->Ingrese el número de variables aleatorias a generar :"))
        #nivelDeSignificacia = float(input("->Ingrese el nivel de significancia para la prueba chi cuadrado :"))
        nivelDeSignificacia = 0.05

        tipoDistribucion = st.norm(media, desviacion)
        objNormal = normalDistribution.Normal(numeroDatos, tipoDistribucion, nivelDeSignificacia, nombreDistribucion,
                                              media, desviacion)

        legendHistogram = r'$\mu$' + "=" + str(
            "{0:.2f}".format(objNormal.meanGenerated)) + " ; " + r'$\sigma$' + "=" + str(
            "{0:.2f}".format(objNormal.stdDesvGenerated))
        legendDensity = r'$\mu$' + "=" + str(media) + " ; " + r'$\sigma$' + "=" + str(desviacion)
        axisX = np.linspace((objNormal.mean - 3 * objNormal.stdDesvGenerated),
                            (objNormal.mean + 3 * objNormal.stdDesvGenerated), 100)


        objNormal.chiSquareTest()
        objNormal.graph(legendHistogram, legendDensity, axisX)

    # DISTRIBUCION WEIBULL
    elif optionSelected ==2:

        os.system("cls")
        nombreDistribucion = "Distribución Weibull"

        print("\t::", nombreDistribucion, "::")

        # Parametros necesarios para la generación
        forma = float(input("\n->Ingrese párametro de forma:"))
        escala= float(input("->Ingrese párametro de escala :"))
        localizacion = float(input("->Ingrese párametro de localización :"))
        numeroDatos = int(input("->Ingrese el número de variables aleatorias a generar :"))
        #nivelDeSignificacia = float(input("->Ingrese el nivel de significancia para la prueba chi cuadrado :"))
        nivelDeSignificacia = 0.05

        tipoDistribucion = st.weibull_min(forma, localizacion, escala)

        objWeibull = weibullDistribution.Weibull(numeroDatos, tipoDistribucion, nivelDeSignificacia, nombreDistribucion,
                                                 forma, escala, localizacion)

        legendHistogram = r'Forma' + "=" + str(
            "{0:.2f}".format(objWeibull.formGenerated)) + " ; " + r'Escala' + "=" + str(
            "{0:.2f}".format(objWeibull.scaleGenerated)) + \
                          " ; " + r'Localización' + "=" + str("{0:.2f}".format(objWeibull.locationGenerated))

        axisX = np.linspace(localizacion, objWeibull.mean + objWeibull.des * 6, 100)
        legendDensity = r'Forma' + "=" + str(objWeibull.form) + " ; " + r'Escala' + "=" + str(
            objWeibull.scale) + " ; " + r'Localizacion' + "=" + str(objWeibull.location)

        objWeibull.chiSquareTest()
        objWeibull.graph(legendHistogram, legendDensity, axisX)

    # DISTRIBUCION EXPONENCIAL
    elif optionSelected == 3:

        os.system("cls")
        nombreDistribucion = "Distribución Exponencial"
        print("\t::", nombreDistribucion, "::")

        # Parametros necesarios para la generació1n
        media = float(input("->Ingrese la media :"))
        numeroDatos = int(input("->Ingrese el número de variables aleatorias a generar :"))
        #nivelDeSignificacia = float(input("->Ingrese el nivel de significancia para la prueba chi cuadrado :"))
        nivelDeSignificacia = 0.05

        tipoDistribucion = st.expon(1, media)

        objExpon = exponDistribution.Exponential(numeroDatos, tipoDistribucion, nivelDeSignificacia, nombreDistribucion,
                                                 media)

        legendHistogram =  r'$\mu$' + "="+ str("{0:.2f}".format(objExpon.meanGenerated))
        legendDensity = r'$\mu$' + "=" + str(objExpon.mean)

        axisX = np.linspace(1, objExpon.mean + 6 * objExpon.des, 100)

        objExpon.chiSquareTest()
        objExpon.graph(legendHistogram, legendDensity, axisX)


    # DISTRIBUCION ERLANG
    elif optionSelected == 4:
        os.system("cls")

        nombreDistribucion = "Distribución Erlang"
        print("\t::", nombreDistribucion, "::")

        # Parametros necesarios para la generación
        forma = float(input("->Ingrese la forma :"))
        valorEsperado = float(input("->Ingrese el valor esperado :"))

        numeroDatos = int(input("->Ingrese el número de variables aleatorias a generar :"))
        #nivelDeSignificacia = float(input("->Ingrese el nivel de significancia para la prueba chi cuadrado :"))
        nivelDeSignificacia = 0.05

        tipoDistribucion = st.erlang(forma, 0, valorEsperado)
        nombreDistribucion = "Distribución Erlang"
        objErlang = erlangDistribution.Erlang(numeroDatos, tipoDistribucion, nivelDeSignificacia, nombreDistribucion,
                                              forma, valorEsperado)

        legendHistogram = r'$\kappa$' + "=" + str("{0:.2f}".format(objErlang.formGenerated)) + " ; " + r'$\theta$' + "=" + str("{0:.2f}".format(objErlang.expectedValueGenerated))
        legendDensity = r'$\kappa$' + "=" + str(forma) + " ; " + r'$\theta$' + "=" + str(valorEsperado)
        axisX = np.linspace(0, objErlang.median + 6 * objErlang.iqr, numeroDatos)
        os.system('cls')

        objErlang.chiSquareTest()
        objErlang.graph(legendHistogram, legendDensity, axisX)


    # DISTRIBUCION UNIFORME CONTINUA
    elif optionSelected == 5:

        os.system("cls")

        nombreDistribucion = "Distribución Uniforme Continua"
        print("\t::", nombreDistribucion, "::")

        # Parametros necesarios para la generación
        limiteInferior = float(input("->Ingrese el límite inferior :"))
        limiteSuperior = float(input("->Ingrese el límite superior :"))


        numeroDatos = int(input("->Ingrese el número de variables aleatorias a generar :"))
        #nivelDeSignificacia = float(input("->Ingrese el nivel de significancia para la prueba chi cuadrado :"))
        nivelDeSignificacia = 0.05

        tipoDistribucion = st.uniform(limiteInferior, (limiteSuperior - limiteInferior))
        nombreDistribucion = "Distribución General Uniforme"
        objUniforme = uniformDistribution.Uniform(numeroDatos, tipoDistribucion, nivelDeSignificacia,
                                                  nombreDistribucion, limiteInferior, limiteSuperior)


        legendDensity = 'a' + "=" + str(limiteInferior) + " ; " + 'b' + "=" + str(limiteSuperior)
        legendHistogram = 'a' + "=" + str("{0:.2f}".format(objUniforme.loc)) + " ; " + 'b' + "=" + str("{0:.2f}".format(objUniforme.scale))

        axisX = np.linspace(limiteInferior, limiteSuperior, 100)

        objUniforme.chiSquareTest()
        objUniforme.graph(legendHistogram, legendDensity, axisX)

    # DISTRIBUCION TRIANGULAR
    elif optionSelected == 6:

        os.system("cls")

        nombreDistribucion = "Distribución Triangular"
        print("\t::", nombreDistribucion, "::")

        # Parametros necesarios para la generación
        limiteInferior = float(input("->Ingrese el límite inferior :"))
        limiteSuperior = float(input("->Ingrese el límite superior :"))
        moda = float(input("->Ingrese parametro de forma (entre 0 y 1):"))

        numeroDatos = int(input("->Ingrese el número de variables aleatorias a generar :"))
        #nivelDeSignificacia = float(input("->Ingrese el nivel de significancia para la prueba chi cuadrado :"))
        nivelDeSignificacia = 0.05

        tipoDistribucion = st.triang(moda, limiteInferior,limiteSuperior-limiteInferior)
        objChi2 = triangularDistribution.Triangular(numeroDatos, tipoDistribucion, nivelDeSignificacia,
                                                    nombreDistribucion, moda, limiteInferior, limiteSuperior)

        legendDensity = 'a' + "=" + str(limiteInferior) + " ; " + 'b' + "=" + str(limiteSuperior)+ " ; " + 'x' + "=" + str(moda)
        legendHistogram = 'a' + "=" + str("{0:.2f}".format(objChi2.limInfGenerated)) + " ; " + 'b' + "=" + str("{0:.2f}".format(objChi2.limSupGenerated)) + " ; " + 'x' + "=" + str(
            "{0:.2f}".format(objChi2.modaGenerated))



        axisX = np.linspace(limiteInferior, limiteSuperior, 100)

        objChi2.chiSquareTest()
        objChi2.graph(legendHistogram, legendDensity, axisX)

    # DISTRIBUCION CHICUADRADO
    elif optionSelected == 7:

        os.system("cls")

        nombreDistribucion = "Distribución Chi Cuadrada"
        print("\t::", nombreDistribucion, "::")

        # Parametros necesarios para la generación
        df = float(input("->Ingrese grados de libertad :"))
        numeroDatos = int(input("->Ingrese el número de variables aleatorias a generar :"))
        #nivelDeSignificacia = float(input("->Ingrese el nivel de significancia para la prueba chi cuadrado :"))
        nivelDeSignificacia = 0.05

        tipoDistribucion = st.chi2(df)
        objChi2 = chiDistribution.ChiSquare(numeroDatos, tipoDistribucion, nivelDeSignificacia,
                                                    nombreDistribucion,df)

        legendDensity = r'k' + "=" + str( "{0:.2f}".format(df))
        legendHistogram = r'k' + "=" + str( "{0:.2f}".format(objChi2.dfGenerated))


        axisX = np.linspace(0,objChi2.mean +6 * objChi2.std, numeroDatos)

        objChi2.chiSquareTest()
        objChi2.graph(legendHistogram, legendDensity, axisX)

    #DISTRIBUICON BINOMIAL
    elif optionSelected == 8:
        os.system("cls")

        nombreDistribucion = "Distribución Binomial"
        print("\t::", nombreDistribucion, "::")

        # Parametros necesarios para la generació1n
        probabilitySuccess = float(input("->Ingrese la probabilidad de éxito :"))
        numeroIntentos = int(input("->Ingrese el número de variables aleatorias a generar :"))
        #nivelDeSignificacia = float(input("->Ingrese el nivel de significancia para la prueba chi cuadrado :"))
        nivelDeSignificacia = 0.05

        binomial = st.binom(numeroIntentos, probabilitySuccess)

        objBinomial = binomialDistribution.Binomial(numeroIntentos, binomial, nivelDeSignificacia, nombreDistribucion,
                                                    probabilitySuccess)

        objBinomial.chiSquareTest()
        objBinomial.graph()

    #DISTRIBUICON POISSON
    elif optionSelected == 9:
        os.system("cls")

        nombreDistribucion = "Distribución de Poisson"
        print("\t::", nombreDistribucion, "::")

        # Parametros necesarios para la generació1n
        media = float(input("->Ingrese la media:"))
        numeroDatos = int(input("->Ingrese el número de variables aleatorias a generar :"))
        #nivelDeSignificacia = float(input("->Ingrese el nivel de significancia para la prueba chi cuadrado :"))
        nivelDeSignificacia = 0.05
        distType = st.poisson(media)
        objPoisson = poissonDistribution.Poisson(numeroDatos, distType, nivelDeSignificacia, nombreDistribucion, media)

        objPoisson.chiSquareTest()
        objPoisson.graph()

    else:
        backToMenu = False