"""
字符串:Python中最常用的数据类型,创建有两种方式:
    一组引号字符串 name='Tom' name="Tom"
    三引号字符串(支持换行) name='''Tom''' name="\"\"Tom"\"\"

"""
# 1.下标:又称索引,就是编号,下标的作用就是通过下标可以快速找到对应的数据,注意:下标从0开始
name = 'abcdefg'
print(name[0])
print(name[1])
print(name[2])

# 2.切片:是指对操作的对象截取一部分的操作,字符串,列表,元组都支持切片操作
'''
语法:序列[开始位置下标:结束位置下标:步长]
注意:
    ①不包含结束位置下标对应的数据,正负整数均可(左闭右开)
    ②步长是选取间隔,正负整数均可,默认步长为1
'''
str = '012345678'
# 正数测试
print(str[2:5:1]) # 234
print(str[2:5:2]) # 24
print(str[2:5]) # 234
print(str[:5]) # 01234 --如果不写开始,默认从0开始选取
print(str[2:]) # 2345678 --如果不写结束,默认选取到最后
print(str[:]) # 012345678 --如果不写开始和结束,表示选取所有
# 负数测试
print(str[::-1]) # 876543210 --如果步长为负数,表示倒序选取
print(str[-4:-1]) # 567 --下标-1表示最后一个数据,依次向前类推
# 终极测试
print(str[-4:-1:1]) # 567
print(str[-4:-1:-1]) # 不能选取出数据:从-4开始到-1结束,选取方向为从左到右,但是-1步长:从右向左选取(如果选取方向与步长的方向冲突,则无法选取数据)
print(str[-1:-4:-1]) # 876


# 3.常用操作方法:字符串的常用操作方法有查找,修改和判断三大类
'''
①查找:所谓字符串查找方法即是查找子串在字符串中的位置或出现的次数
    ·find():检测某个子串是否包含在这个字符串中,如果在,返回这个子串开始的位置下标,否则返回-1
        语法:字符串序列.find(子串,开始位置下标,结束位置下标)  --注意:开始位置和结束位置下标可以省略,表示在整个字符串序列中查找
    ·index():检测某个子串是否包含在这个字符串中,如果在,返回这个子串开始的位置下标,否则则报异常
        语法:字符串序列.index(子串,开始位置下标,结束位置下标) --注意:开始位置和结束位置下标可以省略,表示在整个字符串序列中查找
    ·rfind():和find()功能相同,但查找方向从右侧开始
    ·rindex():和index()功能相同,但查找方向从右侧开始
    ·count():返回某个子串在字符串中出现的次数
'''
str1 = "hello world java python"
a = str1.find('java')
print(a)
print(str1.rfind('java'))
print(str1.find('scala')) # -1
print(str1.find('o',5,8))

print(str1.index('java'))
# print(str1.index('scala')) # 报错
print(str1.index('o',5,8))
print(str1.count('o'))
print(str1.count('scala')) # 0

'''
②修改:所谓字符串修改,指的是通过函数的形式修改字符串中的数据
    ·replace():替换
        语法:字符串序列.replace(旧子串,新子串,替换次数) --注意:如果替换次数超出子串出现次数,则替换次数为该子串出现次数
        数据按照是否能直接修改分为可变类型和不可变类型两种,字符串类型修改的时候不能改变原有字符串,属于不能直接修改的数据类型,即是不可变类型
    ·split():按照指定字符分割字符串
        语法:字符串序列.split(分割字符,num) --注意:num表示的是分割字符出现的次数,即将来返回数据的个数为num+1个
        如果分割字符是原有字符串中的子串,分割后则丢失该字符串
    ·join():用一个字符或子串合并字符串,即是将多个字符串合并为一个新的字符串
        语法:字符或子串.join(多字符串组成的序列)
    ·capitalize():将字符串第一个字符转换成大写
        注意:capitalize()函数转换后,只字符串第一个字符大写,其他的字符全是小写
    ·title():将字符串中每个单词首字母转换成大写
    ·lower():将字符串中大写转小写
    ·upper():将字符串中小写转大写
    ·lstrip():删除字符串左侧空白字符
    ·rstrip():删除字符串右侧空白字符
    ·strip():删除字符串两侧空白字符
    ·ljust():返回一个原字符串左对齐,并使用指定字符(默认空格)填充至对应长度的新字符串
        语法:字符串序列.ljust(长度,填充字符)
    ·rjust():返回一个原字符串右对齐,并使用指定字符(默认空格)填充至对应长度的新字符串,语法和ljust()相同
    ·center():返回一个原字符串居中对齐,并使用指定字符(默认空格)填充至对应长度的新字符串,语法和ljust()相同
'''
str2 = 'hello world and java and Python and scala'
print(str2.replace('and','he'))
print(str2.replace('and','he',2))
print(str2) # 字符串类型修改的时候不能改变原有字符串
print(str2.split('and'))
print(str2.split('and',2))
list = ['a','b','c','d']
print('...'.join(list))
print(str2.capitalize())
print(str2.title())
print(str2.lower())
print(str2.upper())
str3 = ' hello world and java and Python and scala '
print(str3)
print(str3.lstrip())
print(str3.rstrip())
print(str3.strip())
str4 = 'hello'
print(str4.ljust(10,'.'))
print(str4.rjust(10,'.'))
print(str4.center(10,'.'))
'''
③判断:所谓判断即是判断真假,返回的结果是布尔型数据类型:True或False
    ·startswith():检查字符串是否以指定子串开头,是则返回True,否则返回False,如果设置开始和结束位置下标,则在指定范围内检查
        语法:字符串序列.startswith(子串,开始位置下标,结束位置下标)
    ·endswith():检查字符串是否以指定子串结尾,是则返回True,否则返回False,如果设置开始和结束下标,则在指定范围内检查
        语法:字符串序列.endswith(子串,开始位置下标,结束位置下标)
    ·isalpha():如果字符串至少有一个字符并且所有字符都是字母则返回True,否则返回False
    ·isdigit():如果字符串只包含数字则返回True,否则返回False
    ·isalnum():如果字符串中至少有一个字符并且所有字符都是字母或数字则返回Ture,否则返回False
    ·isspace():如果字符串中只包含空白,则返回True,否则返回False
'''
str5 = 'hellopython123'
print(str5.startswith('he'))
print(str5.startswith('he',5,8))
print(str5.endswith('thon'))
str6 = 'hello'
print(str6.isalpha())
print(str5.isdigit())
print(str5.isalnum())
str7 = '     '
print(str7.isspace())
