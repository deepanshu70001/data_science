#building url dynamically
#jinja 2 template engine
#{{}} one way expression to print html
#{%...%} condition for loop

#variable rule
from flask import Flask,render_template,request
#it create instance of flask class
#it will be wsgi(web server gateway interface)
app=Flask(__name__)
@app.route("/")
def welcome():
    return "welcome gt"
@app.route("/1")
def wel():
    return "page 1"

@app.route("/html_ex",methods=['GET'])
def ex():
    return "<html><h1>TRFD33CFRCRFCRCE</h1></html>"

@app.route("/2",methods=['GET','POST'])
def FORM():
    if request.method=='POST':
       n=request.form['name']
       return f"<html>.hello {n}</html> "
    return render_template("index.html") #it will look for html in template folder,we can save html for different pages in template folder

@app.route("/submit",methods=['GET','POST'])
def submit():
    if request.method=='POST':
       n=request.form['name']
       return f"<html>.hello {n}</html> "
    return render_template("index.html")
#variable rule
@app.route("/success/<int:score>")#score is variable ,int: require the value to be an integer
def success(score):
    res=""
    if score>=50:
        res="pass"
    else:
        res="fail"
    return render_template("result.html",result=res)#sending result to html via jinja


if __name__=="__main__":#check for the entry point of program
    app.run(debug=True) #update the page ,it restart the server better for devlopment
