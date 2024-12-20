# Generated from grammarProyecto.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .grammarProyectoParser import grammarProyectoParser
else:
    from grammarProyectoParser import grammarProyectoParser

# This class defines a complete listener for a parse tree produced by grammarProyectoParser.
class grammarProyectoListener(ParseTreeListener):

    # Enter a parse tree produced by grammarProyectoParser#program.
    def enterProgram(self, ctx:grammarProyectoParser.ProgramContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#program.
    def exitProgram(self, ctx:grammarProyectoParser.ProgramContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#main_function.
    def enterMain_function(self, ctx:grammarProyectoParser.Main_functionContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#main_function.
    def exitMain_function(self, ctx:grammarProyectoParser.Main_functionContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#function.
    def enterFunction(self, ctx:grammarProyectoParser.FunctionContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#function.
    def exitFunction(self, ctx:grammarProyectoParser.FunctionContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#function_declaration.
    def enterFunction_declaration(self, ctx:grammarProyectoParser.Function_declarationContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#function_declaration.
    def exitFunction_declaration(self, ctx:grammarProyectoParser.Function_declarationContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#return.
    def enterReturn(self, ctx:grammarProyectoParser.ReturnContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#return.
    def exitReturn(self, ctx:grammarProyectoParser.ReturnContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#return_value.
    def enterReturn_value(self, ctx:grammarProyectoParser.Return_valueContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#return_value.
    def exitReturn_value(self, ctx:grammarProyectoParser.Return_valueContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#param_list.
    def enterParam_list(self, ctx:grammarProyectoParser.Param_listContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#param_list.
    def exitParam_list(self, ctx:grammarProyectoParser.Param_listContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#param.
    def enterParam(self, ctx:grammarProyectoParser.ParamContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#param.
    def exitParam(self, ctx:grammarProyectoParser.ParamContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#code_block.
    def enterCode_block(self, ctx:grammarProyectoParser.Code_blockContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#code_block.
    def exitCode_block(self, ctx:grammarProyectoParser.Code_blockContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#type.
    def enterType(self, ctx:grammarProyectoParser.TypeContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#type.
    def exitType(self, ctx:grammarProyectoParser.TypeContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#statement.
    def enterStatement(self, ctx:grammarProyectoParser.StatementContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#statement.
    def exitStatement(self, ctx:grammarProyectoParser.StatementContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#declaration.
    def enterDeclaration(self, ctx:grammarProyectoParser.DeclarationContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#declaration.
    def exitDeclaration(self, ctx:grammarProyectoParser.DeclarationContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#assignment.
    def enterAssignment(self, ctx:grammarProyectoParser.AssignmentContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#assignment.
    def exitAssignment(self, ctx:grammarProyectoParser.AssignmentContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#conditional.
    def enterConditional(self, ctx:grammarProyectoParser.ConditionalContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#conditional.
    def exitConditional(self, ctx:grammarProyectoParser.ConditionalContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#sino.
    def enterSino(self, ctx:grammarProyectoParser.SinoContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#sino.
    def exitSino(self, ctx:grammarProyectoParser.SinoContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#boolean_expr.
    def enterBoolean_expr(self, ctx:grammarProyectoParser.Boolean_exprContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#boolean_expr.
    def exitBoolean_expr(self, ctx:grammarProyectoParser.Boolean_exprContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#para_loop.
    def enterPara_loop(self, ctx:grammarProyectoParser.Para_loopContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#para_loop.
    def exitPara_loop(self, ctx:grammarProyectoParser.Para_loopContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#direction.
    def enterDirection(self, ctx:grammarProyectoParser.DirectionContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#direction.
    def exitDirection(self, ctx:grammarProyectoParser.DirectionContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#mientras_loop.
    def enterMientras_loop(self, ctx:grammarProyectoParser.Mientras_loopContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#mientras_loop.
    def exitMientras_loop(self, ctx:grammarProyectoParser.Mientras_loopContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#expr.
    def enterExpr(self, ctx:grammarProyectoParser.ExprContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#expr.
    def exitExpr(self, ctx:grammarProyectoParser.ExprContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#term.
    def enterTerm(self, ctx:grammarProyectoParser.TermContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#term.
    def exitTerm(self, ctx:grammarProyectoParser.TermContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#factor.
    def enterFactor(self, ctx:grammarProyectoParser.FactorContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#factor.
    def exitFactor(self, ctx:grammarProyectoParser.FactorContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#function_call.
    def enterFunction_call(self, ctx:grammarProyectoParser.Function_callContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#function_call.
    def exitFunction_call(self, ctx:grammarProyectoParser.Function_callContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#arg_list.
    def enterArg_list(self, ctx:grammarProyectoParser.Arg_listContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#arg_list.
    def exitArg_list(self, ctx:grammarProyectoParser.Arg_listContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#literal.
    def enterLiteral(self, ctx:grammarProyectoParser.LiteralContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#literal.
    def exitLiteral(self, ctx:grammarProyectoParser.LiteralContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#comparation_operator.
    def enterComparation_operator(self, ctx:grammarProyectoParser.Comparation_operatorContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#comparation_operator.
    def exitComparation_operator(self, ctx:grammarProyectoParser.Comparation_operatorContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#output.
    def enterOutput(self, ctx:grammarProyectoParser.OutputContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#output.
    def exitOutput(self, ctx:grammarProyectoParser.OutputContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#input.
    def enterInput(self, ctx:grammarProyectoParser.InputContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#input.
    def exitInput(self, ctx:grammarProyectoParser.InputContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#tensor_declaration.
    def enterTensor_declaration(self, ctx:grammarProyectoParser.Tensor_declarationContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#tensor_declaration.
    def exitTensor_declaration(self, ctx:grammarProyectoParser.Tensor_declarationContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#tensor_dimensions.
    def enterTensor_dimensions(self, ctx:grammarProyectoParser.Tensor_dimensionsContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#tensor_dimensions.
    def exitTensor_dimensions(self, ctx:grammarProyectoParser.Tensor_dimensionsContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#tensor_init.
    def enterTensor_init(self, ctx:grammarProyectoParser.Tensor_initContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#tensor_init.
    def exitTensor_init(self, ctx:grammarProyectoParser.Tensor_initContext):
        pass


    # Enter a parse tree produced by grammarProyectoParser#tensor_acces.
    def enterTensor_acces(self, ctx:grammarProyectoParser.Tensor_accesContext):
        pass

    # Exit a parse tree produced by grammarProyectoParser#tensor_acces.
    def exitTensor_acces(self, ctx:grammarProyectoParser.Tensor_accesContext):
        pass



del grammarProyectoParser