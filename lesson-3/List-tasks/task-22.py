org_list = list(map(int, input().split()))
new_list = []

for i in org_list:
    if i % 2 == 0:
        new_list.append(i)

print('Evens:', *new_list)