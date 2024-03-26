# Adding comments to my file
user_input = input('What would you like to print? ').strip()  # Remove leading/trailing whitespace

# Validate the input to ensure it's not empty
while not user_input:
    print("The input cannot be empty. Please enter something to print.")
    user_input = input('What would you like to print? ').strip()

print(user_input)
