import random

result = random.randint(1, 100)

total = 5
print("\t\t欢迎来到猜数字游戏\n您有%d次机会猜对数字并得到彩蛋，数字范围在 0 ~100之间，Left or Right, Make your choice!\n"%(total))

for i in range(0, total):
    ans = input("第%d次尝试，剩余%d次机会："%(i+1, total - i - 1))
    if ans.isspace() or ans == '' or not ans.isdigit() or int(ans) <= 0:
        print("需要输入正整数，尝试机会 - 1")
        continue
    ans = int(ans)
    if ans == result:
        print("恭喜答对，拿好彩蛋：0b10011110101110110100010")
        break
    else:
        if ans > result:
            print("猜大了")
        else:
            print("猜小了")
else:
    print("不好意思，Game Over!Boom~")
