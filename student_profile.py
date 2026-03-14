### Storing information
# Goal: store and display a student profile.

name = "Dipak"
age = 21
gpa = 3.7
is_enrolled = True

# Step 2 — Print profile

print("Student Name:", name)
print("Age:", age)
print("GPA:", gpa)
print("Enrolled:", is_enrolled)


## Udpate state and store updated states
# Step 3 — Update GPA
gpa = gpa + 0.1
print("Updated GPA: ", gpa)



# Step 4 — Check academic standing
if gpa >= 3.5:
    print("Honor Student")

    