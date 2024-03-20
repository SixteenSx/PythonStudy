# a = 100
# print(type(a))
#
# # b = "hello world"
# # b = 'hello world'
# # b= '''hello world'''
# b="""hello world"""
# print(type(b))
#
# # text = "Sx是世界上最\"厉害\"的人"
# text = 'Sx是世界上最"厉害"的人'
# print(text)
# # '''作用 可以字符串换行
# text2 = '''你好
#             我我我我我我我哦我我我我'''
# # f-string
# name = "Sx"
# age = "24"
# print(f"my name is {name} ,I'm {age} years old")
# a = 1
# b = 2
# print(F"a+b = {a+b}")






# 索引
text = 'Sx是世界上最"厉害"的人'
print(text[0])
print(text[2])
# -1最后一个
print(text[-1])
# 切片
print(text[0:3])
print(text[5:0:-1])
print(text[5:0:-2])

# 常见操作
# 没找到返回-1
print(text.find("x"))
# index 和 find一样 没找到会报错
print(text.index("x"))
# 出现次数
print(text.count("x"))
# replace替换
print(text.replace("x","m"))
# split切分
a = "hello,world"
print(a.split(","))
# cap
print(a.capitalize())


