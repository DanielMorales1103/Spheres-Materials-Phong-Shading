
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