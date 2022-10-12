def floor(x):
    """接受一个浮点数或整数，返回不大于该数的最大整数"""
    ######################Begin###############################
    if x % int(x) == 0:
        return x
    else:
        if x > 0:
            return int(x)
        else:
            return int(x)-1

    ######################End###############################
    
if __name__ == '__main__':
    x = eval(input())
    return_data = floor(x)
    print(return_data)
