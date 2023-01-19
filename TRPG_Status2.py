import tkinter as tki
import time as ti
import math
import random

#from PIL import Image, ImageDraw
#from matplotlib import pyplot as plt
#afrom matplotlib import patches

Status_Name = [
    "筋力　",
    "体力　",
    "体格　",
    "敏捷性",
    "外見　",
    "精神力",
    "知性　",
    "教育　"
    ]

ITEM = [
    "Writer(作家)",
    "Dilettante(ディレッタント)",
    "Doctor(医者)",
    "Journalist(ジャーナリスト)",
    "Police Officer(警官)",
    "Detective(探偵)",
    "Professor(教授)",
    "Antiquarian(古物研究家)"
    ]
SKILL = [
    "オカルトもしくは自然、芸術/製作 (文学)、心理学、図書館、歴史、ほかの言語、母国語、任意のほかの1つの技能",
    "芸術/製作 (任意の分野)、射撃、乗馬、対人関係技能(威圧､言いくるめ, 説得もしくは魅惑)から1つ、ほかの言語、 任意のほかの3つの技能",
    "医学、応急手当、科学(生物学)、科学(薬学)、心理学、ほかの言語(ラテン語など)、研究もしくは個人的な専門として任意のほかの2つの技能 (例えば精神科医なら精神分析)",
    "芸術/製作 (写真術)、心理学、図書館、歴史、対人関係技能(威圧、言いくるめ、説得もしくは魅惑)から一つ、母国語、任意の他の2つの言語",
    "聞き耳、芸術/製作 (演劇) または変装, 射撃、心理学、法律、目星、対人関係技能 (威圧、言いくるめ、説得もしくは魅惑) から1つ、任意のほかの1つの技能",
    "芸術/製作 (写真術)、心理学、図書館、変装、法律、目星、対人関係技能 (威圧、言いくるめ、説得もしくは魅惑) から1つ、任意のほかの1つの技能 (鍵開け、射撃など)",
    "心理学、図書館、ほかの言語、母国語、研究または個人的な専門として任意の4つの技能",
    "鑑定 芸術/製作(任意の分野)、図書館、目星、歴史、対人関係技能 (威圧、言いくるめ, 説得もしくは魅惑)から1つ、ほかの言語、任意のほかの1つの技能"
    ]

def click_btn_1():

    print("処理中")# 処理を開始
    #ti.sleep(1)
    select = val.get()
    print(ITEM[select])
    print(Worker(ITEM[select]))
    StatusChart()
    print("処理を完了しました")

#ウィンドウの作成
root = tki.Tk()
root.title("TRPG Status")
root.resizable(False,False) #大きさ固定
root.geometry("800x600+200+200")

#canvas_1位置指定
canvas_1_width = 400
canvas_1_height = 400
canvas_1 = tki.Canvas(root,
                      width = canvas_1_width ,
                      height = canvas_1_height,
                      bg = "white") #大きさ指定
canvas_1.place(x=5,y=5)

#canvas_2位置指定
canvas_2_width = canvas_1_width
canvas_2_height = 180
canvas_2 = tki.Canvas(root,
                      width = canvas_2_width ,
                      height = canvas_2_height,
                      bg = "white") #大きさ指定
canvas_2.place(x=5,y=canvas_1_height + 10)

n = len(Status_Name)
r = canvas_1_height//2 - 20
d = 360 // n # 度
x = []
y = []
up_x = []
up_y = []
Status = []

def calculation(): #正n角形と名称
    #座標計算と配列x,yに代入
    for i in range(n):
        angle = d * i
        a = math.radians(angle) #ラジアンに変換
        sin = math.sin(a)
        cos = math.cos(a)
        x.append(round(canvas_1_width // 2 - r * sin, 0))
        y.append(round(canvas_1_height // 2 - r * cos, 0))
    print(x)
    print(y)
    #canvas_1のレーダーチャート用
    #6角形
    canvas_1_Hexagonal = canvas_1.create_polygon(x[0], y[0],
                                                 x[1], y[1],
                                                 x[2], y[2],
                                                 x[3], y[3],
                                                 x[4], y[4],
                                                 x[5], y[5],
                                                 x[6], y[6],
                                                 x[7], y[7],
                                                 outline="grey",
                                                 fill="white",
                                                 width=1)
    #中心
    canvas_1_Hexagonal = canvas_1.create_oval(canvas_1_width // 2 - 1, canvas_1_height // 2 - 1,
                                              canvas_1_width // 2 + 1, canvas_1_height // 2 + 1,
                                              activefill = "black")
    #名称
    for i in range(n):
        canvas_1_name = canvas_1.create_text(x[i] + 5,y[i],text = Status_Name[i],font = ("Times New Roman",11))

def Worker(worker):
    if worker == ITEM[0]:
        a = SKILL[0]
    elif worker == ITEM[1]:
        a = SKILL[1]
    elif worker == ITEM[2]:
        a = SKILL[2]
    elif worker == ITEM[3]:
        a = SKILL[3]
    elif worker == ITEM[4]:
        a = SKILL[4]
    elif worker == ITEM[5]:
        a = SKILL[5]
    elif worker == ITEM[6]:
        a = SKILL[6]
    else : a = SKILL[7]
    text_Display.delete("1.0", tki.END)
    text_Display.insert("1.0", a)

#レーダーチャート表示
def StatusValue(StatusArray):
    if StatusArray == Status_Name[2] or StatusArray == Status_Name[6] or StatusArray == Status_Name[7]:
       return 6 + random.randint(1,6) + random.randint(1,6)
    return random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

def StatusChart():
    Status.clear()
    up_x.clear()
    up_y.clear()
    for i in range(n):
        #print(Status_Name[i])
        #print(StatusValue(Status_Name[i]))
        angle = d * i
        b = math.radians(angle) #ラジアンに変換
        sin = math.sin(b)
        cos = math.cos(b)
        Status.append(StatusValue(Status_Name[i]))
        new_r = r // 18 * Status[i]  
        up_x.append(round(canvas_1_width // 2 - new_r * sin, 0))
        up_y.append(round(canvas_1_height // 2 - new_r * cos, 0))
    #6角形
    # 線の削除
    calculation()
    canvas_1.create_polygon(up_x[0], up_y[0],
                            up_x[1], up_y[1],
                            up_x[2], up_y[2],
                            up_x[3], up_y[3],
                            up_x[4], up_y[4],
                            up_x[5], up_y[5],
                            up_x[6], up_y[6],
                            up_x[7], up_y[7],
                            outline="red",
                            fill="orange",
                            tag = "canvas_1_Hexagonal_2 "
                            )
    #def Value():
    for i in range(n):
        print(Status_Name[i])
        print(Status[i])
    #Display()
    canvas_2_ = canvas_2.create_rectangle(70, 10,
                                          300, 175,
                                          fill = "white",
                                          outline = "white")
    for i in range(n):
        canvas_2_Value = canvas_2.create_text(80, 20 * i + 15,
                                           text = Status[i] ,
                                           font = ("Times New Roman",12)
                                           )
    #Display5()
    for i in range(n):
        Display5 = Status[i] * 5
        canvas_2_Value5 = canvas_2.create_text(120, 20 * i + 15,
                                           text = "× 5 = "+ str(Display5) ,
                                           font = ("Times New Roman",12)
                                           )


#def Value():
#    for i in range(n):
#        print(Status_Name[i])
#        print(StatusValue(Status_Name[i]))

#def Display():
#
#    canvas_2_ = canvas_2.create_rectangle(70, 10,
#                                          300, 175,
#                                          fill = "white",
#                                          outline = "white")
#    for i in range(n):
#        canvas_2_Value = canvas_2.create_text(80, 20 * i + 15,
#                                           text = StatusValue(Status_Name[i]) ,
#                                           font = ("Times New Roman",12)
#                                           )

#def Display5():
#    for i in range(n):
#        a = StatusValue(Status_Name[i]) * 5
#        canvas_2_Value5 = canvas_2.create_text(120, 20 * i + 15,
#                                           text = "× 5 = "+ str(a) ,
#                                           font = ("Times New Roman",12)
#                                           )


#canvas_1への描画
#canvas_1のフレーム
canvas_1_Frame = canvas_1.create_rectangle(2,
                                           2, 
                                           canvas_1_width + 2,
                                           canvas_1_height + 2,
                                           outline = "gray")

#canvas_1のレーダーチャート用
calculation()

#canvas_2への描画
#canvas_2のフレーム
canvas_2_Frame = canvas_2.create_rectangle(2,
                                           2, 
                                           canvas_2_width + 2,
                                           canvas_2_height + 2,
                                           outline = "gray")

for i in range(n):
    canvas_2_Script = canvas_2.create_text(40, 20 * i + 15,
                                           text = Status_Name[i] + " :",
                                           font = ("Times New Roman",12)
                                           )

#ボタン(Start)作成
button_Start = tki.Button(root,
                          text = "Start",
                          font = ("Times New Roman",32),
                          bg = "Lightgreen",
                          command = click_btn_1)
button_Start.place(x=480,y=480)

#テキスト入力欄作成
text_Display = tki.Text(width = 50, height = 6, font = ("Times New Roman", 11))
text_Display.place(x = 440,y = 30)

#BooleanVarのオブジェクト用のリスト
#チェック用ボタンのリスト
bvar = [None]*8
cbtn = [None]*8

#チェックリスト
val = tki.IntVar()
for i in range(8):
    cbtn[i] = tki.Radiobutton(root,
                              value = i,
                              variable = val,
                              text = ITEM[i],
                              font = ("Times New Roman", 12),
                              bg = "white")
    cbtn[i].place(x = 440, y = 160 + 40*i)


root.mainloop()