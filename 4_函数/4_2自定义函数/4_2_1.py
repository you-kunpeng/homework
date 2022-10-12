def pow(x, n):  # 幂运算函数
    """接收一个数字x和一个整数n为参数,返回x的n次幂的结果的浮点数类型
    要求使pow(1.0, x) 和 pow(x, 0.0) 总是返回 1.0"""
    #########################Begin############################### 
    Power = x ** n 
    return Power

    #########################End############################### 



if __name__ == '__main__':
    x = float(input())
    n = int(input())
    return_data = pow(x,n)
    print(return_data)
