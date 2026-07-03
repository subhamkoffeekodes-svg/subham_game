import pygame
import random
import sys

pygame.init()

# Screen
WIDTH = 500
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 100, 255)
GRAY = (60, 60, 60)
YELLOW = (255, 255, 0)

clock = pygame.time.Clock()

# Trees
trees = [
    (40, 100), (40, 250), (40, 450), (40, 600),
    (460, 150), (460, 350), (460, 550)
]

# Player
player_x = WIDTH // 2 - 20
player_y = HEIGHT - 120
player_speed = 20

# Enemy
enemy_x = random.randint(100, 350)
enemy_y = -100
enemy_speed = 7

# Score
score = 0
line_y = 0

font = pygame.font.SysFont(None, 35)

# Mobile buttons
left_button = pygame.Rect(20, 620, 80, 50)
right_button = pygame.Rect(400, 620, 80, 50)


def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))


def draw_tree(x, y):
    pygame.draw.rect(screen, (101, 67, 33), (x - 5, y + 15, 10, 20))
    pygame.draw.circle(screen, (0, 180, 0), (x, y), 20)
    pygame.draw.circle(screen, (0, 160, 0), (x - 10, y + 5), 15)
    pygame.draw.circle(screen, (0, 160, 0), (x + 10, y + 5), 15)


def draw_car(x, y, color):
    pygame.draw.rect(screen, color, (x, y, 40, 80), border_radius=8)
    pygame.draw.rect(screen, BLACK, (x + 8, y + 10, 24, 18), border_radius=4)
    pygame.draw.rect(screen, BLACK, (x + 8, y + 50, 24, 15), border_radius=4)
    pygame.draw.circle(screen, BLACK, (x, y + 15), 5)
    pygame.draw.circle(screen, BLACK, (x + 40, y + 15), 5)
    pygame.draw.circle(screen, BLACK, (x, y + 65), 5)
    pygame.draw.circle(screen, BLACK, (x + 40, y + 65), 5)


running = True

while running:

    # Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Mobile tap once
        if event.type == pygame.MOUSEBUTTONDOWN:

            if left_button.collidepoint(event.pos):
                player_x -= player_speed

            if right_button.collidepoint(event.pos):
                player_x += player_speed

    # Keyboard
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= 7

    if keys[pygame.K_RIGHT]:
        player_x += 7

    # Boundary
    if player_x < 80:
        player_x = 80

    if player_x > 380:
        player_x = 380

    # Speed increase every 10 score
    enemy_speed = 7 + (score // 10)

    # Enemy movement
    enemy_y += enemy_speed

    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(100, 350)
        score += 1

    # Collision
    player_rect = pygame.Rect(player_x, player_y, 40, 80)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 40, 80)

    if player_rect.colliderect(enemy_rect):
        print("GAME OVER")
        pygame.quit()
        sys.exit()

    # Background
    screen.fill((0, 150, 0))

    # Trees
    for tree in trees:
        draw_tree(tree[0], tree[1])

    # Road
    pygame.draw.rect(screen, GRAY, (80, 0, 340, HEIGHT))

    # Road lines
    line_y += 5
    if line_y > HEIGHT:
        line_y = 0

    for i in range(-50, HEIGHT, 100):
        pygame.draw.rect(screen, YELLOW, (245, i + line_y, 10, 50))

    # Cars
    draw_car(player_x, player_y, BLUE)
    draw_car(enemy_x, enemy_y, RED)

    # Mobile buttons
    pygame.draw.rect(screen, WHITE, left_button)
    pygame.draw.rect(screen, WHITE, right_button)

    draw_text("L", 50, 635)
    draw_text("R", 430, 635)

    # Score + speed
    draw_text("Score: " + str(score), 20, 20)
    draw_text("Speed: " + str(enemy_speed), 20, 50)

    pygame.display.update()
    clock.tick(60)
