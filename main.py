import pygame
from snake import Snake
from cherry import Cherry

size = 20
xlim = 21
ylim = 15
width = size * xlim
height = size * ylim + 50

pygame.init()                       # Initialization
black = (0,0,0)
gray = (180,180,180)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
screen  = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake')
gameClose = False
gameOver = False
score = 0
speed = 20
multi = 1
clock = pygame.time.Clock()
snake = Snake((xlim-1)/2, (ylim-1)/2, xlim-1, ylim-1, 0.5, 0)
cherry = Cherry(snake, xlim-1, ylim-1)

msg_font = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 20)

def background(screen):
    screen.fill(white)
    for i in range(0,xlim*ylim,2):
        x = i % xlim
        y = i // xlim
        pygame.draw.rect(screen,gray,[x*size,y*size,size,size])

while not gameClose:
    if gameOver:
        msg1 = msg_font.render("Game Over", True, black)
        screen.blit(msg1, [width / 3 +20, height / 3])
        msg2 = msg_font.render("Press 'Spacebar' to restart", True, black)
        screen.blit(msg2, [width / 6, height / 3 + 20])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameClose = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameOver = False
                    snake = Snake((xlim-1)/2, (ylim-1)/2, xlim-1, ylim-1, 0.5, 0)
                    cherry = Cherry(snake, xlim-1, ylim-1)
                    score = 0
                    speed = 20
                    multi = 1
    else:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameClose = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.yd == 0:
                    snake.moveQueue.append('up')
                elif event.key == pygame.K_DOWN and snake.yd == 0:
                    snake.moveQueue.append('down')
                elif event.key == pygame.K_LEFT and snake.xd == 0:
                    snake.moveQueue.append('left')
                elif event.key == pygame.K_RIGHT and snake.xd == 0:
                    snake.moveQueue.append('right')
        if snake.update(cherry.x, cherry.y):
            cherry = Cherry(snake,xlim-1,ylim-1)
        if snake.check():
            gameOver = True
        background(screen)
        pygame.draw.line(screen,black,(0,height-50),(width,height-50),3)
        pygame.draw.line(screen,black,(0,0),(width,0),3)
        pygame.draw.line(screen,black,(0,0),(0,height-50),3)
        pygame.draw.line(screen,black,(width,0),(width,height-50),3)
        pygame.draw.circle(screen, blue, (snake.body[0][0]*size + size/2, snake.body[0][1]*size + size/2), size/2)
        for i in range(1,snake.len-1):
            a = snake.body[i]
            if snake.body[i-1][0] != snake.body[i+1][0] and snake.body[i-1][1] != snake.body[i+1][1]:
                pygame.draw.circle(screen, blue, (a[0]*size + size/2, a[1]*size + size/2), size/2)
            else:
                pygame.draw.rect(screen,blue, [a[0]*size,a[1]*size,size,size])
        pygame.draw.circle(screen,red,(cherry.x*size + size/2, cherry.y*size + size/2), size/4)
        pygame.draw.circle(screen, green, (snake.x*size + size/2, snake.y*size + size/2), size/2)
        value = score_font.render("Score: " + str((snake.len-3)*10), True, black)
        if snake.len - score > 20*multi+3:
            score = snake.len
            speed += 3
            multi += 0.2
        screen.blit(value,[10, height - 50])
        pygame.display.update()
        clock.tick(speed)

pygame.quit()
quit()