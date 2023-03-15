####Q1
product_code = "377B"
product_name = "Beef Liquid Stock"
product_size = "250mL"
product_price = 2.15

print(product_code +  ": " + product_name + ", " + product_size)
print(product_name +  ", " + product_size + ", $" + str(product_price))
print("{0}: {1}, {2}".format(product_code, product_name, product_size))
print("{0}, {1}, ${2}".format(product_name, product_size, str(product_price)))

####Q2
cows_purchase = input("Enter number of cows to purchase: ")
ducks_purchase = input("Enter number of ducks to purchase: ") 
chicken_purchase = input("Enter number of chicken to purchase: ")

cost_of_cow = int(cows_purchase) * 30
cost_of_duck = int(ducks_purchase) * 5
cost_of_chicken = int(chicken_purchase) * 3

total_cost = cost_of_cow + cost_of_duck + cost_of_chicken

print("Cost:")
print(cows_purchase + " cow = " + str(cost_of_cow) + " grassies")
print(ducks_purchase + " duck = " + str(cost_of_duck) + " grassies")
print(chicken_purchase + " chick = " + str(cost_of_chicken) + " grassies")
print("Total = " + str(total_cost) + " grassies")

####Q3
print("{0:>10}{1:^30}{2:<10}".format("Faces", "Name", "Vertices"))
print("{0:>10}{1:^30}{2:<10}".format(4, "Tetrahedron", 4))
print("{0:>10}{1:^30}{2:<10}".format(6, "Cube", 8))
print("{0:>10}{1:^30}{2:<10}".format(8, "Octahedron", 6))
print("{0:>10}{1:^30}{2:<10}".format(12, "Dodecahedron", 20))
print("{0:>10}{1:^30}{2:<10}".format(20, "Icosahedron", 12))

####Q4
print("|{0:<10}|{1:^30}|{2:>10}|".format("Faces", "Name", "Vertices"))
print("|{0:<10}|{1:^30}|{2:>10}|".format(4, "Tetrahedron", 4))
print("|{0:<10}|{1:^30}|{2:>10}|".format(6, "Cube", 8))
print("|{0:<10}|{1:^30}|{2:>10}|".format(8, "Octahedron", 6))
print("|{0:<10}|{1:^30}|{2:>10}|".format(12, "Dodecahedron", 20))
print("|{0:<10}|{1:^30}|{2:>10}|".format(20, "Icosahedron", 12))