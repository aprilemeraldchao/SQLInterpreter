# Generated from SQLGrammar.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("\u00a4\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\6\2\34\n\2\r\2\16\2\35\3\2\3\2\3\3\5\3#\n\3\3\3\3\3\5")
        buf.write("\3\'\n\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4\61\n\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\5\59\n\5\3\5\3\5\3\5\3\5\7\5?\n")
        buf.write("\5\f\5\16\5B\13\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7T\n\7\3\7\3\7\5\7X\n\7")
        buf.write("\3\7\3\7\5\7\\\n\7\3\7\3\7\5\7`\n\7\3\7\7\7c\n\7\f\7\16")
        buf.write("\7f\13\7\3\7\5\7i\n\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t}\n\t\3\t")
        buf.write("\3\t\5\t\u0081\n\t\3\t\5\t\u0084\n\t\3\n\5\n\u0087\n\n")
        buf.write("\3\n\3\n\3\n\3\n\5\n\u008d\n\n\3\13\3\13\5\13\u0091\n")
        buf.write("\13\3\13\3\13\5\13\u0095\n\13\3\13\7\13\u0098\n\13\f\13")
        buf.write("\16\13\u009b\13\13\3\13\5\13\u009e\n\13\3\f\3\f\3\r\3")
        buf.write("\r\3\r\2\2\16\2\4\6\b\n\f\16\20\22\24\26\30\2\4\3\2\23")
        buf.write("\24\3\2\27\30\2\u00af\2\33\3\2\2\2\4\"\3\2\2\2\6\60\3")
        buf.write("\2\2\2\b\62\3\2\2\2\nE\3\2\2\2\fK\3\2\2\2\16l\3\2\2\2")
        buf.write("\20p\3\2\2\2\22\u0086\3\2\2\2\24\u009d\3\2\2\2\26\u009f")
        buf.write("\3\2\2\2\30\u00a1\3\2\2\2\32\34\5\4\3\2\33\32\3\2\2\2")
        buf.write("\34\35\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2\36\37\3\2\2")
        buf.write("\2\37 \7\2\2\3 \3\3\2\2\2!#\7\31\2\2\"!\3\2\2\2\"#\3\2")
        buf.write("\2\2#$\3\2\2\2$&\5\6\4\2%\'\7\31\2\2&%\3\2\2\2&\'\3\2")
        buf.write("\2\2\'(\3\2\2\2()\7\3\2\2)*\7\31\2\2*\5\3\2\2\2+\61\5")
        buf.write("\b\5\2,\61\5\n\6\2-\61\5\f\7\2.\61\5\16\b\2/\61\5\20\t")
        buf.write("\2\60+\3\2\2\2\60,\3\2\2\2\60-\3\2\2\2\60.\3\2\2\2\60")
        buf.write("/\3\2\2\2\61\7\3\2\2\2\62\63\7\b\2\2\63\64\7\31\2\2\64")
        buf.write("\65\7\t\2\2\65\66\7\31\2\2\668\7\25\2\2\679\7\31\2\28")
        buf.write("\67\3\2\2\289\3\2\2\29:\3\2\2\2:;\7\4\2\2;@\5\22\n\2<")
        buf.write("=\7\5\2\2=?\5\22\n\2><\3\2\2\2?B\3\2\2\2@>\3\2\2\2@A\3")
        buf.write("\2\2\2AC\3\2\2\2B@\3\2\2\2CD\7\6\2\2D\t\3\2\2\2EF\7\n")
        buf.write("\2\2FG\7\31\2\2GH\7\t\2\2HI\7\31\2\2IJ\7\25\2\2J\13\3")
        buf.write("\2\2\2KL\7\13\2\2LM\7\31\2\2MN\7\f\2\2NO\7\31\2\2OP\7")
        buf.write("\25\2\2PQ\7\31\2\2QS\7\r\2\2RT\7\31\2\2SR\3\2\2\2ST\3")
        buf.write("\2\2\2TU\3\2\2\2UW\7\4\2\2VX\7\31\2\2WV\3\2\2\2WX\3\2")
        buf.write("\2\2XY\3\2\2\2Yd\5\30\r\2Z\\\7\31\2\2[Z\3\2\2\2[\\\3\2")
        buf.write("\2\2\\]\3\2\2\2]_\7\5\2\2^`\7\31\2\2_^\3\2\2\2_`\3\2\2")
        buf.write("\2`a\3\2\2\2ac\5\30\r\2b[\3\2\2\2cf\3\2\2\2db\3\2\2\2")
        buf.write("de\3\2\2\2eh\3\2\2\2fd\3\2\2\2gi\7\31\2\2hg\3\2\2\2hi")
        buf.write("\3\2\2\2ij\3\2\2\2jk\7\6\2\2k\r\3\2\2\2lm\7\16\2\2mn\7")
        buf.write("\31\2\2no\7\17\2\2o\17\3\2\2\2pq\7\20\2\2qr\7\31\2\2r")
        buf.write("s\5\24\13\2st\7\31\2\2tu\7\21\2\2uv\7\31\2\2v\u0083\7")
        buf.write("\25\2\2wx\7\31\2\2xy\7\22\2\2yz\7\31\2\2z|\7\25\2\2{}")
        buf.write("\7\31\2\2|{\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\u0080\7\7\2\2")
        buf.write("\177\u0081\7\31\2\2\u0080\177\3\2\2\2\u0080\u0081\3\2")
        buf.write("\2\2\u0081\u0082\3\2\2\2\u0082\u0084\5\30\r\2\u0083w\3")
        buf.write("\2\2\2\u0083\u0084\3\2\2\2\u0084\21\3\2\2\2\u0085\u0087")
        buf.write("\7\31\2\2\u0086\u0085\3\2\2\2\u0086\u0087\3\2\2\2\u0087")
        buf.write("\u0088\3\2\2\2\u0088\u0089\7\25\2\2\u0089\u008a\7\31\2")
        buf.write("\2\u008a\u008c\5\26\f\2\u008b\u008d\7\31\2\2\u008c\u008b")
        buf.write("\3\2\2\2\u008c\u008d\3\2\2\2\u008d\23\3\2\2\2\u008e\u0099")
        buf.write("\7\25\2\2\u008f\u0091\7\31\2\2\u0090\u008f\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\u0092\3\2\2\2\u0092\u0094\7\5\2\2")
        buf.write("\u0093\u0095\7\31\2\2\u0094\u0093\3\2\2\2\u0094\u0095")
        buf.write("\3\2\2\2\u0095\u0096\3\2\2\2\u0096\u0098\7\25\2\2\u0097")
        buf.write("\u0090\3\2\2\2\u0098\u009b\3\2\2\2\u0099\u0097\3\2\2\2")
        buf.write("\u0099\u009a\3\2\2\2\u009a\u009e\3\2\2\2\u009b\u0099\3")
        buf.write("\2\2\2\u009c\u009e\7\26\2\2\u009d\u008e\3\2\2\2\u009d")
        buf.write("\u009c\3\2\2\2\u009e\25\3\2\2\2\u009f\u00a0\t\2\2\2\u00a0")
        buf.write("\27\3\2\2\2\u00a1\u00a2\t\3\2\2\u00a2\31\3\2\2\2\27\35")
        buf.write("\"&\608@SW[_dh|\u0080\u0083\u0086\u008c\u0090\u0094\u0099")
        buf.write("\u009d")
        return buf.getvalue()


class SQLGrammarParser ( Parser ):

    grammarFileName = "SQLGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "','", "')'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "CREATE", "TABLE", "DROP", 
                      "INSERT", "INTO", "VALUES", "SHOW", "TABLES", "SELECT", 
                      "FROM", "WHERE", "STRING", "INT", "NAME", "STAR", 
                      "STRING_VALUE", "INT_VALUE", "WS" ]

    RULE_statements = 0
    RULE_statement = 1
    RULE_query = 2
    RULE_create = 3
    RULE_drop = 4
    RULE_insert = 5
    RULE_show = 6
    RULE_select = 7
    RULE_column_definition = 8
    RULE_columns = 9
    RULE_data_type = 10
    RULE_value = 11

    ruleNames =  [ "statements", "statement", "query", "create", "drop", 
                   "insert", "show", "select", "column_definition", "columns", 
                   "data_type", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    CREATE=6
    TABLE=7
    DROP=8
    INSERT=9
    INTO=10
    VALUES=11
    SHOW=12
    TABLES=13
    SELECT=14
    FROM=15
    WHERE=16
    STRING=17
    INT=18
    NAME=19
    STAR=20
    STRING_VALUE=21
    INT_VALUE=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SQLGrammarParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLGrammarParser.StatementContext)
            else:
                return self.getTypedRuleContext(SQLGrammarParser.StatementContext,i)


        def getRuleIndex(self):
            return SQLGrammarParser.RULE_statements

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatements" ):
                listener.enterStatements(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatements" ):
                listener.exitStatements(self)




    def statements(self):

        localctx = SQLGrammarParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.statement()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SQLGrammarParser.CREATE) | (1 << SQLGrammarParser.DROP) | (1 << SQLGrammarParser.INSERT) | (1 << SQLGrammarParser.SHOW) | (1 << SQLGrammarParser.SELECT) | (1 << SQLGrammarParser.WS))) != 0)):
                    break

            self.state = 29
            self.match(SQLGrammarParser.EOF)
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

        def query(self):
            return self.getTypedRuleContext(SQLGrammarParser.QueryContext,0)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SQLGrammarParser.WS)
            else:
                return self.getToken(SQLGrammarParser.WS, i)

        def getRuleIndex(self):
            return SQLGrammarParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = SQLGrammarParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLGrammarParser.WS:
                self.state = 31
                self.match(SQLGrammarParser.WS)


            self.state = 34
            self.query()
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLGrammarParser.WS:
                self.state = 35
                self.match(SQLGrammarParser.WS)


            self.state = 38
            self.match(SQLGrammarParser.T__0)
            self.state = 39
            self.match(SQLGrammarParser.WS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def create(self):
            return self.getTypedRuleContext(SQLGrammarParser.CreateContext,0)


        def drop(self):
            return self.getTypedRuleContext(SQLGrammarParser.DropContext,0)


        def insert(self):
            return self.getTypedRuleContext(SQLGrammarParser.InsertContext,0)


        def show(self):
            return self.getTypedRuleContext(SQLGrammarParser.ShowContext,0)


        def select(self):
            return self.getTypedRuleContext(SQLGrammarParser.SelectContext,0)


        def getRuleIndex(self):
            return SQLGrammarParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuery" ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuery" ):
                listener.exitQuery(self)




    def query(self):

        localctx = SQLGrammarParser.QueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_query)
        try:
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLGrammarParser.CREATE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.create()
                pass
            elif token in [SQLGrammarParser.DROP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.drop()
                pass
            elif token in [SQLGrammarParser.INSERT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.insert()
                pass
            elif token in [SQLGrammarParser.SHOW]:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.show()
                pass
            elif token in [SQLGrammarParser.SELECT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 45
                self.select()
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


    class CreateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(SQLGrammarParser.CREATE, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SQLGrammarParser.WS)
            else:
                return self.getToken(SQLGrammarParser.WS, i)

        def TABLE(self):
            return self.getToken(SQLGrammarParser.TABLE, 0)

        def NAME(self):
            return self.getToken(SQLGrammarParser.NAME, 0)

        def column_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLGrammarParser.Column_definitionContext)
            else:
                return self.getTypedRuleContext(SQLGrammarParser.Column_definitionContext,i)


        def getRuleIndex(self):
            return SQLGrammarParser.RULE_create

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreate" ):
                listener.enterCreate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreate" ):
                listener.exitCreate(self)




    def create(self):

        localctx = SQLGrammarParser.CreateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_create)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(SQLGrammarParser.CREATE)
            self.state = 49
            self.match(SQLGrammarParser.WS)
            self.state = 50
            self.match(SQLGrammarParser.TABLE)
            self.state = 51
            self.match(SQLGrammarParser.WS)
            self.state = 52
            self.match(SQLGrammarParser.NAME)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLGrammarParser.WS:
                self.state = 53
                self.match(SQLGrammarParser.WS)


            self.state = 56
            self.match(SQLGrammarParser.T__1)
            self.state = 57
            self.column_definition()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SQLGrammarParser.T__2:
                self.state = 58
                self.match(SQLGrammarParser.T__2)
                self.state = 59
                self.column_definition()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
            self.match(SQLGrammarParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DROP(self):
            return self.getToken(SQLGrammarParser.DROP, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SQLGrammarParser.WS)
            else:
                return self.getToken(SQLGrammarParser.WS, i)

        def TABLE(self):
            return self.getToken(SQLGrammarParser.TABLE, 0)

        def NAME(self):
            return self.getToken(SQLGrammarParser.NAME, 0)

        def getRuleIndex(self):
            return SQLGrammarParser.RULE_drop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrop" ):
                listener.enterDrop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrop" ):
                listener.exitDrop(self)




    def drop(self):

        localctx = SQLGrammarParser.DropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_drop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(SQLGrammarParser.DROP)
            self.state = 68
            self.match(SQLGrammarParser.WS)
            self.state = 69
            self.match(SQLGrammarParser.TABLE)
            self.state = 70
            self.match(SQLGrammarParser.WS)
            self.state = 71
            self.match(SQLGrammarParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsertContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSERT(self):
            return self.getToken(SQLGrammarParser.INSERT, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SQLGrammarParser.WS)
            else:
                return self.getToken(SQLGrammarParser.WS, i)

        def INTO(self):
            return self.getToken(SQLGrammarParser.INTO, 0)

        def NAME(self):
            return self.getToken(SQLGrammarParser.NAME, 0)

        def VALUES(self):
            return self.getToken(SQLGrammarParser.VALUES, 0)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLGrammarParser.ValueContext)
            else:
                return self.getTypedRuleContext(SQLGrammarParser.ValueContext,i)


        def getRuleIndex(self):
            return SQLGrammarParser.RULE_insert

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsert" ):
                listener.enterInsert(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsert" ):
                listener.exitInsert(self)




    def insert(self):

        localctx = SQLGrammarParser.InsertContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_insert)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(SQLGrammarParser.INSERT)
            self.state = 74
            self.match(SQLGrammarParser.WS)
            self.state = 75
            self.match(SQLGrammarParser.INTO)
            self.state = 76
            self.match(SQLGrammarParser.WS)
            self.state = 77
            self.match(SQLGrammarParser.NAME)
            self.state = 78
            self.match(SQLGrammarParser.WS)
            self.state = 79
            self.match(SQLGrammarParser.VALUES)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLGrammarParser.WS:
                self.state = 80
                self.match(SQLGrammarParser.WS)


            self.state = 83
            self.match(SQLGrammarParser.T__1)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLGrammarParser.WS:
                self.state = 84
                self.match(SQLGrammarParser.WS)


            self.state = 87
            self.value()
            self.state = 98
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 89
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==SQLGrammarParser.WS:
                        self.state = 88
                        self.match(SQLGrammarParser.WS)


                    self.state = 91
                    self.match(SQLGrammarParser.T__2)
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==SQLGrammarParser.WS:
                        self.state = 92
                        self.match(SQLGrammarParser.WS)


                    self.state = 95
                    self.value() 
                self.state = 100
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLGrammarParser.WS:
                self.state = 101
                self.match(SQLGrammarParser.WS)


            self.state = 104
            self.match(SQLGrammarParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SHOW(self):
            return self.getToken(SQLGrammarParser.SHOW, 0)

        def WS(self):
            return self.getToken(SQLGrammarParser.WS, 0)

        def TABLES(self):
            return self.getToken(SQLGrammarParser.TABLES, 0)

        def getRuleIndex(self):
            return SQLGrammarParser.RULE_show

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShow" ):
                listener.enterShow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShow" ):
                listener.exitShow(self)




    def show(self):

        localctx = SQLGrammarParser.ShowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_show)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(SQLGrammarParser.SHOW)
            self.state = 107
            self.match(SQLGrammarParser.WS)
            self.state = 108
            self.match(SQLGrammarParser.TABLES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(SQLGrammarParser.SELECT, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SQLGrammarParser.WS)
            else:
                return self.getToken(SQLGrammarParser.WS, i)

        def columns(self):
            return self.getTypedRuleContext(SQLGrammarParser.ColumnsContext,0)


        def FROM(self):
            return self.getToken(SQLGrammarParser.FROM, 0)

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(SQLGrammarParser.NAME)
            else:
                return self.getToken(SQLGrammarParser.NAME, i)

        def WHERE(self):
            return self.getToken(SQLGrammarParser.WHERE, 0)

        def value(self):
            return self.getTypedRuleContext(SQLGrammarParser.ValueContext,0)


        def getRuleIndex(self):
            return SQLGrammarParser.RULE_select

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect" ):
                listener.enterSelect(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect" ):
                listener.exitSelect(self)




    def select(self):

        localctx = SQLGrammarParser.SelectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_select)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(SQLGrammarParser.SELECT)
            self.state = 111
            self.match(SQLGrammarParser.WS)
            self.state = 112
            self.columns()
            self.state = 113
            self.match(SQLGrammarParser.WS)
            self.state = 114
            self.match(SQLGrammarParser.FROM)
            self.state = 115
            self.match(SQLGrammarParser.WS)
            self.state = 116
            self.match(SQLGrammarParser.NAME)
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 117
                self.match(SQLGrammarParser.WS)
                self.state = 118
                self.match(SQLGrammarParser.WHERE)
                self.state = 119
                self.match(SQLGrammarParser.WS)
                self.state = 120
                self.match(SQLGrammarParser.NAME)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLGrammarParser.WS:
                    self.state = 121
                    self.match(SQLGrammarParser.WS)


                self.state = 124
                self.match(SQLGrammarParser.T__4)
                self.state = 126
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==SQLGrammarParser.WS:
                    self.state = 125
                    self.match(SQLGrammarParser.WS)


                self.state = 128
                self.value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(SQLGrammarParser.NAME, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SQLGrammarParser.WS)
            else:
                return self.getToken(SQLGrammarParser.WS, i)

        def data_type(self):
            return self.getTypedRuleContext(SQLGrammarParser.Data_typeContext,0)


        def getRuleIndex(self):
            return SQLGrammarParser.RULE_column_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_definition" ):
                listener.enterColumn_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_definition" ):
                listener.exitColumn_definition(self)




    def column_definition(self):

        localctx = SQLGrammarParser.Column_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_column_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLGrammarParser.WS:
                self.state = 131
                self.match(SQLGrammarParser.WS)


            self.state = 134
            self.match(SQLGrammarParser.NAME)
            self.state = 135
            self.match(SQLGrammarParser.WS)
            self.state = 136
            self.data_type()
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SQLGrammarParser.WS:
                self.state = 137
                self.match(SQLGrammarParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(SQLGrammarParser.NAME)
            else:
                return self.getToken(SQLGrammarParser.NAME, i)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(SQLGrammarParser.WS)
            else:
                return self.getToken(SQLGrammarParser.WS, i)

        def STAR(self):
            return self.getToken(SQLGrammarParser.STAR, 0)

        def getRuleIndex(self):
            return SQLGrammarParser.RULE_columns

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumns" ):
                listener.enterColumns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumns" ):
                listener.exitColumns(self)




    def columns(self):

        localctx = SQLGrammarParser.ColumnsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_columns)
        self._la = 0 # Token type
        try:
            self.state = 155
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SQLGrammarParser.NAME]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(SQLGrammarParser.NAME)
                self.state = 151
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 142
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==SQLGrammarParser.WS:
                            self.state = 141
                            self.match(SQLGrammarParser.WS)


                        self.state = 144
                        self.match(SQLGrammarParser.T__2)
                        self.state = 146
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==SQLGrammarParser.WS:
                            self.state = 145
                            self.match(SQLGrammarParser.WS)


                        self.state = 148
                        self.match(SQLGrammarParser.NAME) 
                    self.state = 153
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                pass
            elif token in [SQLGrammarParser.STAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.match(SQLGrammarParser.STAR)
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


    class Data_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SQLGrammarParser.STRING, 0)

        def INT(self):
            return self.getToken(SQLGrammarParser.INT, 0)

        def getRuleIndex(self):
            return SQLGrammarParser.RULE_data_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_type" ):
                listener.enterData_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_type" ):
                listener.exitData_type(self)




    def data_type(self):

        localctx = SQLGrammarParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_data_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            _la = self._input.LA(1)
            if not(_la==SQLGrammarParser.STRING or _la==SQLGrammarParser.INT):
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


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_VALUE(self):
            return self.getToken(SQLGrammarParser.STRING_VALUE, 0)

        def INT_VALUE(self):
            return self.getToken(SQLGrammarParser.INT_VALUE, 0)

        def getRuleIndex(self):
            return SQLGrammarParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = SQLGrammarParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            _la = self._input.LA(1)
            if not(_la==SQLGrammarParser.STRING_VALUE or _la==SQLGrammarParser.INT_VALUE):
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





