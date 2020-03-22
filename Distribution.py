
import scipy.stats as st
import math
import numpy as np
import matplotlib.pyplot as plt
class Distribution :
    """
    Cada distribucion cuenta con :
    dataNumber = numero de datos aleatorios a generar
    distributionType = objeto  de tipo de distribucion con el que se trabajara,
    este objeto debera contener los parametros de forma y escala dependiendo de la distribucion
    degreesOfFreedom = grados de libertad con los que se hara el test chi cuadrado
    significanceLevel = nivel de significancia para el test chi cuadrado
    nameOfDistribution = Nombre de la distribucion

    """

    def __init__(self, dataNumber, distributionType, significanceLevel, nameOfDistribution):

        self.dataNumber = dataNumber
        self.distributionType = distributionType
        self.arrayOfAdjustedRandomVariables = self.distributionType.rvs(self.dataNumber)
        #.rvs Genera numeros aleatorios con respecto a una distribucion propuesta
        self.numberOfHistogramClasses = np.round(math.sqrt(dataNumber))
        self.degreesOfFreedom = self.numberOfHistogramClasses-1
        self.significanceLevel = significanceLevel
        self.nameOfDistribution =nameOfDistribution

    def stadisticsValuesOfChiSquare(self):
        """
        funcion que retorna un vector con  el estadistico c y el p-value con k-1 grados de libertad, k hace referencia
        al numero de intervalos
        """

        observedFreq, intervals = np.histogram(self.arrayOfAdjustedRandomVariables,bins=int(self.numberOfHistogramClasses))
        def ei(i):
            return self.dataNumber * (self.distributionType.cdf(intervals[i]) - self.distributionType.cdf(intervals[i - 1]))

        expectedFreq = [ei(i) for i in range(1, len(intervals))]

        # Se retorna un vector en la pos[0] se encuentra el estadistico c y en la pos[1] el p-value
        return st.chisquare(observedFreq, expectedFreq)

    def criticValueOfChiSquareTable(self):
        #calcula es estadistico c de la tabla chiCuadrado
        alfaValue = 1 - self.significanceLevel
        return round(st.chi2.ppf(alfaValue, self.degreesOfFreedom),2)

    def chiSquareTest(self):

        estimator_C = self.stadisticsValuesOfChiSquare()[0]
        tableValue = self.criticValueOfChiSquareTable()
        print("\n:::Prueba de bondad de ajuste chi cuadrado:::")
        print("->Estimador C :" + str(round(estimator_C,2)))
        print("->Valor crítico de la tabla chi cuadrado con nivel de significancia {} y {} grados de libertad :{}".format(self.significanceLevel,self.degreesOfFreedom,str(tableValue)))

        if estimator_C <= tableValue:
            print("\n******NO SE RECHAZA LA HIPÓTESIS NULA******")
        else:
            print("\n******SE RECHAZA LA HIPÓTESIS NULA******")


    def generateHistogram(self , legend):
        #grafico del histograma
        plt.hist(self.arrayOfAdjustedRandomVariables,bins=int(self.numberOfHistogramClasses), edgecolor = 'black',  linewidth=1, density=True, label=legend )

    def generateDensityFunction(self, axisX, legendDensityFunction):
        #grafico de la funcion de densidad
        y = self.distributionType
        plt.plot(axisX, y.pdf(axisX), color='r', label = legendDensityFunction, linewidth =3)


    def graph(self, legendHistogram, legendDensityFunction, axisX):
        #Grafica el histograma y la funcion de densidad con su respectiva legenda
        #axisX(vector de numpy) hace referencia al rango en el ejeX de donde a donde se generara la funcion de densidad

        self.generateHistogram(legendHistogram)
        self.generateDensityFunction(axisX,legendDensityFunction)
        plt.ylabel('$ f ( x )$')
        plt.xlabel('$ x $')
        plt.legend(loc='upper right', frameon = False)
        plt.title(self.nameOfDistribution)
        plt.show()


