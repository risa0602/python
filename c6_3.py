userinfo = input('名前と血液型をカンマで区切って１行で入力 >>')
name,blood = userinfo.split(',')
blood = blood.upper().strip() # アッパーメゾット
# 続けて書くことによってチェーン型になる
print(f'{name}さんは{blood}型なので大吉です')
