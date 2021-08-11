# Python program to accept the strings which contains all the vowels
def check_vowel(string):

    string = string.replace(' ', ' ')
    string = string.lower()
    vowel = [string.count('a'), string.count('e'), string.count('i'), string.count('o'), string.count('u')]

    if vowel.count(0) > 0:
        return ('Not accepted')
    else:
        return ('Accepted')

if __name__ == "__main__":
    string = "miaoued"
    print(check_vowel(string))

    string = "courage"
    print(check_vowel(string))
