import pygame
from pygame.locals import * 

from rt import Raytracer
from figuras import *
from lights import *
from material import *

width = 256
height = 256

pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.SCALED)

# screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

rt = Raytracer(screen)
rt.envMap = pygame.image.load("images/fondo.jpg")
rt.rtClearColor(0.27,0.36,0.52)

flowTexture = pygame.image.load("images/trees.jpg")

brick = Material(diffuse=(1,0.4,0.4), spec = 8,  Ks = 0.01, matType = OPAQUE)
colorFlow = Material(texture = flowTexture, matType = OPAQUE)

mirror = Material(diffuse=(0.9,0.9,0.9), spec = 64, Ks = 0.2, matType = REFLECTIVE)
blueMirror = Material(diffuse=(0.4,0.4,0.9), spec = 32, Ks = 0.15, matType = REFLECTIVE)

glass = Material(diffuse=(0.9,0.9,0.9), spec = 64, Ks = 0.15, ior = 1.5, matType = TRANSPARENT)
diamond = Material(diffuse=(0.9,0.9,0.9), spec = 64, Ks = 0.2, ior = 2.417, matType = TRANSPARENT)


# rt.scene.append(Sphere(position=(-2,1.5,-5), radius = 0.6, material = brick))
# rt.scene.append(Sphere(position=(-2,-1.5,-5), radius = 0.6, material = colorFlow))

# rt.scene.append(Sphere(position=(0,1.5,-5), radius = 0.6, material = mirror))
# rt.scene.append(Sphere(position=(0,-1.5,-5), radius = 0.6, material = blueMirror))

# rt.scene.append(Sphere(position=(2,1.5,-5), radius = 0.6, material = glass))
# rt.scene.append(Sphere(position=(2,-1.5,-5), radius = 0.6, material = diamond))

rt.scene.append(Sphere(position=(0,0.5,-5), radius = 0.6, material = blueMirror))
rt.scene.append(Disk(position=(0,-1,-5), normal = (0,1,0), radius = 1.5, material = mirror))
rt.scene.append(Plane(position=(0,-5,0), normal=(0,1,0), material=brick))

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

rect = pygame.Rect(0,0,width,height)
sub = screen.subsurface(rect)

pygame.quit()


