# indentedGrammarExample.py
#
# Copyright (c) 2006, Paul McGuire
#
# A sample of a pyparsing grammar using indentation for 
# grouping (like Python does).
#

from pyparsing import *


indentStack = [1]

def checkPeerIndent(s,l,t):
    curCol = col(l,s)
    if curCol != indentStack[-1]:
        if (not indentStack) or curCol > indentStack[-1]:
            raise ParseFatalException(s,l,"illegal nesting")
        raise ParseException(s,l,"not a peer entry")

def checkSubIndent(s,l,t):
    curCol = col(l,s)
    if curCol > indentStack[-1]:
        indentStack.append( curCol )
    else:
        raise ParseException(s,l,"not a subentry")

def checkUnindent(s,l,t):
    if l >= len(s): return
    curCol = col(l,s)
    if not(curCol < indentStack[-1] and curCol <= indentStack[-2]):
        raise ParseException(s,l,"not an unindent")

def doUnindent():
    indentStack.pop()
    
INDENT = lineEnd.suppress() + empty + empty.copy().setParseAction(checkSubIndent)
UNDENT = FollowedBy(empty).setParseAction(checkUnindent)
UNDENT.setParseAction(doUnindent)

stmt = Forward()
suite = Group( OneOrMore( empty + stmt.setParseAction( checkPeerIndent ) )  )

identifier = Word(alphas, alphanums)
val = nums | quotedString
rhs = val | identifier

cssid = Group("#" + Word(alphas,alphanums))
csscls = Group("." + Word(alphas,alphanums))
otheratt = Group(identifier + "=" + rhs)

attr = cssid | csscls | otheratt

args = Optional( Group( "(" + delimitedList(attr)  + ")" ) )

tagLine = (identifier + args + ":")
tagApp = Group( tagLine + INDENT + suite + UNDENT )

oneLine = Group(identifier + args + ":" + rhs )


stmt << ( tagApp | oneLine | identifier )



def htmlIt(ts,depth=0) :       
    ind = "  " * depth

    if isinstance(ts, basestring) :
        return ind + ts + "\n"
        
    if len(ts) == 1 :        
        return htmlIt(ts[0])
                    
    if ts[0] == '(' :
        i = 1
        s = ""
        while ts[i] != ')' :
            if ts[i][0]=='#' :
                s = s + " id='%s'" % ts[i][1]
            elif ts[i][0]=='.' :
                s = s + " class='%s'" % ts[i][1]
            elif len(ts[i]) == 3 and ts[i][1] == '=' :
                s = s + " %s='%s'" % (ts[i][0],ts[i][2])
            i=i+1
        return s
    
    elif len(ts)==3 :
        if ts[1] == ':' :
            tag = ind + "<"+ts[0]+">\n"
            ctag = ind + "</"+ts[0]+">\n"        
            middle = "".join([htmlIt(x,depth+1) for x in ts[2]])
            return tag + middle + ctag
            
    else :        
        tag = ind + "<"+ts[0]+ htmlIt(ts[1]) + ">\n"
        ctag = ind + "</"+ts[0]+">\n"        
        middle = "".join([htmlIt(x,depth+1) for x in ts[3]])
        return tag + middle + ctag



    return "ERROR %s"%ts        


data = (open("test.plml")).read()

print data
parseTree = suite.parseString(data)


from pprint import pprint
pprint( parseTree.asList() )

print
print htmlIt(parseTree.asList() )

