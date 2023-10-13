
from math import tan, pi, atan2, acos, sqrt
import libreria as lb
import numpy as np
class Intercept(object):
    def __init__(self, distance, point, normal, obj, texcoords):
        self.distance = distance
        self.point =point
        self.normal = normal
        self.texcoords = texcoords
        self.obj = obj

class Shape(object):
    def __init__(self, position, material):
        self.position = position
        self.material = material

    def ray_intersect(self, orig, dir):
        return None
    
class Sphere(Shape):
    def __init__(self, position, radius, material):
        self.radius = radius
        super().__init__(position, material)
    
    def ray_intersect(self, orig, dir):
        L = lb.subtract_vectors(self.position, orig) 
        lengthL = lb.vector_norm(L)
        tca = lb.dot_product(L, dir)
        d = sqrt(lengthL ** 2 - tca ** 2)

        if d > self.radius:
            return None
        
        thc = sqrt(self.radius ** 2 - d ** 2)
        t0 = tca - thc
        t1 = tca + thc
        if t0 <= 0:
            t0 = t1
        if t0 < 0:
            return None
        
        P = lb.add_vector_scaled(orig, t0, dir)
        normal = lb.subtract_vectors(P, self.position)
        normal_length = lb.vector_norm(normal)
        normal = [normal[i] / normal_length for i in range(3)]

        u = (atan2(normal[2], normal[0]) / (2*pi)) + 0.5
        v = acos(normal[1]) / pi

        return Intercept(distance= t0,
                         point= P,
                         normal= normal,
                         texcoords= (u,v),
                         obj= self)
    

class Plane(Shape):
    def __init__(self, position, normal, material):
        self.normal = lb.normalize_vector(normal)
        # self.normal = normal/np.linalg.norm(normal)
        super().__init__(position, material)
    
    def ray_intersect(self, orig, dir):
        denom = lb.dot_product(dir, self.normal) 
        # denom = np.dot(dir, self.normal)
        
        if abs(denom) <= 0.0001:
            return None
        
        num = lb.dot_product(lb.subtract_vectors(self.position, orig), self.normal)
        # num = np.dot( np.subtract(self.position, orig), self.normal)
        t = num / denom

        if t < 0:
            return None

        P = lb.add_vector_scaled(orig, t, dir)
        # P = np.add(orig, t * np.array(dir))
        return Intercept(distance= t,
                         point= P,
                         normal= self.normal,
                         texcoords= None,
                         obj= self)
        
class Disk(Plane):
    def __init__(self, position, normal, radius, material):
        self.radius = radius
        super().__init__(position, normal, material)
    
    def ray_intersect(self, orig, dir):
        planeIntersect = super().ray_intersect(orig, dir)
        
        if planeIntersect is None:
            return None
        
        # contactDistance = np.subtract(planeIntersect.point, self.position)
        # contactDistance = np.linalg.norm(contactDistance)
        contactDistance = lb.subtract_vectors(planeIntersect.point, self.position)
        contactDistance = lb.vector_norm(contactDistance)
        
        if contactDistance > self.radius:
            return None
        
        return Intercept(distance = planeIntersect.distance,
                         point = planeIntersect.point,
                         normal = self.normal,
                         texcoords= None,
                         obj = self)
    
class AABB(Shape):
    def __init__(self, position, size, material):
        self.size = size
        super().__init__(position, material)

        self.planes = []


        #sides
        leftPlane = Plane( lb.add_vectors(self.position, (-size[0] / 2,0,0)), (-1,0,0), material )
        rigthPlane = Plane( lb.add_vectors(self.position, (size[0] / 2,0,0)), (1,0,0), material )

        bottomPlane = Plane( lb.add_vectors(self.position, (0,-size[1] / 2,0)), (0,-1,0), material )
        topPlane = Plane( lb.add_vectors(self.position, (0,size[1] / 2,0)), (0,1,0), material )

        backPlane = Plane( lb.add_vectors(self.position, (0, 0,-size[2] / 2)), (0,0, -1), material )
        frontPlane = Plane( lb.add_vectors(self.position, (0, 0,size[2] / 2)), (0,0, 1), material )

        self.planes.append(leftPlane)
        self.planes.append(rigthPlane)
        self.planes.append(bottomPlane)
        self.planes.append(topPlane)
        self.planes.append(backPlane)
        self.planes.append(frontPlane)


        # limites 
        self.boundsMin = [0,0,0]
        self.boundsMax = [0,0,0]

        bias = 0.001

        for i in range(3):
            self.boundsMin[i] = self.position[i] - (bias + size[i] / 2)
            self.boundsMax[i] = self.position[i] + (bias + size[i] / 2)
    
    def ray_intersect(self, orig, dir):
        intercect = None
        t = float('inf')

        u = 0
        v = 0

        for plane in self.planes:
            planeIntersect = plane.ray_intersect(orig, dir)
            if planeIntersect is not None:
                planePoint = planeIntersect.point
                if self.boundsMin[0] < planePoint[0] < self.boundsMax[0]:
                    if self.boundsMin[1] < planePoint[1] < self.boundsMax[1]:
                        if self.boundsMin[2] < planePoint[2] < self.boundsMax[2]:
                            if planeIntersect.distance < t:
                                t = planeIntersect.distance
                                intercect = planeIntersect

                                # Generar U V
                                if abs(plane.normal[0]) > 0:
                                    u = (planePoint[1] - self.boundsMin[1]) / (self.size[1] + 0.002)
                                    v = (planePoint[2] - self.boundsMin[2]) / (self.size[2] + 0.002)
                                elif abs(plane.normal[1]) > 0:
                                    u = (planePoint[0] - self.boundsMin[0]) / (self.size[0] + 0.002)
                                    v = (planePoint[2] - self.boundsMin[2]) / (self.size[2] + 0.002)
                                elif abs(plane.normal[2]) > 0:
                                    u = (planePoint[0] - self.boundsMin[0]) / (self.size[0] + 0.002)
                                    v = (planePoint[1] - self.boundsMin[1]) / (self.size[1] + 0.002)
        if intercect is None:
            return None      

        return Intercept(distance = t,
                         point = intercect.point,
                         normal = intercect.normal,
                         texcoords= (u, v),
                         obj = self)


class Triangle(Shape):
    def __init__(self, vertices, material):
        # `vertices` es una lista de tres puntos en el espacio que representan los vértices del triángulo
        self.vertices = vertices
        # Calcula la normal del triángulo
        self.normal = lb.normalize_vector(lb.cross_product(lb.subtract_vectors(vertices[1], vertices[0]), lb.subtract_vectors(vertices[2], vertices[0])))
        super().__init__(position=None, material=material)

    def ray_intersect(self, orig, dir):
        edge1 = lb.subtract_vectors(self.vertices[1], self.vertices[0])
        edge2 = lb.subtract_vectors(self.vertices[2], self.vertices[0])

        h = lb.cross_product(dir, edge2)
        a = lb.dot_product(edge1, h)

        if a > -0.0001 and a < 0.0001:
            return None  # El rayo es paralelo al triángulo

        f = 1 / a
        s = lb.subtract_vectors(orig, self.vertices[0])
        u = f * lb.dot_product(s, h)

        if u < 0 or u > 1:
            return None

        q = lb.cross_product(s, edge1)
        v = f * lb.dot_product(dir, q)

        if v < 0 or u + v > 1:
            return None

        t = f * lb.dot_product(edge2, q)

        if t > 0.0001:  # Asegurarse de que el punto de intersección esté delante del rayo
            point = lb.add_vector_scaled(orig, t, dir)
            return Intercept(distance=t, point=point, normal=self.normal, texcoords=None, obj=self)

        return None  # El punto de intersección está detrás del rayo
