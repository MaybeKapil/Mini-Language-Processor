# Import the 'isfile' function from the 'os.path' submodule.
import os.path

# Global Variables

# Holds the current character
current_char = ''

# Holds the current character's line number
current_line = 0

# Holds the current character's column number
current_column = 0

class fileReader:

    # Reads the next character from the input file and updates character and position values accordingly.
    # Does not return a value.
    def next_char():
        # Ensures reference to global variables, not variables of local scope.
        global current_char, current_line, current_column

        # Reads one character from the file.
        current_char = file.read(1)

        # Check if a new line character was read.
        if (current_char == "\n"):
            # If a new line character is encountered, increment the current_line count.
            current_line += 1

            # Reset the current_column count to 0 for a new line.
            current_column = 0

    # Returns a string containing the character that was just read
    def get_current_char():
        return current_char

    # Returns a string containing the line and column integers separated by a colon character.
    def position():
        pos  = current_line +  ":" + current_column
        return pos

    # Prompt the user to enter a valid file name.
    # Returns the valid file name entered by the user.
    def get_file_name():
        while(True):
            # Assume the file is in the same directory as the executable reader.
            file_name = input("Enter the file name: ")
            path = './' + file_name

            # Verify if the user input corresponds to a valid file.
            # If the input is invalid, prompt the user again for a valid file name until a valid file name is obtained.
            if (os.path.isfile(path) == False):
                print("Invalid file. Please enter a valid file name: ")
                continue
            else:
                break

        return file_name

    # Opens the file specified by the 'some_file' argument in read-only mode ('r').
    # Does not return a value.
    def open_file(some_file):
        file = open(some_file, 'r')

    def main():
        print("fix_me")

    if __name__ == "__main__":
        main()
