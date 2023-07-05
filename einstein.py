#input from user for mass as an integer (in kilograms)
print("Lets find Energy!!!")
mass = int(input("Enter the value of mass(in kilograms): "))
c = 300000000
#Formula
Energy = mass * (c ** 2) 
#output
print(f"The amount of energy used: {Energy} joules")