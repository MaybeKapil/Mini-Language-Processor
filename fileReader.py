class fileReader:

    # Global Variables

    # Holds the current character
    currentChar = ""

    # Holds the current character's line number
    currentLine = 0 

    # Holds the current character's column number
    currentColumn = 0

    # Reads the next character in the input file. Does not return anything.
    # Will cause the next character to be stored in memory.
    def next_char():
        currentChar = 
        currentLine += 1
        currentColumn += 1

    # Returns a string containing the character that was just read
    def current_char():
        return "Hi"

    # Returns a string containing the line and column integers separated by a colon character.
    def position():
        return currentLine +  ":" + currentColumn;

    def main():
        print("Hello World!")

    if __name__ == "__main__":
        main()
