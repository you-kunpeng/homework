import math

def square(length, width):
    """计算长方形的面积"""
    ##########################Begin#########################
    square = length * width
    return f"长方形的面积为{square:.2f}"

    ##########################End#########################

if __name__ == '__main__':
    length, width = map(float, input().split())
    geometry = square(length, width)  # 调用判断图形类型的函数
    print(geometry)                          # 输出函数运行结果

