# script_07
# author Mats Slik

def input_():
    """
    Returns:
        user defined file name
    """
    file_name = input(' type here your Genbank file name: ')
    if file_name == '':
        file_name = 'CFTR.gb'
    return file_name


def read_gen_bank_file(file_name):
    # reading a gen
    """
    Args:
    Returns:
        a dictionary with sections as keys,
        and the information under a section as its value
    """

    file_ = open(file_name)
    temp_dict = {}
    section = ''
    sequence = ''
    for line in file_:
        line = line.rstrip()
        if line.startswith(' '):
            line = line.strip()
            sequence += line
        else:
            temp_dict[section] = sequence
            sequence = ''
            temp = line.split(' ')
            section = temp[0]
            sequence += list_to_string(temp)
    return temp_dict


def list_to_string(list):
    sequence = ''
    for i in range(1, len(list), 1):
        sequence += ' ' + list[i]
    string = sequence
    return string


def make_header(file_dict):
    """
    makes a header with the information stored in the sections :version, definition_
    Args:
        file_dict: dictionary containing the genbank file
    Returns:
        a fasta styled header
    """

    header = '>'

    version = file_dict['VERSION']
    definition_ = file_dict['DEFINITION']

    header += version.lstrip() + definition_.lstrip()

    return header


def make_nuc_seq(file_dict):
    """
    reads a genbank file its given and stores it in a dictinairy
    Args:
        file_dict:
    Returns:
            nucleotide sequence in a list
    """

    sequence = []

    raw_seq = file_dict['ORIGIN']
    raw_seq = raw_seq.lstrip()
    for i in raw_seq:
        if not i.isdigit():
            if i == ' ':
                pass
            else:
                sequence.append(i)
    sequence_return = ''.join(sequence)
    sequence_return = sequence_return.upper()
    return sequence_return


def output(header, sequence, file_name):
    """
    output and creation of file name based on loaded file

    Args:
        header: created
        sequence:
        file_name: is loaded file name

    Returns:

    """

    out_file = file_name.rstrip('.gb')
    out_file += '.fasta'
    out_file = open(out_file, 'w')

    print(header, file=out_file)
    for startposition in range(0, len(sequence), 70):
        print(sequence[startposition:startposition + 70], file=out_file)

    return


def print_file_info(file_dict):
    """
    printing information on screen

    Args:
        file_dict:

    Returns:

    """
    for key in file_dict:
        if key == 'ORIGIN':
            pass
        elif key == 'FEATURES':
            pass
        else:
            print(key + ':' + file_dict[key] + '\n')
    print('FEATURES and ORIGIN sections not displayed because too much information onscreen ')
    return


def main():
    """
    Main script

    Returns:

    """

    file_name = input_()
    file_dict = read_gen_bank_file(file_name)
    print('File_loaded')
    print()
    print_file_info(file_dict)
    print()
    sequence_ = make_nuc_seq(file_dict)

    header = make_header(file_dict)

    output(header, sequence_, file_name)
    print('Done')
    pass


main()
