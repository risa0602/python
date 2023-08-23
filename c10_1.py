try:
    price = int(input('料金を入力 >>'))
    number = int(input('人数を入力 >>'))
    print(f'1人あたり{price/number}です')
except ValueError:
    print('料金または人数は整数してください')
except ZeroDivisionError:
    print('人数に0は入力しないでください')
print('プログラムを終了します')
