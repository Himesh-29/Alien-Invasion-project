import pygame
from pygame.sprite import Sprite
from Settings import Settings

class Bullet(Sprite):
    
    """A class to manage bullets fired from the ship"""
    
    def __init__(self, Settings, screen, ship):
        
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen
        
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, Settings.bullet_width,Settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        self.color = Settings.bullet_color
        self.speed_factor = Settings.bullet_speed_factor
    
    def update(self):
        """Move the bullet up the screen."""
        
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        
        # Update the rect position.
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)