import time

import pygame

from circle import Circle

pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Meditation")
font = pygame.font.SysFont("Futura", 60, True)


def redraw(win, *things):
    win.fill((255, 255, 255))
    text = None
    if circle.direction == "up":
        text = font.render("Breathe in", True, (0, 0, 0))
    else:
        text = font.render("Breathe out", True, (0, 0, 0))
    for i in things:
        i.draw(win)
    rect = text.get_rect(center=(320, 30))
    win.blit(text, rect)
    pygame.display.update()


if __name__ == '__main__':
    circle = Circle(320, 240, 10)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        redraw(window, circle)
        time.sleep(0.05)
        circle.resize()
        circle.recolor()

