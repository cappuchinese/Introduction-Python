# Exersice: Thema 1, Script 3
# Author: Lisa Hu

allowed_nucleic_symbols = "ACGTUIRYKMSWBDHVN-"
allowed_amino_symbols = "ABCDEFGHIJKLMNOPQRSTUVWYZX*-"

# opening a new text file
new_file = open("new_file.txt", "w")

line_length = int(input("How long is each line?" ))
# tries to find input in directory
try:
    files = open(input("Enter the file name (with the extension): "))
except FileNotFoundError:
   print("No such file was found")

# executes while loop if file was found
while True:
    counter = 0
    for line in files:
        line = line.strip()
        if not line.startswith(">"):
            if line.isupper() == False:
                line = line.upper()
            for character in line:
                counter += 1
                new_file.write(character)
                if counter % 10 == 0:
                    new_file.write(" ")
                if counter == line_length:
                    new_file.write("\n")
                    counter = 0
                if character not in allowed_amino_symbols and character not in allowed_nucleic_symbols:
                    print("File contains wrong content")
        else:
            new_file.write(line)
            new_file.write("\n")
    new_file.write("\n")
# asks for new input and file if needed
    question = input("Do you want to input another file? (y/n) ")
    if question == "n":
        break
    elif question == "y":
        try:
            files = open(input("Enter the file name (with the extension): "))
        except FileNotFoundError:
            print("No such file was found in the directory of the project")
    else:
        print("Incorrect Input...")

print("Done")
new_file.close()
