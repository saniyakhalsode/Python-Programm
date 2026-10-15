
def reverse_string(text):
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return reversed_text


def main():
    text = input("Enter a string: ")
    result = reverse_string(text)
    print("Reversed string:", result)

if __name__ == "__main__":
    main()

