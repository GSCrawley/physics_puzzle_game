import pygame
import pymunk
from level import Level
from level_manager import LevelManager


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.space = pymunk.Space()
        self.space.gravity = (0, 981)  # Adjust gravity as needed
        self.level_manager = LevelManager(self.space)
        self.current_level = self.level_manager.get_current_level()
        self.dragging = False
        self.drag_body = None
        self.score = 0
        self.moves = 0
        self.game_state = "playing"  # Can be "playing", "level_complete", or "game_over"

    
    def handle_event(self, event):
        if self.game_state == "playing":
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_down(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.handle_mouse_up(event.pos)
            elif event.type == pygame.MOUSEMOTION:
                self.handle_mouse_move(event.pos)
            elif self.game_state == "level_complete":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.next_level()
                elif self.game_state == "game_over":
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        self.restart_game()
    def update(self):
            if self.game_state == "playing":
                self.space.step(1/60.0)
                self.current_level.update()
                if self.current_level.is_completed():
                    self.game_state = "level_complete"
                    self.score += max(1000 - self.moves * 10, 100)  # Score based on moves
                    print(f"Level completed in {self.moves} moves!")
                    print(f"Score: {self.score}")

    def draw(self):
        self.screen.fill((255, 255, 255))  # White background
        self.current_level.draw(self.screen)
        
        # Draw score and moves
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        moves_text = font.render(f"Moves: {self.moves}", True, (0, 0, 0))
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(moves_text, (10, 50))

        if self.game_state == "level_complete":
            self.draw_level_complete()
        elif self.game_state == "game_over":
            self.draw_game_over()

    def draw_level_complete(self):
        font = pygame.font.Font(None, 72)
        text = font.render("Level Complete!", True, (0, 255, 0))
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)

        font = pygame.font.Font(None, 36)
        instruction = font.render("Press SPACE to continue", True, (0, 0, 0))
        instruction_rect = instruction.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 50))
        self.screen.blit(instruction, instruction_rect)

    def draw_game_over(self):
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(text, text_rect)

        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Final Score: {self.score}", True, (0, 0, 0))
        score_rect = score_text.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 50))
        self.screen.blit(score_text, score_rect)

        instruction = font.render("Press R to restart", True, (0, 0, 0))
        instruction_rect = instruction.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2 + 100))
        self.screen.blit(instruction, instruction_rect)

    def next_level(self):
        if self.level_manager.next_level():
            self.current_level = self.level_manager.get_current_level()
            self.moves = 0
            self.game_state = "playing"
        else:
            self.game_state = "game_over"

    def restart_game(self):
        self.level_manager = LevelManager(self.space)
        self.current_level = self.level_manager.get_current_level()
        self.score = 0
        self.moves = 0
        self.game_state = "playing"

    def handle_mouse_down(self, pos):
        shape = self.space.point_query_nearest(pos, 0, pymunk.ShapeFilter())
        if shape and shape.shape.body.body_type == pymunk.Body.DYNAMIC:
            self.dragging = True
            self.drag_body = shape.shape.body
            self.drag_body.velocity = (0, 0)
            self.moves += 1

    def handle_mouse_up(self, pos):
        self.dragging = False
        self.drag_body = None

    def handle_mouse_move(self, pos):
        if self.dragging and self.drag_body:
            self.drag_body.position = pos