
# Global Variables

# Holds the current character
current_char = ''

# Holds the current character's line number
current_line = 0

# Holds the current character's column number
current_column = 0

class fileReader: 
    
    # Reads the next character in the input file. Does not return anything.
    # Will cause the next character to be stored in memory.
    def next_char():
        global current_char, current_line, current_column
        current_char = 'a'
        current_line += 1
        current_column += 1

    # Returns a string containing the character that was just read
    def get_current_char():
        return "fix_me"

    # Returns a string containing the line and column integers separated by a colon character.
    def position():
        return currentLine +  ":" + currentColumn;
    
    def main():
        print("fix_me")

    if __name__ == "__main__":
        main()
