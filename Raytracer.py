import pygame
from pygame.locals import * 

from rt import Raytracer
from figuras import *
from lights import *
from material import *

width = 256
height = 256

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

rt = Raytracer(screen)
rt.envMap = pygame.image.load("night.jpg")
rt.rtClearColor(0.27,0.36,0.52)

flowTexture = pygame.image.load("flow.jpg")

brick = Material(diffuse=(1,0.4,0.4), spec = 8,  Ks = 0.01)
grass = Material(diffuse=(0.4,1,0.4), spec = 32,  Ks = 0.1)
water = Material(diffuse=(0.4,0.4,1), spec = 256, Ks = 0.2)

mirror = Material(diffuse=(0.9,0.9,0.9), spec = 64, Ks = 0.2, matType = REFLECTIVE)
blueMirror = Material(diffuse=(0.4,0.4,0.9), spec = 32, Ks = 0.15, matType = REFLECTIVE)
colorFlow = Material(texture = flowTexture)
reflectFlow = Material(texture = flowTexture, spec = 64, Ks = 0.1, matType= REFLECTIVE)

rt.scene.append(Sphere(position=(-2,0,-7), radius = 1.5, material = reflectFlow))
rt.scene.append(Sphere(position=(2,0,-7), radius = 2, material = colorFlow))
rt.scene.append(Sphere(position=(0,-1,-5), radius = 0.5, material = mirror))


#Luces
rt.lights.append(AmbientLight(intensity=0.1))
rt.lights.append(DirectionalLight(direction=(-1,-1,-1), intensity=0.9))

rt.rtClear()
rt.rtRender()

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False

pygame.quit()


