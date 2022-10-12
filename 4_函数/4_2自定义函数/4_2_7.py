def factorial(n):
    """接收一个非负整数n为参数，返回n的阶乘，0的阶乘值为1"""
    ######################Begin###############################
    x = 1
    for i in range(1,n+1):
        x *= i   
    return x

    ######################End###############################

if __name__ == '__main__':
    x = int(input())
    return_data = factorial(x)
    print(return_data)

