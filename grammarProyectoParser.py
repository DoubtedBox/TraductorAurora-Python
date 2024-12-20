# Generated from grammarProyecto.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,52,331,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,5,0,67,
        8,0,10,0,12,0,70,9,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        3,5,99,8,5,1,6,1,6,5,6,103,8,6,10,6,12,6,106,9,6,1,6,1,6,1,6,1,6,
        5,6,112,8,6,10,6,12,6,115,9,6,1,6,1,6,5,6,119,8,6,10,6,12,6,122,
        9,6,1,6,3,6,125,8,6,1,7,1,7,1,8,5,8,130,8,8,10,8,12,8,133,9,8,1,
        9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,145,8,10,1,11,
        1,11,1,11,1,11,1,11,3,11,152,8,11,1,11,1,11,1,12,1,12,1,12,1,12,
        3,12,160,8,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        3,13,172,8,13,1,14,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,3,15,191,8,15,1,15,1,15,1,15,
        5,15,196,8,15,10,15,12,15,199,9,15,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,1,18,1,18,1,18,1,18,1,18,
        1,18,1,18,1,19,1,19,1,19,5,19,225,8,19,10,19,12,19,228,9,19,1,20,
        1,20,1,20,5,20,233,8,20,10,20,12,20,236,9,20,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,3,21,246,8,21,1,22,1,22,1,22,1,22,1,22,1,23,
        1,23,1,23,5,23,256,8,23,10,23,12,23,259,9,23,1,23,3,23,262,8,23,
        1,24,1,24,1,25,1,25,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,28,
        1,28,1,28,1,28,1,28,1,28,3,28,282,8,28,1,28,1,28,1,29,1,29,3,29,
        288,8,29,1,29,4,29,291,8,29,11,29,12,29,292,1,30,1,30,1,30,1,30,
        5,30,299,8,30,10,30,12,30,302,9,30,1,30,1,30,1,30,1,30,1,30,1,30,
        5,30,310,8,30,10,30,12,30,313,9,30,1,30,1,30,3,30,317,8,30,1,31,
        1,31,1,31,1,31,1,31,1,31,1,31,5,31,326,8,31,10,31,12,31,329,9,31,
        1,31,0,1,30,32,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,
        36,38,40,42,44,46,48,50,52,54,56,58,60,62,0,8,1,0,2,5,1,0,48,49,
        1,0,11,12,1,0,26,27,1,0,28,29,2,0,23,25,51,52,1,0,42,47,1,0,22,24,
        333,0,64,1,0,0,0,2,71,1,0,0,0,4,77,1,0,0,0,6,83,1,0,0,0,8,90,1,0,
        0,0,10,98,1,0,0,0,12,124,1,0,0,0,14,126,1,0,0,0,16,131,1,0,0,0,18,
        134,1,0,0,0,20,144,1,0,0,0,22,146,1,0,0,0,24,155,1,0,0,0,26,163,
        1,0,0,0,28,173,1,0,0,0,30,190,1,0,0,0,32,200,1,0,0,0,34,212,1,0,
        0,0,36,214,1,0,0,0,38,221,1,0,0,0,40,229,1,0,0,0,42,245,1,0,0,0,
        44,247,1,0,0,0,46,261,1,0,0,0,48,263,1,0,0,0,50,265,1,0,0,0,52,267,
        1,0,0,0,54,271,1,0,0,0,56,275,1,0,0,0,58,290,1,0,0,0,60,316,1,0,
        0,0,62,318,1,0,0,0,64,68,3,2,1,0,65,67,3,4,2,0,66,65,1,0,0,0,67,
        70,1,0,0,0,68,66,1,0,0,0,68,69,1,0,0,0,69,1,1,0,0,0,70,68,1,0,0,
        0,71,72,5,16,0,0,72,73,5,33,0,0,73,74,3,16,8,0,74,75,5,17,0,0,75,
        76,5,35,0,0,76,3,1,0,0,0,77,78,3,6,3,0,78,79,3,16,8,0,79,80,3,8,
        4,0,80,81,5,17,0,0,81,82,5,35,0,0,82,5,1,0,0,0,83,84,5,14,0,0,84,
        85,5,22,0,0,85,86,5,31,0,0,86,87,3,12,6,0,87,88,5,32,0,0,88,89,5,
        33,0,0,89,7,1,0,0,0,90,91,5,15,0,0,91,92,3,10,5,0,92,9,1,0,0,0,93,
        94,3,38,19,0,94,95,5,35,0,0,95,99,1,0,0,0,96,97,5,22,0,0,97,99,5,
        35,0,0,98,93,1,0,0,0,98,96,1,0,0,0,99,11,1,0,0,0,100,104,3,18,9,
        0,101,103,3,58,29,0,102,101,1,0,0,0,103,106,1,0,0,0,104,102,1,0,
        0,0,104,105,1,0,0,0,105,107,1,0,0,0,106,104,1,0,0,0,107,120,3,14,
        7,0,108,109,5,34,0,0,109,113,3,18,9,0,110,112,3,58,29,0,111,110,
        1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,116,
        1,0,0,0,115,113,1,0,0,0,116,117,3,14,7,0,117,119,1,0,0,0,118,108,
        1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,125,
        1,0,0,0,122,120,1,0,0,0,123,125,1,0,0,0,124,100,1,0,0,0,124,123,
        1,0,0,0,125,13,1,0,0,0,126,127,5,22,0,0,127,15,1,0,0,0,128,130,3,
        20,10,0,129,128,1,0,0,0,130,133,1,0,0,0,131,129,1,0,0,0,131,132,
        1,0,0,0,132,17,1,0,0,0,133,131,1,0,0,0,134,135,7,0,0,0,135,19,1,
        0,0,0,136,145,3,22,11,0,137,145,3,24,12,0,138,145,3,52,26,0,139,
        145,3,54,27,0,140,145,3,26,13,0,141,145,3,32,16,0,142,145,3,36,18,
        0,143,145,3,56,28,0,144,136,1,0,0,0,144,137,1,0,0,0,144,138,1,0,
        0,0,144,139,1,0,0,0,144,140,1,0,0,0,144,141,1,0,0,0,144,142,1,0,
        0,0,144,143,1,0,0,0,145,21,1,0,0,0,146,147,5,1,0,0,147,148,3,18,
        9,0,148,151,5,22,0,0,149,150,5,30,0,0,150,152,3,38,19,0,151,149,
        1,0,0,0,151,152,1,0,0,0,152,153,1,0,0,0,153,154,5,35,0,0,154,23,
        1,0,0,0,155,156,5,22,0,0,156,159,5,30,0,0,157,160,3,38,19,0,158,
        160,3,60,30,0,159,157,1,0,0,0,159,158,1,0,0,0,160,161,1,0,0,0,161,
        162,5,35,0,0,162,25,1,0,0,0,163,164,5,6,0,0,164,165,3,30,15,0,165,
        166,5,7,0,0,166,167,5,33,0,0,167,171,3,16,8,0,168,169,5,17,0,0,169,
        172,5,35,0,0,170,172,3,28,14,0,171,168,1,0,0,0,171,170,1,0,0,0,172,
        27,1,0,0,0,173,174,5,8,0,0,174,175,5,33,0,0,175,176,3,16,8,0,176,
        177,5,17,0,0,177,178,5,35,0,0,178,29,1,0,0,0,179,180,6,15,-1,0,180,
        181,3,38,19,0,181,182,3,50,25,0,182,183,3,38,19,0,183,191,1,0,0,
        0,184,185,5,31,0,0,185,186,3,30,15,0,186,187,5,32,0,0,187,191,1,
        0,0,0,188,189,5,50,0,0,189,191,3,30,15,1,190,179,1,0,0,0,190,184,
        1,0,0,0,190,188,1,0,0,0,191,197,1,0,0,0,192,193,10,2,0,0,193,194,
        7,1,0,0,194,196,3,30,15,3,195,192,1,0,0,0,196,199,1,0,0,0,197,195,
        1,0,0,0,197,198,1,0,0,0,198,31,1,0,0,0,199,197,1,0,0,0,200,201,5,
        9,0,0,201,202,5,22,0,0,202,203,5,30,0,0,203,204,5,23,0,0,204,205,
        5,10,0,0,205,206,5,23,0,0,206,207,3,34,17,0,207,208,5,33,0,0,208,
        209,3,16,8,0,209,210,5,17,0,0,210,211,5,35,0,0,211,33,1,0,0,0,212,
        213,7,2,0,0,213,35,1,0,0,0,214,215,5,13,0,0,215,216,3,30,15,0,216,
        217,5,33,0,0,217,218,3,16,8,0,218,219,5,17,0,0,219,220,5,35,0,0,
        220,37,1,0,0,0,221,226,3,40,20,0,222,223,7,3,0,0,223,225,3,40,20,
        0,224,222,1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,226,227,1,0,0,
        0,227,39,1,0,0,0,228,226,1,0,0,0,229,234,3,42,21,0,230,231,7,4,0,
        0,231,233,3,42,21,0,232,230,1,0,0,0,233,236,1,0,0,0,234,232,1,0,
        0,0,234,235,1,0,0,0,235,41,1,0,0,0,236,234,1,0,0,0,237,246,3,48,
        24,0,238,246,3,44,22,0,239,240,5,31,0,0,240,241,3,38,19,0,241,242,
        5,32,0,0,242,246,1,0,0,0,243,246,5,22,0,0,244,246,3,62,31,0,245,
        237,1,0,0,0,245,238,1,0,0,0,245,239,1,0,0,0,245,243,1,0,0,0,245,
        244,1,0,0,0,246,43,1,0,0,0,247,248,5,22,0,0,248,249,5,31,0,0,249,
        250,3,46,23,0,250,251,5,32,0,0,251,45,1,0,0,0,252,257,3,38,19,0,
        253,254,5,34,0,0,254,256,3,38,19,0,255,253,1,0,0,0,256,259,1,0,0,
        0,257,255,1,0,0,0,257,258,1,0,0,0,258,262,1,0,0,0,259,257,1,0,0,
        0,260,262,1,0,0,0,261,252,1,0,0,0,261,260,1,0,0,0,262,47,1,0,0,0,
        263,264,7,5,0,0,264,49,1,0,0,0,265,266,7,6,0,0,266,51,1,0,0,0,267,
        268,5,21,0,0,268,269,3,38,19,0,269,270,5,35,0,0,270,53,1,0,0,0,271,
        272,5,20,0,0,272,273,5,22,0,0,273,274,5,35,0,0,274,55,1,0,0,0,275,
        276,5,1,0,0,276,277,3,18,9,0,277,278,3,58,29,0,278,281,5,22,0,0,
        279,280,5,30,0,0,280,282,3,60,30,0,281,279,1,0,0,0,281,282,1,0,0,
        0,282,283,1,0,0,0,283,284,5,35,0,0,284,57,1,0,0,0,285,287,5,36,0,
        0,286,288,5,23,0,0,287,286,1,0,0,0,287,288,1,0,0,0,288,289,1,0,0,
        0,289,291,5,37,0,0,290,285,1,0,0,0,291,292,1,0,0,0,292,290,1,0,0,
        0,292,293,1,0,0,0,293,59,1,0,0,0,294,295,5,36,0,0,295,300,3,48,24,
        0,296,297,5,34,0,0,297,299,3,48,24,0,298,296,1,0,0,0,299,302,1,0,
        0,0,300,298,1,0,0,0,300,301,1,0,0,0,301,303,1,0,0,0,302,300,1,0,
        0,0,303,304,5,37,0,0,304,317,1,0,0,0,305,306,5,36,0,0,306,311,3,
        60,30,0,307,308,5,34,0,0,308,310,3,60,30,0,309,307,1,0,0,0,310,313,
        1,0,0,0,311,309,1,0,0,0,311,312,1,0,0,0,312,314,1,0,0,0,313,311,
        1,0,0,0,314,315,5,37,0,0,315,317,1,0,0,0,316,294,1,0,0,0,316,305,
        1,0,0,0,317,61,1,0,0,0,318,319,5,22,0,0,319,320,5,36,0,0,320,321,
        7,7,0,0,321,327,5,37,0,0,322,323,5,36,0,0,323,324,7,7,0,0,324,326,
        5,37,0,0,325,322,1,0,0,0,326,329,1,0,0,0,327,325,1,0,0,0,327,328,
        1,0,0,0,328,63,1,0,0,0,329,327,1,0,0,0,25,68,98,104,113,120,124,
        131,144,151,159,171,190,197,226,234,245,257,261,281,287,292,300,
        311,316,327
    ]

class grammarProyectoParser ( Parser ):

    grammarFileName = "grammarProyecto.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'crear'", "'entero'", "'flotante'", "'cadena'", 
                     "'booleano'", "'si'", "'entonces'", "'sino'", "'para'", 
                     "'hasta'", "'incremento'", "'decremento'", "'mientras'", 
                     "'funcion'", "'retornar'", "'inicio'", "'fin'", "'arreglo'", 
                     "'matriz'", "'leer'", "'escribir'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'+'", "'-'", "'*'", "'/'", 
                     "'='", "'('", "')'", "':'", "','", "';'", "'['", "']'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'y'", 
                     "'o'", "'no'", "'verdadero'", "'falso'" ]

    symbolicNames = [ "<INVALID>", "CREAR", "ENTERO", "FLOTANTE", "CADENA", 
                      "BOOLEANO", "SI", "ENTONCES", "SINO", "PARA", "HASTA", 
                      "INCREMENTO", "DECREMENTO", "MIENTRAS", "FUNCION", 
                      "RETORNAR", "INICIO", "FIN", "ARREGLO", "MATRIZ", 
                      "LEER", "ESCRIBIR", "ID", "CONT", "FLOAT", "STRING", 
                      "PLUS", "MINUS", "MULT", "DIVI", "EQUALS", "LPAREN", 
                      "RPAREN", "COLON", "COMMA", "SEMICOLON", "LBRACKET", 
                      "RBRACKET", "WS", "INDENT", "NEWLINE", "COMMENT", 
                      "IGUAL", "DIFERENTE", "MAYOR", "MENOR", "MAYOR_IGUAL", 
                      "MENOR_IGUAL", "AND", "OR", "NOT", "VERDADERO", "FALSO" ]

    RULE_program = 0
    RULE_main_function = 1
    RULE_function = 2
    RULE_function_declaration = 3
    RULE_return = 4
    RULE_return_value = 5
    RULE_param_list = 6
    RULE_param = 7
    RULE_code_block = 8
    RULE_type = 9
    RULE_statement = 10
    RULE_declaration = 11
    RULE_assignment = 12
    RULE_conditional = 13
    RULE_sino = 14
    RULE_boolean_expr = 15
    RULE_para_loop = 16
    RULE_direction = 17
    RULE_mientras_loop = 18
    RULE_expr = 19
    RULE_term = 20
    RULE_factor = 21
    RULE_function_call = 22
    RULE_arg_list = 23
    RULE_literal = 24
    RULE_comparation_operator = 25
    RULE_output = 26
    RULE_input = 27
    RULE_tensor_declaration = 28
    RULE_tensor_dimensions = 29
    RULE_tensor_init = 30
    RULE_tensor_acces = 31

    ruleNames =  [ "program", "main_function", "function", "function_declaration", 
                   "return", "return_value", "param_list", "param", "code_block", 
                   "type", "statement", "declaration", "assignment", "conditional", 
                   "sino", "boolean_expr", "para_loop", "direction", "mientras_loop", 
                   "expr", "term", "factor", "function_call", "arg_list", 
                   "literal", "comparation_operator", "output", "input", 
                   "tensor_declaration", "tensor_dimensions", "tensor_init", 
                   "tensor_acces" ]

    EOF = Token.EOF
    CREAR=1
    ENTERO=2
    FLOTANTE=3
    CADENA=4
    BOOLEANO=5
    SI=6
    ENTONCES=7
    SINO=8
    PARA=9
    HASTA=10
    INCREMENTO=11
    DECREMENTO=12
    MIENTRAS=13
    FUNCION=14
    RETORNAR=15
    INICIO=16
    FIN=17
    ARREGLO=18
    MATRIZ=19
    LEER=20
    ESCRIBIR=21
    ID=22
    CONT=23
    FLOAT=24
    STRING=25
    PLUS=26
    MINUS=27
    MULT=28
    DIVI=29
    EQUALS=30
    LPAREN=31
    RPAREN=32
    COLON=33
    COMMA=34
    SEMICOLON=35
    LBRACKET=36
    RBRACKET=37
    WS=38
    INDENT=39
    NEWLINE=40
    COMMENT=41
    IGUAL=42
    DIFERENTE=43
    MAYOR=44
    MENOR=45
    MAYOR_IGUAL=46
    MENOR_IGUAL=47
    AND=48
    OR=49
    NOT=50
    VERDADERO=51
    FALSO=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def main_function(self):
            return self.getTypedRuleContext(grammarProyectoParser.Main_functionContext,0)


        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarProyectoParser.FunctionContext)
            else:
                return self.getTypedRuleContext(grammarProyectoParser.FunctionContext,i)


        def getRuleIndex(self):
            return grammarProyectoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = grammarProyectoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.main_function()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==14:
                self.state = 65
                self.function()
                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INICIO(self):
            return self.getToken(grammarProyectoParser.INICIO, 0)

        def COLON(self):
            return self.getToken(grammarProyectoParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(grammarProyectoParser.Code_blockContext,0)


        def FIN(self):
            return self.getToken(grammarProyectoParser.FIN, 0)

        def SEMICOLON(self):
            return self.getToken(grammarProyectoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_main_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain_function" ):
                listener.enterMain_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain_function" ):
                listener.exitMain_function(self)




    def main_function(self):

        localctx = grammarProyectoParser.Main_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(grammarProyectoParser.INICIO)
            self.state = 72
            self.match(grammarProyectoParser.COLON)
            self.state = 73
            self.code_block()
            self.state = 74
            self.match(grammarProyectoParser.FIN)
            self.state = 75
            self.match(grammarProyectoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_declaration(self):
            return self.getTypedRuleContext(grammarProyectoParser.Function_declarationContext,0)


        def code_block(self):
            return self.getTypedRuleContext(grammarProyectoParser.Code_blockContext,0)


        def return_(self):
            return self.getTypedRuleContext(grammarProyectoParser.ReturnContext,0)


        def FIN(self):
            return self.getToken(grammarProyectoParser.FIN, 0)

        def SEMICOLON(self):
            return self.getToken(grammarProyectoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)




    def function(self):

        localctx = grammarProyectoParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.function_declaration()
            self.state = 78
            self.code_block()
            self.state = 79
            self.return_()
            self.state = 80
            self.match(grammarProyectoParser.FIN)
            self.state = 81
            self.match(grammarProyectoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(grammarProyectoParser.FUNCION, 0)

        def ID(self):
            return self.getToken(grammarProyectoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(grammarProyectoParser.LPAREN, 0)

        def param_list(self):
            return self.getTypedRuleContext(grammarProyectoParser.Param_listContext,0)


        def RPAREN(self):
            return self.getToken(grammarProyectoParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(grammarProyectoParser.COLON, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_function_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_declaration" ):
                listener.enterFunction_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_declaration" ):
                listener.exitFunction_declaration(self)




    def function_declaration(self):

        localctx = grammarProyectoParser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(grammarProyectoParser.FUNCION)
            self.state = 84
            self.match(grammarProyectoParser.ID)
            self.state = 85
            self.match(grammarProyectoParser.LPAREN)
            self.state = 86
            self.param_list()
            self.state = 87
            self.match(grammarProyectoParser.RPAREN)
            self.state = 88
            self.match(grammarProyectoParser.COLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETORNAR(self):
            return self.getToken(grammarProyectoParser.RETORNAR, 0)

        def return_value(self):
            return self.getTypedRuleContext(grammarProyectoParser.Return_valueContext,0)


        def getRuleIndex(self):
            return grammarProyectoParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)




    def return_(self):

        localctx = grammarProyectoParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(grammarProyectoParser.RETORNAR)
            self.state = 91
            self.return_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(grammarProyectoParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(grammarProyectoParser.SEMICOLON, 0)

        def ID(self):
            return self.getToken(grammarProyectoParser.ID, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_return_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_value" ):
                listener.enterReturn_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_value" ):
                listener.exitReturn_value(self)




    def return_value(self):

        localctx = grammarProyectoParser.Return_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_return_value)
        try:
            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 93
                self.expr()
                self.state = 94
                self.match(grammarProyectoParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.match(grammarProyectoParser.ID)
                self.state = 97
                self.match(grammarProyectoParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarProyectoParser.TypeContext)
            else:
                return self.getTypedRuleContext(grammarProyectoParser.TypeContext,i)


        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarProyectoParser.ParamContext)
            else:
                return self.getTypedRuleContext(grammarProyectoParser.ParamContext,i)


        def tensor_dimensions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarProyectoParser.Tensor_dimensionsContext)
            else:
                return self.getTypedRuleContext(grammarProyectoParser.Tensor_dimensionsContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarProyectoParser.COMMA)
            else:
                return self.getToken(grammarProyectoParser.COMMA, i)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_param_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_list" ):
                listener.enterParam_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_list" ):
                listener.exitParam_list(self)




    def param_list(self):

        localctx = grammarProyectoParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.state = 124
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2, 3, 4, 5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.type_()
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==36:
                    self.state = 101
                    self.tensor_dimensions()
                    self.state = 106
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 107
                self.param()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 108
                    self.match(grammarProyectoParser.COMMA)
                    self.state = 109
                    self.type_()
                    self.state = 113
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==36:
                        self.state = 110
                        self.tensor_dimensions()
                        self.state = 115
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 116
                    self.param()
                    self.state = 122
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(grammarProyectoParser.ID, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = grammarProyectoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(grammarProyectoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarProyectoParser.StatementContext)
            else:
                return self.getTypedRuleContext(grammarProyectoParser.StatementContext,i)


        def getRuleIndex(self):
            return grammarProyectoParser.RULE_code_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_block" ):
                listener.enterCode_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_block" ):
                listener.exitCode_block(self)




    def code_block(self):

        localctx = grammarProyectoParser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_code_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7348802) != 0):
                self.state = 128
                self.statement()
                self.state = 133
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTERO(self):
            return self.getToken(grammarProyectoParser.ENTERO, 0)

        def FLOTANTE(self):
            return self.getToken(grammarProyectoParser.FLOTANTE, 0)

        def CADENA(self):
            return self.getToken(grammarProyectoParser.CADENA, 0)

        def BOOLEANO(self):
            return self.getToken(grammarProyectoParser.BOOLEANO, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = grammarProyectoParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 60) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(grammarProyectoParser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(grammarProyectoParser.AssignmentContext,0)


        def output(self):
            return self.getTypedRuleContext(grammarProyectoParser.OutputContext,0)


        def input_(self):
            return self.getTypedRuleContext(grammarProyectoParser.InputContext,0)


        def conditional(self):
            return self.getTypedRuleContext(grammarProyectoParser.ConditionalContext,0)


        def para_loop(self):
            return self.getTypedRuleContext(grammarProyectoParser.Para_loopContext,0)


        def mientras_loop(self):
            return self.getTypedRuleContext(grammarProyectoParser.Mientras_loopContext,0)


        def tensor_declaration(self):
            return self.getTypedRuleContext(grammarProyectoParser.Tensor_declarationContext,0)


        def getRuleIndex(self):
            return grammarProyectoParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = grammarProyectoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_statement)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 137
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 138
                self.output()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 139
                self.input_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 140
                self.conditional()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 141
                self.para_loop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 142
                self.mientras_loop()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 143
                self.tensor_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREAR(self):
            return self.getToken(grammarProyectoParser.CREAR, 0)

        def type_(self):
            return self.getTypedRuleContext(grammarProyectoParser.TypeContext,0)


        def ID(self):
            return self.getToken(grammarProyectoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(grammarProyectoParser.SEMICOLON, 0)

        def EQUALS(self):
            return self.getToken(grammarProyectoParser.EQUALS, 0)

        def expr(self):
            return self.getTypedRuleContext(grammarProyectoParser.ExprContext,0)


        def getRuleIndex(self):
            return grammarProyectoParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = grammarProyectoParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(grammarProyectoParser.CREAR)
            self.state = 147
            self.type_()
            self.state = 148
            self.match(grammarProyectoParser.ID)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 149
                self.match(grammarProyectoParser.EQUALS)
                self.state = 150
                self.expr()


            self.state = 153
            self.match(grammarProyectoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(grammarProyectoParser.ID, 0)

        def EQUALS(self):
            return self.getToken(grammarProyectoParser.EQUALS, 0)

        def SEMICOLON(self):
            return self.getToken(grammarProyectoParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(grammarProyectoParser.ExprContext,0)


        def tensor_init(self):
            return self.getTypedRuleContext(grammarProyectoParser.Tensor_initContext,0)


        def getRuleIndex(self):
            return grammarProyectoParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = grammarProyectoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(grammarProyectoParser.ID)
            self.state = 156
            self.match(grammarProyectoParser.EQUALS)
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 24, 25, 31, 51, 52]:
                self.state = 157
                self.expr()
                pass
            elif token in [36]:
                self.state = 158
                self.tensor_init()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 161
            self.match(grammarProyectoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(grammarProyectoParser.SI, 0)

        def boolean_expr(self):
            return self.getTypedRuleContext(grammarProyectoParser.Boolean_exprContext,0)


        def ENTONCES(self):
            return self.getToken(grammarProyectoParser.ENTONCES, 0)

        def COLON(self):
            return self.getToken(grammarProyectoParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(grammarProyectoParser.Code_blockContext,0)


        def sino(self):
            return self.getTypedRuleContext(grammarProyectoParser.SinoContext,0)


        def FIN(self):
            return self.getToken(grammarProyectoParser.FIN, 0)

        def SEMICOLON(self):
            return self.getToken(grammarProyectoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_conditional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional" ):
                listener.enterConditional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional" ):
                listener.exitConditional(self)




    def conditional(self):

        localctx = grammarProyectoParser.ConditionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_conditional)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(grammarProyectoParser.SI)
            self.state = 164
            self.boolean_expr(0)
            self.state = 165
            self.match(grammarProyectoParser.ENTONCES)
            self.state = 166
            self.match(grammarProyectoParser.COLON)
            self.state = 167
            self.code_block()
            self.state = 171
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.state = 168
                self.match(grammarProyectoParser.FIN)
                self.state = 169
                self.match(grammarProyectoParser.SEMICOLON)
                pass
            elif token in [8]:
                self.state = 170
                self.sino()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SinoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINO(self):
            return self.getToken(grammarProyectoParser.SINO, 0)

        def COLON(self):
            return self.getToken(grammarProyectoParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(grammarProyectoParser.Code_blockContext,0)


        def FIN(self):
            return self.getToken(grammarProyectoParser.FIN, 0)

        def SEMICOLON(self):
            return self.getToken(grammarProyectoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_sino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSino" ):
                listener.enterSino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSino" ):
                listener.exitSino(self)




    def sino(self):

        localctx = grammarProyectoParser.SinoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_sino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(grammarProyectoParser.SINO)
            self.state = 174
            self.match(grammarProyectoParser.COLON)
            self.state = 175
            self.code_block()
            self.state = 176
            self.match(grammarProyectoParser.FIN)
            self.state = 177
            self.match(grammarProyectoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Boolean_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarProyectoParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarProyectoParser.ExprContext,i)


        def comparation_operator(self):
            return self.getTypedRuleContext(grammarProyectoParser.Comparation_operatorContext,0)


        def LPAREN(self):
            return self.getToken(grammarProyectoParser.LPAREN, 0)

        def boolean_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarProyectoParser.Boolean_exprContext)
            else:
                return self.getTypedRuleContext(grammarProyectoParser.Boolean_exprContext,i)


        def RPAREN(self):
            return self.getToken(grammarProyectoParser.RPAREN, 0)

        def NOT(self):
            return self.getToken(grammarProyectoParser.NOT, 0)

        def AND(self):
            return self.getToken(grammarProyectoParser.AND, 0)

        def OR(self):
            return self.getToken(grammarProyectoParser.OR, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_boolean_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolean_expr" ):
                listener.enterBoolean_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolean_expr" ):
                listener.exitBoolean_expr(self)



    def boolean_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = grammarProyectoParser.Boolean_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_boolean_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 180
                self.expr()
                self.state = 181
                self.comparation_operator()
                self.state = 182
                self.expr()
                pass

            elif la_ == 2:
                self.state = 184
                self.match(grammarProyectoParser.LPAREN)
                self.state = 185
                self.boolean_expr(0)
                self.state = 186
                self.match(grammarProyectoParser.RPAREN)
                pass

            elif la_ == 3:
                self.state = 188
                self.match(grammarProyectoParser.NOT)
                self.state = 189
                self.boolean_expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = grammarProyectoParser.Boolean_exprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_expr)
                    self.state = 192
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 193
                    _la = self._input.LA(1)
                    if not(_la==48 or _la==49):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 194
                    self.boolean_expr(3) 
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Para_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARA(self):
            return self.getToken(grammarProyectoParser.PARA, 0)

        def ID(self):
            return self.getToken(grammarProyectoParser.ID, 0)

        def EQUALS(self):
            return self.getToken(grammarProyectoParser.EQUALS, 0)

        def CONT(self, i:int=None):
            if i is None:
                return self.getTokens(grammarProyectoParser.CONT)
            else:
                return self.getToken(grammarProyectoParser.CONT, i)

        def HASTA(self):
            return self.getToken(grammarProyectoParser.HASTA, 0)

        def direction(self):
            return self.getTypedRuleContext(grammarProyectoParser.DirectionContext,0)


        def COLON(self):
            return self.getToken(grammarProyectoParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(grammarProyectoParser.Code_blockContext,0)


        def FIN(self):
            return self.getToken(grammarProyectoParser.FIN, 0)

        def SEMICOLON(self):
            return self.getToken(grammarProyectoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_para_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPara_loop" ):
                listener.enterPara_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPara_loop" ):
                listener.exitPara_loop(self)




    def para_loop(self):

        localctx = grammarProyectoParser.Para_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_para_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(grammarProyectoParser.PARA)
            self.state = 201
            self.match(grammarProyectoParser.ID)
            self.state = 202
            self.match(grammarProyectoParser.EQUALS)
            self.state = 203
            self.match(grammarProyectoParser.CONT)
            self.state = 204
            self.match(grammarProyectoParser.HASTA)
            self.state = 205
            self.match(grammarProyectoParser.CONT)
            self.state = 206
            self.direction()
            self.state = 207
            self.match(grammarProyectoParser.COLON)
            self.state = 208
            self.code_block()
            self.state = 209
            self.match(grammarProyectoParser.FIN)
            self.state = 210
            self.match(grammarProyectoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DirectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INCREMENTO(self):
            return self.getToken(grammarProyectoParser.INCREMENTO, 0)

        def DECREMENTO(self):
            return self.getToken(grammarProyectoParser.DECREMENTO, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_direction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDirection" ):
                listener.enterDirection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDirection" ):
                listener.exitDirection(self)




    def direction(self):

        localctx = grammarProyectoParser.DirectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_direction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            _la = self._input.LA(1)
            if not(_la==11 or _la==12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mientras_loopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(grammarProyectoParser.MIENTRAS, 0)

        def boolean_expr(self):
            return self.getTypedRuleContext(grammarProyectoParser.Boolean_exprContext,0)


        def COLON(self):
            return self.getToken(grammarProyectoParser.COLON, 0)

        def code_block(self):
            return self.getTypedRuleContext(grammarProyectoParser.Code_blockContext,0)


        def FIN(self):
            return self.getToken(grammarProyectoParser.FIN, 0)

        def SEMICOLON(self):
            return self.getToken(grammarProyectoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_mientras_loop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMientras_loop" ):
                listener.enterMientras_loop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMientras_loop" ):
                listener.exitMientras_loop(self)




    def mientras_loop(self):

        localctx = grammarProyectoParser.Mientras_loopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_mientras_loop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(grammarProyectoParser.MIENTRAS)
            self.state = 215
            self.boolean_expr(0)
            self.state = 216
            self.match(grammarProyectoParser.COLON)
            self.state = 217
            self.code_block()
            self.state = 218
            self.match(grammarProyectoParser.FIN)
            self.state = 219
            self.match(grammarProyectoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarProyectoParser.TermContext)
            else:
                return self.getTypedRuleContext(grammarProyectoParser.TermContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(grammarProyectoParser.PLUS)
            else:
                return self.getToken(grammarProyectoParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(grammarProyectoParser.MINUS)
            else:
                return self.getToken(grammarProyectoParser.MINUS, i)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = grammarProyectoParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.term()
            self.state = 226
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 222
                    _la = self._input.LA(1)
                    if not(_la==26 or _la==27):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 223
                    self.term() 
                self.state = 228
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarProyectoParser.FactorContext)
            else:
                return self.getTypedRuleContext(grammarProyectoParser.FactorContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(grammarProyectoParser.MULT)
            else:
                return self.getToken(grammarProyectoParser.MULT, i)

        def DIVI(self, i:int=None):
            if i is None:
                return self.getTokens(grammarProyectoParser.DIVI)
            else:
                return self.getToken(grammarProyectoParser.DIVI, i)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = grammarProyectoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.factor()
            self.state = 234
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 230
                    _la = self._input.LA(1)
                    if not(_la==28 or _la==29):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 231
                    self.factor() 
                self.state = 236
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(grammarProyectoParser.LiteralContext,0)


        def function_call(self):
            return self.getTypedRuleContext(grammarProyectoParser.Function_callContext,0)


        def LPAREN(self):
            return self.getToken(grammarProyectoParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(grammarProyectoParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(grammarProyectoParser.RPAREN, 0)

        def ID(self):
            return self.getToken(grammarProyectoParser.ID, 0)

        def tensor_acces(self):
            return self.getTypedRuleContext(grammarProyectoParser.Tensor_accesContext,0)


        def getRuleIndex(self):
            return grammarProyectoParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)




    def factor(self):

        localctx = grammarProyectoParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_factor)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.function_call()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.match(grammarProyectoParser.LPAREN)
                self.state = 240
                self.expr()
                self.state = 241
                self.match(grammarProyectoParser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 243
                self.match(grammarProyectoParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 244
                self.tensor_acces()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(grammarProyectoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(grammarProyectoParser.LPAREN, 0)

        def arg_list(self):
            return self.getTypedRuleContext(grammarProyectoParser.Arg_listContext,0)


        def RPAREN(self):
            return self.getToken(grammarProyectoParser.RPAREN, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)




    def function_call(self):

        localctx = grammarProyectoParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_function_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(grammarProyectoParser.ID)
            self.state = 248
            self.match(grammarProyectoParser.LPAREN)
            self.state = 249
            self.arg_list()
            self.state = 250
            self.match(grammarProyectoParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arg_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarProyectoParser.ExprContext)
            else:
                return self.getTypedRuleContext(grammarProyectoParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarProyectoParser.COMMA)
            else:
                return self.getToken(grammarProyectoParser.COMMA, i)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_arg_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArg_list" ):
                listener.enterArg_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArg_list" ):
                listener.exitArg_list(self)




    def arg_list(self):

        localctx = grammarProyectoParser.Arg_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arg_list)
        self._la = 0 # Token type
        try:
            self.state = 261
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22, 23, 24, 25, 31, 51, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.expr()
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 253
                    self.match(grammarProyectoParser.COMMA)
                    self.state = 254
                    self.expr()
                    self.state = 259
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONT(self):
            return self.getToken(grammarProyectoParser.CONT, 0)

        def FLOAT(self):
            return self.getToken(grammarProyectoParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(grammarProyectoParser.STRING, 0)

        def VERDADERO(self):
            return self.getToken(grammarProyectoParser.VERDADERO, 0)

        def FALSO(self):
            return self.getToken(grammarProyectoParser.FALSO, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = grammarProyectoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 263
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6755399499776000) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparation_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IGUAL(self):
            return self.getToken(grammarProyectoParser.IGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(grammarProyectoParser.DIFERENTE, 0)

        def MAYOR(self):
            return self.getToken(grammarProyectoParser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(grammarProyectoParser.MENOR, 0)

        def MAYOR_IGUAL(self):
            return self.getToken(grammarProyectoParser.MAYOR_IGUAL, 0)

        def MENOR_IGUAL(self):
            return self.getToken(grammarProyectoParser.MENOR_IGUAL, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_comparation_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparation_operator" ):
                listener.enterComparation_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparation_operator" ):
                listener.exitComparation_operator(self)




    def comparation_operator(self):

        localctx = grammarProyectoParser.Comparation_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_comparation_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 277076930199552) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OutputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ESCRIBIR(self):
            return self.getToken(grammarProyectoParser.ESCRIBIR, 0)

        def expr(self):
            return self.getTypedRuleContext(grammarProyectoParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(grammarProyectoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)




    def output(self):

        localctx = grammarProyectoParser.OutputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_output)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(grammarProyectoParser.ESCRIBIR)
            self.state = 268
            self.expr()
            self.state = 269
            self.match(grammarProyectoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEER(self):
            return self.getToken(grammarProyectoParser.LEER, 0)

        def ID(self):
            return self.getToken(grammarProyectoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(grammarProyectoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)




    def input_(self):

        localctx = grammarProyectoParser.InputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_input)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(grammarProyectoParser.LEER)
            self.state = 272
            self.match(grammarProyectoParser.ID)
            self.state = 273
            self.match(grammarProyectoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tensor_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREAR(self):
            return self.getToken(grammarProyectoParser.CREAR, 0)

        def type_(self):
            return self.getTypedRuleContext(grammarProyectoParser.TypeContext,0)


        def tensor_dimensions(self):
            return self.getTypedRuleContext(grammarProyectoParser.Tensor_dimensionsContext,0)


        def ID(self):
            return self.getToken(grammarProyectoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(grammarProyectoParser.SEMICOLON, 0)

        def EQUALS(self):
            return self.getToken(grammarProyectoParser.EQUALS, 0)

        def tensor_init(self):
            return self.getTypedRuleContext(grammarProyectoParser.Tensor_initContext,0)


        def getRuleIndex(self):
            return grammarProyectoParser.RULE_tensor_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTensor_declaration" ):
                listener.enterTensor_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTensor_declaration" ):
                listener.exitTensor_declaration(self)




    def tensor_declaration(self):

        localctx = grammarProyectoParser.Tensor_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_tensor_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(grammarProyectoParser.CREAR)
            self.state = 276
            self.type_()
            self.state = 277
            self.tensor_dimensions()
            self.state = 278
            self.match(grammarProyectoParser.ID)
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 279
                self.match(grammarProyectoParser.EQUALS)
                self.state = 280
                self.tensor_init()


            self.state = 283
            self.match(grammarProyectoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tensor_dimensionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(grammarProyectoParser.LBRACKET)
            else:
                return self.getToken(grammarProyectoParser.LBRACKET, i)

        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(grammarProyectoParser.RBRACKET)
            else:
                return self.getToken(grammarProyectoParser.RBRACKET, i)

        def CONT(self, i:int=None):
            if i is None:
                return self.getTokens(grammarProyectoParser.CONT)
            else:
                return self.getToken(grammarProyectoParser.CONT, i)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_tensor_dimensions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTensor_dimensions" ):
                listener.enterTensor_dimensions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTensor_dimensions" ):
                listener.exitTensor_dimensions(self)




    def tensor_dimensions(self):

        localctx = grammarProyectoParser.Tensor_dimensionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_tensor_dimensions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 285
                    self.match(grammarProyectoParser.LBRACKET)
                    self.state = 287
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==23:
                        self.state = 286
                        self.match(grammarProyectoParser.CONT)


                    self.state = 289
                    self.match(grammarProyectoParser.RBRACKET)

                else:
                    raise NoViableAltException(self)
                self.state = 292 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tensor_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(grammarProyectoParser.LBRACKET, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarProyectoParser.LiteralContext)
            else:
                return self.getTypedRuleContext(grammarProyectoParser.LiteralContext,i)


        def RBRACKET(self):
            return self.getToken(grammarProyectoParser.RBRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(grammarProyectoParser.COMMA)
            else:
                return self.getToken(grammarProyectoParser.COMMA, i)

        def tensor_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(grammarProyectoParser.Tensor_initContext)
            else:
                return self.getTypedRuleContext(grammarProyectoParser.Tensor_initContext,i)


        def getRuleIndex(self):
            return grammarProyectoParser.RULE_tensor_init

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTensor_init" ):
                listener.enterTensor_init(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTensor_init" ):
                listener.exitTensor_init(self)




    def tensor_init(self):

        localctx = grammarProyectoParser.Tensor_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_tensor_init)
        self._la = 0 # Token type
        try:
            self.state = 316
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(grammarProyectoParser.LBRACKET)
                self.state = 295
                self.literal()
                self.state = 300
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 296
                    self.match(grammarProyectoParser.COMMA)
                    self.state = 297
                    self.literal()
                    self.state = 302
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 303
                self.match(grammarProyectoParser.RBRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.match(grammarProyectoParser.LBRACKET)
                self.state = 306
                self.tensor_init()
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==34:
                    self.state = 307
                    self.match(grammarProyectoParser.COMMA)
                    self.state = 308
                    self.tensor_init()
                    self.state = 313
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 314
                self.match(grammarProyectoParser.RBRACKET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tensor_accesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(grammarProyectoParser.ID)
            else:
                return self.getToken(grammarProyectoParser.ID, i)

        def LBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(grammarProyectoParser.LBRACKET)
            else:
                return self.getToken(grammarProyectoParser.LBRACKET, i)

        def RBRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(grammarProyectoParser.RBRACKET)
            else:
                return self.getToken(grammarProyectoParser.RBRACKET, i)

        def CONT(self, i:int=None):
            if i is None:
                return self.getTokens(grammarProyectoParser.CONT)
            else:
                return self.getToken(grammarProyectoParser.CONT, i)

        def FLOAT(self, i:int=None):
            if i is None:
                return self.getTokens(grammarProyectoParser.FLOAT)
            else:
                return self.getToken(grammarProyectoParser.FLOAT, i)

        def getRuleIndex(self):
            return grammarProyectoParser.RULE_tensor_acces

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTensor_acces" ):
                listener.enterTensor_acces(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTensor_acces" ):
                listener.exitTensor_acces(self)




    def tensor_acces(self):

        localctx = grammarProyectoParser.Tensor_accesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_tensor_acces)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.match(grammarProyectoParser.ID)
            self.state = 319
            self.match(grammarProyectoParser.LBRACKET)
            self.state = 320
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 321
            self.match(grammarProyectoParser.RBRACKET)
            self.state = 327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 322
                    self.match(grammarProyectoParser.LBRACKET)
                    self.state = 323
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 324
                    self.match(grammarProyectoParser.RBRACKET) 
                self.state = 329
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[15] = self.boolean_expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def boolean_expr_sempred(self, localctx:Boolean_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




