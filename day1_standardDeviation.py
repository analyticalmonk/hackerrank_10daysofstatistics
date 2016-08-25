n = int(input())
nums = [int(x) for x in input().split()]

nums_mean = sum(nums)/n

sd = round(pow(sum([pow((x - nums_mean), 2) for x in nums])/n, 0.5), 1)

print(sd)
