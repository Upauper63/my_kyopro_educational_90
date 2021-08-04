import sys
f = open('006.txt', 'r')
sys.stdin = f

n, k = map(int, input().split(' '))
s = input()
ls = []
for idx, val in enumerate(s):
    while ls and ls[-1] > val:
        ls.pop()
    ls.append(val)
    if idx >= n - k:
        print(ls.pop(0), end='')