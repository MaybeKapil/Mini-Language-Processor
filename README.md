# Kapil Regmi
## Development Specification
### Python 3.10.9
### Python Microsoft Extension for Visual Studio Code v2023.16.0
### Visual Studio Code

#### Run using the command
`python Parser.py`

## Program Usage:
This program will reads files character by character and lexically analyze them.
1. When the program starts, it will prompt you for a file name. Enter the file name of a text file which you want the program to read and display.
2. If the file exists, the contents of the file will be syntactically analyzed. If the file does not exist, you will be asked to enter a valid file name.
3. Once a file is read and syntactically analyzed, you will be asked if you want to read another file or if you would like to terminate the program. To read another file, press enter. Otherwise, type "quit" or "exit" (case sensitive) to terminate the program.

## Parser Process:
- The program syntactically analyses the file by checking the syntax of the tokens of the file.
- There are 3 possible outcomes:
    i. Lexically-invalid token is found and error is reported
    ii. Syntactically-unexpected token is found and error is reported
    iii. No lexical or syntax error is found and the analyzer reports "True" and completion of analysis of the file.
