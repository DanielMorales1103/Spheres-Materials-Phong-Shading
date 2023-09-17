from math import tan, pi
import numpy as np
class Raytracer(object):
    def __init__(self, screen):
        self.screen = screen
        _, _, self.width, self.height = screen.get_rect()

        self.scene = []
        self.lights = []

        self.camPosition = [0,0,0]
        self.rtViewPort(0, 0, self.width, self.height )

        self.rtProyection()
        self.rtColor(1,1,1)
        self.rtClearColor(0,0,0)
        self.rtClear()

    def rtViewPort(self, posX, posY, width, height):
        self.vpX = posX
        self.vpY = posY
        self.vpWidth = width
        self.vpHeight = height

    def rtProyection(self, fov = 60, n= 0.1):
        aspectRatio = self.vpWidth / self.vpHeight
        self.nearplane = n
        self.topEdge = tan((fov * pi / 180) / 2) * self.nearplane
        self.rightEdge = self.topEdge * aspectRatio

    def rtClearColor(self, r, g, b):
        self.ClearColor = (r * 255,g * 255, b * 255)

    def rtClear(self):
        self.screen.fill(self.ClearColor)
    
    def rtColor(self,r,g,b):
        self.currColor = (r * 255,g * 255,b * 255)
    
    def rtPoint(self, x, y, color = None):
        y = self.height -y

        if (0<=x<= self.width) and (0<=y<=self.height):
            if color != None:
                color = (int(color[0] * 255),
                         int(color[1] * 255),
                         int(color[2] * 255),)
                self.screen.set_at((x,y), color)
            else:
                self.screen.set_at((x,y), self.currColor)

    def rtCastRay(self, orig, dir):        
        intercept = None
        hit = None
        for obj in self.scene:
            intercept = obj.ray_intersect(orig, dir)
            if intercept != None:
                hit = intercept

        
        return hit

    def rtRender(self):
        for x in range(self.vpX, self.vpX + self.vpWidth +1):
            for y in range(self.vpY, self.vpY + self.vpHeight +1):
                if 0 <= x <= self.width and 0 <= y <= self.height:
                    Px = ((x + 0.5 - self.vpX) / self.vpWidth) * 2 -1
                    Py = ((y + 0.5 - self.vpY) / self.vpHeight) * 2 -1

                    Px *= self.rightEdge
                    Py *= self.topEdge

                    # crear rayo
                    direction = (Px, Py, -self.nearplane)
                    direction = direction / np.linalg.norm(direction) #Normalizar

                    intercept =  self.rtCastRay(self.camPosition, direction)

                    if intercept != None:

                        surfaceColor = intercept.obj.material.diffuse

                        
                        ambientLightColor = [0,0,0]
                        diffuseLightColor = [0,0,0]
                        specularLightColor =[0,0,0]

                        
                        

                        for light in self.lights:
                            if light.lightType == "Ambient":
                                ambientLightColor = [(ambientLightColor[i] + light.getLightColor()[i]) for i in range (3)]
                              
                            else:
                                diffuseLightColor = [(diffuseLightColor[i] + light.getDiffuseColor(intercept)[i]) for i in range (3)]
                                specularLightColor = [(specularLightColor[i] + light.getSpecularColor(intercept, self.camPosition)[i]) for i in range (3)]

                        lightColor = [(ambientLightColor[i] + diffuseLightColor[i] + specularLightColor[i]) for i in range(3)]

                        finalColor = [min(1,surfaceColor[i] * lightColor[i]) for i in range(3)]
                        self.rtPoint(x,y, finalColor)  
