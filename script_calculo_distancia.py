import numpy as np
def calcular_proyeccion_escalar(p, a, b):
    ap = p - a
    ab = b - a
    ab_norm = np.linalg.norm(ab)
    print(f"ap: {ap}, ab: {ab}, ab_norm: {ab_norm}")

    if ab_norm == 0:
        print("ab_norm es 0, retornando 0")
        return 0

    resultado = np.dot(ap, ab) / ab_norm
    print(f"Proyección escalar: {resultado}")
    return resultado

def distancia_punto_a_recta(c, a, b):
    ab = b - a
    ab_norm = np.linalg.norm(ab)
    print(f"ab: {ab}, ab_norm: {ab_norm}")

    if ab_norm == 0:
        distancia = np.linalg.norm(c - a)
        print(f"ab_norm es 0, distancia: {distancia}")
        return distancia

    norm = calcular_proyeccion_escalar(c, a, b)
    print(f"norm: {norm}")

    if norm < 0:
        proyeccion = a
        print("norm < 0, proyección = a")
    elif norm > ab_norm:
        proyeccion = b
        print("norm > ab_norm, proyección = b")
    else:
        proyeccion = a + (norm / ab_norm) * ab
        print(f"proyección: {proyeccion}")

    distancia = np.linalg.norm(c - proyeccion)
    print(f"Distancia final: {distancia}")
    return distancia

puntos_iniciales = np.array([[35.262817, -59.448227], [35.2626, -59.455128], [35.262867, -59.447266]])

distancia_punto_a_recta(puntos_iniciales[0], puntos_iniciales[1], puntos_iniciales[2])

import matplotlib.pyplot as plt

p = puntos_iniciales[0]
a = puntos_iniciales[1]
b = puntos_iniciales[2]

plt.figure(figsize=(8, 6))
plt.plot([a[0], b[0]], [a[1], b[1]], 'b-', label='Segmento AB')
plt.plot(p[0], p[1], 'ro', label='Punto P')
plt.plot(a[0], a[1], 'go', label='Punto A')
plt.plot(b[0], b[1], 'mo', label='Punto B')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Segmento AB y punto P')
plt.grid(True)
plt.show()