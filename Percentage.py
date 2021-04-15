print()
print("---PERCENTAGE CALCULATOR XD---")
print()
print("Total Marks is 80 Per Subject LOL")
print("____ENTER YOUR MARKS FOR EACH SUBJECT____")
print()

try:
    maths = int(input("Maths Marks : "))
    physics = int(input("Physics Marks: "))
    english = int(input("English Marks: "))
    computer_science = int(input("Computer Science Marks: "))
    chemistry = int(input("Chemistry Marks: "))
except ValueError:
    print("Type Number Only XD!!")

marks_obtained = (maths + physics + english + chemistry + computer_science)
total_marks = 400

percentage = (marks_obtained/total_marks) * 100
print("You got: " + str(percentage) + "percent.")
