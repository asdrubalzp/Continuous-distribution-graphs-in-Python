import Distribution as dt
import scipy.stats as st


#Esta clase herereda los atributos y metodos de la clase Distribution
class ChiSquare(dt.Distribution):

    def __init__(self,dataNumber, distributionType, significanceLevel, nameDistribution, deegresFreedom):
        super().__init__(dataNumber, distributionType, significanceLevel,nameDistribution)
        self.deegresFreedom = deegresFreedom
        # .FIT DEVUELVE LOS PARAMETROS A LOS QUE  SE AJUSTA NUESTRO MODELO
        self.dfGenerated,aux,aux2= st.chi2.fit(self.arrayOfAdjustedRandomVariables)
        self.dfGenerated = aux + aux2 + self.dfGenerated
        self.mean = st.chi2.mean(self.deegresFreedom)
        self.std = st.chi2.std(self.deegresFreedom)
