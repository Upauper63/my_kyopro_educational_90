import sys
f = open('002.txt')
sys.stdin = f

n = int(input())
for i in range(1 << n):
    ls = [0 for _ in range(n)]
    for j in range(n):
        if i >> j & 1:
            ls[j] = 1
    pre_cnt = 0
    suf_cnt = 0
    rst = ''
    for s in ls[::-1]:
        if s:
            suf_cnt += 1
            rst += ')'
            if suf_cnt > pre_cnt:
                break
        else:
            pre_cnt += 1
            rst += '('

    if pre_cnt == suf_cnt:
        print(rst)