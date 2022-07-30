import random, pygame

#Initialize pygame
pygame.init()

#Set display window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paint")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Define colors as RGB tuples
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
CYAN = (0,255,255)
MAGENTA = (255,0,255)

#The main game loop
running = True
display_surface.fill(WHITE)

#Color boxes
def boxes():
    blk_rect = pygame.draw.rect(display_surface, BLACK, (10, 30, 30, 30))
    wht_rect = pygame.draw.rect(display_surface, WHITE, (40, 30, 30, 30))
    red_rect = pygame.draw.rect(display_surface, RED, (70, 30, 30, 30))
    grn_rect = pygame.draw.rect(display_surface, GREEN, (100, 30, 30, 30))
    blue_rect = pygame.draw.rect(display_surface, BLUE, (130, 30, 30, 30))
    ylw_rect = pygame.draw.rect(display_surface, YELLOW, (160, 30, 30, 30))
    cyan_rect = pygame.draw.rect(display_surface, CYAN, (190, 30, 30, 30))
    mgt_rect = pygame.draw.rect(display_surface, MAGENTA, (220, 30, 30, 30))

choosen_color = BLACK

while running:
    #Check to see if user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        boxes()
        #Mouse button
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]
                pygame.draw.circle(display_surface, choosen_color, (mouse_x, mouse_y), 10, 0)

        if event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]
                pygame.draw.circle(display_surface, choosen_color, (mouse_x, mouse_y), 10, 0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos() >= (10, 10):
                if pygame.mouse.get_pos() <= (39, 20):
                    choosen_color = BLACK
                    boxes()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos() >= (40, 10):
                if pygame.mouse.get_pos() <= (69, 20):
                    choosen_color = WHITE
                    boxes()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos() >= (70, 10):
                if pygame.mouse.get_pos() <= (99, 20):
                    choosen_color = RED
                    boxes()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos() >= (100, 10):
                if pygame.mouse.get_pos() <= (129, 20):
                    choosen_color = GREEN
                    boxes()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos() >= (130, 10):
                if pygame.mouse.get_pos() <= (159, 20):
                    choosen_color = BLUE
                    boxes()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos() >= (160, 10):
                if pygame.mouse.get_pos() <= (189, 20):
                    choosen_color = YELLOW
                    boxes()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos() >= (190, 10):
                if pygame.mouse.get_pos() <= (219, 20):
                    choosen_color = CYAN
                    boxes()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos() >= (220, 10):
                if pygame.mouse.get_pos() <= (249, 20):
                    choosen_color = MAGENTA
                    boxes()

    #Update display and tick clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.QUIT()