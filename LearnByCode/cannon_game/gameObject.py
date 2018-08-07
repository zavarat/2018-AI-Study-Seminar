import pygame
import math

BALLS_COLOR = (255, 255, 255)
BARRICADE_Init_POSX = 100
BARRICADE_Init_POSY = 100
BARRICADE_SPEED = 2
BARRICADE_WIDTH = 40
BARRICADE_HEIGHT = 40
BARRICADE_COLOUR = (255, 255, 255)

TERMINATE_Init_POSX = 380
TERMINATE_Init_POSY = 270
TERMINATE_RADIUS = 5
TERMINATE_SIZE = TERMINATE_RADIUS * 2


class Barricade:
    
    def __init__(self, screen, scr_width):
        self.width = BARRICADE_WIDTH
        self.height = BARRICADE_HEIGHT
        self.location_x = BARRICADE_Init_POSX + self.width / 2
        self.location_y = BARRICADE_Init_POSY + self.height / 2
        self.speed = BARRICADE_SPEED
        self.screen = screen
        self.scr_width = scr_width
    
    # tryangle
    def draw(self):
        points = [[self.location_x, self.location_y - self.height / 2], [self.location_x - self.width / 2, self.location_y + self.height / 2], [self.location_x + self.width / 2, self.location_y + self.height / 2]]
        pygame.draw.polygon(self.screen, BARRICADE_COLOUR, points)        
    
    def isClose(self):
        return self.location_x  < 5 or self.location_x > self.scr_width - 5
        
    def update(self):
        if self.isClose() :
            self.speed *= -1 
        self.location_x += self.speed
        
    def iscrashed(self, x, y):
        if math.sqrt((self.location_x - x)**2 + (self.location_y - y)**2) < 15:
            return True
        else:
            return False
        
class Terminate:
    
    def __init__(self, screen, scr_width, scr_height):
        self.screen = screen
        self.location_x = TERMINATE_Init_POSX
        self.location_y = TERMINATE_Init_POSY
        self.size = TERMINATE_SIZE
        self.scr_width = scr_width
        self.scr_height = scr_height
        self.radius = TERMINATE_RADIUS
        
    def draw(self):
       pygame.draw.circle(self.screen, BARRICADE_COLOUR, [self.location_x, self.location_y], self.radius)
       
    def isCrashed(self, x, y):
        distance = math.sqrt((x - self.location_x)**2 + (y - self.location_y) ** 2)
        if distance < 15 :
            return True
        else :
            return False
        
class Character:
    
    def __init__(self, screen):
        self.width = 30
        self.height = 30
        self.location_x = 10 + self.width / 2
        self.location_y = 10 + self.height / 2
        self.screen = screen
        self.pressed = pygame.key.get_pressed()
    
    def draw(self):
        pygame.draw.rect(self.screen, BALLS_COLOR,
            pygame.Rect(self.location_x - self.width / 2, self.location_y - self.height / 2,
            self.height, self.width))
            
    def update(self, pressed):
        if pressed[pygame.K_UP] and self.location_y >= 0 + self.height / 2: self.location_y -= 3
        if pressed[pygame.K_DOWN] and self.location_y <= 300 - self.height / 2 : self.location_y += 3
        if pressed[pygame.K_LEFT] and self.location_x >= 0 + self.width / 2: self.location_x -= 3
        if pressed[pygame.K_RIGHT] and self.location_x <= 400 - self.width/ 2: self.location_x += 3
        

        