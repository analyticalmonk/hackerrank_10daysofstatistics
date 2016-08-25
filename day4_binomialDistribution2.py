p = 0.12
q = 1 - p
n = 10

p_1 = (pow(q, n) + 10*pow(q, n - 1)*p + 45*pow(q, n - 2)*pow(p, 2))
p_2 = 1 - (pow(q, n) + 10*pow(q, n - 1)*p)

print(round(p_1, 3))
print(round(p_2, 3))
