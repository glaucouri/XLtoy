# inspired to: excelExpr by Paul McGuire


from pyparsing import (
    CaselessKeyword,
    Suppress,
    Word,
    alphas,
    alphanums,
    nums,
    Optional,
    Group,
    oneOf,
    Forward,
    infixNotation,
    opAssoc,
    dblQuotedString,
    delimitedList,
    Combine,
    Literal,
    QuotedString,
    ParserElement,
    pyparsing_common as ppc,
)

ParserElement.enablePackrat()

EQ, LPAR, RPAR, COLON, COMMA = map(Suppress, "=():,")
EXCL, DOLLAR = map(Literal, "!$")
sheetRef = Word(alphas, alphanums + '_') | QuotedString("'", escQuote="''")
colRef = Optional(DOLLAR) + Word(alphas, max=2)
rowRef = Optional(DOLLAR) + Word(nums)
cellRef = Combine(
    Group(Optional(sheetRef + EXCL)("sheet") + colRef("col") + rowRef("row"))
)

cellRange = (
    Group(cellRef("start") + COLON + cellRef("end"))("range")
    | cellRef
    | Word(alphas, alphanums)
)('cells')

expr = Forward()

COMPARISON_OP = oneOf("< = > >= <= != <>")
condExpr = expr + Optional(COMPARISON_OP + expr)

ifFunc = (
    CaselessKeyword("if")
    - LPAR
    + Group(condExpr)("condition")
    + COMMA
    + Group(expr)("if_true")
    + COMMA
    + Group(expr)("if_false")
    + RPAR
)


def stat_function(name):
    return Group(CaselessKeyword(name) + Group(LPAR + delimitedList(expr) + RPAR))


sumFunc = stat_function("sum")
minFunc = stat_function("min")
maxFunc = stat_function("max")
aveFunc = stat_function("ave")
funcCall = ifFunc | sumFunc | minFunc | maxFunc | aveFunc

multOp = oneOf("* /")
addOp = oneOf("+ -")
numericLiteral = ppc.number
operand = numericLiteral | funcCall | cellRange | cellRef
arithExpr = infixNotation(
    operand, [(multOp, 2, opAssoc.LEFT),
              ( addOp, 2, opAssoc.LEFT)]
)

textOperand = dblQuotedString | cellRef
textExpr = infixNotation(textOperand, [("&", 2, opAssoc.LEFT),])

expr <<= arithExpr | textExpr

bnf = EQ+expr
xl_parse = bnf.parseString