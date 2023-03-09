# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # print("Alkali metals:")
    # print()
    # print("{0:<15}{1:<10}{2:^25}{3:>15}".format("Element", "Symbol", "Atomic number", "Atomic weight"))
    # print("{0:<15}{1:<10}{2:^25}{3:>15}".format("Lithium", "Li", 3, 6.94))
    # print("{0:<15}{1:<10}{2:^25}{3:>15}".format("Sodium", "Na", 11, 22.990))
    # print("{0:<15}{1:<10}{2:^25}{3:>15}".format("Potassium", "K", 19, 39.098))
    # print("{0:<15}{1:<10}{2:^25}{3:>15}".format("Rubidium", "Rb", 37, 85.468))
    # print("{0:<15}{1:<10}{2:^25}{3:>15}".format("Caesium", "Cs", 55, 132.905))
    # print("{0:<15}{1:<10}{2:^25}{3:>15}".format("Francium", "Fr", 87, 223))
    # print()
    # print("12345678901234567890123456789012345678901234567890123456789012345")

#############################################################################################

    stud_f_name = input("Enter the first name: ")
    stud_l_name = input("Enter the last name: ")
    stud_age = input("Enter the age: ")
    stud_gpa = input("Enter the gpa: ")

    print("{0:<15}{1:<25}".format("Input", "Result"))
    print("{0:<15}{1:<25}".format(stud_f_name, "Enter the first name: " + stud_f_name))
    print("{0:<15}{1:<25}".format(stud_l_name, "Enter the last name: " + stud_l_name))
    print("{0:<15}{1:<25}".format(stud_age, "Enter the age: " + stud_age))
    print("{0:<15}{1:<25}".format(stud_gpa, "Enter the GPA: " + stud_gpa))
    print("{0:<15}{1:<25}".format("", "Name: " + "\t" + stud_f_name + " " + stud_l_name))
    print("{0:<15}{1:<25}".format("", "Age: " + "\t" + stud_age))
    print("{0:<15}{1:<25}".format("", "GPA Score: " + "\t" + stud_gpa))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
