from math import erf


avg = 70
sDev = 10

def clf(x):
    z = (x - avg)/(sDev*pow(2, 0.5))
    return (0.5 * (1 + erf(z)))

print(round((1 - clf(80))*100, 2))
print(round((1 - clf(60))*100, 2))
print(round(clf(60)*100, 2))
