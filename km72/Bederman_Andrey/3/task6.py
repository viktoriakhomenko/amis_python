print("This program calculate how many tables school need to buy for 3 classes")
first=int(input("Enter the number of pupils in 1st group:"))
second=int(input("Enter the number of pupils in 2st group:"))
third=int(input("Enter the number of pupils in 3st group:"))
print("The school need to buy", first//2+first%2+second//2+second%2+third//2+third%2, "tables")
input("\n\nPress Enter to exit the program.")