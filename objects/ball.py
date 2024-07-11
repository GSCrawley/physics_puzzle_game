import pygame
import pymunk

class Ball:
    def __init__(self, space, pos):
        self.body = pymunk.Body(1, 100)
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, 10)
        self.shape.elasticity = 0.8
        self.shape.friction = 0.5
        space.add(self.body, self.shape)

    def update(self):
        pass  # The physics engine handles movement

    def draw(self, screen):
        pos = int(self.body.position.x), int(self.body.position.y)
        pygame.draw.circle(screen, (255, 0, 0), pos, 10)