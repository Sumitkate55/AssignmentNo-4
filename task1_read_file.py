# task1_read_file.py

def read_file_line_by_line(filename):
    """Reads and prints a file line by line with error handling."""
    try:
        # Try to open the file in read mode
        with open(filename, "r") as file:
            print(f"Contents of '{filename}':\n")
            # Read and print each line one by one
            for line in file:
                # end="" avoids extra blank lines
                print(line, end="")
    except FileNotFoundError:
        # This block runs if the file is not found
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        # This handles any other unexpected error
        print(f"An unexpected error occurred: {e}")


# Main part of the program
if __name__ == "__main__":
    # File name as given in the assignment
    read_file_line_by_line("Tutedude PY/week 1/Assignment 4/sample.txt")
