import sys
f = open('016.txt', 'r')
sys.stdin = f

n = int(input())
a, b, c = map(int, input().split(' '))
rst = float('inf')
for i in range(10000):
    for j in range(10000):
        if (n - a * i - b * j) % c:
            continue
        if n - a * i - b * j >= 0:
            rst = min(rst, (i + j + (n - a * i - b * j) // c))
print(rst)