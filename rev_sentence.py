# Function to reverse words of string

def sentence_rev(sentence):

    words = sentence.split(' ')
    sentence_reverse =' '.join(reversed(words))
    return sentence_reverse

if __name__ == "__main__":
    input = 'learning code python'
    print(sentence_rev(input))
