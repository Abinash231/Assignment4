x = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(x + "\n")
print("Data successfully written to output.txt.")
y = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(y + "\n")
print("Data successfully appended.")
print("\nFinal content of output.txt:\n")
with open("output.txt", "r") as file:
    print(file.read())
