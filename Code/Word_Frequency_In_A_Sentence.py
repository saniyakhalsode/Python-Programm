def word_frequency(sentence):
 frequency = {}


 words = sentence.lower().split()

 for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

    return frequency

def main():
 sentence = input("Enter a sentence: ")

 result = word_frequency(sentence)

 print("Word frequency:")
 for word, count in result.items():
    print(f"{word}: {count}")


    if __name__ == "__main__":
     main()
