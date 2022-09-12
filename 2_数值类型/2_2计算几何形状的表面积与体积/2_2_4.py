import math

def sphere(radius):
    """接收球的半径，返回球的表面积和体积，圆周率用math.pi"""
    ########################Begin##############################
    area_of_cube = 4 * math.pi * radius**2
    volume_of_cube = 4/3 * math.pi * radius**3
    return f'球的表面积为{area_of_cube:.2f}, 体积为{volume_of_cube:.2f}'

    ########################End##############################

if __name__ == '__main__':
    radius = float(input())
    geometry = sphere(radius)  # 调用判断图形类型的函数
    print(geometry)                          # 输出函数运行结果 