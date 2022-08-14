"""
Reworked script1
"""

__author__ = "Lisa Hu"
__date__ = 08.2022

# IMPORTS
import sys


# FUNCTIONS
def reader(filename, datatype):
    """
    Read the contents of hte file
    :param filename: Name of the file need to be read
    :param datatype: DNA or RNA input
    """
    with open(filename, "r", encoding="utf8") as opened:
        lines = "".join(line.strip() if not line.startswith(">") else ""
                        for line in opened)
    if datatype.lower() == "rna":
        lines.replace("T", "U")

    result = f"{datatype.upper()} sequence:\n{lines}\n\nTotal characters: {len(lines)}"
    return result


def main():
    filename, datatype = input("Give input: [filename, datatype]").split()
    reader(filename, datatype)
    return 0


if __name__ == '__main__':
    sys.exit(main())
