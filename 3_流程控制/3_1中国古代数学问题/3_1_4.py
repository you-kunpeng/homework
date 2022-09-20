"""有一座八层宝塔，每一层都有一些琉璃灯，每一层的灯数都是上一层的二倍，
已知共有765 盏琉璃灯，计算并输出每层各有多少盏琉璃灯。
输出为8行，每行都是一个正整数，从上往下数字依次增大，每个数字代表本层宝塔上的琉璃灯数目。
"""

    #################Begin#############################

from itertools import count

for first in count(1,1):
    floors = [first*(2**i) for i in range(8)]
    if sum(floors) == 765:
        for index,value in enumerate(floors,start=1):
            print(value)
        break
    #################End#############################