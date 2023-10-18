# Import the FileReader class and string module
import FileReader, string

# Create an instance of the FileReader class to use for reading user's file
reader = FileReader.FileReader()

# cant use this because this uses the FileReader read_file() which doesn't read the file as necessary
# reader.promptUser()

# Defines a constant variable that stores the three types of whitespace characters.
# Types: space (' '), tab ('\t'), line feed ('\n')
WHITE_SPACE_CHARS = string.whitespace

# SPECIAL_CHARS = string.punctuation

# special_characters = '!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~}'

INVALID_CHARS = "!\"#$%&'?@[\]^`{|}~}'"

# Defines a constant variable that stores all uppercase and
# lowercase letter characters of the alphabet (a-z and A-Z).
LETTER_CHARS = string.ascii_letters

# Defines a constant variable that stores all digit character (0-9).
DIGIT_CHARS = string.digits

# Defines a constant variable that stores all the valid operators within the syntax.
# Valid operators includes assignment operator, relational operator, additive operator,
# multiplicative operator, and unary operator.
OPERATOR_CHARS = {':=', '<', '=<', '=', '!=', '>=', '>', '+', '-', '*' , '/'}

# Defines a constant variable that stores all the valid punctuation characters within the syntax.
PUNCTUATION_CHARS = {':', '.', ',', ';', '(', ')'}

# Defines a constant variable that stores the set of all the valid keywords within the syntax.
KEYWORDS = ["program", "bool", "int", "if", "then", "else", "end", \
            "while", "do", "end", "print", "or", "mod", "and", "not", \
                "false", "true"]

class LexicalAnalyzer:

    def __init__(self):
        # Lexeme and token are interchangeable.
        # Defines a variable that will be used to store the current token.
        self.current_token = ""

        # Defines a variable that will be used to store the type of the current token.
        self.token_type = ""

        # Defines a variable that will be used to store the current token.
        self.token_pos = ""

    def get_current_token(self):
        """
        Get the current token value.

        Returns:
            The current token value.
        """

        return self.current_token

    def set_current_token(self, token_val):
        """
        Set the current token value to the provided token value.

        Args:
            token_val (str): The token value to set as the current token.
        """

        self.current_token = token_val

    def get_token_position(self):
        """
        Gets the position of the token.

        The position is represented as a pair consisting of the line number and column where
        the first character of the token occurs.

        Return:
            A string representing the position of the first character of the current token.
            Format: line:column
        """

        return self.token_pos

    def set_token_position(self, position):
        """
        Sets the position of the current token.

        Args:
            position (str): The position value of the current token.
        """

        self.token_pos = position

    def get_token_type(self):
        """
        Get the current token type.

        Returns:
            The current token type.
        """

        return self.token_type

    def set_token_type(self):
        """
        Set the current token value to the provided token value.

        The types include: ID, NUM, end-of-text, keywords*, symbols**, end-of-text

        * For keywords the keyword itself is the kind.
        ** For symbols, the symbol itself is the kind.

        Args:
            token_val (str): The token value to set as the current token.
        """

        global LETTER_CHARS, DIGIT_CHARS, OPERATOR_CHARS, KEYWORDS, \
            token_type

        token = self.get_current_token()

        self.token_type = ""

        if (token.isdigit()):
            self.token_type = "NUM"
        elif (token in KEYWORDS or
              token in OPERATOR_CHARS):
            self.token_type = token
        elif (token == '.'):
            self.token_type = "end-of-text"
        elif all (char in LETTER_CHARS or \
                  char in DIGIT_CHARS or \
                    char == '_' \
                        for char in token):
            self.token_type = "ID"
        else:
            # for parenthesis, comma, colon, and semicolon
            self.token_type = token

    def get_token_value(self):
        """
        Get the current token value.

        Only identifiers ('ID') and integers ('NUM') have values.
        If it not an ID or NUM, then return None to indicate that it does not have a value.

        Returns:
            The current token value.
        """

        type = self.get_token_type()

        if (type == "ID" or type == "NUM"):
            # return self.get_current_token
            return self.get_current_token()

        return None

    def skip_white_spaces(self):
        """
        Skip whitespaces in the file content read by the FileReader instance.
        Advances until a non-whitespace character is encountered.

        No return value.
        """

        global reader, WHITE_SPACE_CHARS

        current_char = reader.get_current_char()
        # if (current_char == ' 'or current_char == '\t' or current_char == '\n')
        #     reader.next_char()

        # if the current character is in the set of whitespace character,
        # then the current character is a whitespace and will be skipped
        # at the end, current_char will not be a white_space, resulting in the end of the while loop
        while (current_char in WHITE_SPACE_CHARS):
            # skip the current (whitespace) character by getting the next character
            reader.next_char()

            # store the new current character to be used for reevaluation of the while conditional statement
            current_char = reader.get_current_char()

    def next_token(self):
        """
        Gets the next token from the file by reading the file
        character by character until all the characters in the
        file have been read.

        No return value.
        """

        global WHITE_SPACE_CHARS, LETTER_CHARS, \
            DIGIT_CHARS, OPERATOR_CHARS, PUNCTUATION_CHARS, \
                reader

        # print("test 12312")

        # use next_char from the last code

        # use next_char to read until you reach a whitespace or character other than _
        # (ignore) how do you prevent stuff like prog_ram? --> first_token should solve this

        # get next character until you reach whitespace or invalid character for that type
        # basically read until you get to whitespace or symbols other than _

        # while (current_char not in white_space_chars and
        #        current_char not in special_chars):

        #     self.append_current_token(current_char)
        #     reader.next_char()
        # return
        # current_char = reader.get_current_char()

        # clear the current_token before getting the new token
        self.set_current_token("")

        # if the current character is a whitespace, skip it and skill all ot
        if (reader.get_current_char() in WHITE_SPACE_CHARS):
            self.skip_white_spaces()

        # after all the white spaces are skipped (if there were any), you end up at a non-whitespace character
        # and therefore need to mark this as the beginning of the token
        self.set_token_position(reader.position())

        if (reader.get_current_char() in OPERATOR_CHARS or
            reader.get_current_char() == ':'):
            while(reader.get_current_char() in OPERATOR_CHARS or
                  reader.get_current_char() == ':'):
                self.consume_current_char()
        elif (reader.get_current_char() in LETTER_CHARS or
                  reader.get_current_char() in DIGIT_CHARS or
                  reader.get_current_char() == '_'):
            while(reader.get_current_char() in LETTER_CHARS or
                  reader.get_current_char() in DIGIT_CHARS or
                  reader.get_current_char() == '_'):
                self.consume_current_char()
        else:
            self.consume_current_char()

        if (self.get_current_token() == "//"):

            # While the file still contains unread characters,
            # keep getting the next character until you reach a line feed
            # and then get the next character so that you are on the next line
            while(reader.get_current_char() and reader.get_current_char() != "\n"):
                reader.next_char()
            reader.next_char()

            # clear the current_token
            self.set_current_token("")

            # if (reader.get_current_char()):
            #     self.next_token()

    def consume_current_char(self):
        global reader

        """
        Appends the current character value that was read
        from the file to the current token value and then
        advanced the file reader to the next character.

        No return value.
        """

        current_char = reader.get_current_char()
        self.append_current_token(current_char)
        reader.next_char()

    def token_printer(self):
        """

        If the current token has a value, print the current
        token's position, type, and value.

        If the current token does not have a value, print
        the current token's position, and type.

        No return value.
        """

        if (self.get_token_value() != None):
            print(f"{self.get_token_position()} '{self.get_token_type()}' {self.get_token_value()}")
        else:
            print(f"{self.get_token_position()} '{self.get_token_type()}'")


    def read_file(self, user_input):
        """
        Gets user input for a file to read, opens the
        file, reads the file character by character,
        and analyzes the tokens.

        Prints out the position of each token followed
        by the character.

        Format: position 'type' value

        No return value.
        """

        global reader

        # Try opening the file.
        # If valid and file was successfully opened, value is 1.
        # If invalid and file was not opened, value is 0.
        valid_file = reader.open_file(user_input)

        if (valid_file == 1):
            # Read the first character from the file.
            reader.next_char()

            # Loop until end-of-text character is reached.
            # This is done by looping until the value of the 'current_char' variable,
            # which is obtained by using get_current_char(), is empty.
            # An empty value indicates that End of File has been reached.
            while(reader.get_current_char()):
                self.next_token()

                # skip token if it it is empty
                if (self.get_current_token() != ""):
                    self.set_token_type()
                    self.token_printer()

            print()
            print(f"Concluded lexical analysis on {user_input}")
            print()

            reader.reset()

    def prompt_user(self):
        """
        Prompts user for a file to lexically analyze.
        Once user inputs valid file, the file is
        lexically analyzed.

        The user can quit at any time they receive a
        prompt by typing 'quit' or 'exit' and
        pressing enter.

        Note: This is the same function from FileReader.py.
        By implementing it in this class (LexicalAnalyzer),
        it uses this classes read_file() function rather than
        the read_file() function contained in FileReader.py

        No return value
        """
        while(True):
            user_input = input(">>> Enter a file name, or type 'quit' or 'exit' to exit: ")
            if(user_input == "quit" or user_input == "exit"):
                print("Program terminating...")
                break
            else:
                self.read_file(user_input)

if __name__ == "__main__":
    # Create an instance of the LexicalAnalyzer class
    lexi = LexicalAnalyzer()
    # Run the main method of the LexicalAnalyzer instance
    lexi.prompt_user()