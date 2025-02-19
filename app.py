from flask import Flask, render_template, jsonify
import pygame
import random
import threading

app = Flask(__name__)

# Pygame Initialization
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("./fahad-ahmed-dj-tonu_joy-bangla-jitbe-abar-nouka-dj-tonu.mp3")
pygame.mixer.music.play(-1)

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)

# Screen dimensions
screen_width = 600
screen_height = 600
gameWindow = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption("snakesWithHasina")
pygame.display.update()

# Game variables
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

# Load and scale images
snake_head_img = pygame.image.load("./Screenshot 2025-02-18 235254.png")
snake_head_img = pygame.transform.scale(snake_head_img, (snake_size, snake_size))
boat_food_img = pygame.image.load("./helmet.png")
boat_food_img = pygame.transform.scale(boat_food_img, (snake_size, snake_size))
game_over_music = "./WhatsApp Audio 2025-02-19 at 01.46.39_e064b8a3.mp3"

clock = pygame.time.Clock()

def game_loop():
    global snake_x, snake_y, snake_size, score, snake_length, snake_list, food_x, food_y, game_over, velocity_x, velocity_y
    exit_game = False
    game_over = False

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
            food_x = random.randint(20, screen_width - snake_size)
            food_y = random.randint(20, screen_height - snake_size)

        if snake_x < 0 or snake_x > screen_width - snake_size or snake_y < 0 or snake_y > screen_height - snake_size:
            game_over = True

        gameWindow.fill(white)
        pygame.draw.rect(gameWindow, blue, [0, 0, screen_width, screen_height], 5)
        pygame.draw.circle(gameWindow, black, (snake_x + snake_size // 2, snake_y + snake_size // 2), snake_size // 2)

        snake_head = [snake_x, snake_y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        pygame.display.update()
        clock.tick(fps)

        if game_over:
            pygame.mixer.music.stop()
            pygame.mixer.music.load(game_over_music)
            pygame.mixer.music.play(1)
            exit_game = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game')
def start_game():
    threading.Thread(target=game_loop).start()
    return jsonify({"status": "Game Started"})

if __name__ == "__main__":
    app.run(debug=True)
