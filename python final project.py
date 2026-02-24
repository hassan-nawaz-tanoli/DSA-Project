# from tkinter import *

# # Create window
# root = Tk()
# root.title("Land Measurement Calculator")
# root.geometry("400x350")
# root.config(bg="#e8f6f3")

# # Heading
# Label(
#     root,
#     text="Land Measurement Calculator",
#     font=("Arial", 16, "bold"),
#     bg="#e8f6f3",
#     fg="#0b5345"
# ).pack(pady=15)

# # Input label
# Label(
#     root,
#     text="Enter Area in Square Feet:",
#     font=("Arial", 11),
#     bg="#e8f6f3"
# ).pack()

# # Input box
# area_entry = Entry(root, font=("Arial", 11), width=25)
# area_entry.pack(pady=10)

# # Result labels
# marla_label = Label(root, text="", font=("Arial", 11), bg="#e8f6f3")
# kanal_label = Label(root, text="", font=("Arial", 11), bg="#e8f6f3")
# acre_label = Label(root, text="", font=("Arial", 11), bg="#e8f6f3")

# # Function
# def calculate():
#     sq_ft = float(area_entry.get())

#     marla = sq_ft / 272.25
#     kanal = marla / 20
#     acre = kanal / 8

#     marla_label.config(text="Marla: " + str(round(marla, 2)))
#     kanal_label.config(text="Kanal: " + str(round(kanal, 2)))
#     acre_label.config(text="Acre: " + str(round(acre, 4)))

#     marla_label.pack()
#     kanal_label.pack()
#     acre_label.pack()

# # Button
# Button(
#     root,
#     text="Calculate",
#     font=("Arial", 11),
#     bg="#48c9b0",
#     fg="white",
#     width=15,
#     command=calculate
# ).pack(pady=15)

# # Run window
# root.mainloop()



# Land Measurement Calculator (Beginner Level)

# Land Measurement Calculator
# Beginner Level – Console Program

# Total land area


# total_area = 0

# # Ask how many squares
# num_squares = int(input("Enter number of squares: "))

# # Loop for each square
# for i in range(1, num_squares + 1):
#     print("\nSquare", i)

#     # Take 4 sides of square (feet)
#     side1 = float(input("Enter side 1 (feet): "))
#     side2 = float(input("Enter side 2 (feet): "))
#     side3 = float(input("Enter side 3 (feet): "))
#     side4 = float(input("Enter side 4 (feet): "))

#     # Opposite sides ka average
#     length = (side1 + side3) / 2
#     width = (side2 + side4) / 2

#     # Area calculation
#     area = length * width
#     total_area = total_area + area

#     print("Area of square", i, "=", round(area, 2), "sq ft")

# # ---- Conversion ----
# marla = total_area / 272.25
# kanal = marla / 20
# acre = kanal / 8

# # Final results
# print("\n==============================")
# print("TOTAL LAND AREA")
# print("==============================")
# print("Square Feet:", round(total_area, 2))
# print("Marla:", round(marla, 2))
# print("Kanal:", round(kanal, 2))
# print("Acre:", round(acre, 4))




# ==========================================
# GPA & CGPA Calculator
# Final Project (Beginner Level)
# ==========================================

total_quality_points = 0
total_credit_hours = 0

# Number of semesters
num_semesters = int(input("Enter number of semesters: "))

# Loop for each semester
for sem in range(1, num_semesters + 1):
    print("\n--- Semester", sem, "---")

    semester_quality = 0
    semester_credits = 0

    # Number of subjects
    num_subjects = int(input("Enter number of subjects: "))

    # Loop for each subject
    for sub in range(1, num_subjects + 1):
        print("\nSubject", sub)

        credit = float(input("Enter credit hours: "))
        grade = float(input("Enter grade points (0.0 - 4.0): "))

        semester_quality += credit * grade
        semester_credits += credit

    # GPA calculation
    semester_gpa = semester_quality / semester_credits

    print("\nGPA of Semester", sem, "=", round(semester_gpa, 2))

    # Add to overall CGPA
    total_quality_points += semester_quality
    total_credit_hours += semester_credits

# CGPA calculation
cgpa = total_quality_points / total_credit_hours

print("\n================================")
print("FINAL RESULT")
print("================================")
print("CGPA =", round(cgpa, 2))
