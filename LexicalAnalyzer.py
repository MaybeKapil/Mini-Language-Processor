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

    def skip_white_spaces(self):
        print("work in progress")

    def first_token(self):
        # # https://stackoverflow.com/a/63173907
        # while(any c in invalid_first_token for c in next_char):
        #     current_token += next_char

        # https://stackoverflow.com/a/63173907
        # while (invalid_first_token_char not in current_token):

        print("work in progress")

    # get the next token
    def next_token(self):
        # use next_char from the last code

        # use next_char to read until you reach a whitespace or character other than _
        # how do you prevent stuff like prog_ram?
        # i think you kind of have to make sure that the first value until white space is

        # get next character until you reach whitespace or invalid character for that type
        # basically read until you get to whitespace or symbols other than _

        # token = ""
        # while (True):
        #     reader.next_char()
        # return


        print("work in progress")

    # The position of the lexeme.
    # The position is a pair consisting of the line number of the lexeme
    # and the position of the first character of the lexeme in that line.
    def token_position():
        print("work in progress")


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