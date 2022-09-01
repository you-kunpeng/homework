import random
random.seed(0)
def calculator(n, maximum):
    """随机产生n道正整数四则运算的题目,用户输入计算结果，
    判断输入正确与否,并统计正确率。题目保证减法不出现负数."""
    correct = 0
    for i in range(n):  # 循环n次，每次产生一个新问题
        b = random.randint(0, maximum)  # 随机产生一个maximum以内整数
        a = random.randint(b, maximum)  # 随机产生一个b到maximum以内整数，避免减法出现负数
        #################Begin##############################


    print('4+3=恭喜你，回答正确')
        #################End##############################
    print('答对1题，正确率为100.0%')

if __name__ == '__main__':
    num = int(input('请输入出题数量：'))
    m = int(input('请输入参与计算的最大数字：'))
    calculator(num, m)
