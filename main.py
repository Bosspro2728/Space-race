import pygame
import random
import os
# import time

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 800, 850
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("name of Game!")

HEALTH_FONT = pygame.font.SysFont('Times New Roman', 40) #here we are defineing the font and size of the text
WINNER_FONT = pygame.font.SysFont('Times New Roman', 100)#here we declare another font

BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

YELLOW_SPACESHIP_WIDTH, YELLOW_SPACESHIP_HEIGHT = 70, 70
YELLOW_SPACESHIP = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png')), (YELLOW_SPACESHIP_WIDTH, YELLOW_SPACESHIP_HEIGHT))

VELOCITY = 5 #how much a spaceship moves one we press one of the kyes

RED_WALL_HIT_SPACESHIP = pygame.USEREVENT +1
WHITE_WALL_HIT_SPACESHIP = pygame.USEREVENT +2
GREEN_WALL_HIT_SPACESHIP = pygame.USEREVENT +3



def create_wall():
    return pygame.Rect(random.randint(5, WIDTH), random.randint(5, 600) ,WIDTH/50, HEIGHT/100)
#we are saying that we want them them to spond no lower then the y position 600 so we have some space from the spaceship      

def colors():
    colors = []
    for _ in range(11):
        colors.append(WHITE)
    for _ in range(12):
        colors.append(RED)
    for _ in range(11):
        colors.append(GREEN)
    return colors

def walls():
    walls = []
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    walls.append(create_wall())
    return walls

colors_of_walls = colors()
array_of_walls = walls()

def draw_wall(colors, walls):
    for i in range(len(colors_of_walls)):
        pygame.draw.rect(WIN, colors[i], walls[i])

timer_duration = 10  # 10 seconds/ 5 seconds/ time(seconds)
# Initialize the timer start time



def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x - VELOCITY > 0:  
        yellow.x -= VELOCITY  
        # this if statement moves the spaceship left because we
        # are subtracting from x. the other one checks is the spaceship cordinates are out of the window
        # it is getting closer to 0,0 because of the pygame coordination system.
        # this means the spaceship will move 5 places on this direction: ←/left/back only if the a key is pressed.
    if keys_pressed[pygame.K_RIGHT] and yellow.x + VELOCITY < WIDTH - yellow.width:  # moves right
        yellow.x += VELOCITY      #we need this               ↑ because when we dont account the width we are saying
        # that the top left corner of spaceship must not br greater than the  top left of the border.but the width
        # would pass to the others side so we need to account the width as well.
    if keys_pressed[pygame.K_UP] and yellow.y - VELOCITY > 0:  # moves up
        yellow.y -= VELOCITY
    if keys_pressed[pygame.K_DOWN] and yellow.y + VELOCITY + yellow.height < HEIGHT : # moves down
        yellow.y += VELOCITY


def update_walls():
    global array_of_walls, colors_of_walls
    array_of_walls = walls()  # Create new walls
    colors_of_walls = colors()  # Create new wall colors
    
def handle_walls(yellow):
# and check if any of the walls have collided with a spaceship
    for wall in array_of_walls:
        if yellow.colliderect(wall): #checks if the spaceship has collided with a bullet
            if colors_of_walls[array_of_walls.index(wall)] == RED:
                pygame.event.post(pygame.event.Event(RED_WALL_HIT_SPACESHIP))# here we are posting an event witch allows us to use this event that we created
                # print(array_of_walls.index(wall)) 
                colors_of_walls.pop(array_of_walls.index(wall))
                array_of_walls.remove(wall) #removes the bullet if it has collided

            elif colors_of_walls[array_of_walls.index(wall)] == GREEN:
                pygame.event.post(pygame.event.Event(GREEN_WALL_HIT_SPACESHIP))
                # print(wall)
                # print(array_of_walls.index(wall)) 
                colors_of_walls.pop(array_of_walls.index(wall))
                array_of_walls.remove(wall)
            
            elif colors_of_walls[array_of_walls.index(wall)] == WHITE:
                pygame.event.post(pygame.event.Event(WHITE_WALL_HIT_SPACESHIP))
                # print(wall)
                # print(array_of_walls.index(wall)) 
                colors_of_walls.pop(array_of_walls.index(wall))
                array_of_walls.remove(wall)


def draw_window(yellow, yellow_health):
    WIN.blit(BACKGROUND_IMAGE, (0, 0))           
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) #WIN.blit(Surface, (x position, y position))
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)#same for yellow
    yellow_position = HEALTH_FONT.render("POS: " + str(yellow.y), 1, WHITE)
    WIN.blit(yellow_position, (650, 750))#we draw it in the window and position it.
    WIN.blit(yellow_health_text, (10, 750))#we draw it in the window and position it.
    pygame.display.update()   

def draw_winner(text):
    winner_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(winner_text, (WIDTH/2 - winner_text.get_width()/2, HEIGHT/2 - winner_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    yellow = pygame.Rect((WIDTH/2)-(YELLOW_SPACESHIP_WIDTH/2)-5, HEIGHT-(YELLOW_SPACESHIP_HEIGHT-2), YELLOW_SPACESHIP_WIDTH, YELLOW_SPACESHIP_HEIGHT)
    yellow_health = 4
    clock = pygame.time.Clock()
    run = True
    # Set up a timer event to update walls every 10 seconds
    pygame.time.set_timer(pygame.USEREVENT + 4, timer_duration * 1000)

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == RED_WALL_HIT_SPACESHIP: 
                yellow_health -= 3
                yellow.y += 150
                # print(yellow_health)
            if event.type == GREEN_WALL_HIT_SPACESHIP: 
                yellow_health +=1
                yellow.y -= 100
                # print(yellow.y)
            if event.type == WHITE_WALL_HIT_SPACESHIP: 
                yellow.y += 200
                # print(yellow.x)
            if event.type == pygame.USEREVENT + 4:  # Triggered every 10 seconds
                update_walls()  # Update wall positions


        winner_text = ""
        if yellow_health <= 0:
            winner_text = "You lose"

        elif yellow.y <= 2:  # Change the condition from `<= 2`because of grren wall
            winner_text = "You win"


        if winner_text != "":
            draw_winner(winner_text)


        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        handle_walls(yellow)
        draw_window(yellow, yellow_health)
        draw_wall(colors_of_walls, array_of_walls)

        pygame.display.update()


    pygame.quit()
    


if __name__ == "__main__":
    main()