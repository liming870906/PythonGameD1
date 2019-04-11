import sys
import pygame

from game.d1.bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """
    响应键盘和鼠标事件
    :return:
    """
    for event in pygame.event.get():
        # 退出命令
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keyup_events(event, ship):
    """
    抬起事件
    :param event:
    :param ship:
    :return:
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """
    按下事件
    :param event:
    :param ai_settings:
    :param screen:
    :param ship:
    :param bullets:
    :return:
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)


def update_screen(ai_settings, screen, ship, bullets):
    """
    每次都循环是都重绘屏幕
    :param ai_settings:
    :param screen:
    :param ship:
    :param bullets:
    :return:
    """
    # 绘制背景颜色
    screen.fill(ai_settings.bg_color)
    # 绘制子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 绘制
    ship.blitme()

def update_bullets(bullets):
    """
    更新子弹代码
    :return:
    """
    bullets.update()
    # 删除移动到屏幕外的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    pass
