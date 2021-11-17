import sys
f = open('014.txt', 'r')
sys.stdin = f

n = int(input())
a_ls = list(map(int, input().split(' ')))
b_ls = list(map(int, input().split(' ')))
a_ls.sort()
b_ls.sort()
rst = 0
for a, b in zip(a_ls, b_ls):
    rst += abs(a - b)
print(rst)