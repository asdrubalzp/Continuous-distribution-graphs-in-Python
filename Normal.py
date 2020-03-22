import Distribution as dt
import scipy.stats as st


#Esta clase herereda los atributos y metodos de la clase Distribution
class Normal(dt.Distribution):

    def __init__(self,dataNumber, distributionType, significanceLevel, nameDistribution, mean, standardDesv):
        super().__init__(dataNumber, distributionType, significanceLevel,nameDistribution)
        self.mean = mean
        self.standardDesv = standardDesv
        # .FIT DEVUELVE LOS PARAMETROS A LOS QUE  SE AJUSTA NUESTRO MODELO
        self.meanGenerated, self.stdDesvGenerated = st.norm.fit(self.arrayOfAdjustedRandomVariables)


