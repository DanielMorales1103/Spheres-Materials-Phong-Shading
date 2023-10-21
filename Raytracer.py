import pygame
from pygame.locals import * 

from rt import Raytracer
from figuras import *
from lights import *
from material import *

width = 512
height = 512

pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.SCALED)

# screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

rt = Raytracer(screen)
rt.envMap = pygame.image.load("images/fondo.jpg")
rt.rtClearColor(0.27,0.36,0.52)

flowTexture = pygame.image.load("images/trees.jpg")
boxTexture = pygame.image.load("images/box2.jpg")

box = Material(texture=boxTexture)

brick = Material(diffuse=(1,0.4,0.4), spec = 8,  Ks = 0.01, matType = OPAQUE)
brickBack = Material(diffuse=(0.6, 0.2, 0.2), spec = 8,  Ks = 0.01, matType = OPAQUE)
colorFlow = Material(texture = flowTexture, matType = OPAQUE)
ceiling_color = Material(diffuse=(0.7, 0.7, 0.7), spec=8, Ks=0.01, matType=OPAQUE)
floor_color = Material(diffuse=(0.5, 0.5, 0.5), spec=8, Ks=0.01, matType=OPAQUE)
water = Material(diffuse=(0,0,1),spec=8, Ks=0.01, matType=OPAQUE)

mirror = Material(diffuse=(0.9,0.9,0.9), spec = 64, Ks = 0.2, matType = REFLECTIVE)
blueMirror = Material(diffuse=(0.4,0.4,0.9), spec = 32, Ks = 0.15, matType = REFLECTIVE)

glass = Material(diffuse=(0.9,0.9,0.9), spec = 64, Ks = 0.15, ior = 1.5, matType = TRANSPARENT)
diamond = Material(diffuse=(0.9,0.9,0.9), spec = 64, Ks = 0.2, ior = 2.417, matType = TRANSPARENT)

##Materiales nuevos

customMaterialAmarillo = Material(diffuse=(0.8, 0.8, 0.2), spec=20, Ks=0.07, matType=OPAQUE)
customReflectiveAzul = Material(diffuse=(0.4, 0.4, 0.9), spec=32, Ks=0.1, matType=REFLECTIVE)
customTransparentVerde = Material(diffuse=(0.2, 0.8, 0.2), spec=64, Ks=0.2, ior=5, matType=TRANSPARENT)



#Cubos
rt.scene.append (Triangle(vertices=[(-1, -1, -5), (1, -1, -5), (0, 2, -5)], material=customMaterialAmarillo))
rt.scene.append (Triangle(vertices=[(1, -1, -5), (0, 2, -5),(2, 2, -10),], material=customReflectiveAzul))
rt.scene.append (Triangle(vertices=[(-2, 2, -5), (0, 2, -5),(-3, -3, -5),], material=customTransparentVerde))


#Luces
rt.lights.append(DirectionalLight(direction=(0,1,0)))
rt.lights.append(AmbientLight(intensity=0.5))
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


