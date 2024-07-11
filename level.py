import pygame
import pymunk
from objects.ball import Ball
from objects.block import Block
from objects.goal import Goal

class Level:
    def __init__(self, space):
        self.space = space
        self.objects = []
        self.ball = None
        self.goal = None
        self.setup_level()

    def setup_level(self):
        # Create a ball
        self.ball = Ball(self.space, (100, 100))
        self.objects.append(self.ball)

        # Create some blocks
        block1 = Block(self.space, (300, 300), (200, 20))
        block2 = Block(self.space, (500, 400), (200, 20))
        self.objects.extend([block1, block2])

        # Create a goal
        self.goal = Goal(self.space, (700, 550))
        self.objects.append(self.goal)

    def update(self):
        for obj in self.objects:
            obj.update()

    def draw(self, screen):
        for obj in self.objects:
            obj.draw(screen)

    def is_completed(self):
        if self.ball and self.goal:
            distance = self.ball.body.position.get_distance(self.goal.body.position)
            return distance < 30  # Adjust this value based on your ball and goal sizes
        return False
