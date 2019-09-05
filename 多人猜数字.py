import random


def write_new(name, count_ci, count_List, avg):
    t = name + ',' + str(count_ci) + ',' + str(count_List) + ',' + str(int(avg))
    with open('猜数字.txt', 'a+', encoding='utf8') as f:
        f.writelines(t + '\n')


def read_old():
    with open('猜数字.txt', 'r', encoding='utf8') as f:
        dict = {}
        A = f.readlines()
        # print(A)
        for i in A:
            record = i.split(',')
            dict[record[0]] = record[1:]
            if name == record[0]:
                print('%s的最好记录:共猜了%s次,最少%s轮猜中,平均%s轮猜中,游戏开始' % (name, record[1], record[2], record[3]))
                list = dict[name]
                return list


def write_old(name, count_ci, count_List, avg):
    with open('猜数字.txt', 'r+', encoding='utf8') as f:
        dict = {}
        lines = f.readlines()
        for i in lines:
            record = i.split(',')
            dict[record[0]] = record[1:]
            if name == record[0]:
                # print('%s的最好记录:共猜对了%s次,最少%s轮猜中,平均%s轮猜中,游戏开始' % (name, record[1], record[2], record[3]))
                dict[name] = [count_ci+int(dict[name][0]), min(count_List,int(record[2])), avg]
    t = name + ',' + str(dict[name][0]) + ',' + str(dict[name][1]) + ',' + str(int(avg))
    with open('猜数字.txt', 'r+', encoding='utf8') as f_w:
        for line in lines:
            if name in line:
                continue
            f_w.write(line)
        f_w.writelines(t)

def guess_ganme(name):
    count = 0
    num = random.randint(1, 10)
    sum = 0
    count_list = []
    count_ci = 0
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
                print("猜对啦!")
                print('本局游戏记录:%s共猜对了%d次,最少%d轮猜中,平均%d轮猜中,游戏开始' % (name, count_ci, count_list[0], int(sum / count_ci)))
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
    return count_ci, count_list[0], int(sum / count_ci)


def user(name):
    with open('猜数字.txt', 'r', encoding='utf8') as f:
        dict = {}
        A = f.readlines()
        # print(A)
        for i in A:
            record = i.split(',')
            # print(record)
            dict[record[0]] = record[1:]
            # print(record[0])
            if name == record[0]:
                list = dict[name]
                t = '%s的最好记录:共猜对了%s次,最少%s轮猜中,平均%s轮猜中,游戏开始' % (name, record[1], record[2], record[3])
                return list, t


if __name__ == '__main__':
    # 判断是不是新用户
    name = input('请输入你的名字:')

    if user(name):
        # user(name)
        print(user(name)[1])
        tup = guess_ganme(name)
        write_old(name, tup[0], tup[1], tup[2])
    else:
        print('%s,你是新用户,开始游戏吧!' % name)
        tup = guess_ganme(name)
        write_new(name, tup[0], tup[1], tup[2])

