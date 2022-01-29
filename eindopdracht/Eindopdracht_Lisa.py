"""
Project: Eindopdracht kwartaal 1
Author: Lisa Hu (414264)
"""


def make_dict(file_name):
    section_dict = {}
    file_ = open(file_name + ".gb")

    for line in file_:
        if line == "\n":
            pass
        elif not line.startswith(" "):
            section = line[:12].rstrip()
            info = line[12:]
        else:
            info = line

        if section not in section_dict:
            section_dict[section] = info
        else:
            section_dict[section] += info

    file_.close()
    return section_dict


def get_sequence(section_dict):
    sequence = ""
    source_info = section_dict["ORIGIN"]
    for line in source_info:
        sequence += line
    for wrong_char in " 1234567890\n":
        sequence = sequence.replace(wrong_char, "")

    return sequence


def make_feat_dict(section_dict):
    feature_dict = {}
    features = section_dict["FEATURES"]
    features = features.split("\n")
    for line in features:
        line = line.lstrip()
        if line.startswith("/") or :
            pass
        else:
            inf = line.split()[0]
            seq_slice = line.split()[-1]
            for num_char in "123456789":
                if line.startswith(num_char):
                    seq_slice += inf
            if inf not in feature_dict:
                feature_dict[inf] = seq_slice

    return feature_dict


def main():
    input_name = "cf"
    dicto = make_dict(input_name)
    get_sequence(dicto)
    make_feat_dict(dicto)


main()
