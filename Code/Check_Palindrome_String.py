def check_palindrome():
  # Take input from the user
  user_input = input("Enter a string to check: ")

  # Clean the string (optional: lowercase and remove non-alphanumeric characters)
  cleaned = "".join(ch.lower() for ch in user_input if ch.isalnum())

  # Check if it equals its reverse
  if cleaned == cleaned[::-1]:
    print(f'"{user_input}" is a palindrome!')
  else:
    print(f'"{user_input}" is not a palindrome.')


# Run the function
check_palindrome()