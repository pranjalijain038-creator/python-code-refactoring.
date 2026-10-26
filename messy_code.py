name = input("Enter student name: ")
m1 = float(input("Enter marks in subject 1: "))
m2 = float(input("Enter marks in subject 2: "))
m3 = float(input("Enter marks in subject 3: "))

total = m1 + m2 + m3
print("Student:", name)
print("Total marks:", total)

avg = total / 3
print("Average marks:", avg)

name2 = input("Enter student name again: ")
print("Student name is", name2)
print("The total is", m1 + m2 + m3)
print("The average is", (m1 + m2 + m3) / 3)

