import pygame
from pygame.sprite import Group

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
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    while True:
        # 事件触发方法
        gf.check_events(ai_settings,screen,ship,bullets)
        # 更新飞机位置
        ship.update()
        # 更新子弹
        bullets.update()
        # 删除子弹
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print("Bullets.Lenght:%d" %len(bullets))
        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship,bullets)
        # 绘制
        ship.blitme()
        # 显示窗口
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
