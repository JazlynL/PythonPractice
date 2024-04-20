import re


def count_substring(string, sub_string):
    textv = re.findall("(?=(" + sub_string + "))", string)

    return len(textv)


if __name__ == '__main__':