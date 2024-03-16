print("Welcome to the Binary/Hexadecimal Converter App")

usr_data = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))
print("Generating lists....complete!")

# Input start and end values from the user to display a part of list in various formats
print("\nUsing slices, we will now show a portion of each list.")
start_value = int(input("What decimal value would you like to start with: "))
end_value = int(input("What decimal value would you like to end with: "))

# Displaying part of list in Decimal format
print(f"\nDecimal values from {start_value} to {end_value}:")
for i in range(start_value, end_value+1):
    print(i)

# Displaying part of list in Binary format
print(f"\nBinary values from {start_value} to {end_value}")
for i in range(start_value, end_value+1):
    print(bin(i))

# Displaying part of list in Hexadecimal format
print(f"\nHexadecimal values from {start_value} to {end_value}")
for i in range(start_value, end_value+1):
    print(hex(i))

# Displaying in Decimal-Binary-Hexadecimal format of the input from the user
input(f"\nPress Enter to see all values from 1 to {usr_data}.")
print("Decimal----Binary----Hexadecima")
print("-------------------------------------")
for i in range(1,usr_data+1):
    print(f"{i}----{bin(i)}----{hex(i)}")