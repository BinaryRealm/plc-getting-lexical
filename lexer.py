import re
tokens=[]
input = """07 1234u hello_world + 123.456e-67 { } 0.56 abc1 0x1.ep+3 2.0e+308 1.0e-324"""

lexeme=""
special_symbols=["+", "-", "*", "/", "=", "(", ")", "{", "}", "[", "]"]
identifier = re.compile("[A-Za-z][A-Za-z0-9_]*")

number = re.compile("(0[0-7]*)(ul|UL|Ul|uL|lu|LU|Lu|lU|u|l|U|L)?|([1-9][0-9]*)(ul|UL|Ul|uL|lu|LU|Lu|lU|u|l|U|L)?|(0(x|X)[0-9A-Fa-f][0-9A-Fa-f]*)(ul|UL|Ul|uL|lu|LU|Lu|lU|u|l|U|L)?")

float = re.compile("[0-9][0-9]*(e|E)(\+|-)?[0-9][0-9]*(fl|FL|Fl|fL|lf|LF|Lf|lF|f|l|F|L)?|[0-9][0-9]*(\.)?(e|E)(\+|-)?[0-9][0-9]*(fl|FL|Fl|fL|lf|LF|Lf|lF|f|l|F|L)?|[0-9][0-9]*\.[0-9][0-9]*(e|E)(\+|-)?[0-9][0-9]*(fl|FL|Fl|fL|lf|LF|Lf|lF|f|l|F|L)?|[0-9][0-9]*\.[0-9][0-9]*(fl|FL|Fl|fL|lf|LF|Lf|lF|f|l|F|L)?|[0-9][0-9]*\.(fl|FL|Fl|fL|lf|LF|Lf|lF|f|l|F|L)?|\.[0-9][0-9]*(e|E)(\+|-)?[0-9][0-9]*(fl|FL|Fl|fL|lf|LF|Lf|lF|f|l|F|L)?|\.[0-9][0-9]*(fl|FL|Fl|fL|lf|LF|Lf|lF|f|l|F|L)?|0(x|X)[0-9A-Fa-f][0-9A-Fa-f]*(\.)?(p|P)(\+|-)?[0-9][0-9]*(fl|FL|Fl|fL|lf|LF|Lf|lF|f|l|F|L)?|0(x|X)[0-9A-Fa-f][0-9A-Fa-f]*\.[0-9A-Fa-f][0-9A-Fa-f]*(p|P)(\+|-)?[0-9][0-9]*(fl|FL|Fl|fL|lf|LF|Lf|lF|f|l|F|L)?|0(x|X)*\.[0-9A-Fa-f][0-9A-Fa-f]*(p|P)(\+|-)?[0-9][0-9]*(fl|FL|Fl|fL|lf|LF|Lf|lF|f|l|F|L)?")

whitespace = re.compile("\s")
length = len(input)

identifier_state = False
number_state = False
float_state = False
i=0
while i < length:
    lexeme+=input[i]
    if i!=length-1:
        if(len(lexeme)==1):
            m = identifier.fullmatch(lexeme)
            n = number.fullmatch(lexeme)
            if m:
                identifier_state = True
            elif n:
                number_state = True
            elif lexeme=="." and float.fullmatch("."+input[i+1]):
                number_state = True
            elif lexeme in special_symbols:
                tokens.append(("special symbol", lexeme))
                lexeme=""
            elif whitespace.fullmatch(lexeme):
                lexeme=""
            else:
                print("lexer error: invalid character")
                break
        elif identifier_state==True:
            m = identifier.fullmatch(lexeme+input[i+1])
            if m:
                ""
            else:
                if input[i+1] not in special_symbols and whitespace.fullmatch(input[i+1])==None:
                    print("lexer error: invalid character")
                    break
                identifier_state = False
                tokens.append(("identifier", lexeme))
                lexeme=""
        elif number_state==True:
            m = number.fullmatch(lexeme+input[i+1])
            n = float.fullmatch(lexeme+input[i+1])
            if m:
                ""
            elif n:
                float_state = True
            else:
                if input[i+1] not in special_symbols and whitespace.fullmatch(input[i+1])==None and input[i+1] not in ["e", "E", "p", "P", "."]:
                    print("lexer error: invalid character")
                    break
                if float_state==True and ((input[i+1] in ["e", "E", "p", "P"]) or ((input[i] in ["e", "E", "p", "P"]) and (input[i+1] in ["+", "-"]))) or input[i+1]==".":
                    float_state = True
                else:
                    if float_state:
                        tokens.append(("float", lexeme))
                    else:
                        tokens.append(("integer", lexeme))
                    number_state = False
                    lexeme=""
        i+=1
    else:
        if identifier.fullmatch(lexeme):
            tokens.append(("identifier", lexeme))
        elif number.fullmatch(lexeme):
            tokens.append(("integer", lexeme))
        elif float.fullmatch(lexeme):
            tokens.append(("float", lexeme))
        elif lexeme in special_symbols:
            tokens.append(("special symbol", lexeme))
        else:
            print("lexer error: invalid character")
        break

print(tokens)

