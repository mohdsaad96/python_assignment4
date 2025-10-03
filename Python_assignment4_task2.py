def write_and_append_to_file():
    filename = 'output.txt'

    # Step 1: Write user input to the file
    user_input = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')
    print("Data successfully written to output.txt.\n")

    # Step 2: Append additional data
    additional_input = input("Enter additional text to append: ")
    with open(filename, 'a') as file:
        file.write(additional_input + '\n')
    print("Data successfully appended.\n")

    # Step 3: Read and display final content
    print("Final content of output.txt:")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# Run the function
write_and_append_to_file()