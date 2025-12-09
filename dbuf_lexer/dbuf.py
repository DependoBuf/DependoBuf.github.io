import json
from pygments.lexer import RegexLexer
from pygments.token import *

class DbufLexer(RegexLexer):
    name = "DependoBuf"
    aliases = ["dbuf"]
    filenames = ["*.dbuf"]

    tokens = {
        'root': [
            # Whitespace
            (r'\s+', Text),
            
            # Storage type keywords (message, enum)
            (r'\b(message|enum)\b', Keyword),
            
            # Types (capitalized words)
            (r'\b[A-Z]\w*\b', Name.Class),
            
            # Numeric constants
            (r'\b\d+u\b', Number),  # Unsigned integers
            (r'[+-]?\d+(\.\d+)?', Number),  # Signed integers and floats
            
            # Boolean constants
            (r'\b(true|false)\b', Keyword.Constant),
            
            # Arrow operator
            (r'=>', Operator),
            
            # Empty pattern (asterisk with lookahead)
            (r'\*(?=\s*,|\s*=>|\s*})', Keyword.Constant),
            
            # Variable/field access (dot notation)
            (r'\b[a-z]\w*(?:\.[a-z]\w*)*\b', Name.Variable),
            
            # Strings
            (r'"', String, 'string'),
            
            # Other punctuation
            (r'[{}[\](),;:]', Punctuation),
            
            # Operators
            (r'[=!<>]=?|[+\-*/%&|^]', Operator),
        ],
        
        'string': [
            # Escaped characters
            (r'\\.', String.Escape),
            # End of string
            (r'"', String, '#pop'),
            # All other characters in string
            (r'[^\\"]+', String),
        ],
    }

