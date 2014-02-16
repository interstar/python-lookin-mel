Python Lookin' 'mel
===================

Wassup?
-------

*You love Python.* It's gorgeous! 

*You hate the 'mel.* It's wack-ass ugly!

What you want is 'mel that LOOKS like Python. 

That's where Python Lookin' 'mel does you.


Huh?
----

Here's 'mel. (You *really* don't wanna be lookin' at that.)

`
<html>
  <head>
    <link rel="stylesheet" href="mystyles.css">
    <script src="libs/jquery.min.js"></script>
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
`

But here's Python Lookin' 'mel. 

`
html:
    head:
        stylesheet:mystyles.css
        importscript:libs/jquery.min.js
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

`

Mmmmm ... now *that's* what I want in MY editor!

WTF? Seriously?
===============
K. Seriously?

Seriously, we're using HTML for two different things these days. 

 * To mark-up text documents. And for that, we don't want to be looking at raw 'mel either. But we have Markdown, which is a great pre-processor that turns something that's for humans into HTML.

 * OTOH, we're also increasingly using HTML to describe the templates for our rich web-apps. These templates basically define a collection of 
 divs (with id and class attributes) and their nested block relationships. We often don't really need to do much more than that because 
 the contents of the divs are generated dynamically, but we seem to be stuck with the whole verbosity of historical SGML with the need to 
 keep track of closing tags. Why can't we have something like Markdown that gives us a clean way of describing this div structure?
 
Python is a beautiful language for defining block-structure cleanly; with meaningful indentation and a minimal syntax. So what if we 
reinvented HTML to look like Python? That's what *Python Lookin' 'mel* aims to be. The Markdown equivalent for people who are writing HTML to 
define UIs as nested divs and widget-sets etc.

It's a small Python pre-processor, built using PyParsing. It pulls in an indentation defined tree of tags and spits out the HTML equivalent with a couple of extra bells and whistles :

* uses css-style . and # to define class and id. Eg. `h2:(#heading, .main)` will become `<h2 id="heading" class="main">`. 
* t










