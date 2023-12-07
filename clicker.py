from pygame import *
from time import sleep
init()
timer = 0
points = 0
background = background = transform.scale(image.load('R.jpg'), (700, 500))
display.set_caption("Clicker")
window = display.set_mode((700, 500))
clock = time.Clock()
points3 = False
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def colliderect(self, rect):
        return self.rect.colliderect(rect)

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()


        

font1 = font.Font(None, 50)





player = Player("amongus.png", 300, 400, 80, 80, 5)
points2 = False
game = True
while game:
    
    window.blit((background), (0, 0))
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:                    
                if points2 == True:
                    points += 2
                elif points3 == True:
                    points += 5
                elif points2 == True and points3 == True:
                    points += 7
                else:
                    points += 1
                if player.rect.y >= 0:
                    player.rect.y -= 1
                if player.rect.y < 0:
                    player.rect.y = 450
                
            if e.key == K_1:
                if points2 == False and points >= 10:
                    points -= 10
                    points2 = True
                else:
                    print('Error')

            if e.key == K_2:
                if points3 == False and points >= 15:
                    points -= 15
                    points3 = True
                else:
                    print('Error')

    remaning = font1.render(
                'Points: ' + str(points), True, (255, 255, 255)
            )
    window.blit(remaning, (0, 100))

    
   
    player.draw()
    player.update()
    timer += 1
    clock.tick(60)
    display.update()