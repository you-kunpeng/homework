#请全部一起复制
#请全部一起复制
#请全部一起复制
#请全部一起复制
#请全部一起复制
'''
编程实现割圆法计算圆周率，并输出分割不同次数时边数、圆周率值以及计算所得圆周率值与math库中的圆周率值的偏差。
'''

import math

def zu(n):
    ## 假设边长为1
    def f(x): ## 由当前边长，求割后边长
        h = 1 - math.sqrt(1-(x/2)**2)
        return math.sqrt(h**2 + (a/2)**2)

    a = 1  ## 初始边长
    k = 6  ## 初始边数
    for i in range(n):
        a = f(a)
        k *= 2

    return a * k / 2

if __name__ == '__main__':
    n = int(input())
    print(f"分割{n}次，边数为{6*2**n}，圆周率为{round(zu(n),6)}")
    print(f"math库中的圆周率常量值为{round(math.pi,6)}")
