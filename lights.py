
import libreria as lb

# def reflectVector(normal, direction):
#     dot_product_result = lb.dot_product(normal, direction)
#     reflect = [2 * dot_product_result * normal[i] for i in range(3)]
#     reflect = [reflect[i] - direction[i] for i in range(3)]
#     reflect_length = lb.vector_norm(reflect)
#     reflect = [reflect[i] / reflect_length for i in range(3)]
#     return reflect
    # reflect = 2 * np.dot(normal, direction)
    # reflect = np.multiply(reflect, normal)
    # reflect = np.subtract(reflect, direction)
    # reflect = reflect / np.linalg.norm(reflect)
    # return reflect

class Light(object):
    def __init__(self, intensity = 1, color = (1,1,1), lightType = "None"):
        self.intensity = intensity
        self.color = color
        self.lightType = lightType

    def getLightColor(self):
        return [self.color[0] * self.intensity,
                self.color[1] * self.intensity,
                self.color[2] * self.intensity]
    
    def getDiffuseColor(self, intercept):
        return None
    
    def getSpecularColor(self, intercept, viewPos):
        return None

class AmbientLight(Light):
    def __init__(self, intensity = 1, color = (1,1,1)):
        super().__init__(intensity, color, "Ambient")

class DirectionalLight(Light):
    def __init__(self, direction = (0, -1, 0),intensity=1, color=(1, 1, 1)):
        # self.direction = direction / np.linalg.norm(direction)
        self.direction = lb.normalize_vector(direction)
        super().__init__(intensity, color, "Directional")

    def getDiffuseColor(self, intercept):

        dir = [(i * -1) for i in self.direction]

        # intensity = np.dot(intercept.normal, dir) * self.intensity
        intensity = lb.dot_product(intercept.normal, dir) * self.intensity
        intensity = max(0, min(1,intensity))
        intensity *= 1 - intercept.obj.material.Ks

        diffuseColor = [(i * intensity) for i in self.color]

        return diffuseColor

    def getSpecularColor(self, intercept, viewPos):
        
        dir = [(i * -1) for i in self.direction]
        reflect = lb.reflect_vector(intercept.normal, dir)

        # viewDir = np.subtract(viewPos, intercept.point)
        # viewDir = viewDir / np.linalg.norm(viewDir)
        viewDir = [viewPos[i] - intercept.point[i] for i in range(3)]
        viewDir = lb.normalize_vector(viewDir)

        # specIntensity = max(0, np.dot(viewDir, reflect)) ** intercept.obj.material.spec
        specIntensity = max(0, lb.dot_product(viewDir, reflect)) ** intercept.obj.material.spec
        specIntensity *= intercept.obj.material.Ks
        specIntensity *= self.intensity

        specColor = [(i * specIntensity) for i in self.color]

        return specColor
        
class PointLight(Light):
    def __init__(self, point = (0,0,0), intensity=1, color=(1, 1, 1)):
        self.point = point
        super().__init__(intensity, color, "Point")

    def getDiffuseColor(self, intercept):
        # dir = np.subtract(self.point, intercept.point)
        # R = np.linalg.norm(dir)
        # dir = dir / R
        dir = lb.subtract_vectors(self.point, intercept.point)
        R = lb.vector_norm(dir)
        dir = lb.normalize_vector(dir)

        # intensity = np.dot(intercept.normal, dir) * self.intensity
        # intensity *= 1 - intercept.obj.material.Ks

        intensity = lb.dot_product(intercept.normal, dir) * self.intensity
        intensity *= 1 - intercept.obj.material.Ks

        if R != 0:
            intensity /= R ** 2

        intensity = max(0, min(1,intensity))

        return [(i * intensity) for i in self.color]
    
    def getSpecularColor(self, intercept, viewPos):
    
        # dir = np.subtract(self.point, intercept.point)
        # R = np.linalg.norm(dir)
        # dir = dir / R

        dir = lb.subtract_vectors(self.point, intercept.point)
        R = lb.vector_norm(dir)
        dir = lb.normalize_vector(dir)

        reflect = lb.reflect_vector(intercept.normal, dir)

        # viewDir = np.subtract(viewPos, intercept.point)
        # viewDir = viewDir / np.linalg.norm(viewDir)
        viewDir = lb.subtract_vectors(viewPos, intercept.point)
        viewDir = lb.normalize_vector(viewDir)

        # specIntensity = max(0, np.dot(viewDir, reflect)) ** intercept.obj.material.spec
        # specIntensity *= intercept.obj.material.Ks
        # specIntensity *= self.intensity
        specIntensity = max(0, lb.dot_product(viewDir, reflect)) ** intercept.obj.material.spec
        specIntensity *= intercept.obj.material.Ks
        specIntensity *= self.intensity

        if R != 0:
            specIntensity /= R ** 2
        specIntensity = max(0, min(1,specIntensity))


        specColor = [(i * specIntensity) for i in self.color]

        return specColor