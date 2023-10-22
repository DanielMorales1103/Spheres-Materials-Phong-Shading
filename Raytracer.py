import pygame
from pygame.locals import * 

from rt import Raytracer
from figuras import *
from lights import *
from material import *

width = 526
height = 512

pygame.init()
screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.SCALED)

# screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE)
screen.set_alpha(None)

rt = Raytracer(screen)
rt.envMap = pygame.image.load("images/fondoCocina.jpg")
rt.rtClearColor(0.27,0.36,0.52)


boxTexture = pygame.image.load("images/box2.jpg")

box = Material(texture=boxTexture)

colorBack = Material(diffuse=(1,1,1), spec = 8,  Ks = 0.01, matType = OPAQUE)


water = Material(diffuse=(0.7, 0.9, 1), spec=8, Ks=0.01, matType=TRANSPARENT, ior=1.333)
glass = Material(diffuse=(0.9,0.9,0.9), spec = 64, Ks = 0.15, ior = 1.5, matType = TRANSPARENT)


#Materiales nuevos
meat = Material(diffuse=(0.8, 0.4, 0.2), spec=16, Ks=0.02, matType=OPAQUE)
wood = Material(diffuse=(0.3, 0.15, 0.05), spec=16, Ks=0.02, matType=OPAQUE)
white_plate = Material(diffuse=(1, 1, 1), spec=32, Ks=0.5, matType=OPAQUE)
internal_plate = Material(diffuse=(1,1,1), spec = 32, Ks = 0.15, matType = REFLECTIVE)
pan_material = Material(diffuse=(0.8, 0.6, 0.4), spec=16, Ks=0.02, matType=OPAQUE)
cheese_material = Material(diffuse=(1, 1, 0.8), spec=32, Ks=0.1, matType=OPAQUE)
pepperoni_material = Material(diffuse=(1, 0, 0), spec=8, Ks=0.02, matType=OPAQUE)
water_droplet = Material(diffuse=(1, 1, 1), spec=64, Ks=0.2, matType=OPAQUE, ior=1.333)



#  Fondo
# rt.scene.append( Plane(position=(0,5,-20),normal=(0,1,0),material=colorBack))
# rt.scene.append( Plane(position=(0,-5,-20),normal=(0,1,0),material=colorBack))

#mesa
rt.scene.append( AABB(position=(0.3,-0.5,-5),size=(5,0.3,2),material=box))
#patas delanteras
rt.scene.append( Cylinder(position=(-2.3,-1.7,-5),height=0.7,radius=0.2,material=wood))
rt.scene.append( Cylinder(position=(3,-1.7,-5),height=0.7,radius=0.2,material=wood))
#patas traseras
rt.scene.append( Cylinder(position=(-2.5,-2.3,-7),height=1.3,radius=0.2,material=wood))
rt.scene.append( Cylinder(position=(3,-2.3,-7),height=1.3,radius=0.2,material=wood))

#plato
rt.scene.append( Disk(position=(0.8,-0.1,-4.9), normal=(0,1,0), radius=1.5, material=white_plate))
rt.scene.append( Disk(position=(0.8,-0.09,-4.8), normal=(0,1,0), radius=1.3, material=internal_plate))
# pan 
rt.scene.append( Triangle(vertices=[(0.1, 0, -4.5), (2.5, 0.5, -4.5), (1.7, 1, -4.5)], material=pan_material))
rt.scene.append( Sphere(position=(2.4,0.41,-4.5),radius=0.1,material=pan_material))
rt.scene.append( Disk(position=(2.35,0.41,-4.4),normal=(0,0,1),radius=0.08,material=cheese_material))
rt.scene.append( Triangle(vertices=[(0.1, 0, -4.5), (2.4, 0.31, -4.5), (1.7, 1, -4.5)], material=pan_material))
# queso 
rt.scene.append( Triangle(vertices=[(0.1, 0.03, -4.4), (2.3, 0.32, -4.4), (1.5, 0.9, -4.4)], material=cheese_material))
rt.scene.append( Disk(position=(0.25, 0.07, -4.3),normal=(0,0,1),radius=0.05,material=cheese_material))
rt.scene.append( Disk(position=(0.48, 0.06, -4.3),normal=(0,0,1),radius=0.05,material=cheese_material))
rt.scene.append( Disk(position=(0.75, 0.15, -4.3),normal=(0,0,1),radius=0.12,material=cheese_material))
rt.scene.append( Disk(position=(0.75, 0.05, -4.3),normal=(0,0,1),radius=0.07,material=cheese_material))
rt.scene.append( Disk(position=(1.2, 0.15, -4.3),normal=(0,0,1),radius=0.09,material=cheese_material))
rt.scene.append( Disk(position=(0.95, 0.24, -4.3),normal=(0,0.5,1),radius=0.15,material=cheese_material))
rt.scene.append( Disk(position=(1.6, 0.28, -4.3),normal=(0,0.5,1),radius=0.15,material=cheese_material))
rt.scene.append( Disk(position=(1.8, 0.3, -4.3),normal=(0,0,1),radius=0.09,material=cheese_material))
rt.scene.append( Disk(position=(2, 0.33, -4.3),normal=(0,0,1),radius=0.07,material=cheese_material))

# peperonis
rt.scene.append( Disk(position=(0.6, 0.25,-4.2), normal=(0,0,1), radius=0.1, material=pepperoni_material))
rt.scene.append( Disk(position=(1, 0.5,-4.2), normal=(0,0,1), radius=0.09, material=pepperoni_material))
rt.scene.append( Disk(position=(1.2, 0.30,-4.2), normal=(0,0,1), radius=0.05, material=pepperoni_material))
rt.scene.append( Disk(position=(1.6, 0.40,-4.2), normal=(0,0,1), radius=0.15, material=pepperoni_material))
rt.scene.append( Disk(position=(1.4, 0.70,-4.2), normal=(0,0,1), radius=0.12, material=pepperoni_material))

# albondigas
rt.scene.append( Disk(position=(0.72, 0.38,-4.2), normal=(0,0,1), radius=0.04, material=meat))
rt.scene.append( Disk(position=(0.92, 0.23,-4.2), normal=(0,0,1), radius=0.04, material=meat))
rt.scene.append( Disk(position=(1.23, 0.6,-4.2), normal=(0,0,1), radius=0.04, material=meat))
rt.scene.append( Disk(position=(1.35, 0.33,-4.2), normal=(0,0,1), radius=0.04, material=meat))
rt.scene.append( Disk(position=(1.85, 0.45,-4.2), normal=(0,0,1), radius=0.04, material=meat))
# Vaso con Agua
rt.scene.append( Cylinder(position=(-1.1,0.05,-3),height=0.3,radius=0.2,material=water))
rt.scene.append( Cylinder(position=(-1.1,0.05,-3),height=0.5,radius=0.25,material=glass))
rt.scene.append( Sphere(position=(-1,0.27,-3.),radius=0.02,material=water_droplet))
rt.scene.append( Sphere(position=(-1.2,0.23,-3.),radius=0.025,material=water_droplet))
rt.scene.append( Sphere(position=(-1.1,0.28,-3.),radius=0.03,material=water_droplet))
rt.scene.append( Sphere(position=(-1,0.2,-3.),radius=0.015,material=water_droplet))
rt.scene.append( Sphere(position=(-0.9,0.18,-3.),radius=0.032,material=water_droplet))
rt.scene.append( Sphere(position=(-1.1,0.18,-3.),radius=0.027,material=water_droplet))
#Luces
rt.lights.append( PointLight(point=(2, 2, -15), intensity=0.8, color=(1, 1, 1)))
rt.lights.append( DirectionalLight(direction=(0,1,0)))
rt.lights.append( DirectionalLight(direction=(2, 2, 5)))
rt.lights.append( AmbientLight(intensity=0.5))


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


