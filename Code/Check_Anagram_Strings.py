def check_anagram(str1, str2):

    str1 = ''.join(str1.lower().split())
    str2 = ''.join(str2.lower().split())

    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


if __name__ == "__main__":

    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")

    if check_anagram(string1, string2):
        print("The strings are Anagrams")
    else:
        print("The strings are Not Anagrams")