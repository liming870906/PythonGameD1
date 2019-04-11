import sys

import os
import pygame


# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print('Base_Dir:%s' %base_dir)
# sys.path.append(base_dir)

from settings import Settings
from ship import Ship

def run_game():
    """
    创建窗口
    :return:
    """
    # 初始化
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建飞机
    ship = Ship(screen)

    while True:
        # 循环检测动作
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # 设置窗口颜色
        set_frame_background_color(screen,ai_settings.bg_color)
        ship.blitme()
        # 显示窗口
        pygame.display.flip()
def set_frame_background_color(screen,bg_color):
    """
    设置窗口颜色
    :param screen:
    :param bg_color:
    :return:
    """
    screen.fill(bg_color)

if __name__ == '__main__':
    run_game()