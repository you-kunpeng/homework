"""有一堵十尺厚的墙，两只老鼠从两边向中间打洞。大老鼠第一天打洞一尺，小老鼠也是打洞一尺。
大老鼠每天的打洞进度是前一天的一倍，小老鼠每天的进度是前一天的一半。计算并输出它们几天可以相逢，
相逢时各打了多少尺。
输入格式：输入1 个整数，代表墙的厚度，单位为尺
输出格式：
第一行输出1 个整数，表示相遇时所需的天数
第二行输出2 个浮点数，分别为小鼠和大鼠打洞的距离，单位为尺，保留小数点后1 位数字。
"""
wall = int(input()) #墙壁的厚度
rat, mouse, day, time = 1, 1, 0, 1 #大鼠速度、小鼠速度、天数、当天工作时长（1表示工作一整天）
distance_of_rat, distance_of_mouse = 0, 0 #大鼠路程、小鼠的路程
while wall > 0:
################Begin#######################
    
    wall = wall - rat - mouse
   
    if wall  <=0:   
        wall = wall + rat + mouse
        x = wall /(rat + mouse)
        distance_of_rat +=   rat * x
        distance_of_mouse +=  mouse * x
        wall = wall - rat - mouse
        day += 1 
        
    else:
        distance_of_rat +=   rat
        distance_of_mouse +=  mouse
        day += 1 
        rat = 2 * rat
        mouse = 1/2 * mouse



################End#######################
print(day)
print(round(distance_of_mouse, 1), round(distance_of_rat, 1)) #使用round函数来保留小数点后一位