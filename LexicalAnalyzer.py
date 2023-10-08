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

# Lexeme and token are interchangeable.
# Defines a variable that will be used to store the current token.
current_token = ""

# Defines a variable that will be used to store the type of the current token.
token_type = ""

# Defines a variable that will be used to store the current token.
token_pos = ""

class LexicalAnalyzer:

    def get_current_token(self):
        """
        Get the current token value.

        Returns:
            The current token value.
        """

        global current_token
        return current_token

    def set_current_token(self, token_val):
        """
        Set the current token value to the provided token value.

        Args:
            token_val (str): The token value to set as the current token.
        """

        global current_token
        current_token = token_val

    def append_current_token(self, token_val):
        """
        Append the provided token value to the current token.

        Args:
            token_val (str): The token value to append to the current token.
        """

        global current_token
        current_token += token_val

    def get_token_position(self):
        """
        Gets the position of the token.

        The position is represented as a pair consisting of the line number and column where
        the first character of the token occurs.

        Return:
            A string representing the position of the first character of the current token.
            Format: line:column
        """

        global token_pos
        return token_pos

    def set_token_position(self, position):
        """
        Sets the position of the current token.

        Args:
            position (str): The position value of the current token.
        """


        global token_pos
        token_pos = position

    def get_token_type(self):
        """
        Get the current token type.

        Returns:
            The current token type.
        """

        global token_type
        return token_type

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

        token_type = ""

        if (token.isdigit()):
            token_type = "NUM"
        elif (token in KEYWORDS or
              token in OPERATOR_CHARS):
            token_type = current_token
        elif (token == '.'):
            token_type = "end-of-text"
        elif all (char in LETTER_CHARS or \
                  char in DIGIT_CHARS or \
                    char == '_' \
                        for char in token):
            token_type = "ID"
        else:
            token_type = token

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
        Prints the current token's position, it's type,
        and it's value if it has one.

        No return value.
        """

        if (self.get_token_value() != None):
            print(f"{self.get_token_position()} '{self.get_token_type()}' {self.get_token_value()}")
        else:
            print(f"{self.get_token_position()} '{self.get_token_type()}'")


    def read_file(self, user_input):
        # file_opened = self.open_file(user_input)

        # if (file_opened == 1):
        #     self.next_char()

        #     # while end-of-text has not been reached
        #     while(self.get_current_char()):
        #         # get first token
        #         self.first_token();

        #         # get next token
        #         self.next_token()
        print("work in progress")

if __name__ == "__main__":
    print("in progress")