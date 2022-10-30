def separate_date(current_date, symbol):
    """接收一个用8个字符表示日期的字符串和一个符号为参数，返回用该符号分隔的日期，字符串类型。
    @参数 current_date：表示日期，字符串类型
    @参数 symbol：分隔符号，字符串类型
    例如传入'20201031'和"/",返回字符串'2020/09/09'
    # >>> test_date = '20000826'
    # >>> sep = '/'
    # >>> separate_date(test_date, sep)
    # '2000/08/26'
    # >>> test_date = '19801226'
    # >>> sep = '-'
    # >>> separate_date(test_date, sep)
    # '1980-12-26'
    """
    ########## Begin ##########
    a = current_date[:4] + symbol + current_date[4:6] + symbol +current_date[6:8]
    return a
    ########## End ##########



if __name__ == '__main__':
    CurrentDate = input()
    sign = input()
    print(separate_date(CurrentDate, sign))
