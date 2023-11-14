# 三目运算符也叫三元运算符或三元表达式
'''
语法: 条件成立执行的表达式 if 条件 else 条件不成立执行的表达式
'''

# 需求:使用input输入a,b,求最大

a = int(input('请输入a:'))
b = int(input('请输入b:'))
# c = a if a >= b else b
print(f'max:{a if a >= b else b}')