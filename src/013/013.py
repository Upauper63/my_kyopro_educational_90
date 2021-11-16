import sys
f = open('013.txt', 'r')
sys.stdin = f

import heapq
n, m = map(int, input().split(' '))
edges = [[] for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split(' '))
    a, b = map(lambda x: x - 1, [a, b])
    edges[a].append((b, c))
    edges[b].append((a, c))

def dijkstra(s):
    dist = [float('inf')] * n
    dist[s] = 0
    q = [(0, s)]
    while q:
        _, idx = heapq.heappop(q)
        for edge, cost in edges[idx]:
            if dist[edge] > dist[idx] + cost:
                dist[edge] = dist[idx] + cost
                heapq.heappush(q, (dist[edge], edge))
    return dist

x = dijkstra(0)
y = dijkstra(n - 1)

for i in range(n):
    print(x[i] + y[i])