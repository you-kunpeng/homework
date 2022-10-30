def days_of_month(current_date):
    """接收一个用8个字符表示日期的字符串为参数，计算这个日期中的月份有多少天？返回值为整型，
    表示当前月份天数。
    @参数 current_date：表示日期，字符串类型
    # >>> test_date = '20000826'
    # >>> days_of_month(test_date)
    # 31
    # >>> test_date = '19000226'
    # >>> days_of_month(test_date)
    # 28
    # >>> test_date = '19800226'
    # >>> days_of_month(test_date)
    # 29
    # >>> test_date = '19990430'
    # >>> days_of_month(test_date)
    # 30
    """
    ########## Begin ##########
    moths_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    if leap(current_date):
        moths_list[1] =29
    month = int(CurrentDate[4:6])
    return moths_list[month-1]
    
    ########## End ##########

def leap(current_date):
    year = int(current_date[:4])
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

if __name__ == '__main__':
    CurrentDate = input()
    days = days_of_month(CurrentDate)
    print(f'{CurrentDate[:4]}年{int(CurrentDate[4:6])}月有{days}天')
