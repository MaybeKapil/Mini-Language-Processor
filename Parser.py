import LexicalAnalyzer

lexi = LexicalAnalyzer.LexicalAnalyzer()
READER = LexicalAnalyzer.reader

set_of_symbols = {}

TOKEN_TYPE_ID = "ID"

class Parser:
    def __init__ (self):
        # Defines a variable that will be used to store the next token
        # returned by the lexical analyzer
        self.csym = ""
        self.csym_type = ""

    def set_csym(self, token):
        self.csym = token

    def next(self):
        lexi.next_token()
        token = lexi.get_current_token()
        self.set_csym(token)
        self.csym_type = lexi.get_token_type()

    def match(self, sym):
        # if (self.csym == sym or self.csym_type == sym):
        #     self.next()
        # else:
        #     # ERROR: At this position see self.csym but expect sym
        #     raise TypeError("Expected {sym}, got {self.csym} at position.")

        assert self.csym == sym or self.csym_type == sym, \
            f"Assertion failed: Expected '{sym}' but current symbol at position {lexi.get_token_position()} is '{self.csym}'"
        self.next()

    def program(self):
        self.match("program")

    def body(self):
        if (self.csym ==  "bool" or self.csym == "int"):
            self.declarations()
        self.statements()

    def declarations(self):
        declaration()

        while (csym in ["bool", "int"]):
            declarations()

    def declaration(self):
        # assert csym in "bool" or "int"

        next_token()
        match(ID)

        while (csym == ","):
            next_token()
            match(ID)

        match(";")

    def statements(self):
        statement()

        while (csym == ";"):
            next_token()

        statement()

    def statement(self):
        if (csym == ID):
            assignment()
        elif (csym == "if"):
            conditional()
        elif (csym == "while"):
            iterative()
        elif (csym == "print"):
            print_s()
        else:
            expected({ID, "if", "while", "print"})

    def expected(self, set_of_symbols):
        if (csym not in set_of_symbols):
            # ERROR: At this position I expected to see set_of_symbols, but I see csym
            raise TypeError("Expected one of the following: {set_of_symbols}, got csym.")

    def assignment(self):
        assert csym is ID
        match(ID)
        match(":=")
        expr()

    def conditional(self):
        assert csym is "if"
        match("if")
        expr()
        match("then")
        body()

    def print(self):
        finish this

    def expr(self):
        simpleexpr()
        relational_operator = {"<", "=<", "=", "!=", ">=", ">"}
        if csym in relational_operator:
            next_token()
            simpleexpr()

    def simpleexpr(self):
        term()
        additive_operator = {"+", "-", "or"}
        while csym in additive_operator:
            next_token()
            term()

    def term(self):
        finish this

    def factor(self):
        if (csym == "-" or csym == "not"):
            next_token()
        if (csym == "false" or "true" is "Num"):
            literal()
        elif (csym is ID):
            next_token()
        elif (csym == "("):
            next_token()
            expr()
            match(")")
        else:
            expected({"false", "true", NUM, ID, "C"})

    def literal(self):
        assert csym == "true" or csym == "false" or csym == NUM
        if (csym is NUM):
            next_token()
        else:
            booleanLiteral()

    def boolean_literal(self):
        assert csym == "true" or csym == "false"
        next_token()

if __name__ == "__main__":
    # Create an instance of the LexicalAnalyzer class
    lexi = LexicalAnalyzer()

    # Create an instance of the Parser class
    par = Parser()

    lexi.next_token()
    program()