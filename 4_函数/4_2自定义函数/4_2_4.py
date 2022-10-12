def fabs(x):
    """返回x的绝对值"""
    ######################Begin###############################
    if x >=0:
        return x
    return -x

    ######################End###############################

if __name__ == '__main__':
    x = eval(input())
    return_data = fabs(x)
    print(return_data)
