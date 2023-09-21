
import math
import libreria as lb

class Intercept(object):
    def __init__(self, distance, point, normal, obj):
        self.distance = distance
        self.point =point
        self.normal = normal
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
        L = lb.subtract_vectors(self.position, orig) # np.subtract(self.position, orig)
        #lenghtL = np.linalg.norm(L)
        lengthL = lb.vector_norm(L)
        tca = lb.dot_product(L, dir)
        # tca = np.dot(L, dir)
        # d = (lengthL ** 2 - tca ** 2) ** 0.5
        d = math.sqrt(lengthL ** 2 - tca ** 2)

        if d > self.radius:
            return None
        
        # thc = (self.radius ** 2 - d ** 2) ** 0.5
        thc = math.sqrt(self.radius ** 2 - d ** 2)
        t0 = tca - thc
        t1 = tca + thc
        if t0 <= 0:
            t0 = t1
        if t0 < 0:
            return None
        
        # P = np.add(orig, t0 * np.array(dir))
        
        # normal = np.subtract(P, self.position)
        # normal = normal / np.linalg.norm(normal)
        P = lb.add_vector_scaled(orig, t0, dir)
        normal = lb.subtract_vectors(P, self.position)
        normal_length = lb.vector_norm(normal)
        normal = [normal[i] / normal_length for i in range(3)]

        return Intercept(distance= t0,
                         point= P,
                         normal= normal,
                         obj= self)