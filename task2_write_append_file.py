# task2_write_append_file.py

def write_to_file(filename, text):
    """Writes (overwrites) the given text to the file."""
    try:
        with open(filename, "w") as file:
            file.write(text + "\n")
        print(f"Data written to '{filename}'.")
    except Exception as e:
        print(f"Error while writing to file: {e}")


def append_to_file(filename, text):
    """Appends the given text to the file."""
    try:
        with open(filename, "a") as file:
            file.write(text + "\n")
        print(f"Data appended to '{filename}'.")
    except Exception as e:
        print(f"Error while appending to file: {e}")


def read_file(filename):
    """Reads and prints the full content of the file."""
    try:
        with open(filename, "r") as file:
            print(f"\nFinal contents of '{filename}':\n")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"Error while reading file: {e}")


if __name__ == "__main__":
    filename = "output.txt"

    # 1️⃣ Take user input and write to the file
    user_input = input("Enter some data to write to the file: ")
    write_to_file(filename, user_input)

    # 2️⃣ Take more input and append to the same file
    more_data = input("Enter some additional data to append: ")
    append_to_file(filename, more_data)

    # 3️⃣ Read and display the final content
    read_file(filename)
