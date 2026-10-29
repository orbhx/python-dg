# Project: Gamma-Ray Interval Flagging
# Purpose: Practise pairing depth and gamma-ray data
# and flagging readings above a specified threshold.
# Threshold: 80 API (illustrative rule for this exercise)

# Gamma-Ray Interval Flagging
# Practice project: Python for Digital Geoscience

depths = [1500, 1505, 1510, 1515, 1520]
gamma_ray = [35, 65, 82, 100, 75]

threshold = 70
count = 0
for depth, gr in zip(depths, gamma_ray):
    if gr > threshold:
        count += 1
        print(f"Depth: {depth} m | Gamma Ray: {gr} API | Review interval")
    else:
        print(f"Depth: {depth} m | Gamma Ray: {gr} API | No flag from this rule")
print(f"Total flagged Intervals: {count}")

total_intervals = len(gamma_ray)
percentage_flagged = (count / total_intervals) * 100

print(f"Total flagged intervals: {count}")
print(f"Percentage flagged: {percentage_flagged}%")
