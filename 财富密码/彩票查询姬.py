str0 = input('请输入彩票开奖数字')
#以‘，’为间隔分割输入字符串，然后转化为int型
lottery0 = str0.split(',')
lottery0 = [int(lottery0[i]) for i in range(len(lottery0))]
assert len(lottery0) == 7
lottery1 = [2,4,16,18,22,4,6]
lottery2 = [3,8,10,25,30,8,11]
lottery3 = [3,6,17,19,31,4,6]
lottery4 = [5,11,19,24,25,8,10]
lottery5 = [7,8,12,21,24,9,11]
lotterybuy = [lottery1,lottery2,lottery3,lottery4,lottery5]
for i in range(5):
    hits1 = 0
    hits2 = 0
    for blue in range(5):
        if lotterybuy[i][blue] in lottery0[:5]:
            hits1 += 1
    for red in range(5,7):
        if lotterybuy[i][red] in lottery0[5:]:
            hits2 += 1
    if hits1 + hits2 == 7:
        print('中了一等奖！')
    elif hits1 == 5 and hits2 == 1:
        print('中了二等奖')
    elif hits1 == 5 and hits2 == 0:
        print('中了1w元')
    elif hits1 == 4 and hits2 == 2:
        print('中了3k元')
    elif hits1 == 4 and hits2 == 1:
        print('中了300元')
    elif hits1 == 3 and hits2 == 2:
        print('中了200元')
    elif hits1 == 4 and hits2 == 0:
        print('中了100元')
    elif hits1 + hits2 == 4:
        print('中了15元')
    elif(hits1 + hits2 == 3) or hits2 == 2:
        print('中了5元')
    else:
        print('第',i+1,'只彩票白给了')
input()
