# 14)A student will not be allowed to sit in exam if his/her attendence is less than 75%.

# Take following input from user

# Number of classes held

# Number of classes attended.

# And print

# percentage of class attended

# Is student is allowed to sit in exam or not.

classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100 #Pemdas Rule follow kre gy

print(f"Percentage of classes attended: {attendance_percentage:2f}%")

if attendance_percentage >= 75:
    print("Student allowed to sit in exam.")
else:
    print("Student NOT allowed to sit in the exam.")
