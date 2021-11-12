import sys
f = open('012.txt', 'r')
sys.stdin = f


import sys
sys.setrecursionlimit(10 ** 9)
from collections import defaultdict
par = defaultdict(tuple)
def find(x):
    if not par[x]:
        return x
    else:
        par[x] = find(par[x])
        return par[x]
def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x[0] > y[0] or (x[0] == y[0] and x[1] > y[1]):
        x, y = y, x
    par[y] = x
def same(x, y):
    return find(x) == find(y)

h, w = map(int, input().split(' '))
q = int(input())
ls = [[0] * w for _ in range(h)]
for _ in range(q):
    val = list(map(lambda x: int(x) - 1, input().split(' ')))
    if val[0]:
        if not (ls[val[1]][val[2]] and ls[val[3]][val[4]]):
            print('No')
        else:
            if same((val[1], val[2]), (val[3], val[4])):
                print('Yes')
            else:
                print('No')
    else:
        ls[val[1]][val[2]] = 1
        if val[1] - 1 >= 0 and ls[val[1] - 1][val[2]]:
            union((val[1], val[2]), (val[1] - 1, val[2]))
        if val[2] + 1 < w and ls[val[1]][val[2] + 1]:
            union((val[1], val[2]), (val[1], val[2] + 1))
        if val[1] + 1 < h and ls[val[1] + 1][val[2]]:
            union((val[1], val[2]), (val[1] + 1, val[2]))
        if val[2] - 1 >= 0 and ls[val[1]][val[2] - 1]:
            union((val[1], val[2]), (val[1], val[2] - 1))