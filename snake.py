'''
snake
made in about 6 hours
really fun project, super proud of making this
got inspired by code bullet's video and really simple way to make the snake move
'''

import pygame
import sys
import time
import random
side_length = 400 # pixels
square_size = 20 # pixels

# WORKS ONLY IF SIDE_LENGTH IS DIVISIBLE BY SQUARE_SIZE!!!!

# i hate oop
class Apple:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
    
    def move(self):
        looping = True
        while looping:
            looping = False
            self.x = random.randint(1, int(side_length/square_size) - 2)
            self.y = random.randint(1, int(side_length/square_size) - 2)
            for n in snake_array:
                if n[0] == self.x and n[1] == self.y:
                    looping = True
    
    def thatbirdthatihate(self):
        print("that bird that i hate")

run = 0
high_run = 0
high_score = 0
while True:
    screen = pygame.display.set_mode((side_length, side_length))
    clock = pygame.time.Clock()
    running = True
    snake_array = [[1, 1], [2, 1], [3, 1], [4, 1]]
    snake_direction = "R"
    score = 0
    apple = Apple(1, 1, 20) 
    apple.move()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    if snake_direction != "D":
                        snake_direction = "U"
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if snake_direction != "U":
                        snake_direction = "D"
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if snake_direction != "R":
                        snake_direction = "L"
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if snake_direction != "L":
                        snake_direction = "R"
        
        screen.fill("black")
        # apple draw
        pygame.draw.rect(screen, "red", (apple.x * square_size, apple.y * square_size, apple.size, apple.size))
        # break logic, snake drawing logic. pretty meh O(n^2) time but its the best i can do
        for i in range(len(snake_array)):
            for j in range(len(snake_array)):
                pygame.draw.rect(screen, "green", (snake_array[j][0] * square_size, snake_array[j][1] * square_size, square_size, square_size))
                if snake_array[i] == snake_array[j] and i != j:
                    running = False
        # APPLE LOGIC :grin:
        last_element = snake_array[len(snake_array) - 1] 
        if last_element[0] == apple.x and last_element[1] == apple.y:
            score += 1
            apple.move()
            apple.thatbirdthatihate() # necessary for good luck (will make sure the code always runs perfectly, no bug-fixing needed)

            # snake logic
            movement_x = snake_array[0][0] - snake_array[1][0]
            movement_y = snake_array[0][1] - snake_array[1][1]
            snake_array = [[snake_array[0][0] + movement_x, snake_array[0][1] + movement_y]] + snake_array
        
        # annoying ahh diddy blud ahh mobility ahh aphug reference ahh logic 67 gurt this gotta be the most shoegaze rug oat musstard kendrick lamar drake "must be the third! heh! mustard!" :skull_crossbones:
        if snake_direction == "U":
            last_element = snake_array[len(snake_array) - 1]
            new_snake_array = snake_array[1:]
            new_snake_array += [[last_element[0], last_element[1] - 1]]
            snake_array = new_snake_array
            print(snake_array)
        elif snake_direction == "D":
            last_element = snake_array[len(snake_array) - 1]
            new_snake_array = snake_array[1:]
            new_snake_array += [[last_element[0], last_element[1] + 1]]
            snake_array = new_snake_array
            print(snake_array)
        elif snake_direction == "L":
            last_element = snake_array[len(snake_array) - 1]
            new_snake_array = snake_array[1:]
            new_snake_array += [[last_element[0] - 1, last_element[1]]]
            snake_array = new_snake_array
            print(snake_array)
        elif snake_direction == "R":
            last_element = snake_array[len(snake_array) - 1]
            new_snake_array = snake_array[1:]
            new_snake_array += [[last_element[0] + 1, last_element[1]]]
            snake_array = new_snake_array
            print(snake_array)
        
        for i in range(2): # for loop, looks nice and is easy to edit compared to two if statements. i am superior
            if last_element[i] <= 0 or last_element[i] >= side_length/square_size - 1:
                running = False
        

        # top left corner used for x-y values for rects, js like p5.js (get it?? :joy_cat:) also this takes priority when drawing
        pygame.draw.rect(screen, "blue", (0, 0, side_length, square_size))
        pygame.draw.rect(screen, "blue", (side_length - square_size, 0, square_size, side_length))
        pygame.draw.rect(screen, "blue", (0, side_length - square_size, side_length, square_size))
        pygame.draw.rect(screen, "blue", (0, 0, square_size, side_length))
        pygame.display.flip()

        clock.tick(side_length/30) # speed of the snake is proportional to the size of the screen
    pygame.quit()
    run += 1
    if score > high_score:
        high_score = score
        high_run = run
    print(f"Apples Eaten in Run {run}: {score}")
    print(f"Best Run - Run {high_run}, {high_score} apples eaten")
    time.sleep(2)