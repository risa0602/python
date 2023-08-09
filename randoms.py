import random
count = 0
while True:
    count += 1
    n=random.randint(1,9999)
    print(f'{count}:{n}')
    if n == 7777:
        break
    print(f'{count}回で7777が出ました!')
