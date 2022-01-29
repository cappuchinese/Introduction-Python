"""
Themaopdracht 1
Mika Wolters (418739)
Lisa Hu (414264)
"""


def create_dict(file_name):
    """
    retrieve sections from genbank file
    :param file_name: str
    :return: dict
    """
    open_gen_file = open(file_name)
    gen_dict = {}
    section = ''
    for line in open_gen_file:
        if not line.startswith(' '):
            #  maak een nieuwe sectie en voeg daar de info aan toe.
            section = line[:10].strip()
            info = line[10:]
            gen_dict[section] = info
        else:
            #  dit is voor als de info over meerdere regels verspreid is.
            gen_dict[section] += line
    open_gen_file.close()
    return gen_dict


def get_block(gen_dict, block):
    """
    get block from file, for example DEFINITION OR FEATURES
    :param block: str
    :param gen_dict: dict
    :return: str
    """
    return gen_dict[block].strip()


def get_features(gen_dict):
    """
    retrieve information defined in genbank FEATURES
    :param gen_dict: dict
    :return: dict
    """
    # intialize
    features = []
    feature = ''
    location = ''
    # are locations in multiple lines?
    location_complete = False

    # get FEATURES from gendict
    lines = gen_dict['FEATURES'].split('\n')
    # remove first line
    lines.pop(0)

    for line in lines:
        # get feature
        new_feature = line[5:21].strip()
        if new_feature != '':
            # start new feature
            feature = new_feature
            location = line[21:].strip()
            location_complete = False
            continue

        if not location_complete:
            # make location complete
            if line[21:22] == '/':
                # last line for location
                location_complete = True
                qualifier = line[21:].strip()
                # append feature to features
                features.append({
                    'feature': feature,
                    'location': location,
                    'qualifier': qualifier
                })
            else:
                # next line for location
                location += line[21:].strip()

    return features


def get_origin(gen_dict):
    """
    retrieve nonformatted ORIGIN sequence from genbank
    :param gen_dict:
    :return:
    """
    seq = get_block(gen_dict, 'ORIGIN')
    #  overbodige data uit genbank file ORIGIN blok verwijderen
    replace = '1234567890 \n'
    for char in replace:
        seq = seq.replace(char, '')

    return seq


def features_seq(file_name, upper):
    """
    write features from genbank to file
    :param upper: bool
    :param file_name: str
    """
    gen_dict = create_dict(file_name)
    features = get_features(gen_dict)
    origin = get_origin(gen_dict)

    open_file = open(file_name.replace('.gb', '_features.txt'), 'w')

    print(get_block(gen_dict, 'DEFINITION'), file=open_file)
    print(file=open_file)
    for feature in features:
        print('>{} {}'.format(feature['feature'], feature['qualifier']), file=open_file)
        seq = seq_location(origin, feature['location'], upper)
        for position in range(0, len(seq), 60):
            print(seq[position:position + 60], file=open_file)
        print(file=open_file)

    open_file.close()


def seq_location(origin, location, upper):
    """
    retrieve sequences for features and handle instructions (join, complement)
    :param upper: bool
    :param origin: str
    :param location: str
    :return:
    """
    seq = ''
    complement = False
    if location.startswith('complement'):
        # handle complement instruction
        complement = True
        location = location[11:-1]

    if location.startswith('join'):
        # handle join instruction
        locations = location[5:-1].split(',')
    elif location.startswith('<'):
        # handle < instruction
        locations = [location[1:]]
    else:
        if location.count('..') == 0:
            # handle single number
            start = int(location)
            eind = start
            location = '{}..{}'.format(start, eind)

        locations = [location]

    # combine location to single sequence
    current = 0
    for location in locations:
        start, eind = location.split('..')
        sub_seq = origin[int(start) - 1: int(eind)]
        if upper:
            seq += origin[current:int(start)]
            sub_seq = sub_seq.upper()
            current = int(eind)

        seq += sub_seq

    if complement:
        # complement and reverse sequence
        complement = {
            'a': 't',
            'c': 'g',
        }
        for char in complement:
            seq = seq.replace(char, 'X').replace(complement[char], char).replace('X', complement[char])

        seq = seq[::-1]

    return seq


def main():
    # file_name = input('mRNA GenBank filename: ').strip()
    file_name = input('enter gb file name (with extension):')
    upper = input('output in: "separated" or "upper":')
    features_seq(file_name, upper == 'upper')


main()
