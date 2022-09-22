import random

def monte_carlo_pi(num):
    """接收正整数为参数，表示随机点的数量，利用蒙特卡洛方法计算圆周率
    返回值为表示圆周率的浮点数"""

  

    N = 0 # 变量N用于统计落在圆内的试验点的个数
    for i in range(int(times)):
        x = random.random() # 获取0-1之间的随机数
        y = random.random() # 获取0-1之间的随机数
        d = (x-0.5)**2+(y-0.5)**2 # 计算试验点到圆心的欧式距离的平方
        if d<=0.5**2: # 通过比较试验点到圆心的欧式距离与圆半径的大小，判断该点是否在圆内
            N+=1
        else:
            pass
    return  4*N/times
    


if __name__ == '__main__':
    sd = int(input())             #读入随机数种子
    random.seed(sd)               #设置随机数种子
    times = int(input())          # 输入正整数，表示产生点数量
    print(monte_carlo_pi(times))  # 输出圆周率值，浮点数
