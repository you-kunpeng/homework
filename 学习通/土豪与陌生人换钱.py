Rich_total_money = 0              #定义富豪给钱总初始   
Stranger_total_money = 0                #定义陌生人给钱总初始
"""分别计算30天富豪与陌生人赚的钱"""
for i in range(1,31):
    Rich_total_money += 100000
    Stranger_total_money += 0.01 * 2**(i-1)
print(f"富豪赚的钱{Stranger_total_money}，陌生人赚的钱{Rich_total_money}  ")
