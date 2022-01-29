# script_06
# author Mats Slik


def input_1():
    file_input = input('please type your file name here with extension: ')
    output_name = input('please type here the name for the output file with extension: ')

    return file_input, output_name


def mutation_func():
    mutation = input('type here the desered mutation exp:(T) or (ATG), for deletion type(-),')

    return mutation


def mutation_pos():
    mutation_beg = input('please type here the location for the mutations begin position: ')
    mutation_end = input('please type here the location for the mutations end position: ')
    mutation_beg = int(mutation_beg)
    mutation_end = int(mutation_end)
    return mutation_beg, mutation_end


def fasta_identifier():
    # header u want to alter in multi fasta bestand
    header_input = input('type here the identifier u want to edit example(NG_016465.4):')
    return header_input


def mutation_insert(sequence, header, mutation_beg, mutation_end, mutation='-'):
    # accounting for 0 based counting

    (mutation_beg) = mutation_beg - 1
    (mutation_end) = mutation_end - 1

    sequence = list(sequence)
    # insertion defined mutation a user defined input location
    if mutation == '-':
        sequence[mutation_beg:mutation_end] = ''
        header_altered = header + ' deletion alteration'
    else:
        sequence[mutation_beg:mutation_end] = mutation
        header_altered = header + ' insertion mutation alteration'
    sequence_altered = ''.join(sequence)

    return sequence_altered, header_altered


def read_file(file_):
    file_ = open(file_)
    header = []
    sequences = []
    sequence_temp = ''
    count = 0

    # reading file and storing headers and sequences in a list
    for line in file_:
        line = line.strip()
        if line.startswith('>'):
            header.append(line)
            sequences.append(sequence_temp)
            sequence_temp = ''
            count += 1
        else:
            if count == 1:
                sequence_temp += line
            else:
                count = 0
                sequence_temp += line
    sequences.append(sequence_temp)
    file_.close()
    return (sequences, header)


def fasta_selection(fasta_dict, identifier):
    header = ''
    sequence_to_be_altered = ''

# searching for fasta identifier in dictinaire

    for key in fasta_dict:
        if identifier in key:
            print('found fasta')
            header = key
            sequence_to_be_altered = fasta_dict[key]

    print(header)
    print(sequence_to_be_altered)
    return header, sequence_to_be_altered


def output(fasta_dict, out_file):
    out_file = open(out_file, 'w')
    #  writhing dictinair to output file
    for key in fasta_dict:
        sequence = fasta_dict[key]
        print(key, file=out_file)
        for startposition in range(0, len(sequence), 70):
            print(sequence[startposition:startposition + 70], file=out_file)

    print(file=out_file)

    out_file.close()
    pass


def main():
    # variables
    fasta_dict = {}

    # getting user input
    file_, output_name = input_1()

    # storing header and sequence in dictionary
    sequence, headers = read_file(file_)
    # joining headers and sequences in a dictionary
    for position in range(0, len(headers)+1, 1):
        fasta_dict[headers[(position - 1)]] = sequence[position]
    # storing header and sequence in dictionary
    # getting mutation
    mutation = mutation_func()
    mutation_beg, mutation_end = mutation_pos()

    identifier = fasta_identifier()
    mut_header, mut_seq = fasta_selection(fasta_dict, identifier)

    # using functions to alter sequence to input from user, and returning altered sequence
    mutation_beg = int(mutation_beg)
    mutation_end = int(mutation_end)

    # altering specified sequence and adding identiefier to header
    sequence_altered, header_altered = mutation_insert(mut_seq, mut_header, mutation_beg, mutation_end, mutation)
    fasta_dict[header_altered] = sequence_altered
    # writhing output file
    output(fasta_dict, output_name)


    pass


main()
