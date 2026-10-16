import math as m
import numpy as np
import scipy.stats as stats

data = np.array([135, 140, 130, 145, 150, 138, 142, 137, 136, 148, 141, 139, 143, 147, 149, 134, 133, 146, 144, 132])


print('Problem 1 Answers:')
n = len(data)
xbar = np.mean(data)
sd = np.std(data, ddof=1)
se = sd / m.sqrt(n)
t90 = stats.t.ppf(0.95, n - 1)
low90 = xbar - t90 * se
high90 = xbar + t90 * se
print('Sample mean:', round(xbar, 4))
print('Standard error:', round(se, 4))
print('t value:', round(t90, 4))
print('90% CI:', round(low90, 4), round(high90, 4))


print('Problem 2 Answers:')
t95 = stats.t.ppf(0.975, n - 1)
low95 = xbar - t95 * se
high95 = xbar + t95 * se
print('Standard error:', round(se, 4))
print('t value:', round(t95, 4))
print('95% CI:', round(low95, 4), round(high95, 4))
if (high95 - low95) > (high90 - low90):
    print('Wider than the 90% interval')
else:
    print('Narrower than the 90% interval')


print('Problem 3 Answers:')
sigma = 5
se_z = sigma / m.sqrt(n)
z95 = stats.norm.ppf(0.975)
low_z = xbar - z95 * se_z
high_z = xbar + z95 * se_z
print('Standard error:', round(se_z, 4))
print('z value:', round(z95, 4))
print('95% CI:', round(low_z, 4), round(high_z, 4))
if (high_z - low_z) > (high95 - low95):
    print('Wider than the Q2 interval')
else:
    print('Narrower than the Q2 interval')
