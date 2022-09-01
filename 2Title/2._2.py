'''
试编程实现分两行输入两个非零浮点数，并在4 行中按顺序输出两个数的加、减、乘、除的计算式和计算结果。计算结果str.format()方法保留小数点后3位数字。要求输出与如下示例格式相同，符号前后各有一个空格。
'''

#输入浮点型变量a和b，定义输入函数
#############Begin##############
a = float(input())
b = float(input())
#############End################

#a和b之间进行四则运算并输出
#############Begin################

print(f'{a} + {b} = {a + b:.3f}')
print(f'{a} - {b} = {a - b:.3f}')
print(f'{a} * {b} = {a * b:.3f}')
print(f'{a} / {b} = {a / b:.3f}')

#############End################