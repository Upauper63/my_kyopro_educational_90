import sys
f = open('020.txt', 'r')
sys.stdin = f

a, b, c = map(int, input().split(' '))
if c ** b - a > 0:
    print('Yes')
else:
    print('No')