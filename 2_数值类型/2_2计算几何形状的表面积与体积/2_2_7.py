import math

def tri_prism(side, height):
    """接收正三棱柱的底边长和高，返回正三棱柱的表面积和体积"""
    ########################Begin##############################
    area_of_cube = 2 * (3 ** 0.5/4 * side * side) + 3 * side * height
    volume_of_cube = (3 ** 0.5/4 * side * side) * height
    return f'正三棱柱的表面积为{area_of_cube:.2f}, 体积为{volume_of_cube:.2f}'

    ########################End##############################

if __name__ == '__main__':
    side, height = map(float, input().split())
    geometry = tri_prism(side, height)  # 调用判断图形类型的函数
    print(geometry)                         # 输出函数运行结果