scores1 = [80,40,50]
scores2 = [80,40,50]
print(f'scores1のidentity: {id(scores1)}')
print(f'scores2のidentity: {id(scores2)}')

if scores1 == scores2:
    print('scores1とscores2は同じ内容です')
else:
    print('scores1とscores2は違う内容です')

if id(scores1) == id(scores2):
    print('scores1とscores2は同じ存在です')
else:
    print('scores1とscores2は違う存在です')

before_names=['a','b','c']
"""
copied_name=list()
for n in before_names:
    copied_names.append(n)
"""
copied_names=before_names[:]
