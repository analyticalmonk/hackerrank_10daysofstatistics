n = int(input())
X = [int(x) for x in input().split()]
F = [int(x) for x in input().split()]

nums = [X[n] for n in range(n) for _i in range(F[n])]
nums.sort()
len_n = len(nums)

q2 = (nums[int(len_n/2)] if (len_n%2 != 0) else ((nums[int(len_n/2 - 1)] + nums[int(len_n/2)]) / 2))

nums1 = nums[:int(len_n/2)]
len_n1 = len(nums1)
q1 = (nums1[int(len_n1/2)] if (len_n1%2 != 0) else ((nums1[int(len_n1/2 - 1)] + nums1[int(len_n1/2)]) / 2))

nums3 = nums[int(len_n/2):] if (len_n%2 == 0) else nums[int(len_n/2) + 1:]
len_n3 = len(nums3)
q3 = (nums3[int(len_n3/2)] if (len_n3%2 != 0) else ((nums3[int(len_n3/2 - 1)] + nums3[int(len_n3/2)]) / 2))

print(float(q3 - q1))
