n = int(input())
num1 = [float(x) for x in input().split()]
num2 = [float(x) for x in input().split()]

mean1 = sum(num1)/n
mean2 = sum(num2)/n
diff1 = [(x - mean1) for x in num1]
diff2 = [(x - mean2) for x in num2]
sd1 = pow(sum([pow(x, 2) for x in diff1])/n, 0.5)
sd2 = pow(sum([pow(x, 2) for x in diff2])/n, 0.5)

rho = sum(diff1[i]*diff2[i] for i in range(n))/(n*sd1*sd2)

print(round(rho, 3))
