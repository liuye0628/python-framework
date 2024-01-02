"""
语法:
while 条件:
    条件成立重复执行的代码1
    条件成立重复执行的代码2
    ......
"""

# 需求:计算1-100偶数累加和
# 方式一: 条件判断和2取余数为0则累加计算(推荐)
i = 1
result = 0
while i <= 100:
    if i % 2 == 0:
        result += i
    i = i + 1
print(result)


# 方式二: 计数器控制增量为0
i = 0
result = 0
while i <= 100:
    result += i
    i = i + 2
print(result)

"""
break:终止此循环
continue:退出当前一次循环继而执行下一次循环

"""
# 比如吃苹果,在吃的过程中,吃完第三个就吃饱了,则不需要再吃第四个和第五个苹果,就可以用break控制循环流程
i = 1
while i <= 5:
    if i == 4:
        print(f'吃饱了不吃了')
        break
    print(f'吃了第{i}个苹果')
    i += 1

# 比如吃苹果,在吃到第三个吃出一个大虫子,这个苹果就不吃了,开始吃第四个苹果,就可以用continue控制循环流程
i = 1
while i <= 5:
    if i == 3:
        print(f'大虫子,第{i}个不吃了')
        # 在continue之前一定要修改计数器,否则会进入死循环
        i += 1
        continue
    print(f'吃了第{i}个苹果')
    i += 1

"""
while嵌套循环应用:打印九九乘法表
"""
i = 1;
while i < 10:
    j = 1
    while j <= i:
        print(f'{i}*{j}={i*j}', end='\t')
        j += 1
    print()
    i += 1
