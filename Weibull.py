import Distribution as dt
import scipy.stats as st
import math
import numpy as np
#Esta clase herereda los atributos y metodos de la clase Distribution
class Weibull(dt.Distribution):

    def __init__(self,dataNumber, distributionType, significanceLevel, nameDistribution, form, scale, location):
        super().__init__(dataNumber, distributionType, significanceLevel,nameDistribution)
        self.form = form
        self.scale = scale
        self.location = location
        #  .FIT DEVUELVE LOS PARAMETROS A LOS QUE  SE AJUSTA NUESTRO MODELO
        self.formGenerated , self.locationGenerated, self.scaleGenerated= st.weibull_min.fit(self.arrayOfAdjustedRandomVariables)


        self.mean = st.weibull_min.mean(self.form,self.location,self.scale)

        self.var = st.weibull_min.var(self.form, self.location, self.scale)
        self.des = math.sqrt(self.var)



