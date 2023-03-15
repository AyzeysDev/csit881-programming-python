#################

#Answer 1
frog_lifecycle = input("Enter the number of steps from egg to frog: ")
arrow = "-->" * int(frog_lifecycle)
print("Here is the expected life cycle:")
print("{0}{1}{2}".format("egg", arrow, "frog"))

######################

#Answer 2
book_name = input("Enter your favourite book name: ")
author_name = input("Enter the author's name: ")
print()
print("Your favourite book is \"{}\" written by \"{}\".".format(book_name, author_name))

######################

#Answer 3
total_puppies = input("Enter the number of puppies: ")
total_kitties = input("Enter the number of kitties: ")
print("You have adopted {} puppies and {} kitties.".format(total_puppies, total_kitties))

insurance_fees = int(total_puppies) * 40 + int(total_kitties) * 30
print("The insurance fee is ${}.".format(str(insurance_fees)))


######################

#Answer 4
first_integer = input("Enter the 1st positive integer: ")
second_integer = input("Enter the 2nd positive integer: ")
third_integer = input("Enter the 3rd positive integer: ")

result = int(first_integer) * int(second_integer) + int(first_integer) * int(third_integer) + int(second_integer) * int(third_integer)
print("Here is the equation:")
print("{0} X {1} + {0} X {2} + {1} X {2} = {3}".format(first_integer, second_integer, third_integer, str(result)))

######################

#Answer 5
first_subject_code = input("Enter the first subject code: ")
first_subject_name = input("Enter the first subject name: ")
first_credit_point = input("Enter the first credit point: ")
second_subject_code = input("Enter the second subject code: ")
second_subject_name = input("Enter the second subject name: ")
second_credit_point = input("Enter the second credit point: ")
print("Your enrolment details are as follows: ")
print("{0:<10}{1:<40}{2:^15}".format("Code", "Name", "Credit"))
print("{0:<10}{1:<40}{2:^15}".format(first_subject_code, first_subject_name, first_credit_point))
print("{0:<10}{1:<40}{2:^15}".format(second_subject_code, second_subject_name, second_credit_point))
print("{0:<10}{1:<40}{2:^15}".format("Total", "", int(first_credit_point) + int(second_credit_point)))