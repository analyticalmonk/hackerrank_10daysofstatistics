sample_size = 100
pop_mean = 500
pop_sd = 80
sample_mean = pop_mean
sample_sd = pop_sd/pow(sample_size, 0.5)

def rev_zScore(z):
  x = sample_sd*z + sample_mean
  return x

print(round(rev_zScore(-1.96), 2))
print(round(rev_zScore(1.96), 2))
