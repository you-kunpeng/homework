"""
在同一行内输入用空格分隔的两个整数，代表头和脚的数量，计算并输出笼中各有多少只鸡和兔，
如无解则输出“Data Error!”，函数无返回值。
输入：35 94
输出：有23 只鸡，12 只兔
输入：100 5
输出：Data Error!
"""
head,feet = map(int, input().split()) #读入以空格分隔的两个整数，表示头和脚的数量
##############Begin#####################

m = (4*head - feet)/2
n = (feet - 2 * head)/2
if (round(m-int(m),4)) > 0 and  (round(m-int(n),4)) >0:
    print("Data Error!")
elif m < 0 or n < 0 :
    print("Data Error!")
else:
    m = int(m)
    n = int(n)
    print(f"有{m}只鸡，{n}只兔")







##############End#####################