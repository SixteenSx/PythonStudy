# # 在控制台打印你好 世界
# print("hello world")
#
#
#
#
# # 变量
# # 变量名 = 变量值      =：赋值符号
# xiaohong = 7
# xiaoming = 2
# xiaohuang = 4
#
# print(xiaohong+xiaoming)
# print(xiaoming+xiaohuang)
#
# # 查看变量类型
# a=3.1415926
# b = "你好 世界 hello world"
# c = [10,20,30]
# d = False
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
#
# # 格式化输出
# age = 10
# name = "HQ"
# score = 99.9
# # .1f表示保留一位小数
# print("我叫%s，今年%d岁,考了%.1f分" %(name,age,score))
#
# # 其他格式化输出
# print("我叫{}，\n我今年{}，\n我考了{}".format(name,age,score))
#
# # 换行输出
# print("sdsacdcdsa\nndjskabhsjbchaajs")
#
# # 练习
# sname = "hq"
# sqq = "276529744"
# stel = "191028xxxxxx"
# sadress = "锦城学院"
#
# print("========我的名片========\n姓名：{}\nQQ：{}\n手机号：{}\n公司地址：{}\n======================".format(sname,sqq,stel,sadress))







# 输入
#
# a = input("请输入内容")
# print(type(a))
# print("您输入的内容是{}".format(a))

# 运算
# a = 10
# b = 20
# print(a+b)
# print(a**b)
# print(a//b)

# 数据类型转换
# a = 123
# print(type(a))

# a = input("请输入")
# a = eval(a)
# print(type(a))

a=1.35
print(type(a))
a = int(a*100)
print(type(a))
a = int(a/100)
print(type(a))