import scipy.stats as st
import numpy as np
import matplotlib.pyplot as plt

class Binomial:
    def __init__(self,dataNumber, distributionType, significanceLevel, nameDistribution, probabilityOfSuccess):
        self.dataNumber = dataNumber
        self.distributionType =distributionType
        self.significanceLevel =significanceLevel
        self.nameDistribution =nameDistribution
        self.probabilityOfSuccess = probabilityOfSuccess
        self.arrayOfAdjustedRandomVariables = self.distributionType.rvs(self.dataNumber)
        # .rvs Genera numeros aleatorios con respecto a una distribucion propuesta
        self.numberOfHistogramClasses = np.round(np.sqrt(dataNumber))
        self.degreesOfFreedom = self.numberOfHistogramClasses - 1

        self.meanExpected = self.dataNumber * self.probabilityOfSuccess
        self.varianza = self.meanExpected * (1 - self.probabilityOfSuccess)
        self.stdExpected = np.sqrt(self.varianza)

        self.meanGenerated = np.mean(self.arrayOfAdjustedRandomVariables)
        self.stdGenerated = np.std(self.arrayOfAdjustedRandomVariables)


    def  graphHistogram(self):

        p = self.meanGenerated/self.dataNumber


        plt.hist(self.arrayOfAdjustedRandomVariables, bins=(int(self.numberOfHistogramClasses)), edgecolor='black', linewidth=1, density=True)

    def probabilityFunction(self, axisX):
        legendDensity = r'n' + "=" + str(self.dataNumber) +" ; "+ r'p' + "=" + str(self.probabilityOfSuccess)
        plt.plot(axisX,  self.distributionType.pmf(axisX), 'ko', ms=5, label=legendDensity)
        plt.vlines(axisX, 0, self.distributionType.pmf(axisX), colors='r', lw=3)

    def graph(self):
        axisX = np.arange(int(self.meanExpected - 4 * self.stdExpected), (self.meanExpected + 4 * self.stdExpected))
        self.probabilityFunction(axisX)
        self.graphHistogram()
        plt.ylabel('$ f ( x )$')
        plt.xlabel('$ x $')
        plt.legend(loc='upper right',frameon = False)
        plt.title(self.nameDistribution)
        plt.show()

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