import random

name = input('请输入你的名字:')
count = 0
count_ci = 0
num = random.randint(1, 10)
count_list = []
sum = 0
record = []
with open('猜数字.txt','r',encoding='utf8') as f:
    global dict
    dict = {}
    A = f.readlines()
    for i in A:
        record = i.split(',')
        dict[record[0]] = record[1:]
        if name == record[0]:
            print('%s的最好记录:共猜了%s次,最少%s轮猜中,平均%s轮猜中,游戏开始'%(name,record[1],record[2],record[3]))
while True:
    a = int(input('请输入一个1-10的数字:'))
    if a:
        if a < num:
            print('猜小了!')
            count += 1
        elif a == num:
            count += 1
            count_ci += 1
            sum += count
            # print(count)
            count_list.append(count)
            count_list.sort()
            # print(count_list[0])
            s = '%s,猜对了!你一共猜了%d次,最少%d轮猜中,平均%.f轮猜中\n' % (name, count_ci, count_list[0], sum / count_ci)
            print(s)
            p = int(input('是否继续,继续输入:1,退出输入:0'))
            if p == 1:
                count = 0
                num = random.randint(1, 10)
                continue
            else:
                break
        elif a > num:
            print('猜大了')
            count += 1
    else:
        print('输入有误,请重新输入!')
t = name+','+ str(count_ci) +','+str(count_list[0])+','+str(sum / count_ci)
with open('猜数字.txt', 'w', encoding='utf8') as f:
    f.write(t+'\n')
print(t)