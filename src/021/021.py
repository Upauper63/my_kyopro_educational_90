import sys
f = open('021.txt', 'r')
sys.stdin = f

import sys
import math
sys.setrecursionlimit(10 ** 9)
n, m = map(int, input().split(' '))
edges = [[] for _ in range(n)]
rev_edges = [[] for _ in range(n)]
ct = 0
for _ in range(m):
    ct += 1
    a, b = map(lambda x: int(x) - 1, input().split(' '))
    edges[a].append(b)
    rev_edges[b].append(a)

is_reached = [False] * n
order = []
cnt = 0
def dfs(p, edges):
    global cnt
    if is_reached[p]:
        return
    is_reached[p] = True
    for edge in edges[p]:
        dfs(edge, edges)
    order.append(p)
    cnt += 1
    return

for i in range(n):
    dfs(i, edges)

rst = 0
is_reached = [False] * n
for p in order[::-1]:
    cnt = 0
    dfs(p, rev_edges)
    if cnt >= 2:
        rst += math.factorial(cnt) // (2 * math.factorial(cnt - 2))
print(rst)