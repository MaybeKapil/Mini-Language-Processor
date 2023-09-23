# Import the 'isfile' function from the 'os.path' submodule.
import os.path

# Import the 'stderr' attribute from the 'sys' module to handle error output.
import sys

# Global Variables

# The current character being processed.
current_char = ''

# The current character's line number.
current_line = 1

# The current character's column number.
current_column = 0

# The file to be read.
input_file = None

class FileReader:
    # Reads the next character from the input file and updates character and position values accordingly.
    # Does not return a value.
    def next_char(self):
        # Ensures reference to global variables, not variables of local scope.
        global current_char, current_line, current_column

        # Reads one character from the file.
        current_char = input_file.read(1)

        # File is assumed to contain Unix-style line ending, not CRLF.
        # In ASCII and Unicode character encodings, LF is represented as '\n'.
        # Check if you reached a Line-Feed, '\n'
        if (current_char == "\n"):
            # Increment the current_line count.
            current_line += 1

            # Reset the current_column count to 0 for a new line.
            current_column = 0

            # # When you reach a Line-Feed, '\n' , consider that as an empty character
            # current_char = ''
        else:
            # If you just read a character that is not a Line-Feed, then you are on the same line
            # so increment the column value without incrementing the line value
            # and the character value will be the same as what was read
            current_column += 1

    # Returns a string containing the character that was just read.
    def get_current_char(self):
        return current_char

    # Returns a string representation of the current position in the format "line:column".
    def position(self):
        # Concatenate the current line and column integers with a colon separator.
        pos = f"{current_line}:{current_column}"
        return pos


    # Prompt the user to enter a valid file name.
    # Returns the valid file name entered by the user.
    def get_file_name(self):
        while(True):
            # Assume the file is in the same directory as the executable reader.
            file_name = input("Enter the file name: ")
            path = './' + file_name

            # Verify if the user input corresponds to a valid file.
            # If the input is invalid, prompt the user again for a valid file name until a valid file name is obtained.
            if (os.path.isfile(path) == False):
                print("Invalid file. Please try again.\n")
                continue
            else:
                break

        return file_name

    # Opens the file specified by the 'some_file' argument in read-only mode ('r').
    # Does not return a value.
    # Used this webpage for help on how to error handle: https://www.topbug.net/blog/2020/10/03/catching-filenotfounderror-watch-out/
    def open_file(self, some_file):
        global input_file

        try:
            input_file = open(some_file, 'r')
        except FileNotFoundError:
            print(f"File {some_file} not found.", file=sys.stderr)
            return
        except PermissionError:
            print(f"Insufficient permission to read {some_file}.", file=sys.stderr)
            return
        except IsADirectoryError:
            print(f"{some_file} is a directory.", file = sys.stderr)
            return

    # End of function definition.

    def read_file(self):

        # Prompt the user for a valid file name and open the file to for reading.
        self.open_file(self.get_file_name())

        # Read the first character from the file.
        self.next_char()

        # Loop until end-of-text character is reached.
        # This is done by looping until the value of the 'current_char' variable, which is obtained by using get_current_char(), is empty.
        # An empty value indicates that End of File has been reached.
        while(self.get_current_char()):
            # Print the position of the current character followed by the character.
            print(self.position() + " ", end="")

            # Check if the current character is a LF character ('\n')
            # If it is an LF character, print an empty line to represent the LF character as an empty string.
            if (self.get_current_char() == '\n'):
                print()
            # If it isn't an LF character, print the current character.
            else:
                print(self.get_current_char())

            # Call the next_char function to read the next character from the file.
            self.next_char()

        # Close file after reading is complete.
        input_file.close