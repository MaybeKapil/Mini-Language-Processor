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

class LexicalAnalyzer:

    def __init__(self):
        # Lexeme and token are interchangeable.
        # Defines a variable that will be used to store the current token.
        self.current_token = ""

        # Defines a variable that will be used to store the type of the current token.
        self.token_type = ""

        # Defines a variable that will be used to store the current token position.
        self.token_pos = ""

        self.token_is_valid = True

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

        No return value.
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


        No return value.
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

        No return value.
        """

        global LETTER_CHARS, DIGIT_CHARS, OPERATOR_CHARS, KEYWORDS

        token = self.get_current_token()

        self.token_type = ""

        # if token contains all digits, then the token type is "NUM"
        if (token.isdigit()):
            self.token_type = "NUM"
        # if the token is a keyword or an operator, then the token type
        # is the token it self and the token will not have a value.
        elif (token in KEYWORDS or
              token in OPERATOR_CHARS):
            self.token_type = token
        # if the token is not a keyword but contains a letter, and/or
        # digits, and/or underscore, then the token ID is of type "ID"
        elif all (char in LETTER_CHARS or \
                  char in DIGIT_CHARS or \
                    char == '_' \
                        for char in token):
            self.token_type = "ID"
        # for parenthesis, comma, colon, and semicolon
        # the type is the token itself and the token will have no value
        else:
            self.token_type = token

    def set_token_type_eot(self):
        """
        Specialized function for setting the token type to 'end-of-text'
        once a file has been fully read and all the tokens are valid.

        Made separate since it serves a single purpose.
        """
        self.token_type = "end-of-text"

    def get_token_value(self):
        """
        Get the current token value.

        Only identifiers ('ID') and integers ('NUM') have values.
        If it not an ID or NUM, then return None to indicate that it does not have a value.

        Returns:
            The current token value.
        """

        type = self.get_token_type()

        if (type in ["ID", "NUM"]):
            return self.get_current_token()

        return None

    def set_token_validity(self, valid):
        """
        Set the validity of the current token.

        Set to true if token is valid.
        Set to false if token is invalid.
        """
        self.token_is_valid = valid

    def get_token_validity(self):
        """
        Get the validity of the current token.
        """
        return self.token_is_valid

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
        while (current_char and current_char in WHITE_SPACE_CHARS):
            # skip the current (whitespace) character by getting the next character
            reader.next_char()

            # store the new current character to be used for reevaluation of the while conditional statement
            current_char = reader.get_current_char()

    def next(self):
        """
        Process the next token.

        Processing the next token includes getting the next token and
        validating the token.

        No return value.
        """

        self.next_token()
        token = self.get_current_token()
        valid = self.validate_token(token)
        self.set_token_validity(valid)

    def next_token(self):
        """
        Gets the next token from the file.

        Skips whitespaces, stores the to-be generated token's starting position,
        builds the token, skips comments, and creates an end-of-text token if the end of text
        is reached.

        An empty token "" is only generated if end of text is reached and EOT is created.

        No return value.
        """

        global WHITE_SPACE_CHARS, LETTER_CHARS, \
            DIGIT_CHARS, OPERATOR_CHARS, PUNCTUATION_CHARS, \
                reader

        while (reader.get_current_char()):
            # local token variable to store the token while the token is being "built"
            token = ""

            # skip consecutive whitespaces until you reach a non-whitespace character
            self.skip_white_spaces()

            # after all the white spaces are skipped (if there were any), you end up at a non-whitespace character
            # and therefore need to mark this as the beginning of the token
            self.set_token_position(reader.position())

            token = self.build_token()

            # the start of a comment was found
            if (token == "//"):
                # clear the current_token to get rid of the double slash
                self.skip_comment()
                # check if end of file is reached after skipping the comment
                if not reader.get_current_char():
                    self.create_eot()
                    break
            # no more tokens can be built, so end of file has been reached
            elif (token == ""):
                self.create_eot()
                break
            else:
                self.set_current_token(token)
                break

    def create_eot(self):
        """
        Create end-of-text token.

        No return value
        """

        self.set_current_token("")
        self.set_token_position(reader.position())
        self.set_token_type_eot()

    def build_token(self):
        """
        Build the token by checking the current character and determining it's type.
        Based on it's type, call a respective function to take care of building the token.

        Return:
            The token
        """
        global reader

        # store the current character
        current_char = reader.get_current_char()

        # if the current character matches any of the first character in the operator character sets
        # then the token should be built as an operator token or a comment token
        # comment token is included in this because division is an operation that is represented by '/'
        # and comment is represented by '//' so they are similar
        if any(current_char == operator[0] for operator in OPERATOR_CHARS):
            return self.build_operator_or_comment_token()
        # check if the current character is a letter
        elif (current_char in LETTER_CHARS):
            return self.build_id_or_keyword_token()

        # check if the current character is a digit
        elif (current_char in DIGIT_CHARS):
            return self.build_number_token()

        # If the current character is not an operator, letter, or digit,
        # then process it individually (single character token) as it is
        # likely to be one of the following symbols: parenthesis, comma,
        # colon, or semicolon
        else:
            reader.next_char()
            return current_char

    def build_operator_or_comment_token(self):
        """
        Build operator or comment token by reading the input file character by character.

        Operator tokens are the following: ':=', '<', '=<', '=', '!=', '>=', '>', '+', '-', '*' , '/'

        Comment token is '//'.

        Return:
            The operator or comment token that was built.
        """

        global reader

        # store the current character
        current_char = reader.get_current_char()

        # set the token to the current character
        token = current_char

        while (True):
            # advance reader to the next character in the file
            reader.next_char()

            # get and store the next character as the current character
            current_char = reader.get_current_char()

            # check if the new current character appended to the current token is
            # still valid operator symbol
            # if so, append to token
            if (current_char and token + current_char in OPERATOR_CHARS):
                token += current_char

            # check if the new current character appended to the current token is
            # a double slash ('//')
            # if so, append to token and stop the loop as a comment token
            # has been reached
            elif (token + current_char == '//'):
                token += current_char
                break

            # stop building the current token
            else:
                break

        return token

    def build_id_or_keyword_token(self):
        """
        Build id or keyword token by reading the input file character by character.

        Identifiers (ID) is a string that begins with a letter and optionally followed by a
        sequence of letters, digits, and/or underscore. IDs are not keywords.

        Keyword tokens are the following:
            "program", "bool", "int", "if", "then", "else", "end",
            "while", "do", "end", "print", "or", "mod", "and", "not",
            "false", "true"

        Return:
            The id or keyword token that was built.
        """

        global reader

        # store the current character
        current_char = reader.get_current_char()

        # set the token to the current character
        # indicates that the first character of the token is a letter
        # this means that the token will be an ID or keyword
        token = current_char

        while (True):
            # advance reader to the next character in the file
            reader.next_char()

            # get and store the next character as the current character
            current_char = reader.get_current_char()

            # if the new current character is non empty and a letter,
            # digit, or underscore, then add it to the token.
            if (current_char and
                (current_char in LETTER_CHARS or
                current_char in DIGIT_CHARS or
                current_char == '_')):
                token += current_char

            # if the new current character is empty or it is not a
            # letter, digit, or underscore, stop building the current token
            else:
                break

        return token

    def build_number_token(self):
        """
        Build number token by reading the input file character by character.

        Number is a string that contains only digits. No commas or periods are allowed.

        All integers are within range and don't need to check for overflow.

        Return:
            The number token that was built.
        """

        global reader

        # store the current character
        current_char = reader.get_current_char()

        # set the token to the current character
        # indicates that the first character of the token is a digit
        # this means that the token will be a number
        token = current_char

        while (True):
            # advance reader to the next character in the file
            reader.next_char()
            # get and store the next character as the current character
            current_char = reader.get_current_char()

            # if the new current character is still a digit,
            # then add it to the token
            if (current_char and current_char in DIGIT_CHARS):
                token += current_char

            # if the new current character is not a digit,
            # stop building the current token
            else:
                break

        return token

    def skip_comment(self):
        """
        Read and discard all subsequent characters after '//'
        up to and including the line feed character ('\n').
        """

        global reader

        # While the file still contains unread characters,
        # keep getting the next character until you reach a line feed
        # and then get the next character so that you are on the next line
        while(reader.get_current_char() and reader.get_current_char() != "\n"):
            reader.next_char()
        reader.next_char()

    def valid_token_msg(self):
        """

        If the current token is valid and has a value, return a string containing the current
        token's position, type, and value.

        If the current token does not have a value, return a string containing
        the current token's position, and type.

        Return:
            String containing valid token info
        """

        if (self.get_token_value() is not None):
            return(f"{self.get_token_position()} '{self.get_token_type()}' {self.get_token_value()}")
        else:
            return(f"{self.get_token_position()} '{self.get_token_type()}'")

    def invalid_token_msg(self):
        """
        If the current token contains an invalid character, then return a string containing
        the character's position, and the error message along
        with the invalid character contained in the token.

        Return:
            String containing invalid character info

        """
        return (f"{self.get_token_position()} ----- Invalid character '{self.get_current_token()}'")

    def print_token(self):
        if (self.token_is_valid):
            self.valid_token_msg()
        else:
            self.invalid_token_msg()

    def validate_token(self, token):
        """
        Returns if the token passed is valid or not.

        If the token contains any of the invalid character(s), then it is considered invalid.
        Underscore or colon or exclamation point by itself is not a valid token.
        Underscore can only appear in ID, which has to start with a letter.

        If token is invalid, return False.
        Otherwise, if token is not empty, set token type and return True.
        Otherwise, if token is empty (only for EOT token), return True without setting token type
        since generation of EOT token automatically sets type.

        """
        INVALID_CHARS = "!\"#$%&'?@[\]^`{|}~}'"

        # If the token is not an empty string and it contains an invalid character
        # then return False to indicate that the token is invalid
        if (token and(token in INVALID_CHARS or token == '_' or token == '!')):
            return False
        # Otherwise, if the token is not empty (but doesn't contain an invalid character),
        # set the token type and return True to indicate that it was validated
        elif (token):
            self.set_token_type()
            return True
        # Otherwise, if the token is empty, then return true but don't set the type
        # This is meant to validate the end-of-text token obtained by using next_token()
        # The program already ignores whitespaces and comments so the only time when
        # the token can be "" is if it's an end-of-text token
        else:
            return True

    def reset(self):
        """
        Restore instance variables of Lexical Analyzer to default state.

        No return value.
        """
        global reader

        reader.reset()

        self.current_token = ""

        self.token_type = ""

        self.token_pos = ""

        self.token_is_valid = True

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
            # If a non-valid token is reached, terminate lexical analyzer.
            while(reader.get_current_char() and self.token_is_valid):
                self.next()
                self.print_token()

            print(f"\nConcluded lexical analysis on {user_input}\n")

            self.reset()

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
                # Process file for lexical analysis
                self.read_file(user_input)

if __name__ == "__main__":
    # Create an instance of the LexicalAnalyzer class
    lexi = LexicalAnalyzer()
    # Run the main method of the LexicalAnalyzer instance
    lexi.prompt_user()