from json import load
from antlr4 import *
from grammarProyectoLexer import grammarProyectoLexer
from grammarProyectoParser import grammarProyectoParser
from grammarProyectoListener import grammarProyectoListener


class TraductorPythonListener(grammarProyectoListener):
    def __init__(self):
        self.python_code = ""
        self.indent_level = 0
        self.thereIsSquare = False
    def _indent(self):
        return "    " * self.indent_level

    def replace_booleans(self, expression):
        # Reemplazar "verdadero" por True y "falso" por False
        if "verdadero" in expression or "falso" in expression:
            expression = expression.replace("verdadero", "True").replace("falso", "False")
        return expression

    def enterProgram(self, ctx):
        # Preparar el código inicial de Python si es necesario
        self.python_code = "# Traducción automática\n\n"

    def enterMain_function(self, ctx):
        # Definir la función principal
        self.python_code += "def main():\n"
        self.indent_level += 1

    def enterFunction(self, ctx):
        # Manejar declaración de funciones
        function_name = ctx.function_declaration().ID().getText()

        
        # Construir la definición de la función
        params = [param.getText() for param in ctx.function_declaration().param_list().param()]
        function_def = f"def {function_name}({', '.join(params)}):\n"
        self.python_code += function_def
        self.indent_level += 1

    def enterReturn(self, ctx):
        return_value = ctx.return_value().getText()
        
        line = self._indent()
        line += f'return {return_value}'
        
        self.python_code += line

    def exitFunction(self, ctx):
        # Reiniciar nivel de indentación
        self.indent_level -= 1
        self.python_code += "\n"

    def enterFunction_call(self, ctx):
        pass
        #function_name = (ctx.ID().getText())
        #if function_name == 'raizCuadrada':
         #   self.python_code += 'math.sqrt'
         
    def enterTensor_declaration(self, ctx):
        # Manejar declaracion de tensores
        tensor_name = ctx.ID().getText()
        
        line = self._indent()
        
        if ctx.tensor_init():
            initValue =ctx.tensor_init().getText()
            line += f"{tensor_name} = {initValue}"
        else:
            line += f"{tensor_name} = []"
        self.python_code += line + "\n"
    
    def enterDeclaration(self, ctx):
        # Manejar declaración de variables
        var_type = ctx.type_().getText()
        var_name = ctx.ID().getText()
        
        # Agregar código de declaración
        line = self._indent()
        
        # Si hay inicialización
        if ctx.expr():
            value = self._translate_expr(ctx.expr())
            line += f"{var_name} = {value}"
        else:
            # Valor por defecto según el tipo
            default_values = {
                'entero': '0',
                'flotante': '0.0',
                'cadena': '""',
                'booleano': 'False'
            }
            line += f"{var_name} = {default_values.get(var_type, 'None')}"

        self.python_code += line + "\n"

    def enterAssignment(self, ctx):
        var_name = ctx.ID().getText()
        
        if ctx.expr():
            value = ctx.expr().getText()
            
        if ctx.tensor_init():
            value = ctx.tensor_init().getText()    
            
        line = self._indent()
        value = self.replace_booleans(value)
        line += f'{var_name} = {value}'
        self.python_code += line + "\n"
        
    def _translate_expr(self, expr_ctx):
        # Método para traducir expresiones matemáticas
        if expr_ctx.term():
            expression = expr_ctx.getText()
            expression = self.replace_booleans(expression)
            expression = self.replace_function_calls(expression)
            return expression
        return "None"

    def enterConditional(self, ctx):
        # Traducir condicionales
        condition = self._translate_boolean_expr(ctx.boolean_expr())
        self.python_code += self._indent() + f"if {condition}:\n"
        self.indent_level += 1
        
    def enterSino(self, ctx):
        # Manejar cláusula else
        self.indent_level -= 1
        self.python_code += self._indent() + "else:\n"
        self.indent_level += 1

    def exitConditional(self, ctx):
        self.indent_level -= 1
        self.python_code += "\n"
        
    def _translate_boolean_expr(self, bool_ctx):

        # Traducir expresiones booleanas
        left = bool_ctx.getChild(0).getText()
        op = bool_ctx.comparation_operator().getText()
        right = bool_ctx.getChild(2).getText()
        
        # Mapear operadores
        op_map = {
            '==': '==',
            '!=': '!=',
            '>': '>',
            '<': '<',
            '>=': '>=',
            '<=': '<='
        }
        expr = f"{left} {op_map.get(op, op)} {right}"
        
        expr = self.replace_booleans(expr)
        return expr

    def enterOutput(self, ctx):
        # Manejar instrucciones de escritura
        expr = ctx.expr()  # Obtener la expresión desde el contexto
        if expr:
            # Convertir la expresión a texto
            output_value = self.get_output_value(expr)

            # Modificar para usar la sintaxis de f-string
            self.python_code += self._indent() + f"print(f\'{output_value}\')\n"

    def get_output_value(self, expr):
        # Convertir la expresión a un string Python válido
        terms = []
        
        # Obtener todos los términos en la expresión
        for i in range(expr.getChildCount()):
            child = expr.getChild(i)
            
            if child.getText() == '+':
                continue  # Ignorar el operador '+'
            
            # Procesar el término para asegurarnos de que esté en el formato correcto
            term_text = child.getText()
            print(term_text)
            term_text = self.replace_function_calls(term_text)
            # Si el término es una cadena (por ejemplo, una literal), eliminar las comillas
            if term_text.startswith('"') and term_text.endswith('"'):
                term_text = term_text[1:-1]  # Quitar comillas
            else:
                term_text = "{" + term_text + "}"
            terms.append(term_text)

        # Unir términos con la concatenación para formar la salida
        output_value = ' '.join(terms)

        return output_value

    def enterInput(self, ctx):
        # Manejar instrucciones de lectura
        input_variable = ctx.ID().getText()
        line = self._indent()
        line += f'{input_variable} = input()'
        self.python_code += line + '\n'
        
    def exitInput(self, ctx):
        pass
    
    def enterPara_loop(self, ctx):
        # Traducir ciclo para
        var = ctx.ID().getText()
        start = ctx.getChild(3).getText()
        end = ctx.getChild(5).getText()
        direction = ctx.direction().getText()
        
        # Determinar paso
        step = '1' if direction == 'incremento' else '-1'
        
        # Construcción de rango en Python
        self.python_code += self._indent() + f"for {var} in range({start}, {end} + 1, {step}):\n"
        self.indent_level += 1

    def exitPara_loop(self, ctx):
        self.indent_level -= 1
        self.python_code += "\n"
    def enterMientras_loop(self, ctx):
        # Traducir ciclo mientras
        condition = self._translate_boolean_expr(ctx.boolean_expr())
        self.python_code += self._indent() + f"while {condition}:\n"
        self.indent_level += 1
        
    def exitMientras_loop(self, ctx):
        self.indent_level -= 1
        self.python_code += "\n"
        
    def exitProgram(self, ctx):
        # Agregar llamada a main si es necesario
        self.python_code += "\n\nif __name__ == '__main__':\n"
        self.python_code += "    main()\n"
        self.indent_level = 0
        
        if self.thereIsSquare:
            self.python_code = f'import math \n\n {self.python_code}'
        # Método final para guardar o imprimir código
        print(self.python_code)
        
        # Opcionalmente, guardar en archivo
        with open('output.py', 'w') as f:
            f.write(self.python_code)
    
    def replace_function_calls(self, expression):
        # Reemplazar llamadas a la función raizCuadrada
        if "raizCuadrada" in expression:
            self.thereIsSquare = True  # Se encontró una llamada a raizCuadrada
            return expression.replace("raizCuadrada", "math.sqrt")
        return expression
def loadFile(link):
    content = open(link, "r").read()
    return content

def main():
    print("Ingrese el nombre de su archivo: ")
    archivo = input("> ")
    codigo = loadFile(archivo)
    print(f'Codigo: \n{codigo}')
    lexer = grammarProyectoLexer(InputStream(codigo))
    stream = CommonTokenStream(lexer)
    parser = grammarProyectoParser(stream)
    tree = parser.program()
    
    print(tree.toStringTree(recog=parser))
    
    # Crear una instancia de ParseTreeWalker y ProyectoCodeListener
    walker = ParseTreeWalker()
    listener = TraductorPythonListener()
    
    # Recorrer el árbol y activar la traducción de Proyecto a texto
    walker.walk(listener, tree)

if __name__ == '__main__':
    main()