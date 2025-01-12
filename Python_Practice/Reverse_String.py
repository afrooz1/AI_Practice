def reverse_string(s):
    return s[::-1]  # Use slicing to reverse the string

# Test the function
string = input("Enter a string: ")
reversed_string = reverse_string(string)
print(f"Reversed string: {reversed_string}")
