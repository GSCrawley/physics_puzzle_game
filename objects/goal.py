import pygame
import pymunk

class Goal:
    def __init__(self, space, pos):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, 20)
        self.shape.sensor = True  # Makes it a sensor (no collision response)
        space.add(self.body, self.shape)

    def update(self):
        pass

    def draw(self, screen):
        pos = int(self.body.position.x), int(self.body.position.y)
        pygame.draw.circle(screen, (0, 0, 255), pos, 20)