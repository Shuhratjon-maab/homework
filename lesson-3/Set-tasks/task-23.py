from random import randint

random_set = set()

for  _ in range(10):
    random_set.add(randint(1, 100))

print(random_set)