# 转义和print的结束符
'''
转义字符:
    \n: 换行
    \t: 制表符,一个tab(4个空格的距离)
'''

print('hello\nworld')
print('\thello world')

'''
结束符:
    在Python中,print(),默认自带end="\n"这个换行结束符,所以会导致每两个print直接会换行展示,用户可以按需求更改结束符
'''
print('hello',end='\n')
print('world',end='\t')
print('python',end='...')