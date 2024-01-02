"""
语法:
for 临时变量 in 序列
    重复执行的代码1
    重复执行的代码2
    .....
"""
# break:终止循环
str = '今天星期二'
for i in str:
    if i == '星':
        print('遇到星不打印')
        break
    print(i)
# continue:跳过循环
for i in str:
    if i == '星':
        print('遇到星不打印')
        continue
    print(i)

'''
else:循环可以和else配合使用,else下方缩进的代码指的是当循环正常结束之后要执行的代码
'''
print('----------------------------------------------')
# else指的是循环正常结束之后要执行的代码,即如果是break终止循环的情况,else下方缩进的代码将不执行
str = '今天星期二'
for i in str:
    if i == '星':
        print('遇到星不打印')
        break
    print(i)
else:
    print('循环正常结束执行的代码')



print('----------------------------------------------')

# continue是退出当前一次循环,继续下一次循环,所以该循环在continue控制下是可以正常结束的,当循环结束后,则执行了else缩进的代码
str = '今天星期二'
for i in str:
    if i == '星':
        print('遇到星不打印')
        continue
    print(i)
else:
    print('循环正常结束执行的代码')