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
        self.declaration()

        while (self.csym in ["bool", "int"]):
            self.declarations()

            # think i need this
            self.next()

    def declaration(self):
        assert self.csym == "bool" or self.csym == "int", \
            f"Assertion failed: Expected 'bool' or 'int', but current symbol at position {lexi.get_token_position()} is '{self.csym}'"
        self.next()
        self.match(TOKEN_TYPE_ID)

        while (self.csym == ","):
            self.next()
            self.match(TOKEN_TYPE_ID)

        self.match(";")

    def statements(self):
        self.statement()

        while (self.csym == ";"):
            self.next()
        self.statement()

    def statement(self):
        if (self.csym_type == TOKEN_TYPE_ID):
            self.assignment()
        elif (self.csym == "if"):
            self.conditional()
        elif (self.csym == "while"):
            self.iterative()
        elif (self.csym == "print"):
            self.print_sym()
        else:
            self.expected({TOKEN_TYPE_ID, "if", "while", "print"})

    def expected(self, set_of_symbols):
        # if (self.csym not in set_of_symbols):

        # ERROR: At this position I expected to see set_of_symbols, but I see self.csym
        raise AssertionError(f"Expected one of the following: {set_of_symbols}, \
                             but current symbol at position {lexi.get_token_position()} is {self.csym}.")

    def assignment(self):
        assert self.csym_type == TOKEN_TYPE_ID, \
            f"Assertion failed: Expected an identifier, but current symbol at position {lexi.get_token_position()} is '{self.csym}'"
        self.match(TOKEN_TYPE_ID)
        self.match(":=")
        self.expr()

    def conditional(self):
        assert self.csym == "if", \
            f"Assertion failed: Expected 'if', but current symbol at position {lexi.get_token_position()} is '{self.csym}'"
        self.match("if")
        self.expr()
        self.match("then")
        self.body()

    def iterative(self):
        assert self.csym == "while", \
            f"Assertion failed: Expected 'while', but current symbol at position {lexi.get_token_position()} is '{self.csym}'"
        self.match("while")
        self.expr()
        self.match("do")
        self.body()
        self.match("end")

    def print_sym(self):
        assert self.csym == "print", \
            f"Assertion failed: Expected 'print', but current symbol at position {lexi.get_token_position()} is '{self.csym}'"
        self.match("print")
        self.expr()

    def expr(self):
        self.simple_expr()
        relational_operator = {"<", "=<", "=", "!=", ">=", ">"}
        if self.csym in relational_operator:
            self.next_token()
            self.simple_expr()

    def simple_expr(self):
        self.term()
        additive_operator = {"+", "-", "or"}
        while self.csym in additive_operator:
            self.next()
            self.term()

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