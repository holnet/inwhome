#!/var/www/html/inwhome/venv/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, session
#print("Die Variable __name__ : " + __name__)
app = Flask(__name__)

@app.route("/")
def start():
    htmlcode = render_template("start.html")
    #print(htmlcode)
    return htmlcode

@app.route("/test")
def test():
    name = request.args.get("name")
    age = request.args.get("age")
    #print(name)
    #print(age)
    htmlcode = render_template("test.html", name=name, age=age)
    #print(htmlcode)
    return htmlcode

@app.route("/links")
def links():
    htmlcode = render_template("links.html")
    #print(htmlcode)
    return htmlcode

@app.route("/serverhilfe")
def serverhilfe():
    htmlcode = render_template("serverhilfe.html")
    #print(htmlcode)
    return htmlcode

@app.route("/powershell")
def powershell():
    htmlcode = render_template("powershell.html")
    #print(htmlcode)
    return htmlcode    

@app.route("/astronomie")
def astronomie():
    htmlcode = render_template("astronomie.html")
    #print(htmlcode)
    return htmlcode    

@app.route("/eishockeywm2022")
def eishockeywm2022():
    htmlcode = render_template("eishockeywm2022.html")
    #print(htmlcode)
    return htmlcode      


