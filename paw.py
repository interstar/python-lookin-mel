# Python Looking 'mel
# Phil Jones 2014

from indentGrammar import *

## Parser definition
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


## Render as HTML
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


if __name__ == '__main__' :
    data = (open("test.plml")).read()

    print data
    parseTree = suite.parseString(data)


    from pprint import pprint
    pprint( parseTree.asList() )

    print
    print htmlIt(parseTree.asList() )

