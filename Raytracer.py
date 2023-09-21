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
rt.rtClearColor(0.27,0.36,0.52)
#Materiales
snow = Material(diffuse=(1, 1, 1), spec = 200, Ks = 0.1)
button = Material(diffuse=(0,0,0), spec = 10, Ks = 0.1)  
teeth = Material(diffuse=(0,0,0), spec = 50, Ks = 0.1)  
carrot = Material(diffuse=(1,0.5,0), spec = 150, Ks = 0.1)
eyes = Material(diffuse=(1,1,1), spec = 300, Ks = 0.1)
pupil = Material(diffuse=(0,0,0), spec = 100, Ks = 0.1)
#Figuras
#Botones
rt.scene.append( Sphere(position=(0,-1.2,-3), radius=0.2, material = button))
rt.scene.append( Sphere(position=(0,-0.45,-3), radius=0.15, material = button))
rt.scene.append( Sphere(position=(0,0.1,-3), radius=0.1, material = button))
#Dientes
rt.scene.append( Sphere(position=(-0.1,1.2,-4), radius=0.05, material = teeth))
rt.scene.append( Sphere(position=(0.1,1.2,-4), radius=0.05, material = teeth))
rt.scene.append( Sphere(position=(-0.25,1.3,-4), radius=0.05, material = teeth))
rt.scene.append( Sphere(position=(0.25,1.3,-4), radius=0.05, material = teeth))
#Nariz
rt.scene.append( Sphere(position=(0,1.5,-4), radius=0.1, material = carrot))
#Ojos
rt.scene.append( Sphere(position=(-0.2,1.72,-4), radius=0.11, material = eyes))
rt.scene.append( Sphere(position=(-0.2,1.7,-3.9), radius = 0.05, material = pupil))
rt.scene.append( Sphere(position=(0.2,1.72,-4), radius=0.11, material = eyes))
rt.scene.append( Sphere(position=(0.2,1.7,-3.9), radius = 0.05, material = pupil))
# Bolas de nieve
rt.scene.append( Sphere(position=(0,-1.5,-5), radius=1.2, material = snow))
rt.scene.append( Sphere(position=(0,0.4,-5), radius=0.9, material = snow))
rt.scene.append( Sphere(position=(0,1.9,-5), radius=0.7, material = snow))


#Luces
rt.lights.append( AmbientLight(intensity=0.3))
rt.lights.append( DirectionalLight(direction=(-1,0,-1), intensity=0.7))
# rt.lights.append( DirectionalLight(direction=(0,-2,-1), intensity= 0.5))
# rt.lights.append( DirectionalLight(direction=(0,3,-1), intensity= 0.5))
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


