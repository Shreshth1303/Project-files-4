import pygame
import time
import random

# Initialize the game
pygame.init()

# Set up display
width = 800
height = 600
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Car Game')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Clock and Car Details
clock = pygame.time.Clock()
car_width = 73

# Load Car Image
car_img = pygame.image.load('racecar.png')  # Make sure to have a car image file in the same directory.

# Define functions

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    game_display.blit(text, (0, 0))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(game_display, color, [thingx, thingy, thingw, thingh])

def car(x, y):
    game_display.blit(car_img, (x, y))

def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

def message_display(text):
    large_text = pygame.font.Font('freesansbold.ttf', 115)
    text_surf, text_rect = text_objects(text, large_text)
    text_rect.center = ((width / 2), (height / 2))
    game_display.blit(text_surf, text_rect)
    pygame.display.update()
    time.sleep(2)
    game_loop()

def crash():
    message_display('You Crashed')

def game_loop():
    x = (width * 0.45)
    y = (height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, width)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    dodged = 0

    game_exit = False

    while not game_exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        game_display.fill(white)

        # Things (obstacles)
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        car(x, y)
        things_dodged(dodged)

        if x > width - car_width or x < 0:
            crash()

        if thing_starty > height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
