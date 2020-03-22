import Distribution as dt
import scipy.stats as st


#Esta clase herereda los atributos y metodos de la clase Distribution
class Uniform(dt.Distribution):

    def __init__(self,dataNumber, distributionType, significanceLevel, nameDistribution, limInf, limSup):
        super().__init__(dataNumber, distributionType, significanceLevel,nameDistribution)
        self.limInf = limInf
        self.limSup = limSup
        # .FIT DEVUELVE LOS PARAMETROS A LOS QUE  SE AJUSTA NUESTRO MODELO
        self.loc, self.scale = st.uniform.fit(self.arrayOfAdjustedRandomVariables)
