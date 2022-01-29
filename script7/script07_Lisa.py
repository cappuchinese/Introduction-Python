# Exercise: Theme 1, script 7
# Author: Lisa Hu

def fill_dicts():
    """
    function opens file and adds content to dictionary
    Return:
        filled dictionary
    """
    section_dict = {}
    files = open("cf.gb")
    for line in files:
        if line == "\n":
            pass
        elif not line.startswith(" "):
            line = line.rstrip()
            temp = line.split(" ")
            section = temp[0]
            info = line[12:]
            section_dict[section] = info
        else:
            section_dict[section] += line.strip()
    print(section_dict)
    return section_dict


def origin(section_dict):
    """
    Function searches for sequence and formats it
    Parameter:
        the filled dictionary
    Return:
        sequence in right format
    """
    var1 = section_dict["ORIGIN"]
    sequence = ""
    new_line = ""
    for line in var1:
        line = line.strip()
        for char in line:
            if char.isalpha():
                sequence += char.upper()
            else:
                pass

    sequence = sequence.strip()

    for startposition in range(0, len(sequence), 70):
        new_line += sequence[startposition:startposition + 70] + "\n"

    return new_line


def make_header(section_dict):
    """
    Function makes header
    Parameter:
        the filled dictionary
    Return:
        the right header
    """
    header = ">" + section_dict["VERSION"] + section_dict["DEFINITION"]
    return header


def write_file():
    """
    Function writes fasta file
    """
    output_fasta = open("cf.fasta", "w")
    section_dict = fill_dicts()
    sequence = origin(section_dict)
    header = make_header(section_dict)

    print(header, sequence, file=output_fasta)


write_file()
