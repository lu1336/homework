import numpy as np
import math as m
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import t

myFile = open('city_vehicle_survey.txt')
data1 = myFile.readlines()
data1 = [float(x) for x in data1]
myFile.close()


print('Problem 2 Answers:')
n = len(data1)
xbar = np.mean(data1)
sd = np.std(data1, ddof=1)
se = sd / m.sqrt(n)
z = (xbar - 5) / se
p = 2 * (1 - norm.cdf(abs(z)))
print('Sample size:', n)
print('Sample mean:', round(xbar, 4))
print('Standard error:', round(se, 4))
print('z score:', round(z, 4))
print('p-value:', round(p, 4))
if p < 0.05:
    print('Significant at 0.05')
else:
    print('Not significant at 0.05')
if p < 0.10:
    print('Significant at 0.10')
else:
    print('Not significant at 0.10')

print('Problem 3 Answers:')
z_crit = norm.ppf(0.975)
max_se = abs(xbar - 5) / z_crit
min_n = m.ceil((sd / max_se) ** 2)
print('Largest standard error:', round(max_se, 4))
print('Minimum sample size:', min_n)

print('Problem 5 Answers:')


myFile1 = open('vehicle_data_1.txt')
data1 = myFile1.readlines()

myFile2 = open('vehicle_data_2.txt')
data2 = myFile2.readlines()

data1 = [float(x) for x in data1]
data2 = [float(y) for y in data2]
myFile1.close()
myFile2.close()

n1 = len(data1)
n2 = len(data2)
mean1 = np.mean(data1)
mean2 = np.mean(data2)
var1 = np.std(data1, ddof=1) ** 2
var2 = np.std(data2, ddof=1) ** 2
se2 = m.sqrt(var1 / n1 + var2 / n2)
z2 = (mean1 - mean2) / se2
p2 = 2 * norm.cdf(-abs(z2))
print('Sample size 1:', n1)
print('Sample size 2:', n2)
print('Sample mean 1:', round(mean1, 4))
print('Sample mean 2:', round(mean2, 4))
print('Standard error:', round(se2, 4))
print('z score:', round(z2, 4))
print('p-value:', p2)
if p2 < 0.05:
    print('Significant at 0.05')
else:
    print('Not significant at 0.05')
if p2 < 0.10:
    print('Significant at 0.10')
else:
    print('Not significant at 0.10')
