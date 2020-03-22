import Distribution as dt
import scipy.stats as st
import math

#Esta clase herereda los atributos y metodos de la clase Distribution
class Erlang(dt.Distribution):

    def __init__(self,dataNumber, distributionType, significanceLevel, nameDistribution, form, expectedValue):
        super().__init__(dataNumber, distributionType, significanceLevel,nameDistribution)
        self.form = form
        self.expectedValue = expectedValue
        # .FIT DEVUELVE LOS PARAMETROS A LOS QUE  SE AJUSTA NUESTRO MODELO

        self.formGenerated,_, self.expectedValueGenerated = st.erlang.fit(self.arrayOfAdjustedRandomVariables)


        self.meanGenerated = st.erlang.mean(self.arrayOfAdjustedRandomVariables)
        var = st.erlang.var(self.arrayOfAdjustedRandomVariables)
        self.desGenerated = (math.sqrt(var))

        self.iqr = st.iqr(self.arrayOfAdjustedRandomVariables)
        self.median = st.erlang.median(self.arrayOfAdjustedRandomVariables)