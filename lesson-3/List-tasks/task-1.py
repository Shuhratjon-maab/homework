ls = input().split()
# or basic list has given without input -> ls = [...]
el = input()

print('result:', ls.count())

# alternative:

cnt = 0

for i in ls:
    cnt += (i == el)

print('result:', cnt)