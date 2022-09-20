'''
输入一个正整数n，使用拉马努金法公式计算思加n次时的圆周率值。
'''
import math


def ramanujan_of_pi(n):
    """接收一个正整数n为参数，用拉马努金公式的前n项计算圆周率并返回。"""
    ################Begin#######################
    x=0
    for k in range(0,10):
        x=x+(2*math.sqrt(2)/9801)* \
        (math.factorial(4*k)*(1103+26390*k))/(math.pow(math.factorial(k),4) \
        *math.pow(396,4*k))
    pi = 1/x
    ################End#######################
    return pi


if __name__ == '__main__':
    n = int(input())                
    cal_pi = ramanujan_of_pi(n)  
    print(cal_pi)                    # 输出函数运行结果
