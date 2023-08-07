height=float(input('身長　cm >>'))
weight=float(input('体重　kg >>'))
bmi = weight / (height/100 * height/100)
print(f'BMIは{bmi:.2f}です')
