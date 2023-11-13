# 数据类型转换

'''
函数 说明
int(x [,base ]) 将x转换为⼀个整数
float(x ) 将x转换为⼀个浮点数
complex(real [,imag ]) 创建⼀个复数，real为实部，imag为虚部
str(x ) 将对象 x 转换为字符串
repr(x ) 将对象 x 转换为表达式字符串
eval(str ) ⽤来计算在字符串中的有效Python表达式,并返回⼀个对象
tuple(s ) 将序列 s 转换为⼀个元组
list(s ) 将序列 s 转换为⼀个列表
chr(x ) 将⼀个整数转换为⼀个Unicode字符
ord(x ) 将⼀个字符转换为它的ASCII整数值
hex(x ) 将⼀个整数转换为⼀个⼗六进制字符串
oct(x ) 将⼀个整数转换为⼀个⼋进制字符串
bin(x ) 将⼀个整数转换为⼀个⼆进制字符串
'''


# 1.float():转换为浮点型
num = 1
print(float(num)) # 1.0
print(type(float(num))) # <class 'float'>

# 2.str():转换为字符串类型
num2 = 10
print(str(num2)) # 10
print(type(str(num2))) # <class 'str'>

# 3.tuple():将一个序列转换为元组
l = [1, 2, 3]
print(tuple(l)) # (1, 2, 3)
print(type(tuple(l))) # <class 'tuple'>

# 4.list():将一个序列转换为列表
t = (1, 2, 3)
print(list(t)) # [1, 2, 3]
print(type(list(t))) # <class 'list'>

# 5.eval():将字符串中的数据转换成python表达式原有类型
str1 = '10'
str2 = '[1, 2, 3]'
str3 = '(1, 2, 3)'

print(type(eval(str1))) # <class 'int'>
print(type(eval(str2))) # <class 'list'>
print(type(eval(str3))) # <class 'tuple'>