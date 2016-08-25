from math import erf


def cdf(x):
  z = (x - 20)/(2*pow(2, 0.5))
  return (0.5 * (1 + erf(z)))

print(round(cdf(19.5), 3))
print(round((cdf(22) - cdf(20)), 3))
