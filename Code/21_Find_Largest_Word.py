import re


def find_largest_word(sentence):

    words = re.findall(r'\b\w+\b', sentence)

    if not words:
        return ""

    return max(words, key=len)


if __name__ == "__main__":

    sentence = input("Enter a sentence: ")

    result = find_largest_word(sentence)

    print("Largest word:", result)
