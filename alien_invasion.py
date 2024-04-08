import sys

import pygame

from time import sleep
from settings import Settings 
from alien import Alien 
from game_stats import GameStats

class AlienInvasion:
    def __init__(self):

        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(((self.settings.screen_width,self.settings.screen_height)))

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        #创建一个用于储存游戏统计信息的实例
        self.stats = GameStats(self)

        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.bg_color = (230,230,230)

        #游戏启动后处于活动状态
        self.game_active = True

    
    def run_game(self):
        while True:
            self._check_events()

            if self.game_active:
                self._update_bullets()
                self._update_aliens()
                # self.ship.update()

            self._update_screen()
            # self.bullets.update()
            self.clock.tick(60)
    
    def _check_events(self):
         for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
         self.screen.fill(self.settings.bg_color)
         self.aliens.draw(self.screen)
         pygame.display.flip()

    def _create_fleet(self):
         """创建外星人舰队"""
         #创建一个外星人
         #创建一个外星人，不断添加，直到没有地方添加
         #外星人之间的间距为外星人的宽度
         alien = Alien(self)
         alien_width,alien_height = alien.rect.size

         current_x,current_y = alien_width,alien_height
         while current_y<(self.settings.screen_height - 3 * alien_height):
             while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x,current_y)
                current_x += 2 * alien_width  
             current_x = alien_width
             current_y += 2 * alien_height
         

    def _create_alien(self,x_position,y_position):
         """创建一外星人，并放入当前行中"""    
         new_alien = Alien(self)
         new_alien.x = x_position
         new_alien.rect.x = x_position
         new_alien.rect.y = y_position
         self.aliens.add(new_alien)    

    def _update_aliens(self):
        """更新外星人舰队中外星人所有位置"""
        self._check_fleet_edges()
        self.aliens.update()

        return
        #检测外星人与飞船的碰撞
        if pygame.sprite.spritecollide(self.ship,self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """当外星人达到边界时采取措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将舰队向下移动并改变方向"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_bullets(self):
        """更新子弹并删除已经消失的子弹"""
        #更新子弹位置
        return
        self.bullets.update()

        #删除已经消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0 :
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        """响应子弹和外星人的碰撞"""
        #删除发生碰撞的子弹和外星人
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)

        if not self.aliens:
            #删除现有子弹，生成新的舰队
            self.bullets.empty()
            self._create_fleet()

    def _ship_hit(self):
        """响应外星人与飞船的碰撞"""
        if self.stats.ships_left > 0 :
             #将ship的left-1
            self.stats.ships_left -= 1


            #清空外星人和子弹列表
            self.bullets.empty()
            self.aliens.empty()

            #创建一个新的外星舰队，将飞船放在底部中央
            self._create_fleet()
            self.ship.center_ship()

            #暂停
            sleep(0.5)
        else:
            self.game_active = False

    def _check_aliens_bottom(self):
        """检查外星人是否达到底部"""
        for aliens in self.aliens.sprite():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


    

