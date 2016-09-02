import numpy as np

m, n = tuple([int(i) for i in input().split()])
in_list = [[float(j) for j in input().split()] for i in range(n)]
q = int(input())
output_x = np.matrix([([1] + [float(j) for j in input().split()]) for i in range(q)])

input_y = np.matrix([in_list[i][-1] for i in range(n)])
input_x = np.matrix([([1] + in_list[i][:-1]) for i in range(n)])

B = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(input_x), input_x)), np.transpose(input_x)), np.transpose(input_y))
output_y = ([float(x) for x in np.dot(output_x, B)])

print(*output_y, sep="\n")
