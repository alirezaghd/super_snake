import pygame ,sys
import random
import time



pygame.init()

class Bomb:

    def __init__(self):
        #self.r = 5
        self.img = pygame.image.load('E:/Python Online/Jalase 11/super_snake/bomb.png')
        self.x = random.randint(0,width - 10)
        self.y = random.randint(0,height - 10)
        self.color = (200,0,0)
        #pygame.draw.circle(display,self.color, [self.x,self.y ], self.r)

    def show(self):
        
        self.img = pygame.transform.scale(self.img,(28,28))
        self.area = display.blit(self.img,(self.x,self.y))

class Apple:

    def __init__(self):
        self.img = pygame.image.load('E:/Python Online/Jalase 11/super_snake/apple.png')
        self.x = random.randint(0,width - 20)
        self.y = random.randint(0,height - 20)
        self.color = (200,0,0)
        

    def show(self):
        
        self.img = pygame.transform.scale(self.img,(28,28))
        self.area = display.blit(self.img,(self.x,self.y))

class Pear:

    def __init__(self):
        #self.r = 5
        self.img = pygame.image.load('E:/Python Online/Jalase 11/super_snake/pear.png')
        self.x = random.randint(0,width-20)
        self.y = random.randint(0,height-20)
        self.color = (200,0,0)
        #pygame.draw.circle(display,self.color, [self.x,self.y ], self.r)

    def show(self):
        self.img = pygame.transform.scale(self.img,(28,28))
        self.area = display.blit(self.img,(self.x,self.y))
    




class Snake:
    def __init__(self):
        self.w = 20
        self.h = 20
        self.x = width / 2
        self.y = height / 2
        self.name = 'Snake '
        self.body_color =pygame.image.load('E:/Python Online/Jalase 11/super_snake/snake.png')
        self.head_color = pygame.image.load('E:/Python Online/Jalase 11/super_snake/snake1.png')
        self.speed = 20
        self.score = 0
        self.x_change = 0
        self.y_change = 0
        self.body = []
        self.font = pygame.font.SysFont(None,30)
        self.time = 0
        self.length = 1
        self.fps = 10

        
           
    def draw_body(self):
        self.body_color = pygame.transform.scale(self.body_color,(20,20))

        self.body_area =[self.x , self.y]
        self.body.append(self.body_area)
        for body in self.body :
            #self.area = pygame.draw.rect(display,(250,0,0),(body[0],body[1],self.w,self.h))
            self.area = display.blit(self.body_color,(body[0] ,body[1]))

            if len(self.body) > self.length:
                del(self.body[0])


    def eat(self):
        self.score += 1
            
    
    def score_display(self):
        
        text_surf = self.font.render('score : '+ str(self.score),True,(255,0,0))
        display.blit(text_surf, (380,15))
    
    def play_time(self):
        
        count_time = self.font.render('FPS : ' + str(self.fps),True,(255,0,0))
        display.blit(count_time, (20,15))

        
    
    def game_over(self):
        if self.score < 0 :
            self.font = pygame.font.SysFont(None,100)
            text_surf = self.font.render('Game Over : ',True,(255,0,0))
            display.blit(text_surf, (380,380))
        
    def difficulty(self):
        
        self.fps += 1

               

    def move(self):
        if self.x_change == -1 :
            self.x -= self.speed 

        elif self.x_change == 1 :
            self.x += self.speed

        elif self.y_change == -1 :
            self.y -= self.speed
        
        elif self.y_change == 1 :
            self.y += self.speed



if __name__ == "__main__":
    
    
    width = 800
    height = 600
    user_text = ''
    display = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Snake')
    img_gameover = pygame.image.load('E:/Python Online/Jalase 11/super_snake/gameover.jpg')
    snake = Snake()
    apple = Apple()
    pear = Pear()
    bomb = Bomb()
    
    run = True

    while run:
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN :


                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    snake.x_change = -1
                    snake.y_change = 0
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    snake.x_change = 1
                    snake.y_change = 0

                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    snake.y_change = -1
                    snake.x_change = 0
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN :
                    snake.y_change = 1
                    snake.x_change = 0
                elif event.key == pygame.K_ESCAPE :
                    exit()
                elif event.key == pygame.K_p:
                    snake.move()
                

        
        snake.move()
        
        display.fill((64,64,64))
        
        snake.draw_body()
        apple.show()
        pear.show()
        bomb.show()
        snake.score_display()

        if snake.x < 0:
            snake.x = width
        if snake.x > width:
            snake.x = 0
        if snake.y < 0:
            snake.y = height
        if snake.y > height:
            snake.y = 0
        
        if snake.area.colliderect(apple.area):
            snake.score += 1
            snake.length += 1
            
            apple = Apple()
        
        elif snake.area.colliderect(pear.area):
            snake.score += 2
            snake.length += 2
            
            pear = Pear()

        elif snake.area.colliderect(bomb.area):
            snake.score -= 1
            snake.length -= 1
            bomb = Bomb()
        
        
        
        if snake.score > 5 :
            snake.fps = 15
        if snake.score > 10 :
            snake.fps = 20   
        if snake.score > 15 :
            snake.fps = 25
            pygame.draw.rect(display,(0,180,0),(1,1,800,600),15)
            pygame.display.flip()
        
        if snake.score < 0 :
            img = pygame.transform.scale(img_gameover,(800,600))
            display.blit(img,(0,0))
            font = pygame.font.SysFont(None,50)
            text = font.render('please insert P for play again', True, (255,255,255))
            display.blit(text, (170,80))
            pygame.display.flip()
            time.sleep(10)
            run = False
 
 

        
        snake.play_time()
        pygame.display.update()
        
        clock.tick(snake.fps)





