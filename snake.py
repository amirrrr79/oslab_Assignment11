import random
import arcade
import math

class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.color = arcade.color.BLUE
        self.speed = 1
        self.width = 16
        self.height = 16
        self.center_x = 250
        self.center_y = 250
        self.change_x = 0
        self.change_y = 0
        self.score = 0
        self.body = []

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,16,16,self.color)
        for i in self.body:
            arcade.draw_rectangle_filled(i[0],i[1],16,16,self.color)
           
    def move(self):
        for i in range(len(self.body)-1, 0, -1):
            self.body[i][0] = self.body[i-1][0]
            self.body[i][1] = self.body[i-1][1]
                
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y
        
        if self.body:
            self.body[0][0] += self.speed * self.change_x
            self.body[0][1] += self.speed * self.change_y

    def eat(self):
        self.body.append([self.center_x,self.center_y])
        self.body.append([self.center_x,self.center_y])
        self.body.append([self.center_x,self.center_y])
        self.body.append([self.center_x,self.center_y])
        self.score+=1
        
        
class Apple(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__('Apple.png')
        self.width = 30
        self.height = 30
        self.center_x = random.randint(10, w)
        self.center_y = random.randint(10, h)

class p(arcade.Sprite):
    def __init__(self, w, h):
        super().__init__('p.png')
        self.width = 30
        self.height = 30
        self.center_x = random.randint(10, w)
        self.center_y = random.randint(10, h) 

class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self, 500, 500, "snake game")
        self.snake = Snake()
        self.apple = Apple(500,500)
        self.p = p(500,500)
        arcade.set_background_color(arcade.color.GREEN)
 
    def on_draw(self):
        arcade.start_render()
    
        self.apple.draw()
        self.snake.draw()
        self.p.draw()
        
        arcade.draw_text('score='+ str(self.snake.score),5,30,arcade.color.BLACK,15)
        if self.snake.score <0 or self.snake.center_x>=500 or self.snake.center_x<=0 or self.snake.center_y>=500 or self.snake.center_y<=0:
            arcade.draw_text('game over',120,250,arcade.color.RED,60)
            self.snake=Snake()
    
        X=0
        Y=0
        if math.sqrt((self.snake.center_x-self.apple.center_x)**2+(self.snake.center_y-self.apple.center_y)**2):
            X=self.apple.center_x
            Y=self.apple.center_y
        
        
        Right=True
        Left=True
        Up=True
        Down=True

        if self.snake.center_x<self.p.center_x and self.snake.center_y==self.p.center_y:
            Right=False
        if self.snake.center_x>self.p.center_x and self.snake.center_y==self.p.center_y:
            Left=False
        if self.snake.center_x==self.p.center_x and self.snake.center_y<self.p.center_y:
            Up=False
        if self.snake.center_x==self.p.center_x and self.snake.center_y>self.p.center_y:
            Down=False

        if  Left and self.snake.center_x>X:
            self.snake.change_x = -1
            self.snake.change_y = 0
            self.snake.move()
        elif Right and  self.snake.center_x <X:
            self.snake.change_x = 1
            self.snake.change_y = 0
            self.snake.move()
        elif Up and self.snake.center_y < Y:
            self.snake.change_y = 1
            self.snake.change_x = 0
            self.snake.move()
        elif Down and self.snake.center_y>Y:
            self.snake.change_y = -1
            self.snake.change_x = 0
            self.snake.move()

        if arcade.check_for_collision(self.snake,self.apple):
            self.apple = Apple(500, 500)
            self.snake.eat()
            
            
   
play_game= Game()
arcade.run()
