import string
# 读文件，返回字符串
def read_file(file):    
   with open(file, 'r', encoding='utf-8') as f:    
        return f.read()  


# 用空格替换所有符号，切分为列表
def word_list(txt):
    for ch in '!"#$%&()*+,-.:;<=>?@[\\]^_’‘{|}~/':
    #########################Begin############################### 
        txt = txt.replace(ch," ")    #所有符号替换为空格
    #print(txt)
    return txt.split()


    #########################End############################### 

    


# 返回单词数量
def number_of_words(ls):
    #########################Begin############################### 
    word = 0
    for sh in ls:
        if sh.isalnum():
            word += 1
    return word

    #########################End############################### 

if __name__ == '__main__':
    filename = 'mayun.txt'  # 读取的文件名
    text = read_file(filename)  # text为字符串
    words_list = word_list(text)  # 单词的列表
    words_counts = number_of_words(words_list)
    print(f'共有{words_counts}单词')
