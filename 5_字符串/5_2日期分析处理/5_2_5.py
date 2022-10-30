def name_of_month(current_date):
    """接收一个用8个字符表示日期的字符串为参数，返回这个月份对应的英文单词及其缩写形式。
    @参数 current_date：表示日期，字符串类型
    例如：current_date为20201031，返回值为'October','Oct.'
    # >>> test_date = '20000826'
    # >>> name_of_month(test_date)
    # ('August', 'Aug.')
    # >>> test_date = '19000226'
    # >>> name_of_month(test_date)
    # ('February', 'Feb.')
    # >>> test_date = '19801226'
    # >>> name_of_month(test_date)
    # ('December', 'Dec.')
    # >>> test_date = '19990430'
    # >>> name_of_month(test_date)
    # ('April', 'Apr.')
    """
    # 日期的英文全称：['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December']
    # 日期的英文缩写：September为前四位字母加点，其余月份均为前三位字母加点，如：'Sept.','Jan.'
    ########## Begin ##########
    moths_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October','November', 'December'] 
    month = int(current_date[4:6]) -1
    English_Month = moths_list[month] 
    if month == 8:
        abbreviation = English_Month[:4] +'.'
    else:
        abbreviation = English_Month[:3] +'.'
    return English_Month ,  abbreviation
    ########## End ##########



if __name__ == '__main__':
    CurrentDate = input()
    monthName, monthAbbr = name_of_month(CurrentDate)
    print(f'{int(CurrentDate[4:6])}月英文是{monthName}，缩写为{monthAbbr}')
