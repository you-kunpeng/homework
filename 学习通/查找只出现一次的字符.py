#查找只出现一次的字符
def one_string(s):   #定义函数
    Value = 1           #赋予判断变量
    for i in range (len(s)):    
        if s.count(s[i]) == 1:
            print(s[i])         #输出只出现一次的的字符串
            Value = 0            
    if Value ==1:
            print("没有只出现一次的的字符串")

            
if __name__ == "__main__":
    s = input("给定任意字符串")
    one_string(s)
    
    
