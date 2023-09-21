from math import isclose
import math

def subtract_vectors(v1, v2):
    return [v1[i] - v2[i] for i in range(3)]

# Define una función para calcular la norma de un vector.
def vector_norm(v):
    return math.sqrt(sum([v[i] ** 2 for i in range(3)]))

# Define una función para calcular el producto escalar de dos vectores.
def dot_product(v1, v2):
    return sum([v1[i] * v2[i] for i in range(3)])

# Define una función para sumar un vector y un escalar multiplicado por otro vector.
def add_vector_scaled(v1, scalar, v2):
    return [v1[i] + scalar * v2[i] for i in range(3)]

def normalize_vector(v):
    length = vector_norm(v)
    return [v[i] / length for i in range(3)]

def reflect_vector(normal, direction):
    dot_product_result = dot_product(normal, direction)
    reflect = [2 * dot_product_result * normal[i] for i in range(3)]
    reflect = [reflect[i] - direction[i] for i in range(3)]
    return reflect