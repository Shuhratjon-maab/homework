lis = input().split()
indx = int(input())

# indx -= 1 if index counted from 1

if indx < len(lis):
    lis.pop(indx) # lis.remove(lis[indx])
    print(lis)
else:
    print('Index is out of range!')