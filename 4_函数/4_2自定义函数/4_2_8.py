def fsum(iterable):
    """接收一个元素为数值的序列为参数，以浮点数类型返回各元素之和"""
    ######################Begin###############################
    #方法一：
    return float(sum(x))
    #方法二：
    """
    total = 0
    for ele in range(0, len(x)):
        total = total + x[ele]
    return float(total)
    """



    ######################End###############################


if __name__ == '__main__':
    x = list(map(eval, input().split()))
    return_data = fsum(x)
    print(return_data)
