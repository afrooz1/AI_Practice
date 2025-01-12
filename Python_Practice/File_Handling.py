def count_word_frequency(input_file, output_file):
    try:
        # Read the file
        with open(input_file, 'r') as file:
            text = file.read()

        # Process the text
        words = text.split()  # Split text into words
        word_count = {}

        for word in words:
            word = word.strip().lower()  # Normalize the word (remove spaces and lowercase)
            word_count[word] = word_count.get(word, 0) + 1

        # Write the results to the output file
        with open(output_file, 'w') as file:
            for word, count in sorted(word_count.items()):
                file.write(f"{word}: {count}\n")

        print(f"Word frequency has been written to {output_file}.")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Program execution complete.")


# Example usage
input_file = "input.txt"  # Replace with your input file name
output_file = "output.txt"  # Replace with your desired output file name
count_word_frequency(input_file, output_file)
