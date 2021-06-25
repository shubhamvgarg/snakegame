
import pygame
import random
import os




pygame.init()



white = (255, 255, 255)
red = (255, 0, 0)

black = (0, 0, 0)
green= (168,245,161)
orange = (245,141,16)


screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))



bgimg = pygame.image.load('back.jpg')
bgimg = pygame.transform.scale(bgimg,(screen_width, screen_height)).convert_alpha()
startimg = pygame.image.load('frn2.jpg')
startimg = pygame.transform.scale(startimg,(screen_width, screen_height)).convert_alpha()
lastimg = pygame.image.load('last.jpg')
lastimg = pygame.transform.scale(lastimg,(screen_width, screen_height)).convert_alpha()


pygame.display.set_caption("Dare to Snake With Shubham")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        gameWindow.blit(startimg, (0, 0))
        #text_screen("Welcome to Snakes", black, 260, 250)
        #text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    gameloop()

        pygame.display.update()
        clock.tick(60)



def gameloop():

    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")
    with open("highscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 15
    fps = 60
    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(hiscore))
            gameWindow.fill((10,1,100))
            gameWindow.blit(lastimg, (0, 0))
            #text_screen("Game Over! Press Enter To Continue", orange, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_SPACE:
                        score +=1

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score +=1
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)


                snk_length +=5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg,(0,0))
            text_screen("Score: " + str(score) + "  Hiscore: "+str(hiscore), green, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True


            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True


            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
