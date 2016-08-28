from math import erf


threshold_wt = 9800
sample_size = 49
pop_mean = 205
pop_sd = 15

sample_sd = 15/pow(sample_size,0.5)
sample_mean = pop_mean
safe_wt = threshold_wt/sample_size

def clf(x):
  z = (x - sample_mean)/(sample_sd*pow(2, 0.5))
  return (0.5*(1 + erf(z)))

print(round(clf(200), 4))
