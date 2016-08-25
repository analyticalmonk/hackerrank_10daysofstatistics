p_b = (1.09/2.09)
p_g = 1 - p_b

final_p = 1 - (pow(p_g, 6) + 6*pow(p_g, 5)*pow(p_b, 1) + 15*pow(p_g, 4)*pow(p_b, 2))

print(round(final_p, 3))
