import numpy as np

"""
Load student scores into a NumPy array. Find top/bottom performers, normalize grades to a 0–100 scale, compute class averages, and flag students below a threshold.
"""
# Array of Student Scores
std_Score = np.array([220, 340, 256, 178, 290, 492, 399, 154, 365, 487, 160])
total_marks = 500

# find percentage
percentage = (std_Score / total_marks) * 100


# Top Student
print("The Top Student Got : ", percentage.max())
# bottom Line Student
print("The bottom Student Got : ", percentage.min())
# Marks avg Student
print(f"Class Average percentage this year : {percentage.mean().round(2)}%")
# List mein pass students using boolean masking
print("Pass Students in Exams : ", std_Score[percentage >= 40])
# List mein pass students using boolean masking
print("Students fail in Exams : ", std_Score[percentage < 40])

