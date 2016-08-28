import math

def poisson(k, l):
  return round(((pow(l, k)*math.exp(-l))/math.factorial(k)), 3)

print(poisson(5, 2.5))
