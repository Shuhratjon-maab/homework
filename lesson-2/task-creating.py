n = int(input('Number of tasks: '))
d = input('Enter folder directory | ')

for i in range(1, n+1):
    file = f'{d}/task-{i}.py'
    open(file, 'w')
    file.close()