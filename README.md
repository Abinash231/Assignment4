# Assignment4
Functionality of the Programs

Task 1: Read a File and Handle Errors

The program attempts to open and read a file named "sample.txt".
It prints each line with line numbers.
If the file does not exist, a FileNotFoundError is raised, and the program displays an error message instead of crashing.


Task 2: Write and Append Data to a File

1. Takes user input and writes it to "output.txt" (overwriting existing content).
2. Takes another input and appends it to the same file.
3. Reads and prints the final content of "output.txt" to verify changes.

Example Outputs:

User Input:
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final Content of output.txt:

Hello, Python!
Learning file handling in Python.
