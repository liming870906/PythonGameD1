import sys

import os
import pygame

# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print('Base_Dir:%s' %base_dir)
# sys.path.append(base_dir)

from game.d1.settings import Settings
from game.d1.ship import Ship

from game.d1 import game_functions as gf


def run_game():
    """
    创建窗口
    :return:
    """
    # 初始化
    pygame.init()
    # 声明配置对象
    ai_settings = Settings()
    # 获得屏幕Surface对象
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    # 设置标题
    pygame.display.set_caption("Alien Invasion")
    # 创建飞机
    ship = Ship(ai_settings,screen)

    while True:
        # 事件触发方法
        gf.check_events(ship)
        # 更新飞机位置
        ship.update()
        # 更新屏幕
        gf.update_screen(ai_settings,screen,ship)
        # 绘制
        ship.blitme()
        # 显示窗口
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
