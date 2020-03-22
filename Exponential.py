import Distribution as dt
import scipy.stats as st

#Esta clase herereda los atributos y metodos de la clase Distribution
class Exponential(dt.Distribution):

    def __init__(self,dataNumber, distributionType, significanceLevel, nameDistribution, mean):
        super().__init__(dataNumber, distributionType, significanceLevel,nameDistribution)

        # .FIT DEVUELVE LOS PARAMETROS A LOS QUE  SE AJUSTA NUESTRO MODELO
        _ , self.meanGenerated = st.expon.fit(self.arrayOfAdjustedRandomVariables)
        self.mean = mean
        self.des = distributionType.std()
