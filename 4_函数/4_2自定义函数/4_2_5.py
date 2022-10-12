def ceil(x):
    """接受一个浮点数或整数，返回大于或等于该数的最小整数"""
    ######################Begin###############################
    if x > 0:
        if x % int(x) == 0:
            return x
        return int(x)+1
    else:
        if x % int(x) == 0:
            return x
        return int(x)

    ######################End###############################

if __name__ == '__main__':
    x = eval(input())
    return_data = ceil(x)
    print(return_data)
