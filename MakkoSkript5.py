# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 13:29:52 2019

@author: Viktor
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 19:42:10 2019

@author: Filip
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:37:53 2019

@author: Filip, Markus og Philip

Versjon: 5.2.3

Credits er i et annet ark
Ting som må fikses:
    Boss og bosstage - Tegnet begge ferdig
    Kommentere all tekst :)
"""

import pygame
import random
pygame.init()

clock = pygame.time.Clock()

s_height = 500
s_width = 1000
win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption("Markus, The Fierce warrior")
fights = [True, False, False, False, False, False, False, False, False, False]

room = 1 #Styrer rommet man er i

songs = ['Musikk.mid','BossMusikk.mid']

#Info til fil
file = open('Highscore.txt','a')

retning = [0,1,2,3,4]
walkRight = [pygame.image.load("R12.png"), pygame.image.load("R22.png"), pygame.image.load("R32.png"), pygame.image.load("R42.png")]
walkDown = [pygame.image.load("F12.png"), pygame.image.load("F22.png"), pygame.image.load("F32.png"), pygame.image.load("F42.png")]
walkLeft = [pygame.image.load("L12.png"), pygame.image.load("L22.png"), pygame.image.load("L32.png"), pygame.image.load("L42.png")]
walkUp = [pygame.image.load("B12.png"), pygame.image.load("B22.png"), pygame.image.load("B32.png"), pygame.image.load("B42.png")]
kister = [pygame.image.load("Kiste.png"), pygame.image.load("KisteÅpen.png")]
kniver = [pygame.image.load("KnivH.png"),pygame.image.load("KnivV.png"),pygame.image.load("KnivN.png"),pygame.image.load("KnivO.png")]
hjerter = [pygame.image.load("Hjerte.png"),pygame.image.load("HjerteTom.png")]
firespirit = [pygame.image.load("Fire1.png"),pygame.image.load("Fire2.png"),pygame.image.load("Fire3.png")]
icespirit = [pygame.image.load("IceElement1.png"),pygame.image.load("IceElement2.png"),pygame.image.load("IceElement3.png")]
spawnx = [50,900]
spawny = [50,400]

class player(object):
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 8
        self.health = health
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.middle_x = self.x + (self.width/2)
        self.middle_y = self.y + (self.height/2)
        self.walkCount = False
        self.standing = False
        self.left = 0
        self.right = 0
        self.down = 0
        self.up = 0
    
    def draw(self, win): #Bestemmer hvilken sprite og loop som skal vises
#        self.hitbox = (self.x + 5, self.y + 7, 33, 40) #Synlig hitbox 
#        pygame.draw.rect(win, (255,0,0), self.hitbox,2) #Kan kommenteres ut

        if self.walkCount + 1 >= 8:
            self.walkCount = 0
        
        if not (self.standing): #Retningene som den skal gå i og koordinaene    
            if self.left == 1:
                win.blit(walkLeft[self.walkCount//2], (self.x,self.y))
                self.walkCount += 1                          
           
            elif self.right == 1:
                win.blit(walkRight[self.walkCount//2], (self.x,self.y))
                self.walkCount += 1
            
            elif self.down == 1:
                win.blit(walkDown[self.walkCount//2], (self.x,self.y))
                self.walkCount += 1
            
            elif self.up == 1:
                win.blit(walkUp[self.walkCount//2], (self.x,self.y))
                self.walkCount += 1
        else:
            if self.right == 1:
                win.blit(walkRight[0], (self.x,self.y))
            elif self.up == 1:
                win.blit(walkUp[0], (self.x,self.y))
            elif self.left == 1:
                win.blit(walkLeft[0], (self.x,self.y))
            elif self.down == 1:
                win.blit(walkDown[0], (self.x,self.y))
                
    def hit(self):
        for fiende in enemies:
            if self.delay == 0:
                if (fiende.x < self.x < fiende.x + fiende.width or fiende.x < self.x + self.width < fiende.x + fiende.width) and (fiende.y < self.y < fiende.y + fiende.height or fiende.y < self.y + self.height < fiende.y + fiende.width):
                    if self.x + self.width/2 > fiende.x + fiende.width/2:
                        if self.x < s_width - self.width - 150:
                            self.x += 100
                        else:
                            self.x = s_width - self.width - 50
                    elif self.x + self.width/2 < fiende.x + fiende.width/2:
                        if self.x > 150:
                            self.x -= 100
                        else:
                            self.x = 50
                            
                    if self.y + self.height/2 > fiende.y + fiende.height/2:
                        if self.y < s_height - self.height - 100:
                            self.y += 50
                        else:
                            self.y = s_height - self.height - 50
                    elif self.y + self.height/2 < fiende.y + fiende.height/2:
                        if self.y > 100:
                            self.y -= 50
                        else:
                            self.y = 50
                    self.delay = 27
            
            
class knife(object):
    def __init__(self):
        self.radius = 10
        self.retning = retning
        self.vel = 15
        self.width = 10
        self.height = 10
        self.delay = 0
        if man.left == 1:
            self.retning = 1
            self.x = man.x - 10
            self.y = man.y + 20
        elif man.right == 1:
            self.retning = 2
            self.x = man.x + man.width + 10
            self.y = man.y + 20
        elif man.up == 1:
            self.retning = 4
            self.x = man.x + man.width/2
            self.y = man.y - 10
        else:
            self.retning = 3
            self.x = man.x + man.width/2
            self.y = man.y + man.height + 10
        
        
    def draw(self,win):
#        [pygame.image.load("KnivV.png"), pygame.image.load("KnivH.png"), pygame.image.load("KnivN.png"), pygame.image.load("KnivO.png")]
        if self.retning == 1:
            kniv = pygame.image.load("KnivV.png")
            win.blit(kniv,(self.x,self.y))
        elif self.retning == 2:
            kniv = pygame.image.load("KnivH.png")
            win.blit(kniv,(self.x,self.y))
        elif self.retning == 3:
            kniv = pygame.image.load("KnivN.png")
            win.blit(kniv,(self.x,self.y))
        elif self.retning == 4:
            kniv = pygame.image.load("KnivO.png")
            win.blit(kniv,(self.x,self.y))
        
    
    def move(self):
        if self.retning == 1:
            if self.x <= 0:
                kniver.pop(kniver.index(self))
                pass
            else:
                self.x -= self.vel
                pass
        
        if self.retning == 2:
            if self.x >= s_width:
                kniver.pop(kniver.index(self))
                pass
            else:
                self.x += self.vel
                pass
        
        if self.retning == 3:
            if self.y >= s_height:
                kniver.pop(kniver.index(self))
                pass
            else:
                self.y += self.vel
                pass
        
        if self.retning == 4:
            if self.y <= 0:
                kniver.pop(kniver.index(self))
                pass
            else:
                self.y -= self.vel
                pass

class key(object):
    def __init__(self, color, x, y, width, height):
        self.x = x
        self.y = y
        self.color = color
        self.height = height
        self.width = width        
        self.show = False       
        self.open = False
        self.hitbox = (self.x, self.y, self.width, self.height)
   
    def draw(self, win):
#        pygame.draw.rect(win, (self.color), (self.x, self.y, self.height, self.width))
        nøkkel = pygame.image.load("Nøkkel.png")
        win.blit(nøkkel,(self.x,self.y))

class doorUp(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 10
        self.color = (150, 75, 0)
        self.locked = True
   
    def draw(self, win):
        pygame.draw.rect(win, (self.color), (self.x, self.y, self.width, self.height))

class doorSide(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 100
        self.color = (150, 75, 0)
        self.locked = True
   
    def draw(self, win):
        pygame.draw.rect(win, (self.color), (self.x, self.y, self.width, self.height))
class hjerte(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
    
    def draw(self,win):
        hjerter = pygame.image.load("Hjerte.png")
        win.blit(hjerter,(self.x,self.y))
        
class tomhjerte(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
    
    def draw(self,win):
        tomhjerter = pygame.image.load("HjerteTom.png")
        win.blit(tomhjerter,(self.x,self.y))
        
class power(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def draw(self,win):
        powerup = pygame.image.load("PowerUp.png")
        win.blit(powerup,(self.x,self.y))
        
class damageicon(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def draw(self,win):
        powerup2 = pygame.image.load("DamageUp.png")
        win.blit(powerup2,(self.x,self.y))
          
gethe = True
getpo = True 
getda = True    
class chest(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.open = False
        self.width = 25
        self.height = 25
        
    def draw(self,win):
        if self.open == False:
            kiste = kister[0]
            win.blit(kiste,(self.x,self.y))
        elif self.open == True:
            kiste = kister[1]
            win.blit(kiste,(self.x,self.y))

class enemy(object):
    def __init__(self, x, y, width, height, vel, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.health = health
#        self.type = types
        
    def draw(self, win):
        if room == 7 or room == 8 or room == 9:
            enemy = icespirit[enemy_delay//10]
        else:
            enemy = firespirit[enemy_delay//10]
        win.blit(enemy,(self.x,self.y))
        pygame.draw.rect(win, (255,0,0), (self.x + 5, self.y - 15, 54, 10)) #Rød healthbar
        pygame.draw.rect(win, (0,255,0), (self.x + 5, self.y - 15, self.health, 10)) #Grønn healthbar
#        pygame.draw.rect(win, (0,200,0), (self.x + 5, self.y + 5, self.width, self.height), 2)
        
    def move(self):
        if man.y + 25 < self.y < man.y + man.height - 25 or man.y + 25 < self.y + self.height < man.y + man.height - 25 or man.y < self.y + self.height/2 < man.y + man.height:
            if self.x < man.x:
                self.x += self.vel
            else:
                self.x -= self.vel
        elif man.x + 25 < self.x < man.x + man.width - 25 or man.x + 25 < self.x + self.width < man.x + man.width - 25 or man.x < self.x + self.width/2 < man.x + man.width:
            if self.y < man.y:
                self.y += self.vel
            else:
                self.y -= self.vel
    
        else:
            if self.x + self.width/2 < man.x + (man.width/2) and self.y + self.height/2 < man.y + (man.height/2):
                self.x += (self.vel**2/2)**0.5
                self.y += (self.vel**2/2)**0.5
            elif self.x + self.width/2 < man.x + (man.width/2) and self.y + self.height/2 > man.y + (man.height/2):
                self.x += (self.vel**2/2)**0.5
                self.y -= (self.vel**2/2)**0.5
            elif self.x + self.width/2 > man.x + (man.width/2) and self.y + self.height/2 < man.y + (man.height/2):
                self.x -= (self.vel**2/2)**0.5
                self.y += (self.vel**2/2)**0.5
            elif self.x + self.width/2 > man.x + (man.width/2) and self.y + self.height/2 > man.y + (man.height/2):
                self.x -= (self.vel**2/2)**0.5
                self.y -= (self.vel**2/2)**0.5

class Boss(object):
    def __init__(self, x, y, height, width, health):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.health = health
        self.atkpattern = 0
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.starthealth = health
        self.manplacement = 0
        self.newmanplacement = 1
    
    def move():
        pass
    
    def search(self):
        
        for i in range(1,6):
            if s_start_x + x_zone*i <= man.x + man.width/2 <= s_end_x - x_zone*i:
                if s_start_y + y_zone*(i-1) <= man.y + man.height/2<= s_start_y + y_zone*i:
                    
                    self.newmanplacement = "N"
                if s_end_y - y_zone*(i-1) >= man.y + man.height/2 >= s_end_y - y_zone*i:
                    self.newmanplacement = "S"
            if s_start_y + y_zone*(i-1) <= man.y + man.height/2 <= s_end_y - y_zone*(i-1):
                if s_start_x + x_zone * (i - 1) <= man.x + man.width/2 <= s_start_x + x_zone * i:
                    self.newmanplacement = "W"
                if s_end_x - x_zone * (i - 1) >= man.x + man.width/2 >= s_end_x - x_zone *i:
                    self.newmanplacement = "E"
        
        if self.newmanplacement == self.manplacement:
            reset_delay()
        self.manplacement = self.newmanplacement
        
        self.attack()
    def attack(self):
        if self.atkpattern == 1:
            projectiles.append(Boss_projectiles(self.manplacement, self.atkpattern, 0))
        elif self.atkpattern == 2:
            for nummer in range(6):
                projectiles.append(Boss_projectiles(self.manplacement, self.atkpattern, nummer))
    def draw(self):
        Mainboss = pygame.image.load("Boss.png")
        win.blit(Mainboss,(self.x,self.y))
        pygame.draw.rect(win, (255,0,0), (200, 5, self.starthealth, 10))
        pygame.draw.rect(win, (0,255,0), (200, 5, self.health, 10))
    
    def spawn():
        enemies.append(enemy(random.choice(spawnx), random.choice(spawny), 40, 50, 3, 54))

class Boss_projectiles(object):
    def __init__(self, retning, atkpattern, nummer):
        self.vel = 3
        self.retning = retning
        self.atkpattern = atkpattern
        self.nummer = nummer
        self.hjørne = hjørne_koordinater[self.retning][self.nummer]
            
        if self.atkpattern == 1:
            self.koordinat = koordinater[self.retning]
            self.width = self.koordinat[2]
            self.height = self.koordinat[3] 
        elif self.atkpattern == 2:
            self.koordinat = koordinater[self.hjørne]
            self.vel *= 2
        self.x = self.koordinat[0]
        self.y = self.koordinat[1]
        
        if self.atkpattern == 2 and (self.nummer == 1 or self.nummer == 4):
            self.height = 15
            self.width = 15
        elif self.atkpattern == 2:
            self.square_x = self.koordinat[0] - 3.5 
            self.square_y = self.koordinat[1] - 3.5
            self.square_width = 7
            self.square_height = 7
            
    def draw(self):
        if self.atkpattern == 1:
            pygame.draw.rect(win, (255,0,0), (self.x, self.y, self.width, self.height))
        elif self.atkpattern == 2 and (self.nummer == 1 or self.nummer == 4):
            pygame.draw.rect(win, (0,255,0), (self.x, self.y, self.width, self.height))
        elif self.atkpattern == 2:
            pygame.draw.circle(win, (0,0,255), (round(self.x), round(self.y)), 5)

    def move(self):
        if self.atkpattern == 1:
            if self.retning == "N":
                self.y -= self.vel/2
            elif self.retning == "S":
                self.y += self.vel/2
            elif self.retning == "W":
                self.x -= self.vel
            elif self.retning == "E":
                self.x += self.vel
            
        elif self.atkpattern == 2:
            if self.hjørne == "TR":
                self.x += (self.vel/2)**0.5
                self.y -= (self.vel/2)**0.5
            elif self.hjørne == "TL":
                self.x -= (self.vel/2)**0.5
                self.y -= (self.vel/2)**0.5
            elif self.hjørne == "BR":
                self.x += (self.vel/2)**0.5
                self.y += (self.vel/2)**0.5
            elif self.hjørne == "BL":
                self.x -= (self.vel/2)**0.5
                self.y += (self.vel/2)**0.5
            elif self.hjørne == "TBR":
                self.x += 2*((self.vel/3)**0.5)
                self.y -= ((self.vel/3)**0.5)
            elif self.hjørne == "TTR":
                self.x += ((self.vel/3)**0.5)
                self.y -=  2*((self.vel/3)**0.5)
            elif self.hjørne == "TBL":
                self.x -=  2*((self.vel/3)**0.5)
                self.y -= ((self.vel/3)**0.5)
            elif self.hjørne == "TTL":
                self.x -= ((self.vel/3)**0.5)
                self.y -=  2*((self.vel/3)**0.5)
            elif self.hjørne == "BTR":
                self.x += 2*((self.vel/3)**0.5)
                self.y += ((self.vel/3)**0.5)
            elif self.hjørne == "BBR":
                self.x += ((self.vel/3)**0.5)
                self.y +=  2*((self.vel/3)**0.5)
            elif self.hjørne == "BTL":
                self.x -= 2*((self.vel/3)**0.5)
                self.y += ((self.vel/3)**0.5)
            elif self.hjørne == "BBL":
                self.x -= ((self.vel/3)**0.5)
                self.y += 2*((self.vel/3)**0.5)
    
    def hit(self):
        if self.atkpattern == 1 or self.atkpattern == 2 and (self.nummer == 1 or self.nummer == 4): 
            if man.x <= self.x <= man.x + man.width or man.x <= self.x + self.width <= man.x +man.width:
                if man.y <= self.y <= man.y + man.height or man.y <= self.y + self.height <= man.y +man.height:
                    projectiles.remove(projectile)
                    man.health -= 1
            elif s_start_x >= self.x or s_end_x <= self.x + self.width:
                projectiles.remove(projectile)
            elif s_start_y >= self.y or s_end_y <= self.y + self.height:
                projectiles.remove(projectile)
        elif self.atkpattern == 2:
            if man.x <= self.square_x <= man.x + man.width or man.x <= self.square_x + self.square_width <= man.x +man.width:
                if man.y <= self.square_y <= man.y + man.height or man.y <= self.square_y + self.square_height <= man.y +man.height:
                    projectiles.remove(projectile)
                    man.health -= 1
            elif s_start_x >= self.square_x or s_end_x <= self.square_x + self.square_width:
                projectiles.remove(projectile)
            elif s_start_y >= self.square_y or s_end_y <= self.square_y + self.square_height:
                projectiles.remove(projectile)

enemies =  []
win_color = ((255, 255, 255)) #Bakgrunnsfarge i rom 1
 
random1 = random.randint(100, 900)
random2 = random.randint(100, 400)
random3 = random.randint(100, 900)
random4 = random.randint(100, 400)

man = player(460, 220, 40, 45, 3) #Informasjon om spiller x, y, width, height, health

#enemy1 = enemy(800, 250, 30, 30, 3, 54) # x, y, width, height, vel, health

liv1 = hjerte(30,30)
tomliv1 = tomhjerte(30,30)
liv2 = hjerte(50,30)
tomliv2 = tomhjerte(50,30)
liv3 = hjerte(70,30)
tomliv3 = tomhjerte(70,30)
liv4 = hjerte(90,30)

powerUp = power(900,30)

damageUp = damageicon(830,30)

kiste1 = chest(470,220)
kiste2 = chest(470,220)
kiste3 = chest(470,220)

key1 = key((255,0,0), random1, random2, 30, 17)  #Verdiene til nøklene på de forskjellige verdene
key2 = key((255,0,0), random3, random4, 30, 17)
key3 = key((255,0,0), random1, random2, 30, 17)
key4 = key((255,0,0), random3, random4, 30, 17)
key5 = key((255,0,0), random1, random2, 30, 17)
key6 = key((255,0,0), random3, random4, 30, 17)
key7 = key((255,0,0), random1, random2, 30, 17)
key8 = key((255,0,0), random3, random4, 30, 17)
key9 = key((255,0,0), random1, random2, 30, 17) #Lage en nøkkel som ser mer spess ut som er for bossen!

door1 = doorUp(s_width/2 - 50, 0) #Plasseringen til dørene på skjermen
door2 = doorUp(s_width/2 - 50, 0)
door3 = doorSide(s_width - 10, s_height/2 - 50)
door4 = doorSide(s_width - 10, s_height/2 - 50)
door5 = doorSide(s_width - 10, s_height/2 - 50)
door6 = doorSide(0, s_height/2 - 50)
door7 = doorSide(0, s_height/2 - 50)
door8 = doorSide(0, s_height/2 - 50)
door9 = doorUp(s_width/2 - 50, s_height - 10)

s_end_x = 1000
s_end_y = 500
s_start_x = 0
s_start_y = 0
Bosses = False
delay = 0

telle = True
antall = 1
def enemy_create(antall):
    global telle
    if telle:
        for z in range(antall):
            enemies.append(enemy(random.choice(spawnx), random.choice(spawny), 40, 50, 3, 54))
            telle = False

drepte_enemies = 0            
def redrawGamewindow():
     global win_color
     win.fill(win_color) 
     win.blit(bg,(0,0))
     
     enemy_create(antall)
     global drepte_enemies
     for fiende in enemies:
            if fiende.health <= 0:
                enemies.remove(fiende)
                drepte_enemies += 1
       
     for fiende in enemies:
         fiende.draw(win)
     
     for kniv in kniver:
         knife.draw(kniv,win)
         
     if room == 3 and kiste1.open == True:
        kiste1.draw(win)
     elif room == 3 and kiste1.open == False and len(enemies) == 0:
        kiste1.draw(win)
    
     if room == 6 and kiste2.open == True and len(enemies) == 0:
         kiste2.draw(win)
     elif room == 6 and kiste2.open == False and len(enemies) == 0:
         kiste2.draw(win)
        
     if room == 9 and kiste3.open == True and len(enemies) == 0:
         kiste3.draw(win)
     elif room == 9 and kiste3.open == False and len(enemies) == 0:
         kiste3.draw(win) 
     
     if kiste3.open == True:
         powerUp.draw(win)
       
     if kiste2.open == True:
         damageUp.draw(win) 
         
     if Bosses == True:
        Main_Boss.draw()
        
        for projectile in projectiles:
            projectile.draw()
    
     man.draw(win)
    
     if man.health == 3:
        liv1.draw(win)
        liv2.draw(win)
        liv3.draw(win)
     elif man.health == 2:
        liv1.draw(win)
        liv2.draw(win)
        tomliv3.draw(win)
     elif man.health == 1:
        liv1.draw(win)
        tomliv2.draw(win)
        tomliv3.draw(win)
     elif man.health == 4:
        liv1.draw(win)
        liv2.draw(win)
        liv3.draw(win)
        liv4.draw(win)
    
     if room == 1:
        platform(0, 0, 25, s_height)   
        platform(s_width - 25, 0, 25, s_height)
        platform(s_width/2 + 50, 0, s_width/2 - 50, 25)
        platform(0, 0, s_width/2 - 50, 25)
        platform(s_width/2 + 50, s_height - 25, s_width/2 - 50, 25)
        platform(0, s_height - 25, s_width/2 - 50, 25)
        
        win_color = (255, 255, 255)
        if door9.locked:
            door9.draw(win)
        if door1.locked:
            door1.draw(win)
        if key1.show:
            key1.draw(win)  
     if room == 2:
        platform(s_width/2 + 50, 0, s_width/2 - 50, 25)
        platform(0, 0, s_width/2 - 50, 25)
        platform(s_width/2 + 50, s_height - 25, s_width/2 - 50, 25)
        platform(0, s_height - 25, s_width/2 - 50, 25)
        platform(s_width - 25, 0, 25, s_height/2 - 50)
        platform(s_width - 25, s_height/2 + 50, 25, s_height/2 - 50)
        platform(0, 0, 25, s_height/2 - 50)
        platform(0, s_height/2 + 50, 25, s_height/2 - 50)
        
        win_color = (128, 128, 128)
        if door6.locked:
            door6.draw(win)
        if door2.locked:
            door2.draw(win)
        if door3.locked:
            door3.draw(win)
        if key2.show:
            key2.draw(win)
     if room == 3:
        platform(0, 0, 25, s_height)   
        platform(s_width - 25, 0, 25, s_height)
        platform(0, 0, s_width, 25)    
        platform(0, s_height - 25, s_width/2 - 50, 25)
        platform(s_width/2 + 50, s_height - 25, s_width/2 - 50, 25)
        
       
        win_color = (200, 128, 24) 
        if key3.show:
            key3.draw(win)
     if room == 4:
        platform(0, 0, s_width, 25)           
        platform(0, s_height - 25, s_width, 25)
        platform(s_width - 25, 0, 25, s_height/2 - 50)
        platform(s_width - 25, s_height/2 + 50, 25, s_height/2 - 50)
        platform(0, 0, 25, s_height/2 - 50)
        platform(0, s_height/2 + 50, 25, s_height/2 - 50)
        
        win_color = (200, 100, 100) 
        if door4.locked:
            door4.draw(win)
        if key3.show:
            key4.draw(win)
     if room == 5:
        platform(0, 0, s_width, 25)          
        platform(0, s_height - 25, s_width, 25)
        platform(s_width - 25, 0, 25, s_height/2 - 50)
        platform(s_width - 25, s_height/2 + 50, 25, s_height/2 - 50)
        platform(0, 0, 25, s_height/2 - 50)
        platform(0, s_height/2 + 50, 25, s_height/2 - 50)
        win_color = (100, 200, 100)
        if door5.locked:
            door5.draw(win)
        if key5.show:
            key5.draw(win)
     if room == 6:
        platform(0, 0, s_width, 25)          
        platform(0, s_height - 25, s_width, 25)
        platform(s_width - 25, 0, 25, s_height)
        platform(0, 0, 25, s_height/2 - 50)
        platform(0, s_height/2 + 50, 25, s_height/2 - 50)
        
        win_color = (0, 0, 0)
        if key6.show:
            key6.draw(win)
     if room == 7:
        platform(0, 0, s_width, 25)           
        platform(0, s_height - 25, s_width, 25)
        platform(s_width - 25, 0, 25, s_height/2 - 50)
        platform(s_width - 25, s_height/2 + 50, 25, s_height/2 - 50)
        platform(0, 0, 25, s_height/2 - 50)
        platform(0, s_height/2 + 50, 25, s_height/2 - 50)
        
        win_color = (0, 200, 200)
        if door7.locked:
            door7.draw(win)
        if key7.show:
            key7.draw(win)
     if room == 8:
        platform(0, 0, s_width, 25)         
        platform(0, s_height - 25, s_width, 25)
        platform(s_width - 25, 0, 25, s_height/2 - 50)
        platform(s_width - 25, s_height/2 + 50, 25, s_height/2 - 50)
        platform(0, 0, 25, s_height/2 - 50)
        platform(0, s_height/2 + 50, 25, s_height/2 - 50)
        win_color = (200, 0, 200)
        if door8.locked:
            door8.draw(win)
        if key8.show:
            key8.draw(win)
            
     if room == 9:
        platform(0, 0, s_width, 25)          
        platform(0, s_height - 25, s_width, 25)
        platform(s_width - 25, 0, 25, s_height/2 - 50)
        platform(s_width - 25, s_height/2 + 50, 25, s_height/2 - 50)
        platform(0, 0, 25, s_height)     
        
        win_color = (200, 200, 0) 
        if key9.show:
            key9.draw(win)
     if room == 10:
        platform(0, 0, s_width, 25)           
        platform(0, s_height - 25, s_width, 25)
        platform(s_width - 25, 0, 25, s_height)
        platform(0, 0, 25, s_height)     
        
        win_color = (0, 100, 100)
        

#Tegner nøkkler
     if key1.show and room == 1:
        key1.draw(win)
     if key2.show and room == 2:
        key2.draw(win)
     if key3.show and room == 3:
        key3.draw(win)
     if key4.show and room == 4:
        key4.draw(win)
     if key5.show and room == 5:
        key5.draw(win)
     if key6.show and room == 6:
        key6.draw(win)
     if key7.show and room == 7:
        key7.draw(win)
     if key8.show and room == 8:
        key8.draw(win)
     if key9.show and room == 9:
        key9.draw(win)
       
       
    #Tegner dører
     if door1.locked and room == 1:
        door1.draw(win)
     if door2.locked and room == 2:
        door2.draw(win)
     if door3.locked and room == 2:
        door3.draw(win)
     if door4.locked and room == 4:
        door4.draw(win)
     if door5.locked and room == 5:
        door5.draw(win)
     if door6.locked and room == 2:
        door6.draw(win)
     if door7.locked and room == 7:
        door7.draw(win)
     if door8.locked and room == 8:
        door8.draw(win)
     if door9.locked and room == 1:
        door9.draw(win)
    
     pygame.display.update()

def reset_delay():
    global delay
    delay = 54
    Main_Boss.atkpattern = 1

def platform(x, y, width, height):
    if man.y + man.height > y and man.y < y + height and man.x + man.width > x and man.x + man.width < x + 2 * man.vel:
        man.x = x - man.width #Venstre
    elif man.y + man.height > y and man.y < y + height and man.x < x + width and man.x > x + width - man.vel * 2:
        man.x = x + width #Høyre
    if man.y + man.height > y and man.y + man.height < y + 2 * man.vel and man.x + man.width > x and man.x < x + width:
        man.y = y - man.height #Over
    elif man.y < y + height and man.y > y + height - man.vel * 2 and man.x + man.width > x and man.x < x + width:
        man.y = y + height #Under
    pass
 
border_ul = platform(0, 0, s_width/2 - 50, 25)
border_ur = platform(s_width/2 + 50, 0, s_width/2 - 50, 25)
border_u = platform(0, 0, s_width, 25)   
border_ru = platform(s_width - 25, 0, 25, s_height/2 - 50)
border_rd = platform(s_width - 25, s_height/2 + 50, 25, s_height/2 - 50)
border_r = platform(s_width - 25, 0, 25, s_height)
border_dl = platform(0, s_height - 25, s_width/2 - 50, 25)
border_dr = platform(s_width/2 + 50, s_height - 25, s_width/2 - 50, 25)
border_d = platform(0, s_height - 25, s_width, 25)
border_lu = platform(0, 0, 25, s_height/2 - 50)
border_ld = platform(0, s_height/2 + 50, 25, s_height/2 - 50)
border_l = platform(0, 0, 25, s_height)   

song_change = True
song_replay = True
show = True
kniver = []
man.delay = 0 
knife.delay = 0
enemy_delay = 0
time_delay = 0
time = 0
bakShow = True
run = True #Hovedloop
slutt = True
music = pygame.mixer.music.load(songs[0])
Boss_fight = True
respawn_delay = 0
while run and man.health > 0: 
    
    if room == 2 and song_replay:
        song_change = True
        if Bosses == False and Boss_fight == True:
            Main_Boss = Boss(450, 200, 100, 100, 600)
#            enemies.append(Main_Boss)
            Boss_projectiles_width = 5
            Boss_projectiles_radius = 5
            Main_Boss.atkpattern = 1
            projectiles = []
            projectile_radius = 5
            
            
            
            hjørne_koordinater = {"N" : ["TBL", "TL", "TTL", "TTR", "TR", "TBR"],
                                  "S" : ["BTL", "BL", "BBL", "BBR", "BR", "BTR"],
                                  "E" : ["TTR", "TR", "TBR", "BTR", "BR", "BBR"],
                                  "W" : ["TTL", "TL", "TBL", "BTL", "BL", "BBL"]}
            koordinater = {"N" : (Main_Boss.x + Main_Boss.width*(1/10), Main_Boss.y - Boss_projectiles_width, Main_Boss.width * (8/10), Boss_projectiles_width),
                           "S" : (Main_Boss.x + Main_Boss.width*(1/10), Main_Boss.y + Main_Boss.height, Main_Boss.width * (8/10), Boss_projectiles_width),
                           "W" : (Main_Boss.x - Boss_projectiles_width, Main_Boss.y + Main_Boss.height*(1/10), Boss_projectiles_width, Main_Boss.height * (8/10)),
                           "E" : (Main_Boss.x + Main_Boss.width, Main_Boss.y + Main_Boss.height*(1/10), Boss_projectiles_width, Main_Boss.height * (8/10)),
                           "TR" : (Main_Boss.x + Main_Boss.width - 15, Main_Boss.y, Main_Boss.width *(1/10) + Boss_projectiles_width, Main_Boss.height *(1/10) + Boss_projectiles_width),
                           "TL" : (Main_Boss.x, Main_Boss.y, Main_Boss.width *(1/10) + Boss_projectiles_width, Main_Boss.height *(1/10) + Boss_projectiles_width),
                           "BR" : (Main_Boss.x + Main_Boss.width - 15, Main_Boss.y + Main_Boss.height - 15, Main_Boss.width *(1/10) + Boss_projectiles_width, Main_Boss.height *(1/10) + Boss_projectiles_width),
                           "BL" : (Main_Boss.x, Main_Boss.y + Main_Boss.height - 15, Main_Boss.width *(1/10) + Boss_projectiles_width, Main_Boss.height *(1/10) + Boss_projectiles_width),
                           "TTR": (Main_Boss.x + Main_Boss.width*(9/10) + Boss_projectiles_width, Main_Boss.y - (Boss_projectiles_width + Boss_projectiles_radius)),
                           "TBR" : (Main_Boss.x + Main_Boss.width + (Boss_projectiles_width + Boss_projectiles_radius), Main_Boss.y + Main_Boss.height*(1/10) - Boss_projectiles_width),
                           "TTL" : (Main_Boss.x + Main_Boss.width*(1/10) - Boss_projectiles_width, Main_Boss.y - (Boss_projectiles_width + Boss_projectiles_radius)),
                           "TBL" : (Main_Boss.x - (Boss_projectiles_width + Boss_projectiles_radius), Main_Boss.y + Main_Boss.height*(1/10) - Boss_projectiles_width),
                           "BTR" : (Main_Boss.x + Main_Boss.width + (Boss_projectiles_width + Boss_projectiles_radius), Main_Boss.y + Main_Boss.height*(9/10) + Boss_projectiles_width),
                           "BBR" : (Main_Boss.x + Main_Boss.width*(9/10) + Boss_projectiles_width, Main_Boss.y + Main_Boss.height + (Boss_projectiles_width + Boss_projectiles_radius)),
                           "BTL" : (Main_Boss.x - (Boss_projectiles_width + Boss_projectiles_radius), Main_Boss.y + Main_Boss.height*(9/10) + Boss_projectiles_width),
                           "BBL" : (Main_Boss.x + Main_Boss.width*(1/10) - Boss_projectiles_width, Main_Boss.y + Main_Boss.height + (Boss_projectiles_width + Boss_projectiles_radius))}
            Bosses = True
            x_zone = (s_end_x - s_start_x - Main_Boss.width)/10
            y_zone = (s_end_y - s_start_y - Main_Boss.height)/10
            
    if Bosses == True:
        if delay > 0:
            delay -= 1
            if delay == 0 and Main_Boss.health <= 400:
                respawn_delay += 1
        
        
        else:
            if Main_Boss.atkpattern == 1:
                Main_Boss.atkpattern = 2
            else:
                Main_Boss.atkpattern = 1
            delay = 54
        if respawn_delay == 5:
            Main_Boss.spawn()
            respawn_delay = 0
        if delay % 3 == 0:
            Main_Boss.search()
        
        for projectile in projectiles:
            projectile.move()
            projectile.hit()
        if Main_Boss.health <= 0:
            enemies.remove(Main_Boss)
            Main_Boss = 0
            Bosses = False
            Boss_fight = False
    if song_change:
        if room == 1:
            pygame.mixer.music.play(-1)
            song_change = False
        elif room == 2:
            music = pygame.mixer.music.load(songs[1])
            pygame.mixer.music.play(-1)
            song_change = False
            song_replay = False
            
#    print(round(clock.get_fps(),0))
    
    if  time_delay % 27 == 0:
        time += 1
    
    if knife.delay > 0:
        knife.delay -= 1
    
    if len(enemies) == 0:
        if room == 1 and not(key1.open):
            key1.show = True
        if room == 2 and not(key2.open):
            key2.show = True
        if room == 3 and not(key3.open):
            key3.show = True
        if room == 4 and not(key4.open):
            key4.show = True
        if room == 5 and not(key5.open):
            key5.show = True
        if room == 6 and not(key6.open):
            key6.show = True
        if room == 7 and not(key7.open):
            key7.show = True
        if room == 8 and not(key8.open):
            key8.show = True
        if room == 9 and not(key9.open):
            key9.show = True
    else:
        if room == 1:
            key1.show = False
        if room == 2:
            key2.show = False
        if room == 3:
            key3.show = False
        if room == 4:
            key4.show = False
        if room == 5:
            key5.show = False
        if room == 6:
            key6.show = False
        if room == 7:
            key7.show = False
        if room == 8:
            key8.show = False
        if room == 9:
            key9.show = False
            
            
    clock.tick(27)
    if man.delay > 0:
        man.delay -= 1
    if enemy_delay > 0:
        enemy_delay -= 9
    else:
        enemy_delay = 27
   
    time_delay += 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            slutt = False

    keys = pygame.key.get_pressed()

        
    if keys[pygame.K_SPACE] and knife.delay == 0:   #antall projektiler som kan være på skjermen 
            kniver.append(knife())
            knife.delay = 27 #round(mar.x + mar.bredde//2), round(mar.y + mar.høyde//2))
    for kniv in kniver:
        kniv.move()

    if room == 1:
        bg = pygame.image.load("BakRoom1.png")
        bak = False
    elif room == 2:
        bg = pygame.image.load("BakRoom2.png")
    elif room == 3:
        bg = pygame.image.load("BakRoom3.png")
    elif room == 4 or room == 5 or room == 7 or room == 8:
        bg = pygame.image.load("BakRoom5.png")
    elif room == 6:
        bg = pygame.image.load("BakRoom6.png")
    elif room == 9:
        bg = pygame.image.load("BakRoom9.png")
    else:
        bg = pygame.image.load("BakRoom10.png")
        
    if room == 1 and bakShow == True and man.x + man.width < 550  and man.x + man.width > 450:
        if man.y + man.height > 200 and man.y + man.height < 300:
            bg = pygame.image.load("BakRoom1_Info.png")
            bak = True
            show = False
    else:
        bakShow = False
        
    for fiende in enemies:
        if bak == True:
            fiende.vel = 0
        else:
            fiende.vel = 3
            
    if gethe == True and kiste1.open == True and man.health < 4 and len(enemies) == 0:
        man.health += 1
        gethe = False
        
    if getpo == True and kiste2.open == True and len(enemies) == 0:
        man.vel = 15
        getpo = False
        
    if getda == True and kiste3.open == True and len(enemies) == 0:
        for kniv in kniver:
            kniv.damage = 18
        getda = False
               
    if len(enemies) == 0:
        if man.x < kiste1.x + kiste1.width and man.x + man.width > kiste1.x and room == 3:
            if man.y + man.height > kiste1.y and man.y < kiste1.y + kiste1.height:
                kiste1.open = True
       
        if man.x < kiste2.x + kiste2.width and man.x + man.width > kiste2.x and room == 6:
            if man.y + man.height > kiste2.y and man.y < kiste2.y + kiste2.height:
                kiste2.open = True
                
        if man.x < kiste3.x + kiste3.width and man.x + man.width > kiste3.x and room == 9:
            if man.y + man.height > kiste3.y and man.y < kiste3.y + kiste3.height:
                kiste3.open = True
        
        #Skjekker om spiller treffer nøkkel
        if man.x < key1.x + key1.width and man.x + man.width > key1.x and room == 1:
            if man.y + man.height > key1.y and man.y < key1.y + key1.height:
                key1.show = False
                key1.open = True
       
        if man.x < key2.x + key2.width and man.x + man.width > key2.x and room == 2:
            if man.y + man.height > key2.y and man.y < key2.y + key2.height:
                key2.show = False
                key2.open = True
       
        if man.x < key3.x + key3.width and man.x + man.width > key3.x and room == 3:
            if man.y + man.height > key3.y and man.y < key3.y + key3.height:
                key3.show = False
                key3.open = True
       
        if man.x < key4.x + key4.width and man.x + man.width > key4.x and room == 4:
            if man.y + man.height > key4.y and man.y < key4.y + key4.height:
                key4.show = False
                key4.open = True
       
        if man.x < key5.x + key5.width and man.x + man.width > key5.x and room == 5:
            if man.y + man.height > key5.y and man.y < key5.y + key5.height:
                key5.show = False
                key5.open = True
       
        if man.x < key6.x + key6.width and man.x + man.width > key6.x and room == 6:
            if man.y + man.height > key6.y and man.y < key6.y + key6.height:
                key6.show = False
                key6.open = True
        if man.x < key7.x + key7.width and man.x + man.width > key7.x and room == 7:
            if man.y + man.height > key7.y and man.y < key7.y + key7.height:
                key7.show = False
                key7.open = True
                
        if man.x < key8.x + key8.width and man.x + man.width > key8.x and room == 8:
            if man.y + man.height > key8.y and man.y < key8.y + key8.height:
                key8.show = False
                key8.open = True
        if man.x < key9.x + key6.width and man.x + man.width > key9.x and room == 9:
            if man.y + man.height > key9.y and man.y < key9.y + key9.height:
                key9.show = False
                key9.open = True
    #Skjekker om spiller treffer dør
    #Skjekker opp og ned
    
    if man.x > s_width/2 - man.width - 23 and man.x + man.width < s_width/2 + man.width + 20:      
        if man.y < man.vel + 1:
            if keys[pygame.K_f] and key1.open and room == 1:                                     
                
                door1.locked = False
#                if door9.locked:
#                    antall = 3
#                else:
#                    antall = 5
#           
            elif not(door1.locked) and room == 1:
                man.y = s_height - man.height - 20
                room = 2 
                telle = True
               
            elif keys[pygame.K_f] and key2.open and room == 2:       
                door2.locked = False
                
#                antall = 3
                
            elif not(door2.locked) and room == 2:
                win_color = (200, 128, 24)  
                telle = True
                #Putte inn sprites og bakgrunn her
                man.y = s_height - man.height - 20
                room = 3
                          
        if man.y > s_height - man.vel - 1 - man.height:
            if room == 2 and key2.open:
                man.y = 20
                room = 1
          
            elif room == 3 and key3.open:
                 man.y = 20
                 room = 2
           
            elif keys[pygame.K_f] and key9.open and room == 1:
                door9.locked = False
                
#                antall = 1
           
            elif not(door9.locked) and room == 1:
                man.y = 20
                room = 10
   
    #Skjekker til siden
    if man.y > s_height/2 - man.height - 23 and man.y + man.height < s_height/2 + man.width + 20:
       
        if man.x > s_width - man.vel - man.width - 1:
            #Høyre siden fremover
           
            if keys[pygame.K_f] and key3.open and room == 2:
                door3.locked = False
                
                antall = 2
       
            elif not(door3.locked) and room == 2:
                man.x = 20
                room = 4
                telle = True
           
            elif keys[pygame.K_f] and key4.open and room == 4:
                door4.locked = False
               
                antall = 3
       
            elif not(door4.locked) and room == 4:
                man.x = 20
                room = 5
                telle = True
           
            elif keys[pygame.K_f] and key5.open and room == 5:
                door5.locked = False
                
                antall = 3
       
            elif not(door5.locked) and room == 5:
                man.x = 20
                room = 6
                telle = True
           
            #Venstre siden bakover
            if room == 7 and key7.open:
                man.x = man.width + 20
                room = 2
           
            elif room == 8 and key8.open:
                man.x = man.width + 20
                room = 7
           
            elif room == 9 and key9.open:
                man.x = man.width + 20
                room = 8
           
           
       
        if man.x < man.vel:
            #Høyre siden bakover
           
            if room == 6 and key6.open:
                man.x = s_width - man.width - 20
                room = 5
           
            elif room == 5 and key5.open:
                man.x = s_width - man.width - 20
                room = 4
           
            elif room == 4 and key4.open:
                man.x = s_width - man.width - 20
                room = 2
           
            #Venstre siden fremover
            if keys[pygame.K_f] and key6.open and room == 2:
                door6.locked = False
               
                antall = 3
       
            elif not(door6.locked) and room == 2:
                man.x = s_width - man.width - 20
                room = 7
                telle = True
           
            elif keys[pygame.K_f] and key7.open and room == 7:
                door7.locked = False
                
                antall = 3
       
            elif not(door7.locked) and room == 7:
                man.x = s_width - man.width - 20
                room = 8
                telle = True
           
            elif keys[pygame.K_f] and key8.open and room == 8:
                door8.locked = False                
                antall = 3
       
            elif not(door8.locked) and room == 8:
                man.x = s_width - man.width - 20
                room = 9
                telle = True
    
    #Bevegelse for spiller
    if keys[pygame.K_d]:
        if man.x < s_width - man.width - man.vel:
            man.x += man.vel
            man.left = 0
            man.right = 1
            man.up = 0
            man.down = 0
            man.standing = False
            man.retning = 2
        else:
            man.x = s_width - man.width
   
    elif keys[pygame.K_a]:
        if man.x > man.vel:
            man.x -= man.vel
            man.left = 1
            man.right = 0
            man.down = 0
            man.up = 0
            man.standing = False
            man.retning = 1
        else:
            man.x = 0
   
    elif keys[pygame.K_w]:
         if man.y > man.vel:
             man.y -= man.vel
             man.left = 0
             man.right = 0
             man.down = 0
             man.up = 1
             man.standing = False
             man.retning = 4
         else:
             man.y = 0
    
    elif keys[pygame.K_s] :
        if man.y < s_height - man.height - man.vel:
            man.y += man.vel
            man.left = 0
            man.right = 0
            man.down = 1
            man.up = 0
            man.standing = False
            man.retning = 3
    
        else:
            man.y = s_height - man.height
    else:
        man.standing = True
        man.walkCount = 0
    
    if keys[pygame.K_u]:
        for fiende in enemies:
            fiende.health -= 9
            Main_Boss.health -= 9
    
    for fiende in enemies:
        for kniv in kniver:
            if kniv.x < fiende.x + fiende.width and kniv.x + kniv.width > fiende.x:
                if kniv.y + kniv.height > fiende.y and kniv.y < fiende.y + fiende.height:
                    fiende.health -= 9
                    kniver.pop(kniver.index(kniv))
                    
        if man.x < fiende.x + fiende.width and man.x + man.width > fiende.x:
            if man.y + man.height > fiende.y and man.y < fiende.y + fiende.height:
                man.hit()
                man.health -= 1
    
    for kniv in kniver:
            if kniv.x < Main_Boss.x + Main_Boss.width and kniv.x + kniv.width > Main_Boss.x:
                if kniv.y + kniv.height > Main_Boss.y and kniv.y < Main_Boss.y + Main_Boss.height:
                    Main_Boss.health -= 9
                    kniver.pop(kniver.index(kniv))
    
    if man.health < 1:
        run2 = True
        
    man.hit()
    
    for fiende in enemies:
        fiende.move()
 
    if man.health == 0:
        for fiende in enemies:
            enemies.clear()
        
    redrawGamewindow()

while slutt:
    bg = pygame.image.load('GameOver.png')
    man.standing = True
    man.x = 0
    man.y = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            slutt = False
    
    redrawGamewindow()

formel = ((drepte_enemies)/100)*man.health
#if formel > 0:    
#    navn = input("Hva heter du?: ")
#    file.write(navn + "    -   " + str(formel))
#    file.write('\n')
    
file.close()

pygame.quit()

