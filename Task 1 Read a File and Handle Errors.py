try:
    with open("sample.txt", "r") as file:
        print("Reading file content:\n")
        for line_num, line in enumerate(file, start=1):
            print(f"Line {line_num}: {line.strip()}")
except FileNotFoundError: #If the file does not exist. Then this message show: Error: The file 'sample.txt' was not found.
    print("Error: The file sample.txt was not found.")
