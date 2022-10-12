def lcm(a, b):
    """接收两个正整数为参数，以整数类型返回两个数的最小公倍数"""
    ######################Begin###############################
    x = a * b
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return int(x / b)

    ######################End###############################

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    return_data = lcm(a,b)
    print(return_data)
