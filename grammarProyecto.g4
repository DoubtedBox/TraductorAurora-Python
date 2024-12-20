grammar grammarProyecto;

// LEXER RULES Palabras clave Declaracion variables
CREAR: 'crear';
ENTERO: 'entero';
FLOTANTE: 'flotante';
CADENA: 'cadena';
BOOLEANO: 'booleano';

// Si (IF)
SI: 'si';
ENTONCES: 'entonces';
SINO: 'sino';

// Ciclos
PARA: 'para';
HASTA: 'hasta';
INCREMENTO: 'incremento';
DECREMENTO: 'decremento';
MIENTRAS: 'mientras';

// Declaracion de funciones
FUNCION: 'funcion';
RETORNAR: 'retornar';

INICIO: 'inicio';
FIN: 'fin';

// Manejo arreglos
ARREGLO: 'arreglo';
MATRIZ: 'matriz';

// Entradas y salidas
LEER: 'leer';
ESCRIBIR: 'escribir';

// Identificadores
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Literales
CONT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' (~["\r\n])* '"';

// Operadores
PLUS: '+';
MINUS: '-';
MULT: '*';
DIVI: '/';
EQUALS: '=';

// Símbolos de puntuación
LPAREN: '(';
RPAREN: ')';
COLON: ':';
COMMA: ',';
SEMICOLON: ';';
LBRACKET: '[';
RBRACKET: ']';

// Espacios en blanco y saltos de línea
WS: [ \n]+ -> skip;
INDENT: [\t]+;
NEWLINE: [\r\n]+;

// Comentarios
COMMENT: '//' ~[\r\n]* -> skip;

// Operadores de comparacion
IGUAL: '==';
DIFERENTE: '!=';
MAYOR: '>';
MENOR: '<';
MAYOR_IGUAL: '>=';
MENOR_IGUAL: '<=';

//Operadores logicos
AND: 'y';
OR: 'o';
NOT: 'no';

// Booleanos
VERDADERO: 'verdadero';
FALSO: 'falso';

// Parser rulerexpr Regla principal (program)
program: main_function (function)*;

main_function: INICIO COLON code_block FIN SEMICOLON;
function: function_declaration code_block return FIN SEMICOLON;
function_declaration: FUNCION ID LPAREN param_list RPAREN COLON;
return: RETORNAR return_value;
return_value: (expr SEMICOLON) | (ID SEMICOLON);

// Lista de parametros vacia o separada por comas
param_list: type (tensor_dimensions)* param (COMMA type (tensor_dimensions)* param)* |;
param: ID;

// Bloque de codigo
code_block: statement*;

// Tipos de datos
type: ENTERO | FLOTANTE | CADENA | BOOLEANO;

// Declaracion
statement: declaration | assignment | output | input | conditional | para_loop | mientras_loop | tensor_declaration;

declaration: CREAR type ID (EQUALS expr)? SEMICOLON;
assignment: ID EQUALS (expr | tensor_init) SEMICOLON;

// Condicional
conditional: SI boolean_expr ENTONCES COLON code_block  ((FIN SEMICOLON) | sino);
sino: (SINO COLON code_block FIN SEMICOLON);
boolean_expr: 
    expr comparation_operator expr 
    | LPAREN boolean_expr RPAREN
    | boolean_expr (AND | OR) boolean_expr
    | NOT boolean_expr;
// ciclo para
para_loop: PARA ID EQUALS CONT HASTA CONT direction COLON code_block FIN SEMICOLON;

direction: INCREMENTO | DECREMENTO;

// Ciclo mientras
mientras_loop: MIENTRAS boolean_expr COLON code_block FIN SEMICOLON;

// Expresiones: números, variables, y operaciones
expr: term ((PLUS | MINUS) term)*;

// Términos: productos y divisiones
term: factor ((MULT | DIVI) factor)*;

// Factores: constantes, identificadores y subexpresiones
factor: literal | function_call | LPAREN expr RPAREN | ID | tensor_acces;

// Llamada a una funcion
function_call: ID LPAREN arg_list RPAREN;

// Lista de argumentos (vacía o separada por comas)
arg_list: expr (COMMA expr)* |;

literal: CONT | FLOAT | STRING | VERDADERO | FALSO;
comparation_operator: IGUAL |DIFERENTE |
MAYOR |
MENOR |
MAYOR_IGUAL |
MENOR_IGUAL;

output: ESCRIBIR expr SEMICOLON;
input: LEER ID SEMICOLON;

// Declaración de tensor con dimensiones
tensor_declaration: CREAR type tensor_dimensions ID (EQUALS tensor_init)? SEMICOLON;

// Dimensiones del tensor (1 o más)
tensor_dimensions: (LBRACKET CONT? RBRACKET)+;

// Inicialización del tensor
tensor_init: LBRACKET literal (COMMA literal)* RBRACKET 
           | LBRACKET tensor_init (COMMA tensor_init)* RBRACKET;

tensor_acces: ID LBRACKET (CONT | FLOAT | ID) RBRACKET (LBRACKET (CONT | FLOAT | ID) RBRACKET)*;