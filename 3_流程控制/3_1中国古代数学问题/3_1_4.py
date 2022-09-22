#此为程序全部，请全选复制！
#此为程序全部，请全选复制！
#此为程序全部，请全选复制！
#此为程序全部，请全选复制！
#此为程序全部，请全选复制！

from itertools import count

for first in count(1,1):
    floors = [first*(2**i) for i in range(8)]
    if sum(floors) == 765:
        for index,value in enumerate(floors,start=1):
            print(value)
        break
