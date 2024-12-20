// Generated from /home/rodrigo/Ejercicios/ProyectoFinal/grammarProyecto.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class grammarProyectoParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		CREAR=1, ENTERO=2, FLOTANTE=3, CADENA=4, BOOLEANO=5, SI=6, ENTONCES=7, 
		SINO=8, PARA=9, HASTA=10, INCREMENTO=11, DECREMENTO=12, MIENTRAS=13, FUNCION=14, 
		RETORNAR=15, INICIO=16, FIN=17, ARREGLO=18, MATRIZ=19, LEER=20, ESCRIBIR=21, 
		ID=22, CONT=23, FLOAT=24, STRING=25, PLUS=26, MINUS=27, MULT=28, DIVI=29, 
		EQUALS=30, LPAREN=31, RPAREN=32, COLON=33, COMMA=34, SEMICOLON=35, LBRACKET=36, 
		RBRACKET=37, WS=38, INDENT=39, NEWLINE=40, COMMENT=41, IGUAL=42, DIFERENTE=43, 
		MAYOR=44, MENOR=45, MAYOR_IGUAL=46, MENOR_IGUAL=47, AND=48, OR=49, NOT=50, 
		VERDADERO=51, FALSO=52;
	public static final int
		RULE_program = 0, RULE_main_function = 1, RULE_function = 2, RULE_function_declaration = 3, 
		RULE_return = 4, RULE_return_value = 5, RULE_param_list = 6, RULE_param = 7, 
		RULE_code_block = 8, RULE_type = 9, RULE_statement = 10, RULE_declaration = 11, 
		RULE_assignment = 12, RULE_conditional = 13, RULE_sino = 14, RULE_boolean_expr = 15, 
		RULE_para_loop = 16, RULE_direction = 17, RULE_mientras_loop = 18, RULE_expr = 19, 
		RULE_term = 20, RULE_factor = 21, RULE_function_call = 22, RULE_arg_list = 23, 
		RULE_literal = 24, RULE_comparation_operator = 25, RULE_output = 26, RULE_input = 27, 
		RULE_tensor_declaration = 28, RULE_tensor_dimensions = 29, RULE_tensor_init = 30, 
		RULE_tensor_acces = 31;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "main_function", "function", "function_declaration", "return", 
			"return_value", "param_list", "param", "code_block", "type", "statement", 
			"declaration", "assignment", "conditional", "sino", "boolean_expr", "para_loop", 
			"direction", "mientras_loop", "expr", "term", "factor", "function_call", 
			"arg_list", "literal", "comparation_operator", "output", "input", "tensor_declaration", 
			"tensor_dimensions", "tensor_init", "tensor_acces"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'crear'", "'entero'", "'flotante'", "'cadena'", "'booleano'", 
			"'si'", "'entonces'", "'sino'", "'para'", "'hasta'", "'incremento'", 
			"'decremento'", "'mientras'", "'funcion'", "'retornar'", "'inicio'", 
			"'fin'", "'arreglo'", "'matriz'", "'leer'", "'escribir'", null, null, 
			null, null, "'+'", "'-'", "'*'", "'/'", "'='", "'('", "')'", "':'", "','", 
			"';'", "'['", "']'", null, null, null, null, "'=='", "'!='", "'>'", "'<'", 
			"'>='", "'<='", "'y'", "'o'", "'no'", "'verdadero'", "'falso'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "CREAR", "ENTERO", "FLOTANTE", "CADENA", "BOOLEANO", "SI", "ENTONCES", 
			"SINO", "PARA", "HASTA", "INCREMENTO", "DECREMENTO", "MIENTRAS", "FUNCION", 
			"RETORNAR", "INICIO", "FIN", "ARREGLO", "MATRIZ", "LEER", "ESCRIBIR", 
			"ID", "CONT", "FLOAT", "STRING", "PLUS", "MINUS", "MULT", "DIVI", "EQUALS", 
			"LPAREN", "RPAREN", "COLON", "COMMA", "SEMICOLON", "LBRACKET", "RBRACKET", 
			"WS", "INDENT", "NEWLINE", "COMMENT", "IGUAL", "DIFERENTE", "MAYOR", 
			"MENOR", "MAYOR_IGUAL", "MENOR_IGUAL", "AND", "OR", "NOT", "VERDADERO", 
			"FALSO"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "grammarProyecto.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public grammarProyectoParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public Main_functionContext main_function() {
			return getRuleContext(Main_functionContext.class,0);
		}
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			main_function();
			setState(68);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==FUNCION) {
				{
				{
				setState(65);
				function();
				}
				}
				setState(70);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Main_functionContext extends ParserRuleContext {
		public TerminalNode INICIO() { return getToken(grammarProyectoParser.INICIO, 0); }
		public TerminalNode COLON() { return getToken(grammarProyectoParser.COLON, 0); }
		public Code_blockContext code_block() {
			return getRuleContext(Code_blockContext.class,0);
		}
		public TerminalNode FIN() { return getToken(grammarProyectoParser.FIN, 0); }
		public TerminalNode SEMICOLON() { return getToken(grammarProyectoParser.SEMICOLON, 0); }
		public Main_functionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_main_function; }
	}

	public final Main_functionContext main_function() throws RecognitionException {
		Main_functionContext _localctx = new Main_functionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_main_function);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			match(INICIO);
			setState(72);
			match(COLON);
			setState(73);
			code_block();
			setState(74);
			match(FIN);
			setState(75);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionContext extends ParserRuleContext {
		public Function_declarationContext function_declaration() {
			return getRuleContext(Function_declarationContext.class,0);
		}
		public Code_blockContext code_block() {
			return getRuleContext(Code_blockContext.class,0);
		}
		public ReturnContext return_() {
			return getRuleContext(ReturnContext.class,0);
		}
		public TerminalNode FIN() { return getToken(grammarProyectoParser.FIN, 0); }
		public TerminalNode SEMICOLON() { return getToken(grammarProyectoParser.SEMICOLON, 0); }
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_function);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			function_declaration();
			setState(78);
			code_block();
			setState(79);
			return_();
			setState(80);
			match(FIN);
			setState(81);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Function_declarationContext extends ParserRuleContext {
		public TerminalNode FUNCION() { return getToken(grammarProyectoParser.FUNCION, 0); }
		public TerminalNode ID() { return getToken(grammarProyectoParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(grammarProyectoParser.LPAREN, 0); }
		public Param_listContext param_list() {
			return getRuleContext(Param_listContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(grammarProyectoParser.RPAREN, 0); }
		public TerminalNode COLON() { return getToken(grammarProyectoParser.COLON, 0); }
		public Function_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_declaration; }
	}

	public final Function_declarationContext function_declaration() throws RecognitionException {
		Function_declarationContext _localctx = new Function_declarationContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_function_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(83);
			match(FUNCION);
			setState(84);
			match(ID);
			setState(85);
			match(LPAREN);
			setState(86);
			param_list();
			setState(87);
			match(RPAREN);
			setState(88);
			match(COLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnContext extends ParserRuleContext {
		public TerminalNode RETORNAR() { return getToken(grammarProyectoParser.RETORNAR, 0); }
		public Return_valueContext return_value() {
			return getRuleContext(Return_valueContext.class,0);
		}
		public ReturnContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return; }
	}

	public final ReturnContext return_() throws RecognitionException {
		ReturnContext _localctx = new ReturnContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_return);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(90);
			match(RETORNAR);
			setState(91);
			return_value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Return_valueContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(grammarProyectoParser.SEMICOLON, 0); }
		public TerminalNode ID() { return getToken(grammarProyectoParser.ID, 0); }
		public Return_valueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_return_value; }
	}

	public final Return_valueContext return_value() throws RecognitionException {
		Return_valueContext _localctx = new Return_valueContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_return_value);
		try {
			setState(98);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(93);
				expr();
				setState(94);
				match(SEMICOLON);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				{
				setState(96);
				match(ID);
				setState(97);
				match(SEMICOLON);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Param_listContext extends ParserRuleContext {
		public List<TypeContext> type() {
			return getRuleContexts(TypeContext.class);
		}
		public TypeContext type(int i) {
			return getRuleContext(TypeContext.class,i);
		}
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public List<Tensor_dimensionsContext> tensor_dimensions() {
			return getRuleContexts(Tensor_dimensionsContext.class);
		}
		public Tensor_dimensionsContext tensor_dimensions(int i) {
			return getRuleContext(Tensor_dimensionsContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(grammarProyectoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(grammarProyectoParser.COMMA, i);
		}
		public Param_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param_list; }
	}

	public final Param_listContext param_list() throws RecognitionException {
		Param_listContext _localctx = new Param_listContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_param_list);
		int _la;
		try {
			setState(124);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ENTERO:
			case FLOTANTE:
			case CADENA:
			case BOOLEANO:
				enterOuterAlt(_localctx, 1);
				{
				setState(100);
				type();
				setState(104);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==LBRACKET) {
					{
					{
					setState(101);
					tensor_dimensions();
					}
					}
					setState(106);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(107);
				param();
				setState(120);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(108);
					match(COMMA);
					setState(109);
					type();
					setState(113);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==LBRACKET) {
						{
						{
						setState(110);
						tensor_dimensions();
						}
						}
						setState(115);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					setState(116);
					param();
					}
					}
					setState(122);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case RPAREN:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParamContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(grammarProyectoParser.ID, 0); }
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Code_blockContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public Code_blockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_code_block; }
	}

	public final Code_blockContext code_block() throws RecognitionException {
		Code_blockContext _localctx = new Code_blockContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_code_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(131);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7348802L) != 0)) {
				{
				{
				setState(128);
				statement();
				}
				}
				setState(133);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeContext extends ParserRuleContext {
		public TerminalNode ENTERO() { return getToken(grammarProyectoParser.ENTERO, 0); }
		public TerminalNode FLOTANTE() { return getToken(grammarProyectoParser.FLOTANTE, 0); }
		public TerminalNode CADENA() { return getToken(grammarProyectoParser.CADENA, 0); }
		public TerminalNode BOOLEANO() { return getToken(grammarProyectoParser.BOOLEANO, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(134);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 60L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public OutputContext output() {
			return getRuleContext(OutputContext.class,0);
		}
		public InputContext input() {
			return getRuleContext(InputContext.class,0);
		}
		public ConditionalContext conditional() {
			return getRuleContext(ConditionalContext.class,0);
		}
		public Para_loopContext para_loop() {
			return getRuleContext(Para_loopContext.class,0);
		}
		public Mientras_loopContext mientras_loop() {
			return getRuleContext(Mientras_loopContext.class,0);
		}
		public Tensor_declarationContext tensor_declaration() {
			return getRuleContext(Tensor_declarationContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_statement);
		try {
			setState(144);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(136);
				declaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(137);
				assignment();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(138);
				output();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(139);
				input();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(140);
				conditional();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(141);
				para_loop();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(142);
				mientras_loop();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(143);
				tensor_declaration();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends ParserRuleContext {
		public TerminalNode CREAR() { return getToken(grammarProyectoParser.CREAR, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode ID() { return getToken(grammarProyectoParser.ID, 0); }
		public TerminalNode SEMICOLON() { return getToken(grammarProyectoParser.SEMICOLON, 0); }
		public TerminalNode EQUALS() { return getToken(grammarProyectoParser.EQUALS, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(146);
			match(CREAR);
			setState(147);
			type();
			setState(148);
			match(ID);
			setState(151);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUALS) {
				{
				setState(149);
				match(EQUALS);
				setState(150);
				expr();
				}
			}

			setState(153);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(grammarProyectoParser.ID, 0); }
		public TerminalNode EQUALS() { return getToken(grammarProyectoParser.EQUALS, 0); }
		public TerminalNode SEMICOLON() { return getToken(grammarProyectoParser.SEMICOLON, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Tensor_initContext tensor_init() {
			return getRuleContext(Tensor_initContext.class,0);
		}
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(155);
			match(ID);
			setState(156);
			match(EQUALS);
			setState(159);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
			case CONT:
			case FLOAT:
			case STRING:
			case LPAREN:
			case VERDADERO:
			case FALSO:
				{
				setState(157);
				expr();
				}
				break;
			case LBRACKET:
				{
				setState(158);
				tensor_init();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(161);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionalContext extends ParserRuleContext {
		public TerminalNode SI() { return getToken(grammarProyectoParser.SI, 0); }
		public Boolean_exprContext boolean_expr() {
			return getRuleContext(Boolean_exprContext.class,0);
		}
		public TerminalNode ENTONCES() { return getToken(grammarProyectoParser.ENTONCES, 0); }
		public TerminalNode COLON() { return getToken(grammarProyectoParser.COLON, 0); }
		public Code_blockContext code_block() {
			return getRuleContext(Code_blockContext.class,0);
		}
		public SinoContext sino() {
			return getRuleContext(SinoContext.class,0);
		}
		public TerminalNode FIN() { return getToken(grammarProyectoParser.FIN, 0); }
		public TerminalNode SEMICOLON() { return getToken(grammarProyectoParser.SEMICOLON, 0); }
		public ConditionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditional; }
	}

	public final ConditionalContext conditional() throws RecognitionException {
		ConditionalContext _localctx = new ConditionalContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_conditional);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(163);
			match(SI);
			setState(164);
			boolean_expr(0);
			setState(165);
			match(ENTONCES);
			setState(166);
			match(COLON);
			setState(167);
			code_block();
			setState(171);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FIN:
				{
				{
				setState(168);
				match(FIN);
				setState(169);
				match(SEMICOLON);
				}
				}
				break;
			case SINO:
				{
				setState(170);
				sino();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SinoContext extends ParserRuleContext {
		public TerminalNode SINO() { return getToken(grammarProyectoParser.SINO, 0); }
		public TerminalNode COLON() { return getToken(grammarProyectoParser.COLON, 0); }
		public Code_blockContext code_block() {
			return getRuleContext(Code_blockContext.class,0);
		}
		public TerminalNode FIN() { return getToken(grammarProyectoParser.FIN, 0); }
		public TerminalNode SEMICOLON() { return getToken(grammarProyectoParser.SEMICOLON, 0); }
		public SinoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sino; }
	}

	public final SinoContext sino() throws RecognitionException {
		SinoContext _localctx = new SinoContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_sino);
		try {
			enterOuterAlt(_localctx, 1);
			{
			{
			setState(173);
			match(SINO);
			setState(174);
			match(COLON);
			setState(175);
			code_block();
			setState(176);
			match(FIN);
			setState(177);
			match(SEMICOLON);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Boolean_exprContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public Comparation_operatorContext comparation_operator() {
			return getRuleContext(Comparation_operatorContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(grammarProyectoParser.LPAREN, 0); }
		public List<Boolean_exprContext> boolean_expr() {
			return getRuleContexts(Boolean_exprContext.class);
		}
		public Boolean_exprContext boolean_expr(int i) {
			return getRuleContext(Boolean_exprContext.class,i);
		}
		public TerminalNode RPAREN() { return getToken(grammarProyectoParser.RPAREN, 0); }
		public TerminalNode NOT() { return getToken(grammarProyectoParser.NOT, 0); }
		public TerminalNode AND() { return getToken(grammarProyectoParser.AND, 0); }
		public TerminalNode OR() { return getToken(grammarProyectoParser.OR, 0); }
		public Boolean_exprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_boolean_expr; }
	}

	public final Boolean_exprContext boolean_expr() throws RecognitionException {
		return boolean_expr(0);
	}

	private Boolean_exprContext boolean_expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Boolean_exprContext _localctx = new Boolean_exprContext(_ctx, _parentState);
		Boolean_exprContext _prevctx = _localctx;
		int _startState = 30;
		enterRecursionRule(_localctx, 30, RULE_boolean_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(190);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(180);
				expr();
				setState(181);
				comparation_operator();
				setState(182);
				expr();
				}
				break;
			case 2:
				{
				setState(184);
				match(LPAREN);
				setState(185);
				boolean_expr(0);
				setState(186);
				match(RPAREN);
				}
				break;
			case 3:
				{
				setState(188);
				match(NOT);
				setState(189);
				boolean_expr(1);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(197);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new Boolean_exprContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_boolean_expr);
					setState(192);
					if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
					setState(193);
					_la = _input.LA(1);
					if ( !(_la==AND || _la==OR) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(194);
					boolean_expr(3);
					}
					} 
				}
				setState(199);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Para_loopContext extends ParserRuleContext {
		public TerminalNode PARA() { return getToken(grammarProyectoParser.PARA, 0); }
		public TerminalNode ID() { return getToken(grammarProyectoParser.ID, 0); }
		public TerminalNode EQUALS() { return getToken(grammarProyectoParser.EQUALS, 0); }
		public List<TerminalNode> CONT() { return getTokens(grammarProyectoParser.CONT); }
		public TerminalNode CONT(int i) {
			return getToken(grammarProyectoParser.CONT, i);
		}
		public TerminalNode HASTA() { return getToken(grammarProyectoParser.HASTA, 0); }
		public DirectionContext direction() {
			return getRuleContext(DirectionContext.class,0);
		}
		public TerminalNode COLON() { return getToken(grammarProyectoParser.COLON, 0); }
		public Code_blockContext code_block() {
			return getRuleContext(Code_blockContext.class,0);
		}
		public TerminalNode FIN() { return getToken(grammarProyectoParser.FIN, 0); }
		public TerminalNode SEMICOLON() { return getToken(grammarProyectoParser.SEMICOLON, 0); }
		public Para_loopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_para_loop; }
	}

	public final Para_loopContext para_loop() throws RecognitionException {
		Para_loopContext _localctx = new Para_loopContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_para_loop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(200);
			match(PARA);
			setState(201);
			match(ID);
			setState(202);
			match(EQUALS);
			setState(203);
			match(CONT);
			setState(204);
			match(HASTA);
			setState(205);
			match(CONT);
			setState(206);
			direction();
			setState(207);
			match(COLON);
			setState(208);
			code_block();
			setState(209);
			match(FIN);
			setState(210);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DirectionContext extends ParserRuleContext {
		public TerminalNode INCREMENTO() { return getToken(grammarProyectoParser.INCREMENTO, 0); }
		public TerminalNode DECREMENTO() { return getToken(grammarProyectoParser.DECREMENTO, 0); }
		public DirectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_direction; }
	}

	public final DirectionContext direction() throws RecognitionException {
		DirectionContext _localctx = new DirectionContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_direction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(212);
			_la = _input.LA(1);
			if ( !(_la==INCREMENTO || _la==DECREMENTO) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Mientras_loopContext extends ParserRuleContext {
		public TerminalNode MIENTRAS() { return getToken(grammarProyectoParser.MIENTRAS, 0); }
		public Boolean_exprContext boolean_expr() {
			return getRuleContext(Boolean_exprContext.class,0);
		}
		public TerminalNode COLON() { return getToken(grammarProyectoParser.COLON, 0); }
		public Code_blockContext code_block() {
			return getRuleContext(Code_blockContext.class,0);
		}
		public TerminalNode FIN() { return getToken(grammarProyectoParser.FIN, 0); }
		public TerminalNode SEMICOLON() { return getToken(grammarProyectoParser.SEMICOLON, 0); }
		public Mientras_loopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mientras_loop; }
	}

	public final Mientras_loopContext mientras_loop() throws RecognitionException {
		Mientras_loopContext _localctx = new Mientras_loopContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_mientras_loop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(214);
			match(MIENTRAS);
			setState(215);
			boolean_expr(0);
			setState(216);
			match(COLON);
			setState(217);
			code_block();
			setState(218);
			match(FIN);
			setState(219);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public List<TermContext> term() {
			return getRuleContexts(TermContext.class);
		}
		public TermContext term(int i) {
			return getRuleContext(TermContext.class,i);
		}
		public List<TerminalNode> PLUS() { return getTokens(grammarProyectoParser.PLUS); }
		public TerminalNode PLUS(int i) {
			return getToken(grammarProyectoParser.PLUS, i);
		}
		public List<TerminalNode> MINUS() { return getTokens(grammarProyectoParser.MINUS); }
		public TerminalNode MINUS(int i) {
			return getToken(grammarProyectoParser.MINUS, i);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_expr);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(221);
			term();
			setState(226);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(222);
					_la = _input.LA(1);
					if ( !(_la==PLUS || _la==MINUS) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(223);
					term();
					}
					} 
				}
				setState(228);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public List<FactorContext> factor() {
			return getRuleContexts(FactorContext.class);
		}
		public FactorContext factor(int i) {
			return getRuleContext(FactorContext.class,i);
		}
		public List<TerminalNode> MULT() { return getTokens(grammarProyectoParser.MULT); }
		public TerminalNode MULT(int i) {
			return getToken(grammarProyectoParser.MULT, i);
		}
		public List<TerminalNode> DIVI() { return getTokens(grammarProyectoParser.DIVI); }
		public TerminalNode DIVI(int i) {
			return getToken(grammarProyectoParser.DIVI, i);
		}
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	}

	public final TermContext term() throws RecognitionException {
		TermContext _localctx = new TermContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_term);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(229);
			factor();
			setState(234);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(230);
					_la = _input.LA(1);
					if ( !(_la==MULT || _la==DIVI) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(231);
					factor();
					}
					} 
				}
				setState(236);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public LiteralContext literal() {
			return getRuleContext(LiteralContext.class,0);
		}
		public Function_callContext function_call() {
			return getRuleContext(Function_callContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(grammarProyectoParser.LPAREN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(grammarProyectoParser.RPAREN, 0); }
		public TerminalNode ID() { return getToken(grammarProyectoParser.ID, 0); }
		public Tensor_accesContext tensor_acces() {
			return getRuleContext(Tensor_accesContext.class,0);
		}
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_factor);
		try {
			setState(245);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(237);
				literal();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(238);
				function_call();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(239);
				match(LPAREN);
				setState(240);
				expr();
				setState(241);
				match(RPAREN);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(243);
				match(ID);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(244);
				tensor_acces();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Function_callContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(grammarProyectoParser.ID, 0); }
		public TerminalNode LPAREN() { return getToken(grammarProyectoParser.LPAREN, 0); }
		public Arg_listContext arg_list() {
			return getRuleContext(Arg_listContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(grammarProyectoParser.RPAREN, 0); }
		public Function_callContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_call; }
	}

	public final Function_callContext function_call() throws RecognitionException {
		Function_callContext _localctx = new Function_callContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_function_call);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(247);
			match(ID);
			setState(248);
			match(LPAREN);
			setState(249);
			arg_list();
			setState(250);
			match(RPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Arg_listContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(grammarProyectoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(grammarProyectoParser.COMMA, i);
		}
		public Arg_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arg_list; }
	}

	public final Arg_listContext arg_list() throws RecognitionException {
		Arg_listContext _localctx = new Arg_listContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_arg_list);
		int _la;
		try {
			setState(261);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
			case CONT:
			case FLOAT:
			case STRING:
			case LPAREN:
			case VERDADERO:
			case FALSO:
				enterOuterAlt(_localctx, 1);
				{
				setState(252);
				expr();
				setState(257);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(253);
					match(COMMA);
					setState(254);
					expr();
					}
					}
					setState(259);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			case RPAREN:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralContext extends ParserRuleContext {
		public TerminalNode CONT() { return getToken(grammarProyectoParser.CONT, 0); }
		public TerminalNode FLOAT() { return getToken(grammarProyectoParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(grammarProyectoParser.STRING, 0); }
		public TerminalNode VERDADERO() { return getToken(grammarProyectoParser.VERDADERO, 0); }
		public TerminalNode FALSO() { return getToken(grammarProyectoParser.FALSO, 0); }
		public LiteralContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literal; }
	}

	public final LiteralContext literal() throws RecognitionException {
		LiteralContext _localctx = new LiteralContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_literal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(263);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 6755399499776000L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Comparation_operatorContext extends ParserRuleContext {
		public TerminalNode IGUAL() { return getToken(grammarProyectoParser.IGUAL, 0); }
		public TerminalNode DIFERENTE() { return getToken(grammarProyectoParser.DIFERENTE, 0); }
		public TerminalNode MAYOR() { return getToken(grammarProyectoParser.MAYOR, 0); }
		public TerminalNode MENOR() { return getToken(grammarProyectoParser.MENOR, 0); }
		public TerminalNode MAYOR_IGUAL() { return getToken(grammarProyectoParser.MAYOR_IGUAL, 0); }
		public TerminalNode MENOR_IGUAL() { return getToken(grammarProyectoParser.MENOR_IGUAL, 0); }
		public Comparation_operatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparation_operator; }
	}

	public final Comparation_operatorContext comparation_operator() throws RecognitionException {
		Comparation_operatorContext _localctx = new Comparation_operatorContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_comparation_operator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(265);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 277076930199552L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OutputContext extends ParserRuleContext {
		public TerminalNode ESCRIBIR() { return getToken(grammarProyectoParser.ESCRIBIR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(grammarProyectoParser.SEMICOLON, 0); }
		public OutputContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_output; }
	}

	public final OutputContext output() throws RecognitionException {
		OutputContext _localctx = new OutputContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_output);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(ESCRIBIR);
			setState(268);
			expr();
			setState(269);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InputContext extends ParserRuleContext {
		public TerminalNode LEER() { return getToken(grammarProyectoParser.LEER, 0); }
		public TerminalNode ID() { return getToken(grammarProyectoParser.ID, 0); }
		public TerminalNode SEMICOLON() { return getToken(grammarProyectoParser.SEMICOLON, 0); }
		public InputContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_input; }
	}

	public final InputContext input() throws RecognitionException {
		InputContext _localctx = new InputContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_input);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(271);
			match(LEER);
			setState(272);
			match(ID);
			setState(273);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Tensor_declarationContext extends ParserRuleContext {
		public TerminalNode CREAR() { return getToken(grammarProyectoParser.CREAR, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public Tensor_dimensionsContext tensor_dimensions() {
			return getRuleContext(Tensor_dimensionsContext.class,0);
		}
		public TerminalNode ID() { return getToken(grammarProyectoParser.ID, 0); }
		public TerminalNode SEMICOLON() { return getToken(grammarProyectoParser.SEMICOLON, 0); }
		public TerminalNode EQUALS() { return getToken(grammarProyectoParser.EQUALS, 0); }
		public Tensor_initContext tensor_init() {
			return getRuleContext(Tensor_initContext.class,0);
		}
		public Tensor_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tensor_declaration; }
	}

	public final Tensor_declarationContext tensor_declaration() throws RecognitionException {
		Tensor_declarationContext _localctx = new Tensor_declarationContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_tensor_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(275);
			match(CREAR);
			setState(276);
			type();
			setState(277);
			tensor_dimensions();
			setState(278);
			match(ID);
			setState(281);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUALS) {
				{
				setState(279);
				match(EQUALS);
				setState(280);
				tensor_init();
				}
			}

			setState(283);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Tensor_dimensionsContext extends ParserRuleContext {
		public List<TerminalNode> LBRACKET() { return getTokens(grammarProyectoParser.LBRACKET); }
		public TerminalNode LBRACKET(int i) {
			return getToken(grammarProyectoParser.LBRACKET, i);
		}
		public List<TerminalNode> RBRACKET() { return getTokens(grammarProyectoParser.RBRACKET); }
		public TerminalNode RBRACKET(int i) {
			return getToken(grammarProyectoParser.RBRACKET, i);
		}
		public List<TerminalNode> CONT() { return getTokens(grammarProyectoParser.CONT); }
		public TerminalNode CONT(int i) {
			return getToken(grammarProyectoParser.CONT, i);
		}
		public Tensor_dimensionsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tensor_dimensions; }
	}

	public final Tensor_dimensionsContext tensor_dimensions() throws RecognitionException {
		Tensor_dimensionsContext _localctx = new Tensor_dimensionsContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_tensor_dimensions);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(290); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(285);
					match(LBRACKET);
					setState(287);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==CONT) {
						{
						setState(286);
						match(CONT);
						}
					}

					setState(289);
					match(RBRACKET);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(292); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,20,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Tensor_initContext extends ParserRuleContext {
		public TerminalNode LBRACKET() { return getToken(grammarProyectoParser.LBRACKET, 0); }
		public List<LiteralContext> literal() {
			return getRuleContexts(LiteralContext.class);
		}
		public LiteralContext literal(int i) {
			return getRuleContext(LiteralContext.class,i);
		}
		public TerminalNode RBRACKET() { return getToken(grammarProyectoParser.RBRACKET, 0); }
		public List<TerminalNode> COMMA() { return getTokens(grammarProyectoParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(grammarProyectoParser.COMMA, i);
		}
		public List<Tensor_initContext> tensor_init() {
			return getRuleContexts(Tensor_initContext.class);
		}
		public Tensor_initContext tensor_init(int i) {
			return getRuleContext(Tensor_initContext.class,i);
		}
		public Tensor_initContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tensor_init; }
	}

	public final Tensor_initContext tensor_init() throws RecognitionException {
		Tensor_initContext _localctx = new Tensor_initContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_tensor_init);
		int _la;
		try {
			setState(316);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,23,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(294);
				match(LBRACKET);
				setState(295);
				literal();
				setState(300);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(296);
					match(COMMA);
					setState(297);
					literal();
					}
					}
					setState(302);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(303);
				match(RBRACKET);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(305);
				match(LBRACKET);
				setState(306);
				tensor_init();
				setState(311);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(307);
					match(COMMA);
					setState(308);
					tensor_init();
					}
					}
					setState(313);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(314);
				match(RBRACKET);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Tensor_accesContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(grammarProyectoParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(grammarProyectoParser.ID, i);
		}
		public List<TerminalNode> LBRACKET() { return getTokens(grammarProyectoParser.LBRACKET); }
		public TerminalNode LBRACKET(int i) {
			return getToken(grammarProyectoParser.LBRACKET, i);
		}
		public List<TerminalNode> RBRACKET() { return getTokens(grammarProyectoParser.RBRACKET); }
		public TerminalNode RBRACKET(int i) {
			return getToken(grammarProyectoParser.RBRACKET, i);
		}
		public List<TerminalNode> CONT() { return getTokens(grammarProyectoParser.CONT); }
		public TerminalNode CONT(int i) {
			return getToken(grammarProyectoParser.CONT, i);
		}
		public List<TerminalNode> FLOAT() { return getTokens(grammarProyectoParser.FLOAT); }
		public TerminalNode FLOAT(int i) {
			return getToken(grammarProyectoParser.FLOAT, i);
		}
		public Tensor_accesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tensor_acces; }
	}

	public final Tensor_accesContext tensor_acces() throws RecognitionException {
		Tensor_accesContext _localctx = new Tensor_accesContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_tensor_acces);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(318);
			match(ID);
			setState(319);
			match(LBRACKET);
			setState(320);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 29360128L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(321);
			match(RBRACKET);
			setState(327);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(322);
					match(LBRACKET);
					setState(323);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 29360128L) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(324);
					match(RBRACKET);
					}
					} 
				}
				setState(329);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,24,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 15:
			return boolean_expr_sempred((Boolean_exprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean boolean_expr_sempred(Boolean_exprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u00014\u014b\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0001\u0000\u0001\u0000\u0005\u0000C\b\u0000"+
		"\n\u0000\f\u0000F\t\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005"+
		"c\b\u0005\u0001\u0006\u0001\u0006\u0005\u0006g\b\u0006\n\u0006\f\u0006"+
		"j\t\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006"+
		"p\b\u0006\n\u0006\f\u0006s\t\u0006\u0001\u0006\u0001\u0006\u0005\u0006"+
		"w\b\u0006\n\u0006\f\u0006z\t\u0006\u0001\u0006\u0003\u0006}\b\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0005\b\u0082\b\b\n\b\f\b\u0085\t\b\u0001\t"+
		"\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0003\n\u0091\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0003\u000b\u0098\b\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0003\f\u00a0\b\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0003\r\u00ac\b\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u00bf\b\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u00c4\b\u000f\n\u000f"+
		"\f\u000f\u00c7\t\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0005\u0013\u00e1\b\u0013\n\u0013\f\u0013\u00e4"+
		"\t\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0005\u0014\u00e9\b\u0014"+
		"\n\u0014\f\u0014\u00ec\t\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015\u00f6"+
		"\b\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0005\u0017\u0100\b\u0017\n\u0017\f\u0017"+
		"\u0103\t\u0017\u0001\u0017\u0003\u0017\u0106\b\u0017\u0001\u0018\u0001"+
		"\u0018\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001c\u0001"+
		"\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0001\u001c\u0003\u001c\u011a"+
		"\b\u001c\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0003\u001d\u0120"+
		"\b\u001d\u0001\u001d\u0004\u001d\u0123\b\u001d\u000b\u001d\f\u001d\u0124"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0005\u001e\u012b\b\u001e"+
		"\n\u001e\f\u001e\u012e\t\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001e\u0005\u001e\u0136\b\u001e\n\u001e\f\u001e"+
		"\u0139\t\u001e\u0001\u001e\u0001\u001e\u0003\u001e\u013d\b\u001e\u0001"+
		"\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0005\u001f\u0146\b\u001f\n\u001f\f\u001f\u0149\t\u001f\u0001\u001f"+
		"\u0000\u0001\u001e \u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>\u0000\b\u0001\u0000\u0002"+
		"\u0005\u0001\u000001\u0001\u0000\u000b\f\u0001\u0000\u001a\u001b\u0001"+
		"\u0000\u001c\u001d\u0002\u0000\u0017\u001934\u0001\u0000*/\u0001\u0000"+
		"\u0016\u0018\u014d\u0000@\u0001\u0000\u0000\u0000\u0002G\u0001\u0000\u0000"+
		"\u0000\u0004M\u0001\u0000\u0000\u0000\u0006S\u0001\u0000\u0000\u0000\b"+
		"Z\u0001\u0000\u0000\u0000\nb\u0001\u0000\u0000\u0000\f|\u0001\u0000\u0000"+
		"\u0000\u000e~\u0001\u0000\u0000\u0000\u0010\u0083\u0001\u0000\u0000\u0000"+
		"\u0012\u0086\u0001\u0000\u0000\u0000\u0014\u0090\u0001\u0000\u0000\u0000"+
		"\u0016\u0092\u0001\u0000\u0000\u0000\u0018\u009b\u0001\u0000\u0000\u0000"+
		"\u001a\u00a3\u0001\u0000\u0000\u0000\u001c\u00ad\u0001\u0000\u0000\u0000"+
		"\u001e\u00be\u0001\u0000\u0000\u0000 \u00c8\u0001\u0000\u0000\u0000\""+
		"\u00d4\u0001\u0000\u0000\u0000$\u00d6\u0001\u0000\u0000\u0000&\u00dd\u0001"+
		"\u0000\u0000\u0000(\u00e5\u0001\u0000\u0000\u0000*\u00f5\u0001\u0000\u0000"+
		"\u0000,\u00f7\u0001\u0000\u0000\u0000.\u0105\u0001\u0000\u0000\u00000"+
		"\u0107\u0001\u0000\u0000\u00002\u0109\u0001\u0000\u0000\u00004\u010b\u0001"+
		"\u0000\u0000\u00006\u010f\u0001\u0000\u0000\u00008\u0113\u0001\u0000\u0000"+
		"\u0000:\u0122\u0001\u0000\u0000\u0000<\u013c\u0001\u0000\u0000\u0000>"+
		"\u013e\u0001\u0000\u0000\u0000@D\u0003\u0002\u0001\u0000AC\u0003\u0004"+
		"\u0002\u0000BA\u0001\u0000\u0000\u0000CF\u0001\u0000\u0000\u0000DB\u0001"+
		"\u0000\u0000\u0000DE\u0001\u0000\u0000\u0000E\u0001\u0001\u0000\u0000"+
		"\u0000FD\u0001\u0000\u0000\u0000GH\u0005\u0010\u0000\u0000HI\u0005!\u0000"+
		"\u0000IJ\u0003\u0010\b\u0000JK\u0005\u0011\u0000\u0000KL\u0005#\u0000"+
		"\u0000L\u0003\u0001\u0000\u0000\u0000MN\u0003\u0006\u0003\u0000NO\u0003"+
		"\u0010\b\u0000OP\u0003\b\u0004\u0000PQ\u0005\u0011\u0000\u0000QR\u0005"+
		"#\u0000\u0000R\u0005\u0001\u0000\u0000\u0000ST\u0005\u000e\u0000\u0000"+
		"TU\u0005\u0016\u0000\u0000UV\u0005\u001f\u0000\u0000VW\u0003\f\u0006\u0000"+
		"WX\u0005 \u0000\u0000XY\u0005!\u0000\u0000Y\u0007\u0001\u0000\u0000\u0000"+
		"Z[\u0005\u000f\u0000\u0000[\\\u0003\n\u0005\u0000\\\t\u0001\u0000\u0000"+
		"\u0000]^\u0003&\u0013\u0000^_\u0005#\u0000\u0000_c\u0001\u0000\u0000\u0000"+
		"`a\u0005\u0016\u0000\u0000ac\u0005#\u0000\u0000b]\u0001\u0000\u0000\u0000"+
		"b`\u0001\u0000\u0000\u0000c\u000b\u0001\u0000\u0000\u0000dh\u0003\u0012"+
		"\t\u0000eg\u0003:\u001d\u0000fe\u0001\u0000\u0000\u0000gj\u0001\u0000"+
		"\u0000\u0000hf\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000\u0000ik\u0001"+
		"\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000kx\u0003\u000e\u0007\u0000"+
		"lm\u0005\"\u0000\u0000mq\u0003\u0012\t\u0000np\u0003:\u001d\u0000on\u0001"+
		"\u0000\u0000\u0000ps\u0001\u0000\u0000\u0000qo\u0001\u0000\u0000\u0000"+
		"qr\u0001\u0000\u0000\u0000rt\u0001\u0000\u0000\u0000sq\u0001\u0000\u0000"+
		"\u0000tu\u0003\u000e\u0007\u0000uw\u0001\u0000\u0000\u0000vl\u0001\u0000"+
		"\u0000\u0000wz\u0001\u0000\u0000\u0000xv\u0001\u0000\u0000\u0000xy\u0001"+
		"\u0000\u0000\u0000y}\u0001\u0000\u0000\u0000zx\u0001\u0000\u0000\u0000"+
		"{}\u0001\u0000\u0000\u0000|d\u0001\u0000\u0000\u0000|{\u0001\u0000\u0000"+
		"\u0000}\r\u0001\u0000\u0000\u0000~\u007f\u0005\u0016\u0000\u0000\u007f"+
		"\u000f\u0001\u0000\u0000\u0000\u0080\u0082\u0003\u0014\n\u0000\u0081\u0080"+
		"\u0001\u0000\u0000\u0000\u0082\u0085\u0001\u0000\u0000\u0000\u0083\u0081"+
		"\u0001\u0000\u0000\u0000\u0083\u0084\u0001\u0000\u0000\u0000\u0084\u0011"+
		"\u0001\u0000\u0000\u0000\u0085\u0083\u0001\u0000\u0000\u0000\u0086\u0087"+
		"\u0007\u0000\u0000\u0000\u0087\u0013\u0001\u0000\u0000\u0000\u0088\u0091"+
		"\u0003\u0016\u000b\u0000\u0089\u0091\u0003\u0018\f\u0000\u008a\u0091\u0003"+
		"4\u001a\u0000\u008b\u0091\u00036\u001b\u0000\u008c\u0091\u0003\u001a\r"+
		"\u0000\u008d\u0091\u0003 \u0010\u0000\u008e\u0091\u0003$\u0012\u0000\u008f"+
		"\u0091\u00038\u001c\u0000\u0090\u0088\u0001\u0000\u0000\u0000\u0090\u0089"+
		"\u0001\u0000\u0000\u0000\u0090\u008a\u0001\u0000\u0000\u0000\u0090\u008b"+
		"\u0001\u0000\u0000\u0000\u0090\u008c\u0001\u0000\u0000\u0000\u0090\u008d"+
		"\u0001\u0000\u0000\u0000\u0090\u008e\u0001\u0000\u0000\u0000\u0090\u008f"+
		"\u0001\u0000\u0000\u0000\u0091\u0015\u0001\u0000\u0000\u0000\u0092\u0093"+
		"\u0005\u0001\u0000\u0000\u0093\u0094\u0003\u0012\t\u0000\u0094\u0097\u0005"+
		"\u0016\u0000\u0000\u0095\u0096\u0005\u001e\u0000\u0000\u0096\u0098\u0003"+
		"&\u0013\u0000\u0097\u0095\u0001\u0000\u0000\u0000\u0097\u0098\u0001\u0000"+
		"\u0000\u0000\u0098\u0099\u0001\u0000\u0000\u0000\u0099\u009a\u0005#\u0000"+
		"\u0000\u009a\u0017\u0001\u0000\u0000\u0000\u009b\u009c\u0005\u0016\u0000"+
		"\u0000\u009c\u009f\u0005\u001e\u0000\u0000\u009d\u00a0\u0003&\u0013\u0000"+
		"\u009e\u00a0\u0003<\u001e\u0000\u009f\u009d\u0001\u0000\u0000\u0000\u009f"+
		"\u009e\u0001\u0000\u0000\u0000\u00a0\u00a1\u0001\u0000\u0000\u0000\u00a1"+
		"\u00a2\u0005#\u0000\u0000\u00a2\u0019\u0001\u0000\u0000\u0000\u00a3\u00a4"+
		"\u0005\u0006\u0000\u0000\u00a4\u00a5\u0003\u001e\u000f\u0000\u00a5\u00a6"+
		"\u0005\u0007\u0000\u0000\u00a6\u00a7\u0005!\u0000\u0000\u00a7\u00ab\u0003"+
		"\u0010\b\u0000\u00a8\u00a9\u0005\u0011\u0000\u0000\u00a9\u00ac\u0005#"+
		"\u0000\u0000\u00aa\u00ac\u0003\u001c\u000e\u0000\u00ab\u00a8\u0001\u0000"+
		"\u0000\u0000\u00ab\u00aa\u0001\u0000\u0000\u0000\u00ac\u001b\u0001\u0000"+
		"\u0000\u0000\u00ad\u00ae\u0005\b\u0000\u0000\u00ae\u00af\u0005!\u0000"+
		"\u0000\u00af\u00b0\u0003\u0010\b\u0000\u00b0\u00b1\u0005\u0011\u0000\u0000"+
		"\u00b1\u00b2\u0005#\u0000\u0000\u00b2\u001d\u0001\u0000\u0000\u0000\u00b3"+
		"\u00b4\u0006\u000f\uffff\uffff\u0000\u00b4\u00b5\u0003&\u0013\u0000\u00b5"+
		"\u00b6\u00032\u0019\u0000\u00b6\u00b7\u0003&\u0013\u0000\u00b7\u00bf\u0001"+
		"\u0000\u0000\u0000\u00b8\u00b9\u0005\u001f\u0000\u0000\u00b9\u00ba\u0003"+
		"\u001e\u000f\u0000\u00ba\u00bb\u0005 \u0000\u0000\u00bb\u00bf\u0001\u0000"+
		"\u0000\u0000\u00bc\u00bd\u00052\u0000\u0000\u00bd\u00bf\u0003\u001e\u000f"+
		"\u0001\u00be\u00b3\u0001\u0000\u0000\u0000\u00be\u00b8\u0001\u0000\u0000"+
		"\u0000\u00be\u00bc\u0001\u0000\u0000\u0000\u00bf\u00c5\u0001\u0000\u0000"+
		"\u0000\u00c0\u00c1\n\u0002\u0000\u0000\u00c1\u00c2\u0007\u0001\u0000\u0000"+
		"\u00c2\u00c4\u0003\u001e\u000f\u0003\u00c3\u00c0\u0001\u0000\u0000\u0000"+
		"\u00c4\u00c7\u0001\u0000\u0000\u0000\u00c5\u00c3\u0001\u0000\u0000\u0000"+
		"\u00c5\u00c6\u0001\u0000\u0000\u0000\u00c6\u001f\u0001\u0000\u0000\u0000"+
		"\u00c7\u00c5\u0001\u0000\u0000\u0000\u00c8\u00c9\u0005\t\u0000\u0000\u00c9"+
		"\u00ca\u0005\u0016\u0000\u0000\u00ca\u00cb\u0005\u001e\u0000\u0000\u00cb"+
		"\u00cc\u0005\u0017\u0000\u0000\u00cc\u00cd\u0005\n\u0000\u0000\u00cd\u00ce"+
		"\u0005\u0017\u0000\u0000\u00ce\u00cf\u0003\"\u0011\u0000\u00cf\u00d0\u0005"+
		"!\u0000\u0000\u00d0\u00d1\u0003\u0010\b\u0000\u00d1\u00d2\u0005\u0011"+
		"\u0000\u0000\u00d2\u00d3\u0005#\u0000\u0000\u00d3!\u0001\u0000\u0000\u0000"+
		"\u00d4\u00d5\u0007\u0002\u0000\u0000\u00d5#\u0001\u0000\u0000\u0000\u00d6"+
		"\u00d7\u0005\r\u0000\u0000\u00d7\u00d8\u0003\u001e\u000f\u0000\u00d8\u00d9"+
		"\u0005!\u0000\u0000\u00d9\u00da\u0003\u0010\b\u0000\u00da\u00db\u0005"+
		"\u0011\u0000\u0000\u00db\u00dc\u0005#\u0000\u0000\u00dc%\u0001\u0000\u0000"+
		"\u0000\u00dd\u00e2\u0003(\u0014\u0000\u00de\u00df\u0007\u0003\u0000\u0000"+
		"\u00df\u00e1\u0003(\u0014\u0000\u00e0\u00de\u0001\u0000\u0000\u0000\u00e1"+
		"\u00e4\u0001\u0000\u0000\u0000\u00e2\u00e0\u0001\u0000\u0000\u0000\u00e2"+
		"\u00e3\u0001\u0000\u0000\u0000\u00e3\'\u0001\u0000\u0000\u0000\u00e4\u00e2"+
		"\u0001\u0000\u0000\u0000\u00e5\u00ea\u0003*\u0015\u0000\u00e6\u00e7\u0007"+
		"\u0004\u0000\u0000\u00e7\u00e9\u0003*\u0015\u0000\u00e8\u00e6\u0001\u0000"+
		"\u0000\u0000\u00e9\u00ec\u0001\u0000\u0000\u0000\u00ea\u00e8\u0001\u0000"+
		"\u0000\u0000\u00ea\u00eb\u0001\u0000\u0000\u0000\u00eb)\u0001\u0000\u0000"+
		"\u0000\u00ec\u00ea\u0001\u0000\u0000\u0000\u00ed\u00f6\u00030\u0018\u0000"+
		"\u00ee\u00f6\u0003,\u0016\u0000\u00ef\u00f0\u0005\u001f\u0000\u0000\u00f0"+
		"\u00f1\u0003&\u0013\u0000\u00f1\u00f2\u0005 \u0000\u0000\u00f2\u00f6\u0001"+
		"\u0000\u0000\u0000\u00f3\u00f6\u0005\u0016\u0000\u0000\u00f4\u00f6\u0003"+
		">\u001f\u0000\u00f5\u00ed\u0001\u0000\u0000\u0000\u00f5\u00ee\u0001\u0000"+
		"\u0000\u0000\u00f5\u00ef\u0001\u0000\u0000\u0000\u00f5\u00f3\u0001\u0000"+
		"\u0000\u0000\u00f5\u00f4\u0001\u0000\u0000\u0000\u00f6+\u0001\u0000\u0000"+
		"\u0000\u00f7\u00f8\u0005\u0016\u0000\u0000\u00f8\u00f9\u0005\u001f\u0000"+
		"\u0000\u00f9\u00fa\u0003.\u0017\u0000\u00fa\u00fb\u0005 \u0000\u0000\u00fb"+
		"-\u0001\u0000\u0000\u0000\u00fc\u0101\u0003&\u0013\u0000\u00fd\u00fe\u0005"+
		"\"\u0000\u0000\u00fe\u0100\u0003&\u0013\u0000\u00ff\u00fd\u0001\u0000"+
		"\u0000\u0000\u0100\u0103\u0001\u0000\u0000\u0000\u0101\u00ff\u0001\u0000"+
		"\u0000\u0000\u0101\u0102\u0001\u0000\u0000\u0000\u0102\u0106\u0001\u0000"+
		"\u0000\u0000\u0103\u0101\u0001\u0000\u0000\u0000\u0104\u0106\u0001\u0000"+
		"\u0000\u0000\u0105\u00fc\u0001\u0000\u0000\u0000\u0105\u0104\u0001\u0000"+
		"\u0000\u0000\u0106/\u0001\u0000\u0000\u0000\u0107\u0108\u0007\u0005\u0000"+
		"\u0000\u01081\u0001\u0000\u0000\u0000\u0109\u010a\u0007\u0006\u0000\u0000"+
		"\u010a3\u0001\u0000\u0000\u0000\u010b\u010c\u0005\u0015\u0000\u0000\u010c"+
		"\u010d\u0003&\u0013\u0000\u010d\u010e\u0005#\u0000\u0000\u010e5\u0001"+
		"\u0000\u0000\u0000\u010f\u0110\u0005\u0014\u0000\u0000\u0110\u0111\u0005"+
		"\u0016\u0000\u0000\u0111\u0112\u0005#\u0000\u0000\u01127\u0001\u0000\u0000"+
		"\u0000\u0113\u0114\u0005\u0001\u0000\u0000\u0114\u0115\u0003\u0012\t\u0000"+
		"\u0115\u0116\u0003:\u001d\u0000\u0116\u0119\u0005\u0016\u0000\u0000\u0117"+
		"\u0118\u0005\u001e\u0000\u0000\u0118\u011a\u0003<\u001e\u0000\u0119\u0117"+
		"\u0001\u0000\u0000\u0000\u0119\u011a\u0001\u0000\u0000\u0000\u011a\u011b"+
		"\u0001\u0000\u0000\u0000\u011b\u011c\u0005#\u0000\u0000\u011c9\u0001\u0000"+
		"\u0000\u0000\u011d\u011f\u0005$\u0000\u0000\u011e\u0120\u0005\u0017\u0000"+
		"\u0000\u011f\u011e\u0001\u0000\u0000\u0000\u011f\u0120\u0001\u0000\u0000"+
		"\u0000\u0120\u0121\u0001\u0000\u0000\u0000\u0121\u0123\u0005%\u0000\u0000"+
		"\u0122\u011d\u0001\u0000\u0000\u0000\u0123\u0124\u0001\u0000\u0000\u0000"+
		"\u0124\u0122\u0001\u0000\u0000\u0000\u0124\u0125\u0001\u0000\u0000\u0000"+
		"\u0125;\u0001\u0000\u0000\u0000\u0126\u0127\u0005$\u0000\u0000\u0127\u012c"+
		"\u00030\u0018\u0000\u0128\u0129\u0005\"\u0000\u0000\u0129\u012b\u0003"+
		"0\u0018\u0000\u012a\u0128\u0001\u0000\u0000\u0000\u012b\u012e\u0001\u0000"+
		"\u0000\u0000\u012c\u012a\u0001\u0000\u0000\u0000\u012c\u012d\u0001\u0000"+
		"\u0000\u0000\u012d\u012f\u0001\u0000\u0000\u0000\u012e\u012c\u0001\u0000"+
		"\u0000\u0000\u012f\u0130\u0005%\u0000\u0000\u0130\u013d\u0001\u0000\u0000"+
		"\u0000\u0131\u0132\u0005$\u0000\u0000\u0132\u0137\u0003<\u001e\u0000\u0133"+
		"\u0134\u0005\"\u0000\u0000\u0134\u0136\u0003<\u001e\u0000\u0135\u0133"+
		"\u0001\u0000\u0000\u0000\u0136\u0139\u0001\u0000\u0000\u0000\u0137\u0135"+
		"\u0001\u0000\u0000\u0000\u0137\u0138\u0001\u0000\u0000\u0000\u0138\u013a"+
		"\u0001\u0000\u0000\u0000\u0139\u0137\u0001\u0000\u0000\u0000\u013a\u013b"+
		"\u0005%\u0000\u0000\u013b\u013d\u0001\u0000\u0000\u0000\u013c\u0126\u0001"+
		"\u0000\u0000\u0000\u013c\u0131\u0001\u0000\u0000\u0000\u013d=\u0001\u0000"+
		"\u0000\u0000\u013e\u013f\u0005\u0016\u0000\u0000\u013f\u0140\u0005$\u0000"+
		"\u0000\u0140\u0141\u0007\u0007\u0000\u0000\u0141\u0147\u0005%\u0000\u0000"+
		"\u0142\u0143\u0005$\u0000\u0000\u0143\u0144\u0007\u0007\u0000\u0000\u0144"+
		"\u0146\u0005%\u0000\u0000\u0145\u0142\u0001\u0000\u0000\u0000\u0146\u0149"+
		"\u0001\u0000\u0000\u0000\u0147\u0145\u0001\u0000\u0000\u0000\u0147\u0148"+
		"\u0001\u0000\u0000\u0000\u0148?\u0001\u0000\u0000\u0000\u0149\u0147\u0001"+
		"\u0000\u0000\u0000\u0019Dbhqx|\u0083\u0090\u0097\u009f\u00ab\u00be\u00c5"+
		"\u00e2\u00ea\u00f5\u0101\u0105\u0119\u011f\u0124\u012c\u0137\u013c\u0147";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}