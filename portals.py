import pygame
import time
import random
import math
WIDTH=400
HEIGHT=400

pygame.init()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
clock=pygame.time.Clock()
fps=30

fake=pygame.image.load("car.png")

t=0
blue=(0,0,200)
green=(0,200,0)
red=(200,0,0)
orange=(255, 174, 0)
yellow=(251, 255, 0)
purple=(200, 0, 255)
pink=(255, 74, 252)
light_red=(255,0,0)
light_green=(0,255,0)
light_blue=(0,0,255)

black=(0,0,0)
white=(255,255,255)

directions={
    "down":[0,2],
    "right":[2,0],
    "left":[-2,0],
    "up":[0,-2],
    "":[0,0]
    
    }

actual_direction=[
     "down",
    "right",
     "left",
    "up",
     ""
    
    ]

move_directions=[
[0,2],
[2,0],
[-2,0],
[0,-2],
[0,0]
    ]
direction=""
class Player:
    def __init__(self,pos,dimensions,color):
        self.pos=pos
        self.rect=pygame.rect.Rect([pos[0],pos[1],dimensions[0],dimensions[1]])
        self.dimensions=dimensions
        self.img=pygame.image.load("companion_cube.png")
        self.color=color
        self.colliding=False
        self.move_vector=[0,0]
        self.speed=0
    def draw(self):
        self.rect=pygame.rect.Rect([self.pos[0],self.pos[1],self.dimensions[0],self.dimensions[1]])

        screen.blit(self.img,self.rect)
        #pygame.draw.rect(screen,self.color,self.rect)
    def move(self,velocity):
            self.move_vector[0]=velocity[0]
        
            self.move_vector[1]=velocity[1]
    def collide(self,rect,rect1):
     coll=  rect.colliderect(rect1)>0
     return (coll)
    def tp(self,new_pos):
        self.pos=new_pos
    def update(self):
        global direction
        #self.move_vector=[0,0]
        key_pressed=pygame.key.get_pressed()
        push=2
        slow=4
        if key_pressed[pygame.K_RIGHT]:
            self.move([push,0])
            direction="right"
        elif key_pressed[pygame.K_LEFT]:
            self.move([-push,0])
            direction="left"
        elif key_pressed[pygame.K_UP]:
            self.move([0,-push])
            direction="up"
        elif key_pressed[pygame.K_DOWN]:
            self.move([0,push])
            direction="down"
        else:
            pass
        
        for i in self.move_vector:
            if i!=0:
                self.speed=i
        
        collision=pygame.rect.Rect([self.pos[0]+self.move_vector[0],self.pos[1]+self.move_vector[1],self.dimensions[0],self.dimensions[1]])
        move_directions=[
        [0,self.speed],
        [self.speed,0],
        [-self.speed,0],
        [0,-self.speed],
        [0,0]
            ]
        for obj in objects:
            if obj!=self:
                
                self.colliding=self.collide(collision,obj.rect)
                if self.colliding:
                    obj.colliding=True
                    if type(obj)==type(por):
                        
                        if obj.dim[0]==obj.portal.dim[0]:
                             p=obj.portal.pos
                             pos=[]
                             pos.append(p[0])
                             pos.append(p[1])
                             

                             direction=move_directions.index(self.move_vector)
                             direction=actual_direction[direction]

                             if direction=="up":
                                 fake_rect=self.rect
                                 
                                 fake_rect.height=int(fake_rect.height/2)
                                 
                                 img=pygame.image.load("com_d.png")
                             if direction=="down":
                                 fake_rect=self.rect
                                 
                                 fake_rect.height=int(fake_rect.height/2)
                                 fake_rect.y+= fake_rect.height
                                 
                                 img=pygame.image.load("com_u.png")
                             if direction=="right":
                                 fake_rect=self.rect
                                 
                                 fake_rect.width=int(fake_rect.width/2)

                                 fake_rect.x+= fake_rect.width
                                 img=pygame.image.load("com_r.png")
                             if direction=="left":
                                 fake_rect=self.rect
                                 
                                 fake_rect.width=int(fake_rect.width/2)
                                 
                                 img=pygame.image.load("com_l.png")
                            
                           
                             screen.blit(img,fake_rect)
                             #pygame.draw.rect(screen,self.color,self.rect)
                             self.move_vector[0]=-self.move_vector[0]
                             self.move_vector[1]=-self.move_vector[1]
                             pos[0]+=self.move_vector[0]*5
                             pos[1]+=self.move_vector[1]*5
                             self.tp(pos)
                        
                        else:
                            most_v=max(self.move_vector)
                            least_v=min(self.move_vector)
                            most=self.move_vector.index(most_v)
                            least=self.move_vector.index(least_v)
                            direct=move_directions.index(self.move_vector)
                            direction=actual_direction[direct]

                            if direction=="up":
                                 fake_rect=self.rect
                                 
                                 fake_rect.height=int(fake_rect.height/2)
                                 
                                 img=pygame.image.load("com_d.png")
                            if direction=="down":
                                 fake_rect=self.rect
                                 
                                 fake_rect.height=int(fake_rect.height/2)
                                 fake_rect.y+= fake_rect.height
                                 
                                 img=pygame.image.load("com_u.png")
                            if direction=="right":
                                 fake_rect=self.rect
                                 
                                 fake_rect.width=int(fake_rect.width/2)

                                 fake_rect.x+= fake_rect.width
                                 img=pygame.image.load("com_r.png")
                            if direction=="left":
                                 fake_rect=self.rect
                                 
                                 fake_rect.width=int(fake_rect.width/2)
                                 
                                 img=pygame.image.load("com_l.png")
                            
                           
                            screen.blit(img,fake_rect)
                            #pygame.draw.rect(screen,self.color,self.rect)
                            self.move_vector[least]=most_v
                            self.move_vector[most]=least_v
                            p=obj.portal.pos
                            pos=[]
                            pos.append(p[0])
                            pos.append(p[1])
                             

                           
                            
                            pos[0]+=self.move_vector[0]*5
                            pos[1]+=self.move_vector[1]*5
                            self.tp(pos)
                        
                        
                    break
        if self.colliding:
            pass
        else:
            self.pos[0]+=self.move_vector[0]
            self.pos[1]+=self.move_vector[1]
        
        self.draw()

class Portal:
    def __init__(self,pos,dimensions,color,portal=None):
        self.pos=pos
        self.rect=pygame.rect.Rect([pos[0],pos[1],dimensions[0],dimensions[1]])
        self.dimensions=dimensions
        self.default_color=color
        self.color=color
        self.portal=portal
        self.colliding=False

        most_dim=dimensions.index(max(dimensions))
        least_dim=dimensions.index(min(dimensions))

        if most_dim==0 and least_dim==1:
            self.dim="h x w"
        else:
            self.dim="w x h"
            
    def draw(self):
        self.rect=pygame.rect.Rect([self.pos[0],self.pos[1],self.dimensions[0],self.dimensions[1]])
        
        pygame.draw.rect(screen,self.color,self.rect)

    def set_portal(self,portal):
        self.portal=portal
    def colliding(self):
        pass
    def update(self):
        if self.portal!=None:
            pass
        if self.colliding:
            pass
        else:
            self.color=self.default_color
        self.colliding=False
        
        self.draw()
run=True
por=Portal([0,0],[0,0],red)
objects=[]
objects.append(Player([150,150],[10,10],light_blue))

objects.append(Portal([135,90],[20,5],blue))
objects.append(Portal([130,120],[5,20],orange,portal=objects[1]))
objects[1].set_portal(objects[2])

objects.append(Portal([135,40],[20,5],red))
objects.append(Portal([180,120],[5,20],green,portal=objects[3]))
objects[3].set_portal(objects[4])

while run:
    screen.fill(white)
    pygame.display.set_caption("Thinking with portals")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if pygame.mouse.get_pressed()[0]:
            objects[0].pos = list(pygame.mouse.get_pos())
    for obj in objects:
        obj.update()
    clock.tick(fps)
    pygame.display.update()
    pygame.event.pump()
