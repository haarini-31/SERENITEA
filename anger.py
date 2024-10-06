import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
FONT = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Coping Strategies
COPING_STRATEGIES = [
    ("Deep Breathing", "Take deep breaths to calm down."),
    ("Counting", "Count to ten slowly."),
    ("Mindfulness", "Focus on the present moment."),
]

# Player Class
class Player:
    def __init__(self, avatar):
        self.rect = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)
        self.mood = 5
        self.coping_cards = []
        self.avatar = avatar  # Store selected avatar

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def collect_card(self, card):
        self.coping_cards.append(card)

# Level Class
class Level:
    def __init__(self, name):
        self.name = name

# Game Functions
def display_mood(screen, player):
    mood_text = FONT.render(f'Mood Level: {player.mood}', True, BLACK)
    screen.blit(mood_text, (10, 10))

def display_cards(screen, player):
    cards_text = FONT.render("Coping Cards: " + ", ".join(player.coping_cards), True, BLACK)
    screen.blit(cards_text, (10, 50))

def display_avatar(screen, player):
    avatar_text = FONT.render(f'Avatar: {player.avatar}', True, BLACK)
    screen.blit(avatar_text, (10, 90))

def show_educational_snippet(screen, snippet):
    snippet_text = FONT.render(snippet, True, BLACK)
    screen.blit(snippet_text, (10, HEIGHT - 50))

def customization_menu():
    # Simple avatar and theme selection
    print("Select your avatar: [1] Avatar1 [2] Avatar2 [3] Avatar3")
    avatar_choice = input("Enter the number of your choice: ")
    avatar = f"Avatar{avatar_choice}"

    print("Select a theme: [1] Default [2] Blue [3] Red")
    theme_choice = input("Enter the number of your choice: ")
    if theme_choice == "2":
        return avatar, BLUE
    elif theme_choice == "3":
        return avatar, RED
    else:
        return avatar, WHITE

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    avatar, theme_color = customization_menu()  # Get customization choices
    player = Player(avatar)

    levels = [Level("Urban"), Level("Nature"), Level("Office")]
    current_level_index = 0
    current_level = levels[current_level_index]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.move(-5, 0)
        if keys[pygame.K_RIGHT]: player.move(5, 0)
        if keys[pygame.K_UP]: player.move(0, -5)
        if keys[pygame.K_DOWN]: player.move(0, 5)

        # Collect coping strategies
        if random.random() < 0.01:  # Random chance to collect a card
            strategy = random.choice(COPING_STRATEGIES)
            player.collect_card(strategy[0])
            show_educational_snippet(screen, strategy[1])  # Show educational snippet

        # Mood adjustment example
        if len(player.coping_cards) > 0 and random.random() < 0.02:
            player.mood += 1
            player.mood = min(player.mood, 10)

        # Check level completion
        if player.mood >= 10:
            current_level_index += 1
            if current_level_index < len(levels):
                current_level = levels[current_level_index]
                player.mood = 5
                print(f"Moving to the next level: {current_level.name}")
            else:
                print("You've completed all levels! Game Over.")
                running = False

        # Drawing
        screen.fill(theme_color)  # Fill the screen with the selected theme color
        pygame.draw.rect(screen, GREEN, player.rect)
        display_mood(screen, player)
        display_cards(screen, player)
        display_avatar(screen, player)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
