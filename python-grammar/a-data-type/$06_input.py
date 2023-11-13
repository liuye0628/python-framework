'''
input: 功能输入,等待用户输入,输入完成后在继续向下执行
    ①一般将input接收的数据存储到变量
    ②input接收的任何数据默认都是字符串数据类型
'''

password = input('请输入你的密码:')
print(f'你输入的密码是{password}')
print(type(password)) #str
