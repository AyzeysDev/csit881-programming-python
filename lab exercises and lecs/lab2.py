####Q6
product_code = "377B"
product_name = "Beef Liquid Stock"
product_size = "250mL"
product_price = 2.15

print(product_code + ": " + product_name + ", " + product_size)

####Q7
product_code = "377B"
product_name = "Beef Liquid Stock"
product_size = "250mL"
product_price = 2.15

print("\"Beef Liquid Stock\"" + ", " + product_size)

####Q8
product_code = "377B"
product_name = "Beef Liquid Stock"
product_size = "250mL"
product_price = 2.15

print(product_name + ", " + product_size + ", " + "$" + str(product_price))

####Q9
first_int = input("Enter the first integer: ")
second_int = input("Enter the second integer: ") 
third_int = input("Enter the third integer: ")

sq_first = int(first_int) ** 2
sq_second = int(second_int) ** 2
sq_third = int(third_int) ** 2

sum = sq_first + sq_second + sq_third

print("Here is the equation:")
print(first_int + "x" + first_int + " + " + second_int + "x" + second_int + " + " + third_int + "x" + third_int + " = " + str(sq_first) + " + " + str(sq_second) + " + " + str(sq_third) + " = " + str(sum)) 