def leap(current_date):
    """接收一个用8个字符表示日期的字符串为参数，判断这个日期中的年份是否为闰年
    返回值为布尔型。
    @参数 current_date：表示日期，字符串类型
    闰年的判定方法是：能被400整除或能被4整除且同时不能被100整除的是闰年。
    # >>> test_date = '20000426'
    # >>> leap(test_date)
    # True
    # >>> test_date = '19000426'
    # >>> leap(test_date)
    # False
    # >>> test_date = '19990426'
    # >>> leap(test_date)
    # False
    """
    ########## Begin ##########
    if int(current_date) % 400 == 0 or int(current_date) % 4 == 0 and int(current_date) %100 != 0 :
        return True
    else:
        return False

    ########## End ##########


if __name__ == '__main__':
    CurrentDate = input()
    if leap(CurrentDate[:4]):
        print(f'{CurrentDate[:4]}年是闰年')
    else:
        print(f'{CurrentDate[:4]}年不是闰年')
