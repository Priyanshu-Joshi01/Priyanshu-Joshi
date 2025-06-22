
name = input("Enter the student's name: ")
student_class = input("Enter the student's class: ")
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))
mark4 = float(input("Enter marks for Subject 4: "))
mark5 = float(input("Enter marks for Subject 5: "))
total_marks = mark1 + mark2 + mark3 + mark4 + mark5
percentage = (total_marks / 500) * 100
print(total_marks)
print(percentage)
if percentage > 50:
    print("Grade A")
elif percentage > 50:
    print("Grade B")
elif percentage > 40:
    print("Grade C")
else:
    print("Fail")






# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# combined = str1 + str2
# print("\nConcatenated String:", combined)
# print("Uppercase       :", combined.upper())
# print("Lowercase       :", combined.lower())
# print("Title Case      :", combined.title())
# print("Capitalized     :", combined.capitalize())
# print("Length          :", len(combined))
# print("Is Alphabetic   :", combined.isalpha())
# print("Is Numeric      :", combined.isnumeric())
# print("Starts with 'A' :", combined.startswith('A'))
# print("Ends with 'z'   :", combined.endswith('z'))
# print("Replaced 'a' with '@' :", combined.replace('a', '@'))
# print("Count of 'a'    :", combined.count('a'))
# print("Index of first 'a'    :", combined.find('a'))
# print("String Reversed :", combined[::-1])
