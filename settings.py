class Settings:
    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,64)
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_dirtction=1 右边移动 -1 左边移动
        self.fleet_direction = 1
        #子弹设置
        self.bullet_speed = 2.5
        self.bullet_width= 3
        #飞船设置
        self.ship_speed = 1.5
        self.ships_limit = 3