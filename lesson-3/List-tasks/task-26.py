lis = input().split()
l = len(lis)

print('middle:', lis[(l-1)//2], lis[l//2] if l % 2 == 0 else '')