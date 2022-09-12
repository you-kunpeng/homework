'''
AB 是圆的一条弦，ABC形成一个弓形，在两行中分别输入AB和CD的长度，计算输出弓形面积的大小，结果均严格保留小数点后2位有效数字，应用三角函数和反三角函数时查阅math模块文档或利用自动补全完成。
'''

import math

AB = float(input())  # 弦长度
CD = float(input())  # 弓高度

# 半弦长
AD = AB / 2
# 半径
OA = (AD ** 2 + CD ** 2) / (2 * CD)

# 圆心角
AOB = 2 * math.asin(AD / OA)
################Begin######################
# 弓形所在扇形的面积
pi = math.pi
sector = AOB / (2* pi)*pi * OA **2
# 三角形面积
triangle = 1/2 * OA **2 * math.sin(AOB)
# 弓形面积
area_of_arch = sector - triangle

print(f'{area_of_arch:.2f}')
################End######################