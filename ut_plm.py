
from plm import *
import unittest

class TestPLM(unittest.TestCase) :
    def testStyle(self) :
        data = """
html:
    head:
        stylesheet:mystyles.css
"""
        desired = """<html>
  <head>
    <link rel="stylesheet" href="mystyles.css">
  </head>
</html>
"""
        self.assertEquals(comp(data)[0],desired)
                
    def testAll(self) :    
        data =  """
html:
    head:
        stylesheet:mystyles.css
        script:
            url1
    body:
        div(#menu, .mainmenu):
            menu
        div(#content, .first, .big):
            main
        div(#footer, x=y):
            p:            
                copyright
            p:
                img(width=533):http://pictures.com/img1

"""
        desired = """<html>
  <head>
    <link rel="stylesheet" href="mystyles.css">
    <script>
      url1
    </script>
  </head>
  <body>
    <div id="menu" class="mainmenu" >
      menu
    </div>
    <div id="content" class="first big" >
      main
    </div>
    <div x="y" id="footer" >
      <p>
        copyright
      </p>
      <p>
        <img width="533" src="http://pictures.com/img1"/>
      </p>
    </div>
  </body>
</html>
"""
        self.assertEquals(comp(data)[0],desired)


if __name__ == "__main__" :
    unittest.main()
