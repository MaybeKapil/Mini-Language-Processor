# Not uploaded to BitBucket

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
    # def __init__(self):
    #     self.current_char = ''
    #     self.current_line = 1
    #     self.current_column = 0
    #     self.input_file = None

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
        global current_char
        return current_char

    # Returns a string representation of the current position in the format "line:column".
    def position(self):
        # Concatenate the current line and column integers with a colon separator.
        pos = f"{current_line}:{current_column}"
        return pos

    # Opens the file specified by the 'some_file' argument in read-only mode ('r').
    # Returns 1 if file was successfully opened, otherwise returns 0.
    # Used this webpage for help on how to error handle: https://www.topbug.net/blog/2020/10/03/catching-filenotfounderror-watch-out/
    def open_file(self, some_file):
        global input_file

        # Try to open the file in read-only mode
        try:
            input_file = open(some_file, 'r')
            # If file opened successfully, return 1.
            return 1
        # If file not found, report error.
        except FileNotFoundError:
            print(f"ERROR: File {some_file} not found.\n", file=sys.stderr)
            return 0
        # If there is a lack of permission, report error.
        except PermissionError:
            print(f"ERROR: Insufficient permission to read {some_file}.\n", file=sys.stderr)
            return 0
        # If the file is not a file but rather a directory, report error.
        except IsADirectoryError:
            print(f"ERROR: {some_file} is a directory.\n", file = sys.stderr)
            return 0

    def reset_file(self):
        global input_file

        input_file.close
        input_file = None

    # Gets user input for a file to read, opens the file, and reads the file character by character.
    # Printing out the position of each character followed by the character.
    # Format: line:column character
    def read_file(self, user_input):

        # Try opening the file.
        # If valid and file was successfully opened, value is 1.
        # If invalid and file was not opened, value is 0.
        valid_file = self.open_file(user_input)

        if (valid_file == 1):
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

            print()
            print("Reading and displaying the input file has been completed")
            print()

            self.reset_file()

    def prompt_user(self):
        while(True):
            user_input = input(">>> Enter a file name, or type 'quit' or 'exit' to exit: ")
            if(user_input == "quit" or user_input == "exit"):
                print("Program terminating...")
                break
            else:
                self.read_file(user_input)

if __name__ == "__main__":
    # Create an instance of the FileReader class
    reader = FileReader()
    # Run the main method of the FileReader instance
    reader.prompt_user()