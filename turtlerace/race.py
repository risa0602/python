import random
import turtle

ts=['blue','red','yellow','brown','green'] # 亀配列

def setup():
    global ts 
    screen=turtle.Screen() # 画面生成
    screen.setup(1290,720) # 画面サイズ設定
    screen.bgpic('pavement.gif') # 背景画像設定
    startline=-620 # スタートのx座標の値

    for i in range(len(ts)):
        t=turtle.Turtle()
        t.shape('turtle')
        t.color(ts[i]) # 亀の色設定
        t.penup() # 最初は線の描画はしない
        t.setpos(startline,(len(ts)//2)*-40+40*i) # 亀のスタート位置
        t.pendown() # 以降は線を描画
        ts[i] = t # リストを更新

def race():
    global ts
    finishline = 540

    while True:
        for current_t in ts:
            move=random.randint(0,20)
            current_t.forward(move)

            x=current_t.xcor() # 亀のx座標取得
            # ゴールしたかの判定
            if x >= finishline:
                winner_color=current_t.color() # 色取得
                # 文字の描画(内容,font(フォントの種類,文字の大きさ,ウェイト))
                current_t.write('Win!'+winner_color[0],font=('Arial',16,'bold'))
                return # 誰かがゴールしたら関数を抜ける
setup()
race()
turtle.mainloop()
