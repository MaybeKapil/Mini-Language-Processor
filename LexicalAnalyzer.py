# import FileReader

# reader = FileReader()
# reader.promptUser()

import string

token_dictionary = {}
current_token = ""

special_characters = string.punctuation

invalid_first_token_char = string.punctuation + " "
# invalid_first_token_char = '!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~}'

class LexicalAnalyzer:
    # global reader

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