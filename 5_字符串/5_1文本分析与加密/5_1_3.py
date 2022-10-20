import string

# 用字符串中字符ASCII值的和对26取模为偏移量
def offset_cal(day):
    #########################Begin############################### 
    sum_of_ch = 0
    for c in day:
        sum_of_ch = sum_of_ch +ord(c)
    offset = sum_of_ch % 26
    return offset


    #########################End############################### 


if __name__ == '__main__':
    secret_word = input()
    offset_number = offset_cal(secret_word)
    print(offset_number)
