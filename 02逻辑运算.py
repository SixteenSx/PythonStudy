# a = 10
# b = 20
# # 判断
# print( a > b or b != a)
#
# age = 14
# if age >= 18:
#     print("可以进入网吧")
# else:
#     print("小屁孩快努力长大，就可以进网吧了")
#
#
# score = 100
# if score >= 90:
#     print("非常优秀")
# elif score >= 80 and score <= 90:
#     print("优秀")
# elif score <80 and score >= 70:
#     print("还行")
# elif score <70 and score >= 60:
#     print("及格")
# else:
#     print("小辣鸡")






# if嵌套


# 去火车站坐火车，有票进站，没票不进  安检  刀>10

# piao = 1
# knife = 9

# # 错误示范
# if piao == 1:
#     print("进入火车站")
# elif knife < 10:
#     print("进入火车站")
# else:
#     print("请买票")

# if piao == 1:
#     print("进入火车站")
#     if knife <10:
#         print("可以进入")
#     else:
#         print("安检未通过")
# else:
#     print("没有票，无法进入")








# 循环语句

# i = 0
#
# while 1<100:
#     i += 1
# print("sorry, I didn't understand{}".format(i))

# i = 1
#
# while True:
#     i += 1
#     if i == 5:
#         break
#     print("sorry{}".format(i))


# 1-100 累计和
# i = 1
# sum = 0
# while i <= 100:
#     sum = sum + i
#     i += 1
# print("1~100累积和为:%d" % sum)

# 1-100 偶数累积和
# a = 1
# sum = 0
# while a <= 100:
#     if a % 2 == 0:
#         sum = sum + a
#     a += 1
#
# print("1-100偶数和为{}".format(sum))




# for循环 break continue

# name = "Sx"
# for i in name:
#     print(i)
#
# for i in range(0,10000):
#     if i == 5:
#         # break跳出循环
#         # break
#         # continue结束当次循环
#         continue
#     print("sorry{}".format(i))



# 练习
# 1.从一台电脑输入要出的拳 ---剪刀（1）、石头（2）、布（3）
# 2.电脑 随机 出拳
# 3.比较胜负

# import random
#
# a = random.randint(1,3)
# b = input("剪刀（1）、石头（2）、布（3）、请出拳：")
#
# if a == 1 and b == 3:
#     print("win，对方出拳：{}".format(b))
# elif a == 2 and b == 1:
#     print("win，对方出拳：{}".format(b))
# elif a == 3 and b == 2:
#     print("win，对方出拳：{}".format(b))
# elif b == a:
#     print("平局，对方出拳：{}".format(b))
# else:
#     print("defeat，对方出拳：{}".format(b))


# 参考答案

# 参考答案有问题/已解决
# player = int(input("请输入您要出的拳：石头1/剪刀2/布3:")) //必须要转换输入类型
import random
a = random.randint(1,10)
print(a)

player = int(input("请输入您要出的拳：石头1/剪刀2/布3:"))
computer = random.randint(1,3)
print(computer)

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("玩家胜利～")
elif player == computer:
    print("平局")
else:
    print("玩家失败～")



