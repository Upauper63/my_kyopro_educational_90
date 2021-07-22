import sys
f = open('004.txt', 'r')
sys.stdin = f

h, w = map(int, input().split(' '))
row_sum = [0] * h
col_sum = [0] * w
ls = []
for i in range(h):
    row = list(map(int, input().split(' ')))
    ls.append(row)
    row_sum[i] = sum(row)
    for j, val in enumerate(row):
        col_sum[j] += val
for i in range(h):
    exp = []
    for j in range(w):
        exp.append(str(row_sum[i] + col_sum[j] - ls[i][j]))
    print(" ".join(exp))
