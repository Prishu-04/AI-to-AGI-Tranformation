import numpy as np


students = np.array([
    [85, 90, 5],
    [72, 80, 4],
    [45, 70, 3],
    [91, 95, 6],
    [60, 78, 2]
])

print("Original Dataset:")
print(students)

print("-" * 40)

scale_values = np.array([100, 100, 10])

scaled_students = students / scale_values

print("Scaled Dataset:")
print(scaled_students)

print("-" * 40)

weights = np.array([0.5, 0.3, 0.2])

weighted_scores = scaled_students * weights

print("Weighted Scores:")
print(weighted_scores)

print("-" * 40)

final_scores = np.sum(weighted_scores, axis=1)

print("Final Scores:")
print(final_scores)

print("-" * 40)

excellent_mask = final_scores >= 0.75
good_mask = (final_scores >= 0.55) & (final_scores < 0.75)
needs_improvement_mask = final_scores < 0.55

print("Excellent Students:")
print(students[excellent_mask])

print("Good Students:")
print(students[good_mask])

print("Needs Improvement Students:")
print(students[needs_improvement_mask])

print("-" * 40)

print("Counts:")
print("Excellent:", len(students[excellent_mask]))
print("Good:", len(students[good_mask]))
print("Needs Improvement:", len(students[needs_improvement_mask]))