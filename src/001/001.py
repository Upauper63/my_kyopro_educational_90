import sys
f = open('001.txt', 'r')
sys.stdin = f

n, l = map(int, input().split(' '))
k = int(input())
a_ls = [0] + list(map(int, input().split(' '))) + [l]

diff_ls = []
for i in range(n + 1):
    diff_ls.append(a_ls[i + 1] - a_ls[i])

def check(mid):
    val = 0
    m = 0
    ls = []
    for i in diff_ls:
        val += i
        if val >= mid:
            m += 1
            ls.append(val)
            val = 0
    return m, ls

top = l
btm = 0
mid = (top - btm) // 2
is_end = False
while not is_end:
    m, ls = check(mid)
    if m >= k + 1:
        if top - btm > 1:
            btm = mid
            mid = (top + btm) // 2
        else:
            print(min(ls))
            is_end = True
    else:
        top = mid
        mid = (top + btm) // 2

