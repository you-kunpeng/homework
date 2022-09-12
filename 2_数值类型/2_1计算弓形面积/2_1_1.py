'''
AB 是圆的一条弦，ABC形成一个弓形，在两行中分别输入AB和CD的长度，计算并输出该圆的半径，结果均严格保留小数点后2位有效数字，应用三角函数和反三角函数时查阅math模块文档或利用自动补全完成。
'''
from decimal import Decimal
import math

AB = float(input())  # 弦长度 c = float(Decimal(str(a))
CD = float(input())  # 弓高度
############Begin###############
# 半弦长
AD = AB / 2

# 半径

OA = (AD** 2+CD** 2)/(2 * CD)
print("%.2f" % OA)
############End###############
