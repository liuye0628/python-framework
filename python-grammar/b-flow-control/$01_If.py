# 猜拳游戏
"""
玩家和电脑进行猜拳(0-石头,1-剪刀,2-布)
    玩家手动出拳,电脑随机出拳
    结果:
        ①玩家获胜
        ②平局
        ③电脑获胜
"""


# 导入random模块
import random

# 玩家出拳
player = int(input('请出拳: 0-石头, 1-剪刀, 2-布:'))
print(f'玩家出拳:{player}');

# 电脑出拳

computer = random.randint(0,2)
print(f'电脑出拳:{computer}')

if((player == 0 and computer == 1) or (player == 1 and computer == 2) or(player == 2 and computer == 0)):
    print('玩家获胜')
elif player == computer:
    print('平局')
else:
    print('电脑获胜')