import pygame


class Ship:
    def __init__(self,ai_settings, screen):
        """
        初始化位置
        :param screen:
        """
        # 获得Setting对象
        self.ai_settings = ai_settings
        self.screen = screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # 设置位置
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # 右侧移动标记
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        # 存在小数值
        self.center = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)

    def update(self):
        """
        更新位置
        :return:
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        elif self.moving_up and self.rect.top > self.screen_rect.top:
            self.bottom -= self.ai_settings.ship_speed_factor
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor
        # 设置更新的位置
        self.rect.centerx = self.center
        self.rect.bottom = self.bottom

    def blitme(self):
        """
        在指定位置绘制飞机图片
        :return:
        """
        self.screen.blit(self.image, self.rect)
