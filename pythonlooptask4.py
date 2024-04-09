number_student_pass = 0
number_student_fail = 0

for numbers in range(1, 16):
	teacher_input = int(input("Enter student's score: "))
	if teacher_input >= 45:
		number_student_pass += 1
	elif teacher_input < 45:
		number_student_fail += 1

print("Number of students who passed = ",number_student_pass)
print("Number of students who failed = ",number_student_fail)