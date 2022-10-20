import math   #导入库
def fact(n):   #定义求阶乘函数
    num = 1
    #方法一：用循环的方法求阶乘
    if n == 0:
        num =1
    else:
        for i in range (1,n+1):
            num *=i
    return num
'''
    #方法二：用math库中的factoial函数求阶乘
    num = math.factorial(n)
    return num
    
    #方法三：用递归方法求阶乘
    if n == 0:
        num = 1
    else :
        num = n * fact(n-1)
    return num
'''
def fun(m,n):
    m_factorial =fact(m)
    n_factorial =fact(n)
    m_n_factorial =fact(m-n)
    return m_factorial /(n_factorial * m_n_factorial)

if __name__ == "__main__":
    m =int(input("请输入一个m的值"))
    n  =int(input("请输入一个n的值"))
    if m < n:
        m,n =n,m
    print(int(fun(m,n)))
    
    
    
        
