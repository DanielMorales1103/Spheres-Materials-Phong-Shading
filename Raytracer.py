import pygame
from pygame.locals import * 

from rt import Raytracer
from figuras import *
from lights import *
from material import *

width = 512
height = 512

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

rt = Raytracer(screen)
rt.rtClearColor(0.5,0.5,0.5)
#Materiales
brick = Material(diffuse=(1, 0.4, 0.4), spec = 8)
grass = Material(diffuse=(0.4, 1, 0.4), spec = 32)
water = Material(diffuse=(0.4, 0.4, 1), spec = 256)
#Figuras
rt.scene.append( Sphere(position=(-2,0,-5), radius=0.5, material = brick))
rt.scene.append( Sphere(position=(0,0,-5), radius=0.5, material = grass))
rt.scene.append( Sphere(position=(2,0,-5), radius=0.5, material = water))
#Luces
rt.lights.append( AmbientLight(intensity=0.1))
rt.lights.append( DirectionalLight(direction=(-1,-1,-1), intensity=0.7))


isRunning = True

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
    
    rt.rtClear()


    rt.rtRender()
    pygame.display.flip()


pygame.quit()


