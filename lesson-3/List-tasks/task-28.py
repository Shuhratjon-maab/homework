lis = input().split()

begin = int(input())
end = int(input())

sublist = lis[begin - 1 : end]

print('Min:', min(sublist), 'for', *sublist)