import numpy as np
import math
import cmath
import statsmodels.api as sm

z0 = 50
zl = [0,510,-434.783j,-400j,-370.370j,7.59j,8.25j,8.91j,7.392+58.753j,60.961+215.121j,44.695-179.271j,3.859-16.166j,4.983+11.535j,9.062+46.957j,41.842+11.000j,57.321+17.848j,74.836+4.394j,129.298-220.689j,12.470-56.378j,6.917-15.611j,3.868+7.382j,7.770+41.144j,35.744+129.642j]
zlb = []
gamma = []




for i in range(len(zl)):
    zlb.append(zl[i]/z0)
    gamma.append((zlb[i]-1)/(zlb[i]+1))
    print(cmath.polar(gamma[i])[0],np.rad2deg(cmath.polar(gamma[i])[1]))

print(20*np.log10(2.264/1.034))