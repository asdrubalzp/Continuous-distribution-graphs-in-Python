import Distribution as dt
import scipy.stats as st
import numpy as np

#Esta clase herereda los atributos y metodos de la clase Distribution
class Triangular(dt.Distribution):

    def __init__(self,dataNumber, distributionType, significanceLevel, nameDistribution, moda, min, max):
        super().__init__(dataNumber, distributionType, significanceLevel,nameDistribution)
        self.min = min
        self.max = max
        self.moda = moda
        # .FIT DEVUELVE LOS PARAMETROS A LOS QUE  SE AJUSTA NUESTRO MODELO
        self.modaGenerated,self.limInfGenerated, self.limSupGenerated = st.triang.fit(self.arrayOfAdjustedRandomVariables)


