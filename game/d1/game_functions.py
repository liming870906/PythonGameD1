import sys
import pygame

def check_events(ship):
    """
    响应键盘和鼠标事件
    :return:
    """
    for event in pygame.event.get():
        # 退出命令
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                ship.moving_left = True
            elif event.key == pygame.K_UP:
                ship.moving_up = True
            elif event.key == pygame.K_DOWN:
                ship.moving_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False
            elif event.key == pygame.K_UP:
                ship.moving_up = False
            elif event.key == pygame.K_DOWN:
                ship.moving_down = False


def update_screen(ai_settings,screen,ship):
    """
    每次都循环是都重绘屏幕
    :param ai_settings: settings
    :param screen:
    :param ship:
    :return:
    """
    # 绘制背景颜色
    screen.fill(ai_settings.bg_color)
    # 绘制
    ship.blitme()