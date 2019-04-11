import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """
    外星人函数
    """
    def __init__(self,ai_settings,screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        # 加载图片信息
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        # 设置图片位置
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # 存储准确X轴位置
        self.x = float(self.rect.x)

    def blitme(self):
        """
        绘制图片
        :return:
        """
        self.screen.blit(self.image,self.rect)