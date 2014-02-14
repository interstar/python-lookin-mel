# Python Looking 'mel
# Phil Jones 2014

from indentGrammar import *

## Parser definition
stmt = Forward()
suite = Group( OneOrMore( empty + stmt.setParseAction( checkPeerIndent ) )  )

identifier = Word(alphas, alphanums)
val = identifier | quotedString

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

class Attributes(dict) :

    def __init__(self,attributes) :        
        for a in attributes :
            if a == "(" : continue
            if a == ")" : break
            if len(a) == 3 and a[1] == "=" :
                self[a[0]]=a[2]
                continue
            if a[0]=='#' :
                self['id']=a[1]
                continue
            if a[0]=='.' :
                if not self.has_key('class') :
                    self['class'] = []
                self['class'].append(a[1])

    def __str__(self) :
        build = ""
        for k,v in self.iteritems() :
            if k == "class" :
                build = build + """class="%s" """ % " ".join(x for x in self["class"])
            else :
                build = build + """%s=%s """ % (k,v)
        return build        
                
        
class Magic :

    @classmethod 
    def contains(cls,name) :
        try :
            getattr(cls,name)
            return True
        except Exception, e:    
            return False
        
    @classmethod 
    def call(cls,name,*args) :
        try :
            return getattr(cls,name)(*args)
        except Exception, e :
            raise e

    @classmethod
    def img(cls,depth,attributes,data) :
        atts = Attributes(attributes)
        return "  "*depth + "<img %ssrc='%s'/>\n" % (atts.__str__(),data)
        
    
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
        if Magic.contains(ts[0]) :
            return Magic.call(ts[0],depth,ts[1],ts[3])
            
        tag = ind + "<"+ts[0]+ htmlIt(ts[1]) + ">\n"
        ctag = ind + "</"+ts[0]+">\n"
        if isinstance(ts[3], basestring) : middle = ts[3] + "\n"
        else :
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

