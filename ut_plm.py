
from plm import *
import unittest

class TestPLM(unittest.TestCase) :

    def testOuterStruct(self):
        data = """
html:
    head/
    body:
        hello"""
        desired = """<!DOCTYPE html>
<html>
  <head/>
  <body>
    hello
  </body>
</html>
"""       
        self.assertEquals(comp(data)[0],desired)
      
          
        
                
    def testTitle(self): 
        data = """
html:
    head:
        title:This is a title"""
        desired = """<!DOCTYPE html>
<html>
  <head>
    <title>This is a title</title>
  </head>
</html>
"""
        self.assertEquals(comp(data)[0],desired)        
                

    def testMeta(self) :
        data = """
html:
    head:
        meta(charset="utf-8")/
    body/
"""
        desired = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
  </head>
  <body/>
</html>
"""     
        self.assertEquals(comp(data)[0],desired)    
        
    def testStyle(self) :
        data = """
html:
    head:
        stylesheet:mystyles.css
        importscript:libs/jquery.min.js
"""
        desired = """<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="mystyles.css">
    <script src="libs/jquery.min.js"></script>
  </head>
</html>
"""
        self.assertEquals(comp(data)[0],desired)

    def testAll(self) :    
        data =  """
html:
    head:
        title:This is a title
        stylesheet:mystyles.css
        importscript:libs/jquery.min.js
    body:
        div(#menu, .mainmenu):
            menu
        div(#content, .first, .big):
            main
            p:
                img(width=533):http://pictures.com/img1
        div(#footer, x=y):
            p:            
                copyright

"""
        desired = """<!DOCTYPE html>
<html>
  <head>
    <title>This is a title</title>
    <link rel="stylesheet" href="mystyles.css">
    <script src="libs/jquery.min.js"></script>
  </head>
  <body>
    <div id="menu" class="mainmenu" >
      menu
    </div>
    <div id="content" class="first big" >
      main
      <p>
        <img width="533" src="http://pictures.com/img1"/>
      </p>
    </div>
    <div x="y" id="footer" >
      <p>
        copyright
      </p>
    </div>
  </body>
</html>
"""
        self.assertEquals(comp(data)[0],desired)


if __name__ == "__main__" :
    unittest.main()
