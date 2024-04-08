import pygame
class Ship:
    def center_ship(self):
        """将飞船放在底部正中央"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)