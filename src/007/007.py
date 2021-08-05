from io import TextIOWrapper
import sys
f = open('007.txt', 'r')
sys.stdin = f

n = int(input())
a_ls = list(map(int, input().split(' ')))
a_ls.sort()

def check(q):
    top = n - 1
    btm = 0
    while top - btm > 1:
        mid = (top + btm) // 2
        if q >= a_ls[mid]:
            btm = mid
        else:
            top = mid
    top_val = abs(q - a_ls[top])
    btm_val = abs(q - a_ls[btm])
    if top_val <= btm_val:
        return top_val
    else:
        return btm_val

q = int(input())
for _ in range(q):
    b = int(input())
    print(check(b))