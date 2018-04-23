import pygame
WHITE = (255, 255, 255)
BLACK = (0,0,0)

class Snowflake (pygame.sprite.Sprite):

    def __init__ (self, color, width, height, speed):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
    
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

        pygame.draw.line(self.image, self.color, [0,0], [20, 20], 2)
        pygame.draw.line(self.image, self.color, [20, 0], [0, 20], 2)
        pygame.draw.line(self.image, self.color, [10, 0], [10, 20], 2)
        pygame.draw.line(self.image, self.color, [0,10], [20, 10], 2)

        self.rect = self.image.get_rect()

    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20

    def changeSpeed (self,speed):
        self.speed = speed
