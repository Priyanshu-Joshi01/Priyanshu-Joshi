name = input("Enter student name: ")
cls = input("Enter class: ")
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))


total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

if percentage >= 60:
    grade = 'A'
elif percentage >= 50:
    grade = 'B'
elif percentage >= 40:
    grade = 'C'
elif percentage >= 33:
    grade = 'D'
else:
    grade = 'Fail'

print(f"Name: {name}")
print(f"Class: {cls}")
print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")