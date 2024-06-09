def swap_case(s):
    newString = ""
    for letter in range(0, len(s)):
        if s[letter].isupper():
            newString = newString + s[letter].lower()
        elif s[letter].lower():
            newString = newString + s[letter].upper()

    return newString


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)