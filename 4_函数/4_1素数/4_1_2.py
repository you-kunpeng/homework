def is_prime(n):
    """判断素数的函数,接收一个正整数为参数，参数是素数时返回True，否则返回False。减小判定区间，减少循环次数，提升效率"""
    #======================Begin=================================
    # 补充你的代码
    if n < 2:
        return False 
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True
    #=======================End================================


def output_prime(number):
    """接收一个正整数为参数，遍历从0到number之间的所有整数
    在一行中输出不大于number的所有素数，每个数字后一个空格，函数无返回值。"""
    #======================Begin=================================
    # 补充你的代码
    for i in range(number+1):
        if is_prime(i):
            print(i,end=" ")
        
            
    #=======================End================================


positive_int = int(input())  
output_prime(positive_int)    
