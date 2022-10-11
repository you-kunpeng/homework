def is_prime(n): 
    """判断素数的函数,接收一个正整数为参数，返回值是布尔类型。参数是素数时返回True，否则返回False"""
    #==================Begin=================================
    # 补充你的代码
    if n < 2:
        return False 
    for i in range(2,n):
        if n % i == 0:
            return False
    else:
        return True
    
    #===================End================================


positive_int = int(input())      # 输入一个正整数
if is_prime(positive_int):
    print(f'{positive_int}是素数') 
else:
    print(f'{positive_int}不是素数')
