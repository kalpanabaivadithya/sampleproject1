import pandas as pd

# Create dataset 1: Students
students = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "name": ["Asha", "Ravi", "Kiran", "Meena", "Arjun"],
    "department": ["CSE", "EEE", "CSE", "ECE", "EEE"]
})

# Create dataset 2: Marks
marks = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "maths": [85, 70, 88, 60, 95],
    "science": [78, 65, 82, 75, 92],
    "english": [90, 72, 85, 70, 88]
})

# Merge datasets
data = pd.merge(students, marks, on="student_id")

# Calculate total and average
data["total"] = data["maths"] + data["science"] + data["english"]
data["average"] = data["total"] / 3

# Assign grade
def get_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

data["grade"] = data["average"].apply(get_grade)

# Find top student
top_student = data.loc[data["average"].idxmax()]

# Department-wise average
dept_avg = data.groupby("department")["average"].mean()

# Display results
print("\n--- Full Data ---")
print(data)

print("\n--- Top Performer ---")
print(top_student)

print("\n--- Department-wise Average ---")
print(dept_avg)

# Save to file
data.to_csv("result.csv", index=False)