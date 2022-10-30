def legal_judge(current_date):
    """接收一个用8个字符表示日期的字符串为参数，判定日期的合法性，返回值为布尔型。
    1，3，5，7，8，10，12月各31天，4，6，9，11各30天，闰年2月29天，平年2月28天。
    @参数 current_date：表示日期，字符串类型
    # >>> test_date = '20000426'
    # >>> legal_judge(test_date)
    # True
    # >>> test_date = '19000229'
    # >>> legal_judge(test_date)
    # False
    # >>> test_date = '19990431'
    # >>> legal_judge(test_date)
    # False
    """
    ########## Begin ##########
    moths_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    if leap(current_date):
        moths_list[1] =29
    month = int(CurrentDate[4:6])
    if moths_list[month-1] >= int(current_date[6:8]):
        return True
    else:
        return False
    ########## End ##########

def leap(current_date):
    year = int(current_date[:4])
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

if __name__ == '__main__':
    CurrentDate = input()
    if legal_judge(CurrentDate):
        print(f'{CurrentDate}是合法日期')
    else:
        print(f'{CurrentDate}是非法日期')
