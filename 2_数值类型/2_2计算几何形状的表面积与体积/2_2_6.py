import math

def cone(radius, height):
    """接收圆锥的底面半径和高，返回圆锥的表面积和体积，圆周率用math.pi"""
    ########################Begin##############################
    area_of_cube = math.pi * radius *(radius + math.sqrt(radius ** 2 + height ** 2))
    volume_of_cube = 1/3 * math.pi * height * radius  **2
    return f'圆锥的表面积为{area_of_cube:.2f}, 体积为{volume_of_cube:.2f}'

    ########################End##############################

if __name__ == '__main__':
    radius, height = map(float, input().split())
    geometry = cone(radius, height)  # 调用判断图形类型的函数
    print(geometry)                          # 输出函数运行结果