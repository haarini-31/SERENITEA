import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Positive Word Puzzle Game")

# Colors
BACKGROUND_COLOR = (255, 255, 255)  # White
TEXT_COLOR = (0, 0, 0)  # Black
BOX_COLOR = (173, 216, 230)  # Light Blue

# Load background image
background_image = pygame.image.load(r"C:\Users\haari\OneDrive\Desktop\imparathon\finalgames\bg.jpeg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Font setup
font = pygame.font.Font(None, 36)

# Score tracking
score = 0

def draw_text(text, pos, color):
    label = font.render(text, True, color)
    screen.blit(label, pos)

def show_popup(message):
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, BOX_COLOR, (50, 50, 700, 300))
    draw_text(message, (100, 150), TEXT_COLOR)
    pygame.display.flip()
    pygame.time.wait(2000)  # Wait for 2 seconds

def animate_correct():
    for _ in range(10):
        screen.fill((0, 255, 0))  # Green flash
        pygame.display.flip()
        pygame.time.delay(50)
        screen.blit(background_image, (0, 0))  # Restore background
        pygame.display.flip()
        pygame.time.delay(50)

def animate_incorrect():
    for _ in range(10):
        screen.fill((255, 0, 0))  # Red flash
        pygame.display.flip()
        pygame.time.delay(50)
        screen.blit(background_image, (0, 0))  # Restore background
        pygame.display.flip()
        pygame.time.delay(50)

def word_puzzle():
    global score
    words = ["CALM", "BREATHE", "HOPE", "GRATITUDE", "MINDFUL", "STRENGTH", "BALANCE", "JOY", "PEACE", "COMPASSION"]
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))
    timer = 30  # 30 seconds timer
    running = True

    while running:
        screen.blit(background_image, (0, 0))  # Draw background
        draw_text(f"Unscramble the word: {scrambled}", (50, 100), TEXT_COLOR)
        draw_text(f"Score: {score}", (50, 50), TEXT_COLOR)
        draw_text(f"Time Left: {timer}s", (600, 50), TEXT_COLOR)
        pygame.display.flip()

        user_input = ''
        input_box = pygame.Rect(50, 200, 140, 32)
        color_inactive = pygame.Color('lightskyblue3')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        clock = pygame.time.Clock()
        start_ticks = pygame.time.get_ticks()  # Timer start

        while running:
            seconds = (pygame.time.get_ticks() - start_ticks) // 1000  # Calculate elapsed time
            timer = 30 - seconds

            if timer <= 0:
                show_popup(f"Time's up! The correct word was {word}.")
                running = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            if text.upper() == word:
                                score += 1
                                animate_correct()
                                show_popup("Correct! You found a positive word!")
                            else:
                                animate_incorrect()
                                show_popup(f"Oops! The correct word was {word}. Try again.")
                            running = False
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            screen.blit(background_image, (0, 0))  # Draw background
            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(screen, color, input_box, 2)
            draw_text(f"Unscramble the word: {scrambled}", (50, 100), TEXT_COLOR)
            draw_text(f"Score: {score}", (50, 50), TEXT_COLOR)
            draw_text(f"Time Left: {timer}s", (600, 50), TEXT_COLOR)
            pygame.display.flip()
            clock.tick(30)

def main_menu():
    while True:
        screen.blit(background_image, (0, 0))  # Draw background
        draw_text("Welcome to the Positive Word Puzzle Game!", (150, 100), TEXT_COLOR)
        draw_text("Choose a difficulty level:", (150, 200), TEXT_COLOR)

        # Difficulty buttons
        draw_text("Press 1 for Easy", (150, 250), TEXT_COLOR)
        draw_text("Press 2 for Medium", (150, 300), TEXT_COLOR)
        draw_text("Press 3 for Hard", (150, 350), TEXT_COLOR)

        draw_text("Press ESC to Quit", (250, 500), TEXT_COLOR)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_1:
                    word_puzzle()  # Start easy mode
                elif event.key == pygame.K_2:
                    word_puzzle()  # Start medium mode
                elif event.key == pygame.K_3:
                    word_puzzle()  # Start hard mode

# Start the game
main_menu()
