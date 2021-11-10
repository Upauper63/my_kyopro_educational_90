import sys
f = open('010.txt', 'r')
sys.stdin = f

n = int(input())
c1 = []
c2 = []
for _ in range(n):
    c, p = map(int, input().split(' '))
    if c - 1:
        c1.append(0)
        c2.append(p)
    else:
        c1.append(p)
        c2.append(0)

for i in range(len(c1) - 1):
    c1[i + 1] += c1[i]
for i in range(len(c2) - 1):
    c2[i + 1] += c2[i]
q = int(input())
for _ in range(q):
    l, r = map(lambda x: int(x) - 1, input().split(' '))
    if l:
        print(c1[r] - c1[l - 1], c2[r] - c2[l - 1])
    else:
        print(c1[r], c2[r])

