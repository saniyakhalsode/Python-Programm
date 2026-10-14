from collections import Counter


def count_user_characters():
  # Take input from the user
  user_input = input("Enter a string to count character frequencies: ")

  # Optional: Convert to lowercase to treat 'A' and 'a' as the same character
  # user_input = user_input.lower()

  # Count frequencies
  frequencies = Counter(user_input)

  # Display the results neatly
  print("\n--- Character Frequencies ---")
  for char, count in frequencies.items():
    # Handle spaces visually so they are clear in the output
    display_char = "Space (' ')" if char == " " else f"'{char}'"
    print(f"{display_char}: {count}")


# Run the function
count_user_characters()