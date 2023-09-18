import pygame
from pygame.locals import * 

from rt import Raytracer
from figuras import *
from lights import *
from material import *

width = 512
height = 756

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

rt = Raytracer(screen)
rt.rtClearColor(0.5,0.5,0.5)
#Materiales
snow = Material(diffuse=(1, 1, 1), spec = 200, Ks = 0.1)
#Figuras
rt.scene.append( Sphere(position=(0,-1.5,-5), radius=1.2, material = snow))
rt.scene.append( Sphere(position=(0,0.4,-5), radius=0.9, material = snow))
rt.scene.append( Sphere(position=(0,1.7,-5), radius=0.7, material = snow))
#Luces
rt.lights.append( AmbientLight(intensity=0.1))
rt.lights.append( DirectionalLight(direction=(-1,-1,-1), intensity=0.7))
rt.lights.append( DirectionalLight(direction=(0,-2,-1), intensity= 0.5))
#rt.lights.append( PointLight(point=(2.5,0,-5),intensity=1, color=(1,0,1)))


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


