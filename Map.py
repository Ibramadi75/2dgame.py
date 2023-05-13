import pygame

class Map:
    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()

    def map_limit(self):
        color = (255, 255, 255)
        line_width = 5

        part = 10
        left_top_corner = (self.width/part, self.height/part)
        right_top_corner = (self.width-(self.width/part), self.height/part)
        left_bot_corner = (self.width/part, self.height-(self.height/part))
        right_bot_corner = (self.width-(self.width/part), self.height-(self.height/part))

        line_start = left_top_corner
        line_end = right_top_corner
        pygame.draw.line(self.screen, color, line_start, line_end, line_width)

        line_end = left_bot_corner
        pygame.draw.line(self.screen, color, line_start, line_end, line_width)

        line_start = right_bot_corner
        pygame.draw.line(self.screen, color, line_start, line_end, line_width)

        line_end = right_top_corner
        pygame.draw.line(self.screen, color, line_start, line_end, line_width)

        #line_start = right_bot_corner
        #pygame.draw.line(self.screen, color, line_start, line_end, line_width)