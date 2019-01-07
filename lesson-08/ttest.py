import numpy as np
import scipy.stats as stats

np.random.seed(282629734)
x = stats.t.rvs(10, size=1000)
print(x.mean())
print(x.var())
print(x.min())
print(x.max())
m, v, s, k = stats.t.stats(10, moments='mvsk')
print(stats.t.stats(100, moments='mvsk'))