# Exercise: Theme 1, Script 6
# Author: Lisa Hu

def input_file():
    """
    Returns:
        user defined file name
    """
    file_name = open(input("Enter file name: "))
    return file_name


def get_content(file_name):
    """
    Function goes through the file and separately stores header and sequence
    Parameter:
        opened file
    Returns:
        new header with notification of mutation
        the sequence of the file
    """
    new_header = ""
    sequence = ""
    for line in file_name:
        line = line.strip()
        if line.startswith(">"):
            header = line
            identifier = get_identifier(header)
            new_header = "Sequence " + identifier + " has been mutated"
        else:
            sequence += line
    return new_header, sequence


def get_identifier(header):
    """
    Function stores identifier
    Parameter:
        header of the file
    Return:
        the identifier of the header
    """
    identifier = input("Enter identifier: ")
    if header[1:len(identifier) + 1].upper() == identifier:
        identifier = header.split()[0]
        if ":" in identifier:
            identifier = identifier.split(":")[0]
    return identifier


def file_format(sequence):
    """
    Function writes sequence in lines of 70
    Parameter:
        sequence of the file
    Return:
        sequence in lines of 70
    """
    new_sequence = ""
    for startposition in range(0, len(sequence), 70):
        new_sequence += sequence[startposition:startposition + 70] + "\n"
    return new_sequence


def mutate(sequence):
    """
    Function asks user for the mutation and applies mutation
    Parameter:
        sequence of the file
    Return:
        the mutation applied to the sequence
    """
    mutation_type = input("What type of mutation? (sub/del) ")
    mutation_start = int(input("Enter start position: ")) - 1
    mutation_end = int(input("Enter end position: "))
    if mutation_type == "sub":
        mutation = input("Enter mutation: ")
        mutated_seq = sequence[0:mutation_start] + mutation + sequence[mutation_end:]
    else:
        mutated_seq = sequence[0:mutation_start] + sequence[mutation_end:]

    mutated_seq = file_format(mutated_seq)

    return mutated_seq


def write_file(new_header, sequence):
    """
    Function writes to output file
    Parameter:
        the the customized header, made in get_content()
        mutated sequence in right file format
    """
    output_file = open(input("Enter output file: "), "w")
    print(new_header + "\n" + mutate(sequence), file=output_file)


def main():
    """
    Main script
    """
    file_ = input_file()
    new_header, sequence = get_content(file_)
    write_file(new_header, sequence)


main()
