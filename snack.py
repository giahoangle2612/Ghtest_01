import numpy
import time
import random

# Khởi tạo kích thước cửa sổ trò chơi
width = 800
height = 600

# Khởi tạo màu sắc
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Khởi tạo đầu rắn và kích thước ô
snake_block = 10
snake_speed = 30

# Khởi tạo font chữ
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(gameDisplay, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    gameDisplay.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    # Khởi tạo vị trí ban đầu của con rắn
    x1 = width / 2
    y1 = height / 2

    # Khởi tạo biến thay đổi vị trí
    x1_change = 0
    y1_change = 0

    # Khởi tạo đuôi rắn
    snake_List = []
    Length_of_snake = 1

    # Khởi tạo vị trí thức ăn
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Khởi tạo màn hình trò chơi
    pygame.init()
    gameDisplay = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Snake Game')

    # Khởi tạo clock object
    clock = pygame.time.Clock()

    while not game_over:

        while game_close == True:
            gameDisplay.fill(blue)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            # Xử lý sự kiện khi game over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                         # Xử lý sự kiện khi đang chơi game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                     y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Xử lý vị trí mới của đầu rắn
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        gameDisplay.fill(blue)
        pygame.draw.rect(gameDisplay, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Kiểm tra va chạm với đuôi rắn
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        pygame.display.update()

        # Kiểm tra nếu rắn ăn thức ăn
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()

gameLoop()
