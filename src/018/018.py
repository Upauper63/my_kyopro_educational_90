import sys
f = open('018.txt', 'r')
sys.stdin = f

import math
t = int(input())
l, x, y = map(int, input().split(' '))
q = int(input())
for _ in range(q):
    e = int(input())
    rad = e / t * 2 * math.pi - math.pi / 2
    tmp_y =  - (l / 2) * math.cos(rad)
    tmp_z = (l / 2) * math.sin(rad) + l / 2
    dist = math.sqrt(x ** 2 + (tmp_y - y) ** 2)
    print(math.degrees(math.atan2(tmp_z, dist)))