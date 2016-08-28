from math import erf


pop_mean = 2.4
pop_sd = 2.0
sample_size = 100
sample_mean = pop_mean
sample_sd = pop_sd/pow(sample_size, 0.5)
tickets_left = 250
target = tickets_left/sample_size

def clf(x):
  z = (x - sample_mean)/(sample_sd*pow(2, 0.5))
  return (0.5*(1 + erf(z)))

print(round(clf(target), 4))
