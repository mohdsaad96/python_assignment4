def read_file(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())  # strip() removes leading/trailing whitespace
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function with the desired filename
read_file('sample.txt')