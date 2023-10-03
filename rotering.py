#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:54:09 2020

@author: markusdahljorgensen
"""

from pylab import * 
import pygame
pygame.init()
win = pygame.display.set_mode((400, 400))
#def rotate(rect, degrees):
#    corner = [rect[x] for x in range(4)]
#    mid = (corner[0][0] + (corner[0][0] + corner[1][0])/2, corner[0][1] + (corner[0][1] + corner[2][1])/2)
#    length = ((mid[0] - corner[0][0])**2 + (mid[1] - corner[0][1])**2)**0.5
#    x_change = length * sin(degrees)
#    y_change = length * cos(degrees)
#    return [(rect[0][0] + x_change, rect[0][1] - y_change), (rect[1][0] + y_change, rect[1][1] + x_change), (rect[2][0] - x_change, rect[2][1] + y_change), (rect[1][0] - y_change, rect[1][1] - x_change)]
#
#rekt = [(20,20), (40,20), (20,40), (40,40)]
def rotate(rect, degrees):
    mid = (corner[0][0] + (corner[0][0] + corner[1][0])/2, corner[0][1] + (corner[0][1] + corner[2][1])/2)
    length = ((mid[0] - corner[0][0])**2 + (mid[1] - corner[0][1])**2)**0.5
    
rotate(rekt, 45)
while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            quit()
    win.fill((0,0,0))
    pygame.draw.polygon(win, pygame.Color("red"), rekt, 2)
    pygame.display.update()