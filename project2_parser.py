# If you haven't read the P2 post in campuswire, read it before you continue.

# If you have working lexer of project 1, then you are good to go, you just
# need few modifications in the lexer. I believe you are better off, if you
# just extend it.

# If you don't have a working lexer for project 1, we have provide a skelton of 
# lexer. You need to complete the functions commented with tokenize.


class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0
        if self.code:
            self.current_char = self.code[self.position]    # Set to the first character
        else:
            self.current_char = None

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        self.position += 1
        if self.position < len(self.code):
            self.current_char = self.code[self.position]
        else:
            self.current_char = None
        if self.current_char == '\n':  # Skip over newline characters
            self.advance()

    def peek(self):
        peek_pos = self.position + 1
        if peek_pos < len(self.text):
            return self.text[peek_pos]
        else:
            return None
        
    def peek_token(self):
        """Peek at the next significant token without consuming it."""
        old_position = self.position
        old_char = self.current_char
        next_token = self.get_token()  # Temporarily generate the next token
        self.position = old_position  # Restore the original position
        self.current_char = old_char  # Restore the original character
        return next_token

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            #print(f"Current character: {self.current_char}")
            self.advance()

    # implement
    def number(self):
        result = ''
        dot_seen = False
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.' and not dot_seen):
            #print(f"current_char: {self.current_char}")
            if self.current_char == '.':
                dot_seen = True
            result += self.current_char
            self.advance()
        #print(f"Number result: {result}")

        if dot_seen:
            return ("FLOAT", 'float')
        else:
            return ("INT", 'int')
        
    # Tokenize identifiers and condition keywords
    def identifier(self):
        result = ''
        
        # Identifiers contain alphabetic characters, digits, and underscores
        while self.current_char is not None and (self.current_char.isalpha() or self.current_char.isdigit() or self.current_char == '_'):
            #print(f"current_char: {self.current_char}")
            result += self.current_char
            self.advance()
        #print(f"Identifier result: {result}")
        # Match identifiers to condition keywords or return as a general identifier
        if result == 'if':
            return ("IF", result)
        elif result == 'then':
            return ("THEN", result)
        elif result == 'else':
            return ("ELSE", result)
        elif result == 'while':
            return ("WHILE", result)
        elif result == 'do':
            return ("DO", result)
        elif result == 'int':
            return ("INT", result)
        elif result == 'float':
            return ("FLOAT", result)
        else:
            return ("ID", result)


    # Move the lexer position and identify next possible tokens
    def get_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit() or self.current_char == '.':
                return self.number()

            if self.current_char.isalpha() or self.current_char == '_':
                return self.identifier()

            if self.current_char == '+':
                self.advance()
                return ("PLUS", '+')

            if self.current_char == '-':
                self.advance()
                return ("MINUS", '-')

            if self.current_char == '*':
                self.advance()
                return ("MULTIPLY", '*')

            if self.current_char == '/':
                self.advance()
                return ("DIVISION", '/')

            if self.current_char == '(':
                self.advance()
                return ("LPAREN", '(')

            if self.current_char == ')':
                self.advance()
                return ("RPAREN", ')')
            
            if self.current_char == '{':
                self.advance()
                return ("LSCOPE", '{')
            
            if self.current_char == '}':
                self.advance()
                return ("RSCOPE", '}')
            
            if self.current_char == '\n':
                self.advance()
                return ("DELIMITER", '\n')

            if self.current_char == '=':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return ("EQ", '==') # Equality operator
                return ("ASSIGN", '=')  # Assignment operator
            
            if self.current_char == '>':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return ("GE", '>=') # Greater than or equal to
                return ("GT", '>')  # Greater than

            if self.current_char == '<':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return ("LE", '<=') # Less than or equal to
                return ("LT", '<')  # Less than

            if self.current_char == '!':
                self.advance()
                if self.current_char == '=':
                    self.advance()
                    return ("NEQ", '!=')    # Not equal to

        return ("EOF", None)    # End of file token when there are no more characters to read
    

# Parse Tree Node definitions.
# Don't need to modify these definitions for the completion of project 2.

# But if you are interested in modifying these definitions for
# learning purposes. Then Don't whatever you want.

class Node:
    pass

class ProgramNode(Node):
    def __init__(self, statements):
        self.statements = statements

class DeclarationNode(Node):
    def __init__(self, identifier, expression, myType):
        self.identifier = identifier
        self.expression = expression
        self.type       = myType

class AssignmentNode(Node):
    def __init__(self, identifier, expression):
        self.identifier = identifier
        self.expression = expression

class IfStatementNode(Node):
    def __init__(self, condition, if_block, else_block):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

class WhileLoopNode(Node):
    def __init__(self, condition, loop_block):
        self.condition = condition
        self.loop_block = loop_block

class ConditionNode(Node):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

class ArithmeticExpressionNode(Node):
    def __init__(self, operator, left, right, myType):
        self.operator = operator
        self.left = left
        self.right = right
        self.type  = myType

class TermNode(Node):
    def __init__(self, operator, left, right, myType):
        self.operator = operator
        self.left = left
        self.right = right
        self.type  = myType

class FactorNode(Node):
    def __init__(self, value, myType):
        self.value = value
        self.type = myType




# final parser - student copy

# Skelton of Parser class.
# For project 1, we should have implemented parser that returns a string representation.
# For project 2:
  # 1. You have to build the Parse tree with the node definitions given to you. The core
  # logic of how to parse the lanague will not differ, but you to have create Tree node
  # whereever you are creating tuple in the project 1.
  # 2. Implement symbol table and scoping rules. 
  #   Hint: You can use stack to model the nested scopes and a dictionary to store identifiers
  #   and its type.

  # For those who are interested, you call print_parse_tree to view the text representation
  # of Parse Tree.


class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_token()
        # implement symbol table and scopes
        self.symbol_table = {'global': {}}
        self.scopes = ['global']
        self.scope_counter = 0  # Initialize a counter for unique scope naming
        self.messages = []

    def print_parse_tree(self, node, indent=0):
        message = ""
        if isinstance(node, ProgramNode):
            message += '  ' * indent + 'Program\n'
            for statement in node.statements:
                message += self.print_parse_tree(statement, indent + 1)
        elif isinstance(node, DeclarationNode):
            message += '  ' * indent + 'Declaration: ' + node.identifier + '\n'
            message += self.print_parse_tree(node.expression, indent + 1)
        elif isinstance(node, AssignmentNode):
            message += '  ' * indent + 'Assignment: ' + node.identifier + '\n'
            message += self.print_parse_tree(node.expression, indent + 1)
        elif isinstance(node, IfStatementNode):
            message += '  ' * indent + 'If Statement\n'
            message += self.print_parse_tree(node.condition, indent + 1)
            message += '  ' * indent + 'Then Block:\n'
            for statement in node.if_block:
                message += self.print_parse_tree(statement, indent + 2)
            if node.else_block:
                message += '  ' * indent + 'Else Block:\n'
                for statement in node.else_block:
                    message += self.print_parse_tree(statement, indent + 2)
        elif isinstance(node, WhileLoopNode):
            message += '  ' * indent + 'While Loop\n'
            message += self.print_parse_tree(node.condition, indent + 1)
            message += '  ' * indent + 'Loop Block:\n'
            for statement in node.loop_block:
                message += self.print_parse_tree(statement, indent + 2)
        elif isinstance(node, ConditionNode):
            message += '  ' * indent + 'Condition : with operator ' + node.operator + '\n'
            message += '  ' * indent + 'LHS\n'
            message += self.print_parse_tree(node.left, indent + 2)
            message += '  ' * indent + 'RHS\n'
            message += self.print_parse_tree(node.right, indent + 2)
        elif isinstance(node, ArithmeticExpressionNode):
            message += '  ' * indent + 'Arithmetic Expression: ' + node.operator + '\n'
            message += self.print_parse_tree(node.left, indent + 1)
            message += self.print_parse_tree(node.right, indent + 1)
        elif isinstance(node, TermNode):
            message += '  ' * indent + 'Term: ' + node.operator + '\n'
            message += self.print_parse_tree(node.left, indent + 1)
            message += self.print_parse_tree(node.right, indent + 1)
        elif isinstance(node, FactorNode):
            message += '  ' * indent + 'Factor: ' + str(node.value) + '\n'

        return message


    def error(self, message):
        self.messages.append(message)

    def eat(self, token_type):
        #print(f"Before eating: expecting {token_type}, current token is {self.current_token}")
        # Map from expected symbols to token types
        token_type_map = {
            '>': 'GT',
            '<': 'LT',
            '>=': 'GE',
            '<=': 'LE',
            '=': 'ASSIGN',
            '==': 'EQ',
            '!=': 'NEQ',
            '+': 'PLUS',
            '-': 'MINUS',
            '*': 'MULTIPLY',
            '/': 'DIVIDE',
            '(': 'LPAREN',
            ')': 'RPAREN',
            '{': 'LSCOPE',
            '}': 'RSCOPE'
        }
        # Check if the token type needs to be mapped
        expected_token_type = token_type_map.get(token_type, token_type)

        if self.current_token[0] == expected_token_type:
            self.current_token = self.lexer.get_token()
            #print(f"After eating: next token is {self.current_token}")
        else:
            self.error(f'Expected token of type {token_type}, but found {self.current_token[0]}')
            print(f'Expected token of type {token_type}, but found {self.current_token[0]}')
            if self.current_token[0] == 'EOF':
                return  # Optionally handle EOF gracefully

    # enter the new scope in the program
    def enter_scope(self, scope_prefix):
        new_scope = f"{self.current_scope()}_{scope_prefix}"
        self.scopes.append(new_scope)
        # Copy the parent scope's symbol table to the new scope
        if scope_prefix == "else":
            parent_scope = self.scopes[-2] if len(self.scopes) > 1 else 'global'
        else:
            parent_scope = self.scopes[-1] if len(self.scopes) > 0 else 'global'
    
        if parent_scope in self.symbol_table:
            self.symbol_table[new_scope] = self.symbol_table[parent_scope].copy()
        else:
            self.symbol_table[new_scope] = {}
        
    # leave the current scope
    def leave_scope(self):
        if self.scopes:
            scope_to_remove = self.scopes.pop()
            if scope_to_remove in self.symbol_table and scope_to_remove != 'global':
                del self.symbol_table[scope_to_remove]

    # return the current scope
    def current_scope(self):
        if self.scopes:
            return self.scopes[-1]
        return 'global' 
    
    def checkVarDeclared(self, identifier):
        # check if variable is already declared in the current scope
        #implement = False
        current_scope = self.current_scope()
        
        if identifier in self.symbol_table[current_scope]:
            self.error(f'Variable {identifier} has already been declared in the current scope')
            print(f'Variable {identifier} has already been declared in the current scope')
            raise Exception(f'Variable {identifier} has already been declared in the current scope')
        else:
            self.symbol_table[current_scope][identifier] = None  # Assuming True means declared
            #print(f'[DEBUG] Declaring new variable {identifier} in {current_scope}')
            
            

    def checkVarUse(self, identifier):
        # check var declared, so we can use it.
        # Check if variable is declared in the current or any enclosing scopes
        found = False
        for scope in reversed(self.scopes):
            if identifier in self.symbol_table.get(scope, {}):
                found = True
                break
        if not found:
            self.error(f'Variable {identifier} has not been declared in the current or any enclosing scopes')
            print(f'Variable {identifier} has not been declared in the current or any enclosing scopes')

            #raise Exception(f'Variable {identifier} has not been declared in the current or any enclosing scopes')
            

    # return false when types mismatch, otherwise ret true
    def checkTypeMatch(self, vType, eType, var, exp):
        if vType == 'FLOAT':
            vType = 'float'
        elif vType == 'INT':
            vType = 'int'
        
        if eType == 'FLOAT':
            eType = 'float'
        elif eType == 'INT':
            eType = 'int'    

        if vType != eType:
            self.error(f'Type Mismatch between {vType} and {eType}')
            print(f'Type Mismatch between {vType} and {eType}')
            return False
        return True

    # return its type or None if not found
    def getMyType(self, identifier):
        for scope in self.scopes:
            if scope in self.symbol_table and identifier in self.symbol_table[scope]:
                return self.symbol_table[scope][identifier]
            self.checkVarUse(identifier)
        # If not found, search backwards to handle cases where type was declared in outer scopes    
        return None
    
    def findTypeForVariable(self, identifier):
    # Search from the most local scope to the global scope for the first occurrence of the identifier
        for scope in reversed(self.scopes):
            if identifier in self.symbol_table.get(scope, {}):
                return self.symbol_table[scope][identifier]
        #self.error(f"Variable {identifier} used without declaration.")
        #print(f"Variable {identifier} used without declaration.")
        return None  # Return None if no type is found.
      

    def parse_program(self):
        statements = []
        while self.current_token[0] != 'EOF':
            if self.current_token[0] in ['INT', 'FLOAT', 'ID', 'IF', 'WHILE', 'LSCOPE']:
                statements.append(self.parse_statement())
            elif self.current_token[0] == 'DELIMITER':
                self.eat('DELIMITER')
            else:
                self.error(f"Unexpected token {self.current_token[0]}")
                #print(f"Unexpected token {self.current_token[0]} at program level")
                self.current_token = self.lexer.get_token()  # Consume unexpected token    
        return ProgramNode(statements)


    def parse_statement(self):
        try:
            if self.current_token[0] == 'INT' or self.current_token[0] == 'FLOAT':
                return self.parse_declaration()
            elif self.current_token[0] == 'ID':
                next_token = self.lexer.peek_token()
                if next_token[0] in ['INT', 'FLOAT']:  # It's a redeclaration
                    return self.parse_declaration()  # Parse it as a new declaration
                else:
                    return self.parse_assignment()  # No new type, just an assignment
            elif self.current_token[0] == 'IF':
                return self.parse_if_statement()
            elif self.current_token[0] == 'WHILE':
                return self.parse_while_loop()
        except Exception as e:
            #print(f"Error encountered: {str(e)}")
            # Skip to the end of the current block or handle the flow control as needed
            self.recover_to_next_statement()
            return None
        else:
            self.error(f'Invalid statement: {self.current_token[1]}')
            self.eat(self.current_token[0])
            return None


    def recover_to_next_statement(self):
    # Recovery logic: skip tokens until a statement delimiter or new block is found
        while self.current_token and self.current_token[0] not in ['DELIMITER', 'RSCOPE', 'EOF']:
            self.current_token = self.lexer.get_token()

    def parse_declaration(self):
        myType = self.current_token[0]
        self.eat(myType)

        identifier = self.current_token[1]
        self.eat('ID')
        self.checkVarDeclared(identifier)
        
        self.eat('ASSIGN')
        expression = self.parse_arithmetic_expression()
        if expression is not None and not self.checkTypeMatch(myType, expression.type, identifier, expression):
            #self.checkVarUse(identifier)
            return None
        
        # Check if variable is already declared in the current scope
        current_scope = self.current_scope()
        if current_scope not in self.symbol_table:
                self.symbol_table[current_scope] = {}
        self.symbol_table[current_scope][identifier] = myType
        return DeclarationNode(identifier, expression, myType)


    def parse_assignment(self):
        identifier = self.current_token[1]
        self.eat('ID')

        vType = self.getMyType(identifier)
        if not vType:
        # If no type is found and it's crucial, handle the case or report an error.
            vType = self.findTypeForVariable(identifier)
            if not vType:
                # Handle cases where no type is found; decide if you want to return, raise an error, or set a default type
                print(f"No type found for variable {identifier}, cannot proceed with assignment.")
                return None
        #self.checkVarUse(identifier)
        self.eat('ASSIGN')
        expression = self.parse_arithmetic_expression()
        
        if expression.type is None or not self.checkTypeMatch(vType, expression.type, identifier, expression):
            #self.error(f'Type Mismatch between {vType} and {expression.type}')
            #print(f'Type Mismatch between {vType} and {expression.type}')
            return None
        return AssignmentNode(identifier, expression)

    def parse_if_statement(self):
        self.eat('IF')
        condition = self.parse_condition()

        self.eat('THEN')
        self.eat('{')  # consume the '{' token
        self.enter_scope('if')
        # Parse statements within the if
        # self.leave_scope()
        if_block = []
        
        #self.enter_scope('if')
        while self.current_token[0] != 'RSCOPE' and self.current_token[0] != 'EOF':
            #try:
            if_block.append(self.parse_statement())
            #except Exception as e:
            #    print(f"Caught error in if block: {str(e)}")
            #    self.recover_to_next_statement()  # Move to a logical recovery point  

        self.eat('RSCOPE')  # consume the '}' token
        self.leave_scope()

        else_block = []
        if self.current_token[0] == 'ELSE':
            self.eat('ELSE')
            self.eat('{')  # consume the '{' token
            self.enter_scope('else')
            while self.current_token[0] != 'RSCOPE' and self.current_token[0] != 'EOF':
                #try:
                else_block.append(self.parse_statement())
                #except Exception as e:
                #    print(f"Caught error in else block: {str(e)}")
                #    self.recover_to_next_statement()  # Move to a logical recovery point
            self.eat('RSCOPE')  # consume the '}' token
            self.leave_scope()
        return IfStatementNode(condition, if_block, else_block)
 
    
    def parse_while_loop(self):
        self.eat('WHILE')
        condition = self.parse_condition()

        self.eat('DO')
        self.eat('{')

        self.enter_scope('while')
        loop_block = []
        try:
            while self.current_token[0] != 'RSCOPE' and self.current_token[0] != 'EOF':
                loop_block.append(self.parse_statement())
        finally:
            self.eat('RSCOPE')
            self.leave_scope()

        return WhileLoopNode(condition, loop_block)
    
    # Helper function to parse a statement
    def attempt_parse_statement(self):
        try:
            return self.parse_statement()
        except Exception as e:
            print(f"Error during parsing: {str(e)}")
            self.recover_to_next_statement()
            return None
    # No need to check type mismatch here.
    def parse_condition(self):
        left = self.parse_arithmetic_expression()
        operator = self.current_token[1]
        self.eat(operator)
        right = self.parse_arithmetic_expression()
        return ConditionNode(left, operator, right)
    
    # To find the result type of an arithmetic expression, we need to check the types of the operands and the operator.
    def get_result_type(self, left_type, right_type, operator):
        if operator in ['*', '/', '+', '-', '==', '!=', '<', '>', '<=', '>=']:
            if left_type == right_type:
                return left_type
            if 'float' in [left_type, right_type]:
                return 'float' if None not in [left_type, right_type] else None # Promote to float if either operand is float
            else:
                return None  # Return None for unsupported operations
        return None  # Return None for unsupported operations

    # Parse for arithmetic expressions
    def parse_arithmetic_expression(self):
        left = self.parse_term()
        operator = self.current_token[1]
        while operator in ['+', '-']:
            self.eat(operator)
            right = self.parse_term()
            # Determine the resulting type based on operand types
            result_type = self.get_result_type(left.type, right.type, operator)
            if result_type is None:
                
                left.type = None  # Propagate the error by setting type to None
                #self.error(f'Type Mismatch between {left.type} and {right.type}')
                #print(f'Type Mismatch between {left.type} and {right.type}')

            else:
                left = ArithmeticExpressionNode(operator, left, right, result_type if result_type else 'None')
            operator = self.current_token[1]
        return left

        
    # Parse for multiply or divide operations
    def parse_term(self):
        left = self.parse_factor()
        operator = self.current_token[1]
        while operator in ['*', '/']:
            self.eat(operator)
            right = self.parse_factor()
            
            result_type = self.get_result_type(left.type, right.type, operator)
            if result_type is None:
                left.type = None  # Propagate the error by setting type to None
            else:
                left = TermNode(operator, left, right, result_type if result_type else 'None')
            operator = self.current_token[1]
        return left

    # Checking for the type of the expression
    def parse_factor(self):
        if self.current_token[0] == 'INT':
            value = self.current_token[1]
            self.eat('INT')
            return FactorNode(value, 'int')
        elif self.current_token[0] == 'FLOAT':
            value = self.current_token[1]
            self.eat('FLOAT')
            return FactorNode(value, 'float')
        
        elif self.current_token[0] == 'ID':
            identifier = self.current_token[1]
            self.eat('ID')
        
            # Use symbol table to get the type of the identifier
            var_type = self.getMyType(identifier)
            return FactorNode(identifier, var_type)
        elif self.current_token[0] == 'LPAREN':
            self.eat('LPAREN')
            node = self.parse_arithmetic_expression()
            self.eat('RPAREN')
            return node
        else:
            self.error(f'Invalid factor: {self.current_token[1]}')
            print(f'Invalid factor: {self.current_token[1]}')
            #self.eat(self.current_token[0])
            return None
