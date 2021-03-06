# Python Looking 'mel
# Phil Jones 2014

from indentGrammar import *
from pprint import pprint

## Parser definition
stmt = Forward()
suite = Group( OneOrMore( empty + stmt.setParseAction( checkPeerIndent ) )  )

identifier = Word(alphas, alphanums)
val = identifier | Word(nums) | dblQuotedString

rhs = val | identifier


cssid = Group("#" + Word(alphas,alphanums))
csscls = Group("." + Word(alphas,alphanums))
otheratt = Group(identifier + "=" + rhs)

attr = cssid | csscls | otheratt

args = Optional( Group( "(" + delimitedList(attr)  + ")" ) )

tagLine = (identifier + args + ":")
tagApp = Group( tagLine + INDENT + suite + UNDENT )

oneLine = Group(identifier + args + ":" + restOfLine ) | Group(identifier + ":" + restOfLine) | Group(identifier + "/") |  Group(identifier + args + "/")

stmt << ( tagApp | oneLine | val )

IN = "  "

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
                if v[0] == '"' and v[-1] == '"' : 
                    v = v.strip('"')
                build = build + """%s="%s" """ % (k,v)
        return build        
                

def optionalAttributes(f) :
    def g(cls,depth,*args) :
        if len(args) == 2 :        
            attributes = Attributes(args[0])
            data = args[1]
        else :
            data = args[0]
            attributes = Attributes([])
        return f(cls,depth,attributes,data)
    return g 


        
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
    @optionalAttributes
    def img(cls,depth,atts,data) :
        return IN*depth + """<img %ssrc="%s"/>\n""" % (atts.__str__(),data)
        
    @classmethod
    @optionalAttributes
    def stylesheet(cls,depth,atts,data) :
        return IN*depth + """<link rel="stylesheet" href="%s">\n""" % data

    @classmethod
    @optionalAttributes
    def importscript(cls,depth,atts,data) :
        return IN*depth + """<script src="%s"></script>\n""" % data
    
## Render as HTML
def htmlIt(ts,depth=0) :       
    ind = IN * depth

    if isinstance(ts, basestring) :
        return ind + ts + "\n"
        
    if len(ts) == 1 :        
        return htmlIt(ts[0])
                    
    if ts[0] == '(' :
        atts = Attributes(ts)
        return " " + atts.__str__()
        
    elif len(ts)==2 :
        if ts[1] == '/' :
            return ind + "<" + ts[0]+"/>\n"
        else :
            return ("ERROR WITH %s" % ", ".join(ts)) + " Only two items but second was a /"
            
    elif len(ts)==3 :
        if ts[1] == ':' :
            # 3 items, ts[1] is : to define something
            if isinstance(ts[2],basestring) : 
                # we have 3 items, ts[2] is data on same line
                if Magic.contains(ts[0]) :
                    return Magic.call(ts[0],depth,ts[2])
                else : 
                    return ind + "<%s>%s</%s>\n" % (ts[0],ts[2],ts[0])
            else :
                # we have 3 items, ts[2] is sub-block
                tag = ind + "<"+ts[0]+">\n"
                ctag = ind + "</"+ts[0]+">\n"
                middle = "".join([htmlIt(x,depth+1) for x in ts[2]])
                return tag + middle + ctag
        elif ts[2] == '/' :
            # 3 items, ts[1] is attributes, ts[2] closes it 
            atts = Attributes(ts[1])
            return ind + "<%s %s/>\n" % (ts[0],atts.__str__())
    else :
        if Magic.contains(ts[0]) :
            return Magic.call(ts[0],depth,ts[1],ts[3])
            
        tag = ind + "<"+ts[0]+ htmlIt(ts[1]) + ">\n"
        ctag = ind + "</"+ts[0]+">\n"
        if isinstance(ts[3], basestring) : 
            middle = ts[3] + "\n"
        else :
            middle = "".join([htmlIt(x,depth+1) for x in ts[3]])
        return tag + middle + ctag

    return "ERROR %s"%ts

def comp(data) :
    parseTree = suite.parseString(data)
    l = parseTree.asList()
    return ("<!DOCTYPE html>\n"+htmlIt(l),l)

if __name__ == '__main__' :
    import sys
    fName = sys.argv[1]
    
    data = (open(fName)).read()
    
    """
    print "Original Data"
    print "___________________"
    print data
    print
    """
    out, lst = comp(data)
    """
    print "ParseTree as List"
    print "_________________________"
    pprint( lst )
    print
    print "Out"
    print "_______"
    """
    
    print out



