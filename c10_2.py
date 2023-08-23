try:
    price = int(input('料金を入力 >>'))
    number = int(input('人数を入力 >>'))
    print(f'1人あたり{price/number}です')
except: 
    print('料金と人数に適正な整数を入力してください')

print('プログラムを終了します')
