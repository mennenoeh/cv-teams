import numpy as np
import math


vertical = [0,1]
V1 = [3,3]
V1_unit = V1 / np.linalg.norm(V1)


angle = np.arccos(np.dot(V1_unit, vertical))

print(math.degrees(angle))