import sys
f = open('003.txt', 'r')
sys.stdin = f

import sys
sys.setrecursionlimit(10 ** 9)
n = int(input())
edges = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split(' '))
    edges[a].append(b)
    edges[b].append(a)
dist = [[] for _ in range(n)]
is_reached = [False] * n
def dfs(edge, val):
    if is_reached[edge] == True:
        return
    is_reached[edge] = True
    dist[edge] = val
    for edge in edges[edge]:
        dfs(edge, val + 1)
dfs(0, 0)
term = dist.index(max(dist))
dist = [[] for _ in range(n)]
is_reached = [False] * n
dfs(term, 0)
print(max(dist) + 1)