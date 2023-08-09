import random

num = random.randint(5,10) # 5∼10の値をランダムに１個生成
print(num) # 8

dices = []
count = int(input('何回振る? >>'))
for _ in range(count):
    dices.append(random.randint(1,6))
    print(dices)
    print(f'合計は{sum(dice)}でした')
