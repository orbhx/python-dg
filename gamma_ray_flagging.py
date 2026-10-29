# Gamma-Ray Interval Flagging
# Practice project: Python for Digital Geoscience

depths = [1500, 1505, 1510, 1515, 1520]
gamma_ray = [35, 65, 82, 100, 75]

threshold = 80

for depth, gr in zip(depths, gamma_ray):
    if gr > threshold:
        print(f"Depth: {depth} m | Gamma Ray: {gr} API | Review interval")
    else:
        print(f"Depth: {depth} m | Gamma Ray: {gr} API | No flag from this rule")
