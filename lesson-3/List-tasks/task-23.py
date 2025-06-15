org_list = list(map(int, input().split()))
new_list = []

for i in org_list:
    if i % 2:
        new_list.append(i)

print('Odds:', *new_list)