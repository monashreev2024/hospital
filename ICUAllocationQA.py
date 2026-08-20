from ICUAllocation import *

print("ICU ALLOCATION QA")
print("------------------")

# 1. Critical patient
result = add_patient(
    "P001", 65, 85, 130, 80, 39, "Heart Disease"
)
print("Critical Patient:", result)


# 2. Normal patient
result = add_patient(
    "P002", 30, 98, 75, 120, 37, "None"
)
print("Normal Patient:", result)


# 3. Emergency case
result = add_patient(
    "P003", 70, 80, 140, 75, 40, "Heart Disease", True
)
print("Emergency Case:", result)


# 4. No ICU beds
result = add_patient(
    "P004", 50, 95, 80, 110, 37, "None"
)
print("No ICU Bed:", result)


# 5. Duplicate patient
result = add_patient(
    "P001", 65, 90, 100, 100, 37, "None"
)
print("Duplicate Patient:", result)


# 6. Invalid oxygen level
result = add_patient(
    "P005", 40, 150, 80, 120, 37, "None"
)
print("Invalid Oxygen:", result)


# 7. Invalid heart rate
result = add_patient(
    "P006", 40, 98, 0, 120, 37, "None"
)
print("Invalid Heart Rate:", result)


# 8. Priority boundary
score, priority = calculate_priority(
    93, 120, 100, 37
)
print("Priority Boundary:", score, priority)


# 9. Multiple patients
result = add_patient(
    "P007", 60, 88, 125, 85, 39, "Diabetes"
)
print("Multiple Patient:", result)


print("------------------")
print("QA TESTING COMPLETED")
