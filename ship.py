import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen

        image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(image, (60, 60))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blitme(self):

        self.screen.blit(self.image, self.rect)
