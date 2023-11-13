# 运算符


'''
①算术运算符: + - * /(除) //(整除) % **(指数) ()
优先级:()高于**高于* / // % 高于 + -
'''
print(9 / 4)
print(9 // 4)


'''
②赋值运算符: = += -= *= /= //= %= **=
'''
a = 10
a += 1
print(a)
# 多个变量赋值
num1, float1, str1 = 10, 10.0, 'hello world'
print(num1)
print(float1)
print(str1)
# 多个变量赋相同值
t1 = t2 = 100
print(t1)
print(t2)
# 注意:先算复合赋值运算符右面的表达式,再算复合赋值运算
b = 10
b *= 1 + 2
print(b) # 30

'''
③关系运算符: == != > < >= <=
'''
c = 1
d = 2
print(c == d)

'''
④逻辑运算符: and or not
'''
e = 0
f = 1
h = 2
print((e < f) and (f < h)) # True
print((e > f) or (f > h)) # False
print(not e > h) # True

# 数字之间的逻辑运算
# and运算符,只要一个值为0,结果为0,否则结果为最后一个非0数字
print( e and f)
print( f and h)
print( h and f)

# or运算符,只有所有值为0结果才为0,否则结果为第一个非0数字
print(e or f)
print(f or h)
print(h or f)
