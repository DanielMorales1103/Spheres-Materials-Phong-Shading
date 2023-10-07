from math import isclose
import math
def subtract_vectors(v1, v2):
    return [v1[i] - v2[i] for i in range(3)]

def add_vectors(v1, v2):
    return [v1[i] + v2[i] for i in range(3)]

# Define una función para calcular la norma de un vector.
def vector_norm(v):
    return math.sqrt(sum([v[i] ** 2 for i in range(3)]))
#Regresa vector normalizado
def normalize_vector(v):
    length = vector_norm(v)
    return [v[i] / length for i in range(3)]
# Define una función para calcular el producto escalar de dos vectores.
def dot_product(v1, v2):
    return sum([v1[i] * v2[i] for i in range(3)])

# Define una función para sumar un vector y un escalar multiplicado por otro vector.
def add_vector_scaled(v1, scalar, v2):
    return [v1[i] + scalar * v2[i] for i in range(3)]



def multiply_vector_scalar(v, scalar):
    return [scalar * v[i] for i in range(3)]



def reflect_vector(normal, direction):
    dot_product_result = dot_product(normal, direction)
    reflect = [2 * dot_product_result * normal[i] for i in range(3)]
    reflect = [reflect[i] - direction[i] for i in range(3)]
    return reflect

def refract_vector(normal, incident, n1, n2):
    c1 = dot_product(normal, incident)

    if c1 < 0:
        c1 = -c1
    else:
        normal = [i * -1 for i in normal]
        n1, n2 = n2, n1
    
    n = n1 / n2

    escalar = (1 - n**2 * (1 - c1**2)) ** 0.5
    v1 = multiply_vector_scalar(add_vector_scaled(incident, c1, normal), n) 
    v2 =  multiply_vector_scalar(normal, escalar)
    T = subtract_vectors(v1, v2)
    T =  normalize_vector(T)
    return T


def totalInternalreflection(incident, normal, n1, n2):
    c1 = dot_product(normal, incident)

    if c1 < 0:
        c1 = -c1
    else:
        normal = [i * -1 for i in normal]
        n1, n2 = n2, n1

    if n1 < n2:
        return False
    
    theta1 = math.acos(c1)
    thetaC = math.asin(n2/n1)
    
    return theta1 >= thetaC

def fresnel(normal, incident, n1, n2):
    c1 = dot_product(normal, incident)

    if c1 < 0:
        c1 = -c1
    else:
        n1, n2 = n2, n1
    
    s2 = (n1 * (1 - c1**2) **0.5) / n2
    c2 = (1 - s2 ** 2) ** 0.5

    F1 = (((n2 * c1) - (n1 * c2)) / ((n2 * c1) + (n1 * c2))) ** 2
    F2 = (((n1 * c2) - (n2 * c1)) / ((n1 * c2) + (n2 * c1))) ** 2

    Kr = (F1 + F2) / 2
    Kt = 1 - Kr
    return Kr, Kt
