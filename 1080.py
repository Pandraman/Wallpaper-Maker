import pygame,random,time,os

from pygame.constants import K_ESCAPE, K_KP_ENTER, K_SPACE

Tree_seed = []
Clock = pygame.time.Clock()
VER = 0.1
WIDTH,HEIGHT = 1080,720
Main = True
dir = 0
x,y = -1,HEIGHT/2-200
Tree_seed = random.randint(0,100)
WIN = pygame.display.set_caption("Landschaftsgenerator")
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
Tree = pygame.transform.scale(pygame.image.load("1.png"),(20,50))
while Main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN and not event.key == K_ESCAPE and not event.key == pygame.K_SPACE:
            x = -1
            y = WIDTH/2
            dir = 0
            WIN.fill((166,213,223))
            Tree = pygame.transform.scale(pygame.image.load("1.png"),(20,50))
            for j in range(7):
                x = -1
                Tree_seed = []
                y = WIDTH/2-random.randint(-100,100)
                Tree = pygame.transform.scale(pygame.image.load(str(j+1)+".png"),(20+j*10,50+j*10))
                dir = 3
                for i in range(int(WIDTH)):
                    Treeshhold = 90
                    Tree_seed.append(random.randint(0,100))
                    
                    Tree_set = Tree_seed[i]
                    if Tree_set > 98.5:
                        WIN.blit(Tree,(x-Tree.get_size()[0]/2,y-(Tree.get_size()[1]-12*j)))
                        WIN.set_colorkey((0,0,0))
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            pygame.quit()
                    
                    x += 1
                    y += dir/10
                    dir += random.uniform(1.0,-1.0)
                    
                    pygame.draw.rect(WIN,(22+25-j*5,38+25-j*5,53+25-j*5),pygame.Rect(x,y,1,(HEIGHT-y)+1))
                    
                    pygame.display.update()
        if event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
        if event.type == pygame.KEYDOWN and event.key == K_SPACE:
            time_lt = time.localtime()
            os.chdir('output')
            img = time.strftime("%B-%d-%Y-%H-%M-%S", time_lt)
            pygame.image.save(WIN, img+".png")
            print(img+".png")
