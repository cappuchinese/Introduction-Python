"""
Reworked script3
"""

__author__ = "Lisa Hu"
__date__ = 08.2022

# IMPORTS
import sys


# FUNCTIONS
def reader(filename):
    """
    Read the file and split content from header
    :param filename: Name of the file need to be read
    """
    # Open read file
    with open(filename, "r", encoding="utf8") as opened_r:
        # Get the header
        header = opened_r.readline()
        # Rest of the content is one long string
        lines = "".join(line.strip() if not line.startswith(">") else ""
                        for line in opened_r)

    return header, lines


def check(lines):
    """
    Check if the content contains the allowed letters
    :param lines: String of the content
    """
    allowed_symbols = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P',
                       'Q', 'R', 'S', 'T', 'V', 'W', 'Y']
    content = sorted(set(lines))
    for i in content:
        if i not in allowed_symbols:
            return False
        else:
            continue
    return True


def writer(new_file, lines, length, header):
    """
    Write the output file with the given line length
    """
    lines = "\n".join(lines[i:i+length] for i in range(0, len(lines), length))
    with open(new_file, "w", encoding="utf8") as opened_w:
        opened_w.write(header)
        opened_w.write(lines)
        opened_w.write("\n")


def main():
    while True:
        # Get the files and line length
        files = input("Give filenames split by whitespace: ").split()
        string_length = int(input("Give length of line: "))

        # Iterate through the different files
        for i in files:
            # Write the different outputs
            header, lines = reader(i)
            if check(lines):
                newfile = i.replace("fasta", "txt")
                writer(newfile, lines, string_length, header)
            else:
                print("File contains wrong content")

        # Continue or not
        cont = input("Enter new input? (y/n) ")
        if cont == "n":
            return 0
        else:
            continue


if __name__ == '__main__':
    sys.exit(main())
