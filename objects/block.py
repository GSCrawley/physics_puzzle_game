import pygame
import pymunk

class Block:
    def __init__(self, space, pos, size):
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = pos
        self.shape = pymunk.Poly.create_box(self.body, size)
        self.shape.elasticity = 0.5
        self.shape.friction = 0.7
        space.add(self.body, self.shape)
        self.size = size

    def update(self):
        pass  # Static bodies don't need updating

    def draw(self, screen):
        pos = int(self.body.position.x), int(self.body.position.y)
        rect = pygame.Rect(pos[0] - self.size[0]//2, pos[1] - self.size[1]//2, self.size[0], self.size[1])
        pygame.draw.rect(screen, (0, 255, 0), rect)
