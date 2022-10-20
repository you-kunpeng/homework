import string
# 读文件，返回字符串  
def read_file(file):  
    ##################Begin##################
    with open(file,'r',encoding='utf-8') as f:
        return f.read()
    ###################End###################

# 返回大写字母、小写字母、数字、空格和其他字符的数量  
def classify_char(txt):  
    ##################Begin##################
    upper,lower,digit,space,other = 0,0,0,0,0
    for ch in txt:
        if ch.islower():
            lower = lower + 1
        elif ch.isupper():
            upper = upper + 1
        elif ch.isnumeric():
            digit = digit + 1
        elif ch.isspace():
            space = space + 1
        else:
            other = other + 1
    return upper,lower,digit,space,other




    ###################End###################

if __name__ == '__main__':  
    filename = 'mayun.txt'  # 读取的文件名  
    text = read_file(filename)  # text为字符串  
    print(*classify_char(text))  
