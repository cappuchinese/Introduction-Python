"""
Reworked script2
"""

__author__ = "Lisa Hu"
__date__ = 08.2022

# IMPORTS
import sys


# FUNCTIONS
def reader(filename):
    """
    Read the contents of hte file
    :param filename: Name of the file need to be read
    """
    # Read the file and save the content
    with open(filename, "r", encoding="utf8") as opened:
        lines = "".join(line.strip() if not line.startswith(">") else ""
                        for line in opened)
    # Calculate the gc percentage
    gc_perc = (lines.count("C") + lines.count("G")) / len(lines) * 100
    return lines, gc_perc


def results(lines):
    """
    Create the different results (counts, diagram and DNA check)
    :param lines: Content from the file
    """
    letter_set = sorted(set(lines))  # Get the content's letters
    count_dict = dict.fromkeys(letter_set, 0)  # Create a dictionary of the set
    # Add the counts of each letter respectively
    for letter in letter_set:
        count = lines.count(letter)
        count_dict[letter] = count

    # Create the diagram based on the counts (hashes give percentage)
    diagram = ""
    for i in count_dict:
        hashes = count_dict[i]/len(lines) * 100
        diagram += f"{i} {'#'*int(hashes)}\n"

    # Check if the content is DNA
    nucleotides = ["A", "C", "G", "T"]
    if letter_set == nucleotides:
        check = True
    else:
        check = False

    return count_dict, diagram, check


def main():
    # Get the files
    files = input("Insert filenames split by whitespace: ").split()
    # Iterate through the files
    for i in files:
        # Print the different results
        lines, gc_perc = reader(i)
        count, diagram, check = results(lines)
        print(count, diagram, f"DNA is {check}", sep="\n")
    return 0


if __name__ == '__main__':
    sys.exit(main())
