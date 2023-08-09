import random
dices = []
count = int(input('何回振る? >>'))
for _ in range(count):
    dices.append(random.randint(1,6))
    print(dices)
print(f'合計は{sum(dices)}でした')
