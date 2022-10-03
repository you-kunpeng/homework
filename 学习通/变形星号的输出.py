width = 1  #设定初始参数
Number_of_grids = 9  #设定每行格数
asterisks = '*'   #定义星号
while width<6:      #循环运行
    print('{0:^{1}}'.format(asterisks, Number_of_grids))
    asterisks += '**'
    width += 1
