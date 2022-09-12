import math

def cube(length, width, height):
    """计算长方体的表面积和体积"""
    ########################Begin##############################
    area_of_cube = length * width * 2 + width * height * 2 + length * height * 2
    volume_of_cube = length * width * height
    return f'长方体的表面积为{area_of_cube:.2f}, 体积为{volume_of_cube:.2f}'
    ########################End##############################

if __name__ == '__main__':
    length, width, height = map(float, input().split())
    geometry = cube(length, width, height)  # 调用判断图形类型的函数
    print(geometry)                          # 输出函数运行结果

