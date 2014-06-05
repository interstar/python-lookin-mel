Python Lookin' 'mel
===================

Wassup?
-------

*You love Python.* It's gorgeous! 

*You hate the 'mel.* It's wack-ass ugly!

What you want is 'mel that LOOKS like Python. 

That's where Python Lookin' 'mel comes in.


Huh?
----

Here's 'mel. (You *really* don't wanna be lookin' at that.)

```
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
```

But here's Python Lookin' 'mel. 


```
html:
    head:
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

```


Mmmmm ... now *that's* what I want in MY editor!

WTF? Seriously?
---------------
K. Seriously?

Seriously, we're using HTML for two different things these days. 

 * To mark-up text documents. And for that, we don't want to be looking at raw 'mel either. But we have Markdown, which is a great pre-processor that turns something that's for humans into HTML.

 * OTOH, we're also increasingly using HTML to describe the templates for our rich web-apps. These templates define a collection of 
 divs (with id and class attributes) and their nested block relationships. That's often a fairly simple structure but we seem to be stuck with the whole verbosity of historical SGML (and the need to keep track of closing tags) in order to do it. What we want is something *like* Markdown that gives us a clean way of describing this structure.
 
Python is a beautiful language for defining block-structure cleanly; with meaningful indentation and a minimal syntax. So what if we 
reinvented HTML to look like Python? That's what *Python Lookin' 'mel* aims to be. The Markdown equivalent for people who are writing HTML to 
define UIs as nested divs and widget-sets etc.

It's a small pre-processor, built using PyParsing. It pulls in an indentation-defined tree of tags and spits out the HTML equivalent with a couple of extra bells and whistles :

* uses css-style . and # to define class and id. Eg. `h2(#heading, .main):` will become `<h2 id="heading" class="main">`. 
* has some special shorthands for common activities. For example `stylesheet:mystyles.css` becomes `<link rel="stylesheet" href="mystyles.css">`

Quick Start
-----------

    easy_install pyparsing
    git clone https://github.com/interstar/python-lookin-mel.git plm
    cd plm

To run the unit tests :

    python ut_plm.py
    
To run the main program : 

    python plm.py test.plm
    
This reads the input data from test.plm and writes to stdout.

FAQ
---
*Q : Is it ready for serious use?*

A : Not yet. This is a first draft I'm putting on GitHub because I've got to put it somewhere :-) It's probably going to break if you try to use it. But tell me in the bug-tracker.

*Q : Isn't this awfully like an [HTML pre-processor](http://blog.codepen.io/documentation/editor/using-html-preprocessors/)?*

A : Yes, it is isn't it? But it's the most Python Lookin' HTML preprocessor I've seen so far.

*Q : Is PLM a templating language?*

A : Not at the moment. To be honest I'm more interested in working on templates that will be dynamically filled by code running in the browser than creating them on the server. 

At the moment ...

*Q : How / Where in my production pipeline should I use it?*

A : Either as a compiler. Personally I compile my CoffeeScript files to .js files during development rather than on-the-fly. I'm now starting to use Python Lookin' 'mel in a couple of projects, and compile plm files to html at the same time.

Or you can try including the compiler in your Python server. And turn plm files into html every time you serve them. You're responsible for figuring out how this interacts with your templating engine though. ;-)












