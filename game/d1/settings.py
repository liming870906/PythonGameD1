class Settings:
    def __init__(self):
        # 屏幕大小
        self.screen_width = 360
        self.screen_height = 640
        # 背景颜色
        self.bg_color = (72, 118, 255)
        # 飞机速度
        self.ship_speed_factor = 1.5
        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 设置子弹最大数量
        self.bullet_allowed = 3
