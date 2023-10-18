# Kapil Regmi
## Development Specification
### Python 3.10.9
### Python Microsoft Extension for Visual Studio Code v2023.16.0
### Visual Studio Code

#### Compile using the command
`python LexicalAnalyzer.py`

## Program Usage:
This program will reads files character by character and lexically analyze them.
1. When the program starts, it will prompt you for a file name. Enter the file name of a text file which you want the program to read and display.
2. If the file exists, the contents of the file will be lexically analyzed. If the file does not exist, you will be asked to enter a valid file name.
3. Once a file is read and lexically analyzed, you will be asked if you want to read another file or if you would like to terminate the program. To read another file, press enter. Otherwise, type "quit" or "exit" (case sensitive) to terminate the program.

## Lexical Analysis Process:
- The program lexically analyses the file by tokenizing the content of the file.
- Characters that are not valid to the grammar generates an error and the analysis of the current file is interrupted.
- Each valid token is printed with it's position, and type. The value is also printed if the token is a number or an identifier.
- There are 5 different lexemes: identifiers ("ID"), Numbers ("NUM"), keywords, symbols/operators, end-of-text ('.').
