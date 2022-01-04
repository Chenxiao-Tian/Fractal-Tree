#uuid_share#  cb781d8a-8a19-40b3-8e59-447690b8a4b4  #
# 1. 导入海龟模块
import turtle 

#turtle.tracer(0) # 去掉注释，海龟暴走

# 海龟颜色表（有些在PyLn中没有效果的可以参照下面链接的RGB值）
# http://gis4g.pku.edu.cn/python-turtle-color-names/
# https://www.tcl.tk/man/tcl8.6/TkCmd/colors.htm

# 2. 生成一只海龟，做一些设定
#t = turtle.Turtle()
#t.pencolor("green")  # 画笔颜色
#t.pensize(3)  # 画笔粗细


# 3. 用海龟作图
import turtle as p
import random
import math
def moon(x,y,r):
    p.penup()
    p.goto(x,y)
    p.pendown()
    p.pensize(15)
    p.begin_fill()
    p.color("yellow","gold")
    p.circle(r)
    p.end_fill()
    p.penup()
    p.color('orange','orange')
    p.goto(200,135)
    p.begin_fill()
    p.pendown()
    p.circle(15)
    p.end_fill()
    p.penup()
    p.goto(0,0)
def star(count):
    p.hideturtle()
    p.speed(500)
    p.pensize(2)
    for i in range(count):
        r = random.random()
        g = random.random()
        b = random.random()
        s=random.randint(0,5)
        if s==0:
            p.color("orange","orange")
        elif s==1:
            p.color("yellow","yellow")
        elif s==2:
            p.color("gold","gold")
        elif s==3:
            p.color("red","red")
        else:
            p.color("blue","blue")
        p.pu()
        p.goto(random.randint(-350, 350), random.randint(1, 270))
        p.pd()
        starsize = random.randint(10, 14)
        for _ in range(5):
            p.begin_fill()
            p.forward(starsize)  
            p.right(144) 
            p.end_fill()
def snowground(count):
    p.hideturtle()
    p.speed(500)
    for i in range(count):
        p.pensize(random.randint(5, 10))
        x = random.randint(-400, 350)
        y = random.randint(-280, -1)
        r = -y / 280
        g = -y / 280
        b = -y / 280
        p.pencolor("snow")
        p.penup()  
        p.goto(x, y)  
        p.pendown()  
        p.forward(random.randint(40, 100)) 
def main():
    t=p.Turtle()
    ts = t.getscreen()
    ts.bgcolor("black")
    star(60)
    snowground(250)
    p.mainloop()
moon(200,105,50)  
main()
printer = turtle.Turtle()
printer.hideturtle()
printer.penup()
printer.back(200)
printer.color("gold")
printer.penup()
printer.goto(83,220)
p.pendown()
printer.write("雪晴春夜\n\n", align="right", font=("隶书", 64, "bold"))
import turtle as T
import random
import time
def Tree(branch, t):
    if branch > 3 :
        if 8 <= branch <= 12:
            s= random.randint(0,2)
            if s == 0:
                v=random.randint(0,0)
                if v==0:
                    x=random.randint(9,10)
                    t.right(90)
                    t.color("darkgreen")
                    t.forward(x)
                    t.pensize(1)
                    t.color("snow")
                    t.pensize(0.5)
                    t.backward(x)
                    t.left(180)
                    t.color("darkgreen")
                    t.forward(x)
                    t.pensize(1)
                    t.color("snow")
                    t.pensize(0.5)
                    t.backward(x)
                    t.right(90)
                t.color('red') 
                t.pensize(min(branch / 3,0.55))
            elif s==1 :
                v=random.randint(0,0)
                if v==0:
                    x=random.randint(9,10)
                    t.right(90)
                    t.color("darkgreen")
                    t.forward(x)
                    t.pensize(1)
                    t.color("snow")
                    t.pensize(0.5)
                    t.backward(x)
                    t.left(180)
                    t.color("darkgreen")
                    t.forward(x)
                    t.pensize(1)
                    t.color("snow")
                    t.pensize(0.5)
                    t.backward(x)
                    t.right(90)
                t.color('red') 
                t.pensize(min(branch / 3,0.55))
        elif branch < 8:
            if random.randint(0, 1) == 0:
                v=random.randint(0,0)
                if v==0:
                    x=random.randint(9,10)
                    t.right(90)
                    t.color("darkgreen")
                    t.forward(x)
                    t.pensize(1)
                    t.color("snow")
                    t.pensize(0.5)
                    t.backward(x)
                    t.left(180)
                    t.color("darkgreen")
                    t.forward(x)
                    t.pensize(1)
                    t.color("snow")
                    t.pensize(0.5)
                    t.backward(x)
                    t.right(90)
                t.color('red')
                t.pensize(min(branch / 3,0.55))
               
            else:
                v=random.randint(0,0)
                if v==0:
                    x=random.randint(9,10)
                    t.right(90)
                    t.color("darkgreen")
                    t.forward(x)
                    t.pensize(1)
                    t.color("snow")
                    t.pensize(0.5)
                    t.backward(x)
                    t.left(180)
                    t.color("darkgreen")
                    t.forward(x)
                    t.pensize(1)
                    t.color("snow")
                    t.pensize(0.5)
                    t.backward(x)
                    t.right(90)
                t.color('red')  
                t.pensize(min(branch / 3,0.55))
                t.color('red')  
            t.pensize(branch / 2)
        else:
            t.color('sienna')  
            t.pensize(branch / 10) 
        t.forward(branch/1.8)
        a = 1.5 * random.random()
        b= 1.5 * random.random()
        t.right(20 * a)
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20* a)
      
        t.pensize(branch/50)
        t.color("snow")
        t.backward(branch/1.8)     
def leaves(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        c=random.randint(0,6)
        t.color('green')  #
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)
def flower(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        c=random.randint(0,6)
        t.color('red')  
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)
def snow(m, t):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        t.up()
        t.forward(b)
        t.left(90)
        t.forward(a)
        t.down()
        c=random.randint(0,6)
        t.color('snow') 
        t.circle(1)
        t.up()
        t.backward(a)
        t.right(90)
        t.backward(b)

t = T.Turtle()
t.hideturtle()  
t.getscreen().tracer(5, 0)
t.left(90)
t.up()
t.backward(150)
t.down()
t.color('sienna')
ts = t.getscreen()
Tree(75, t)
#leaves(200, t)
flower(200,t)
#snow(200,t)


# 4. 结束作图
t.hideturtle()
turtle.update()

# 5. 设置背景，收尾
#ts = turtle.getscreen()
#ts.bgcolor("lime")

turtle.done()