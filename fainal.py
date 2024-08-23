import random
import turtle

colo = [[198, 13, 32],
 [248, 236, 25], [40, 76, 188],
 [39, 216, 69], [238, 227, 5], [227, 159, 49]]

# Turtle の初期設定
t = turtle.Turtle()
t.speed(0)  # 速度を最大に設定
turtle.colormode(255)  # RGB モードを設定
t.hideturtle()

# ドットの設定
dot_size = 10  # ドットのサイズ
spacing = 30    # ドットの間隔

# 描画範囲の設定
width = 300
height = 300

# ドットを描く
t.penup()
for y in range(-height // 2, height // 2 , spacing):
    for x in range(-width // 2, width // 2 , spacing):
        t.goto(x, y)
        t.dot(dot_size, random.choice(colo))  # ドットのサイズと色を設定

# ウィンドウを閉じるのを待つ
turtle.done()