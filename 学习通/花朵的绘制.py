#导入库
import turtle
import random
#编辑花瓣个数
Number_of_circles = int(input("请输入花瓣个数"))
Number_of_divisions = 360 / Number_of_circles
for i in range(Number_of_circles):
    #创建颜色列表
    Color_list = ['black', 'grey', 'rosybrown', 'lightcoral', 'maroon', 'red', 'mistyrose','coral','sienna','yellow','orange','green','blue','lime','teal','indigo']
    Random_color = random.choice(Color_list)
    #绘画
    turtle.pencolor(Random_color)
    turtle.circle(100)
    turtle.left(Number_of_divisions)
