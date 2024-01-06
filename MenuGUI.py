import pygame
import sys
import configparser

# Initialize Pygame
pygame.init()

# Set up the window dimensions
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Menu with Options")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GRAY = (169, 169, 169)

# Set up fonts
font = pygame.font.Font('BreatheFire.ttf', 36)

# Function to display text on the screen
def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to handle resolution selection
def handle_resolution_click(pos):
    if 250 <= pos[0] <= 550:
        y_offset = 200
        for i, res in enumerate(resolutions):
            if y_offset + i * 50 <= pos[1] <= y_offset + (i + 1) * 50:
                save_resolution(res[0], res[1])

# Function to display screen resolutions
def display_resolutions():
    y_offset = width / 2
    for i, res in enumerate(resolutions):
        draw_text(f"{res[0]} x {res[1]}", WHITE, 300, y_offset + i * 50)

# Read resolution from config file or set default
def read_resolution():
    config = configparser.ConfigParser()
    config.read('config.ini')
    if 'Display' in config:
        width = int(config['Display'].get('width'))
        height = int(config['Display'].get('height'))
        return width, height
    else:
        return 1280, 720  # Default resolution if not found in config

# Options menu loop
def options_menu():
    options = True

    while options:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    handle_resolution_click(pygame.mouse.get_pos())
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    options = False

        screen.fill(BLACK)
        draw_text("Options Menu", WHITE, 280, 50)
        draw_text("Click on a resolution to set:", WHITE, 180, 150)
        display_resolutions()
        draw_text("Press ESC to go back", WHITE, 250, 500)

        pygame.display.flip()

# Run the options menu
resolutions = [
    (800, 600),
    (1024, 768),
    (1280, 720),
    (1920, 1080)
]

initial_width, initial_height = read_resolution()
window_size = (initial_width, initial_height)
screen = pygame.display.set_mode(window_size)

options_menu()

# Quit Pygame properly
pygame.quit()
sys.exit()
