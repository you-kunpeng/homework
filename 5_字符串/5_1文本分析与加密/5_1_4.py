import string
# 读文件，返回字符串  
def read_file(file):  
    with open(file, 'r', encoding='utf-8') as f:  
        return f.read()

# 用字符串中字符ASCII值的和对26取模为偏移量  
def offset_cal(day):  
    sum_of_ch = 0  
    for c in day:  
        sum_of_ch = sum_of_ch + ord(c)  
    offset = sum_of_ch % 26  
    return offset

def kaisa(txt, number):  
    ###########################Begin###########################
    lower = string.ascii_lowercase  #小写字母
    upper = string.ascii_uppercase  #大写字母
    before = string.ascii_letters
    after = lower[number:] + lower[:number] + upper[number:] +upper[:number]
    table = ''.maketrans(before,after)  #创建映射表
    return txt.translate(table)



    ############################End############################

if __name__ == '__main__':  
    filename = 'mayun.txt'  # 读取的文件名  
    text = read_file(filename)  # text为字符串  
    secret_word = input()  
    offset_number = offset_cal(secret_word)  
    print(kaisa(text, offset_number))  
