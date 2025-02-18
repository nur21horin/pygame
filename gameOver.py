import pygame
import random

# Initialize Pygame
pygame.init()

# Initialize the mixer module
pygame.mixer.init()

# Load and play background music
pygame.mixer.music.load("./fahad-ahmed-dj-tonu_joy-bangla-jitbe-abar-nouka-dj-tonu.mp3")
pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)

# Screen dimensions
screen_width = 600
screen_height = 600
gameWindow = pygame.display.set_mode((screen_height, screen_width))

# Game title
pygame.display.set_caption("snakesWithHasina")
pygame.display.update()

# Game loop variables
exit_game = False
game_over = False

# Snake variables
snake_x = 45
snake_y = 55
snake_size = 25
fps = 60
velocity_x = 0
velocity_y = 0
score = 0
snake_length = 5
snake_list = []

# Food position
food_x = random.randint(0, screen_width - snake_size)
food_y = random.randint(0, screen_height - snake_size)

# Load and scale the snake head image
snake_head_img = pygame.image.load("./Screenshot 2025-02-18 235254.png")
snake_head_img = pygame.transform.scale(snake_head_img, (snake_size, snake_size))

# Create a circular mask
mask_surface = pygame.Surface((snake_size, snake_size), pygame.SRCALPHA)
pygame.draw.circle(mask_surface, (255, 255, 255), (snake_size // 2, snake_size // 2), snake_size // 2)

# Apply the circular mask to the snake head image
snake_head_img.set_colorkey((0, 0, 0))
mask_surface.blit(snake_head_img, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

# Load and scale the boat food image
boat_food_img = pygame.image.load("./helmet.png")  # Replace with the actual image file
boat_food_img = pygame.transform.scale(boat_food_img, (snake_size, snake_size))

# Load game over music
game_over_music = "./WhatsApp Audio 2025-02-19 at 01.46.39_e064b8a3.mp3"  # Replace with the actual path to the game over music file

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, snake_list, snake_head_img):
    for i, (x, y) in enumerate(snake_list):
        if i == len(snake_list) - 1:
            gameWindow.blit(snake_head_img, (x, y))
        else:
            pygame.draw.circle(gameWindow, black, (x + snake_size // 2, y + snake_size // 2), snake_size // 2)

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 2
                velocity_y = 0
            if event.key == pygame.K_LEFT:
                velocity_x = -2
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y = -2
                velocity_x = 0
            if event.key == pygame.K_DOWN:
                velocity_y = 2
                velocity_x = 0

    snake_x += velocity_x
    snake_y += velocity_y

    if abs(snake_x - food_x) < 6 and abs(snake_y - food_y) < 6:
        score += 1
        snake_length += 1
        print("Score:", score * 10)
        food_x = random.randint(20, screen_width - snake_size)
        food_y = random.randint(20, screen_height - snake_size)

    # Check for boundary collision
    if snake_x < 0 or snake_x > screen_width - snake_size or snake_y < 0 or snake_y > screen_height - snake_size:
        game_over = True

    gameWindow.fill(white)
    text_screen("Score: " + str(score * 10), red, 5, 5)
    gameWindow.blit(boat_food_img, (food_x, food_y))  # Use boat image for food

    snake_head = [snake_x, snake_y]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    plot_snake(gameWindow, snake_list, mask_surface)

    # Draw blue boundary
    pygame.draw.rect(gameWindow, blue, [0, 0, screen_width, screen_height], 5)

    pygame.display.update()
    clock.tick(fps)

    if game_over:
        # Stop current music and play game over music
        pygame.mixer.music.stop()
        pygame.mixer.music.load(game_over_music)
        pygame.mixer.music.play(1)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    exit_game = True
                    break
            if exit_game:
                break

pygame.quit()
quit()
