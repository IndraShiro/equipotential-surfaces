#Superficies equipotenciales
#I.I. DE LEÓN CORTÉS: ileon001@alumno.uaemex.mx
#C. GILL MEDINA: cgilm002@alumno.uaemex.mx

#Electrodinámica a cargo del Dr. J.M.DÁVILA DÁVILA.


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from skimage import measure
from matplotlib import cm

def potencial_electrico(x, y, z, a, k):
    r1 = np.sqrt(x**2 + y**2 + z**2)
    r2 = np.sqrt((x - a)**2 + y**2 + z**2)
    return k * (1/r1 + 1/(3*r2))

# Definir parámetros
a = 1
k = 2
x = np.linspace(-1, 2, 50)
y = np.linspace(-1, 2, 50)
z = np.linspace(-1, 2, 50)
X, Y, Z = np.meshgrid(x, y, z)
V = potencial_electrico(X, Y, Z, a, k)

# Ajustar niveles de contorno dentro del rango válido
V_min, V_max = np.min(V), np.max(V)
contour_levels = np.linspace(V_min + 0.01 * (V_max - V_min), V_max - 0.01 * (V_max - V_min), 10)

# Crear figura 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Dibujar superficies equipotenciales como espacios opacos
for level in contour_levels:
    verts, faces, _, _ = measure.marching_cubes(V, level)
    verts = verts * [x.ptp() / V.shape[0], y.ptp() / V.shape[1], z.ptp() / V.shape[2]]  # Escalar a coordenadas reales
    ax.plot_trisurf(verts[:, 0] - 1, verts[:, 1] - 1, faces, verts[:, 2] - 1, cmap=cm.coolwarm, alpha=0.5)

# Dibujar cargas
ax.scatter([0, a], [0, 0], [0, 0], color=['red', 'black'], s=100, label='Cargas')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Guardar la gráfica en un archivo (opcional)
plt.savefig('equipotenciales_3d.png')
print("Gráfica guardada como 'equipotenciales_3d.png'")