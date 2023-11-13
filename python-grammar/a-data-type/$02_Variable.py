# 变量

'''
定义变量
    变量名 = 值
'''

today = "Monday"
print(today)

'''
    标识符命名:
        ·由数字,字母和下划线组成
        ·不能数字开头
        ·不能使用内置关键字
        严格区分大小写

'''

'''
    数据类型
        ①整型: int
        ②浮点型: float
        ③字符型: str
        ④布尔型: bool
        ⑤元组: tuple
        ⑥集合: set
        ⑦字典: dict
        ⑧列表: list
'''


a = 1   # int -- 整型
print(type(a))

b = 1.1 # float --浮点型
print(type(b))

c = 'hello world' # str --字符串,特点:数据都要带引号
print(type(c))

d = True # bool --布尔型:True和False
print(type(d))

e = [1, 2, 3] # list --列表
print(type(e))

f = (1, 2, 3) # tuple --元组
print(type(f))

g = {1, 2, 3} # set --集合
print(type(g))

h = {'name':'刘备', 'age':18} # dict --字典:键值对
print(type(h))

