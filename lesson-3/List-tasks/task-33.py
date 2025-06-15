lis = input().split()
elm = input()
inds = []

for i in range(len(lis)):
    if lis[i] == elm:
        inds.append(i)
        # print(i) or i + 1 for natural counting

print('indices of element:', *inds)