#********* Begin *********#
import turtle

Bob = turtle.Turtle()
turtle.pencolor('red')
turtle.fd(200)
turtle.left(120)
turtle.fd(200)
turtle.left(120)
turtle.fd(200)
turtle.left(120)
turtle.fd(100)
turtle.begin_fill()#准备开始填充图形；
turtle.pencolor('blue')

turtle.left(60)
turtle.fd(100)
turtle.left(120)
turtle.fd(100)
turtle.left(120)
turtle.fd(100)

turtle.fillcolor('yellow')
turtle.end_fill()#填充完成；

#********* End *********#
#保存屏幕图片
ts = turtle.getscreen()
ts.getcanvas().postscript(file="Python/src1/py1-2/yourimg/sj.ps")
