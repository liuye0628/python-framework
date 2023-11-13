# 格式化输出: 即按照一定的格式输出内容

'''
格式符号 转换
%s 字符串
%d 有符号的⼗进制整数
%f 浮点数
%c 字符
%u ⽆符号⼗进制整数
%o ⼋进制整数
%x ⼗六进制整数（⼩写ox）
%X ⼗六进制整数（⼤写OX）
%e 科学计数法（⼩写'e'）
%E 科学计数法（⼤写'E'）
%g %f和%e的简写
%G %f和%E的简写

技巧
    ①%06d，表示输出的整数显示位数，不⾜以0补全，超出当前位数则原样输出
    ②%.2f，表示⼩数点后显示的⼩数位数。
'''

age = 18
name = '刘备'
weight = 60.0
stu_id = 1

# 我的名字是刘备
print('我的名字是%s' % name)
# 我的学号是0001
print('我的学号是%04d' % stu_id)
# 我的体重是60.00公斤
print('我的体重是%.2f公斤' % weight)
# 我的名字是刘备,今年18岁了
print('我的名字是%s,今年%d岁了' % (name, age))
# 我的名字是刘备,明年19岁了
print('我的名字是%s,明年%d岁了' % (name, age+1))

'''
f-格式化字符串 Python3.6中新增的格式化方法
'''
print(f'我的名字是{name},明年{age+1}岁了')