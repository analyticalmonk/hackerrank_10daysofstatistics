n = int(input())
num1 = [float(x) for x in input().split()]
num1_s = sorted(num1)
num2 = [float(x) for x in input().split()]
num2_s = sorted(num2)

rank1 = [j+1 for i in range(n) for j in range(n) if num1[i] == num1_s[j]]
rank2 = [j+1 for i in range(n) for j in range(n) if num2[i] == num2_s[j]]

spearman_r = 1 - 6*(sum([pow(rank1[i] - rank2[i], 2) for i in range(n)]))/(n*(pow(n, 2)-1))

print(round(spearman_r, 3))
